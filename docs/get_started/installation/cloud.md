---
openspp:
  doc_status: draft
---

# Cloud Deployment

This guide is for **sys admins** deploying OpenSPP to cloud platforms. It covers AWS, Azure, and Google Cloud Platform with infrastructure-as-code templates and best practices.

Cloud deployment provides high availability, scalability, managed backups, and geographic distribution for production OpenSPP installations.

## Cloud Platform Comparison

| Feature | AWS | Azure | GCP |
|---------|-----|-------|-----|
| **Compute** | EC2 | Virtual Machines | Compute Engine |
| **Managed DB** | RDS PostgreSQL | Azure Database | Cloud SQL |
| **Object Storage** | S3 | Blob Storage | Cloud Storage |
| **Load Balancer** | ALB/NLB | Load Balancer | Cloud Load Balancing |
| **Container Service** | ECS/EKS | AKS | GKE |
| **CDN** | CloudFront | Azure CDN | Cloud CDN |
| **Estimated Cost/Month** | $200-500 | $180-450 | $190-480 |

**Cost estimates** for production setup (2 app servers, managed PostgreSQL, load balancer, storage).

## Prerequisites

All platforms require:

- Cloud provider account with billing enabled
- CLI tools installed (aws-cli, az, or gcloud)
- Docker images pushed to container registry
- SSL certificate (can use Let's Encrypt)
- Domain name for your OpenSPP instance

## AWS Deployment

### Architecture

```
Internet
   ↓
Application Load Balancer (HTTPS)
   ↓
ECS Fargate Tasks (OpenSPP containers)
   ↓
RDS PostgreSQL + S3 (filestore)
```

### 1. Install AWS CLI

```shell
# Ubuntu/Debian
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# macOS
brew install awscli

# Configure
aws configure
```

Enter your AWS Access Key ID, Secret Access Key, and default region.

### 2. Create Infrastructure

Create `terraform/aws/main.tf`:

```hcl
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# VPC
resource "aws_vpc" "openspp" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "openspp-vpc"
  }
}

# Subnets
resource "aws_subnet" "public_a" {
  vpc_id            = aws_vpc.openspp.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "openspp-public-a"
  }
}

resource "aws_subnet" "public_b" {
  vpc_id            = aws_vpc.openspp.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "us-east-1b"

  tags = {
    Name = "openspp-public-b"
  }
}

resource "aws_subnet" "private_a" {
  vpc_id            = aws_vpc.openspp.id
  cidr_block        = "10.0.10.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "openspp-private-a"
  }
}

resource "aws_subnet" "private_b" {
  vpc_id            = aws_vpc.openspp.id
  cidr_block        = "10.0.11.0/24"
  availability_zone = "us-east-1b"

  tags = {
    Name = "openspp-private-b"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "openspp" {
  vpc_id = aws_vpc.openspp.id

  tags = {
    Name = "openspp-igw"
  }
}

# RDS PostgreSQL
resource "aws_db_instance" "openspp" {
  identifier             = "openspp-db"
  engine                 = "postgres"
  engine_version         = "15.4"
  instance_class         = "db.t3.medium"
  allocated_storage      = 100
  storage_type           = "gp3"
  storage_encrypted      = true

  db_name  = "openspp_prod"
  username = "openspp"
  password = var.db_password  # Use variables for secrets!

  vpc_security_group_ids = [aws_security_group.rds.id]
  db_subnet_group_name   = aws_db_subnet_group.openspp.name

  backup_retention_period = 7
  backup_window          = "03:00-04:00"
  maintenance_window     = "sun:04:00-sun:05:00"

  skip_final_snapshot = false
  final_snapshot_identifier = "openspp-final-snapshot"

  tags = {
    Name = "openspp-db"
  }
}

# S3 Bucket for filestore
resource "aws_s3_bucket" "filestore" {
  bucket = "openspp-filestore-${random_id.bucket_suffix.hex}"

  tags = {
    Name = "openspp-filestore"
  }
}

resource "aws_s3_bucket_versioning" "filestore" {
  bucket = aws_s3_bucket.filestore.id

  versioning_configuration {
    status = "Enabled"
  }
}

# ECS Cluster
resource "aws_ecs_cluster" "openspp" {
  name = "openspp-cluster"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}

# ECS Task Definition
resource "aws_ecs_task_definition" "openspp" {
  family                   = "openspp"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "2048"
  memory                   = "4096"
  execution_role_arn       = aws_iam_role.ecs_execution.arn
  task_role_arn            = aws_iam_role.ecs_task.arn

  container_definitions = jsonencode([
    {
      name      = "openspp"
      image     = "ghcr.io/openspp/openspp:17.0-latest"
      cpu       = 2048
      memory    = 4096
      essential = true

      environment = [
        {
          name  = "PGHOST"
          value = aws_db_instance.openspp.address
        },
        {
          name  = "PGDATABASE"
          value = "openspp_prod"
        },
        {
          name  = "PGUSER"
          value = "openspp"
        },
        {
          name  = "AWS_BUCKET"
          value = aws_s3_bucket.filestore.bucket
        }
      ]

      secrets = [
        {
          name      = "PGPASSWORD"
          valueFrom = aws_secretsmanager_secret.db_password.arn
        }
      ]

      portMappings = [
        {
          containerPort = 8069
          protocol      = "tcp"
        }
      ]

      logConfiguration = {
        logDriver = "awslogs"
        options = {
          "awslogs-group"         = "/ecs/openspp"
          "awslogs-region"        = "us-east-1"
          "awslogs-stream-prefix" = "ecs"
        }
      }
    }
  ])
}

# Application Load Balancer
resource "aws_lb" "openspp" {
  name               = "openspp-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb.id]
  subnets            = [aws_subnet.public_a.id, aws_subnet.public_b.id]

  tags = {
    Name = "openspp-alb"
  }
}

resource "aws_lb_target_group" "openspp" {
  name        = "openspp-tg"
  port        = 8069
  protocol    = "HTTP"
  vpc_id      = aws_vpc.openspp.id
  target_type = "ip"

  health_check {
    path                = "/web/health"
    healthy_threshold   = 2
    unhealthy_threshold = 10
    timeout             = 60
    interval            = 300
  }
}

# Variables
variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}

# Outputs
output "alb_dns_name" {
  value = aws_lb.openspp.dns_name
}

output "db_endpoint" {
  value = aws_db_instance.openspp.endpoint
}
```

### 3. Deploy Infrastructure

```shell
# Install Terraform
wget https://releases.hashicorp.com/terraform/1.6.0/terraform_1.6.0_linux_amd64.zip
unzip terraform_1.6.0_linux_amd64.zip
sudo mv terraform /usr/local/bin/

# Initialize Terraform
cd terraform/aws
terraform init

# Create terraform.tfvars
echo 'db_password = "CHANGE-THIS-PASSWORD"' > terraform.tfvars

# Plan deployment
terraform plan

# Apply (create resources)
terraform apply
```

Deployment takes 15-20 minutes.

### 4. Configure Domain

```shell
# Get load balancer DNS
terraform output alb_dns_name

# Create Route53 record or update your DNS
aws route53 change-resource-record-sets \
  --hosted-zone-id YOUR_ZONE_ID \
  --change-batch '{
    "Changes": [{
      "Action": "CREATE",
      "ResourceRecordSet": {
        "Name": "openspp.example.com",
        "Type": "CNAME",
        "TTL": 300,
        "ResourceRecords": [{"Value": "openspp-alb-123456.us-east-1.elb.amazonaws.com"}]
      }
    }]
  }'
```

### 5. SSL Certificate

```shell
# Request certificate
aws acm request-certificate \
  --domain-name openspp.example.com \
  --validation-method DNS \
  --region us-east-1

# Follow validation steps in ACM console
```

## Azure Deployment

### Architecture

```
Internet
   ↓
Azure Load Balancer (HTTPS)
   ↓
Container Instances (OpenSPP)
   ↓
Azure Database for PostgreSQL + Blob Storage
```

### 1. Install Azure CLI

```shell
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# macOS
brew install azure-cli

# Login
az login
```

### 2. Create Resource Group

```shell
# Set variables
RESOURCE_GROUP="openspp-rg"
LOCATION="eastus"
DB_PASSWORD="<generate-strong-password>"

# Create resource group
az group create \
  --name $RESOURCE_GROUP \
  --location $LOCATION
```

### 3. Create PostgreSQL Database

```shell
# Create PostgreSQL server
az postgres flexible-server create \
  --resource-group $RESOURCE_GROUP \
  --name openspp-db \
  --location $LOCATION \
  --admin-user openspp \
  --admin-password "$DB_PASSWORD" \
  --sku-name Standard_D2s_v3 \
  --tier GeneralPurpose \
  --version 15 \
  --storage-size 128 \
  --public-access 0.0.0.0

# Create database
az postgres flexible-server db create \
  --resource-group $RESOURCE_GROUP \
  --server-name openspp-db \
  --database-name openspp_prod
```

### 4. Create Storage Account

```shell
# Create storage account
az storage account create \
  --name opensppfilestore \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --sku Standard_LRS

# Create container
az storage container create \
  --name filestore \
  --account-name opensppfilestore
```

### 5. Deploy Container Instance

```shell
# Get database connection string
DB_HOST=$(az postgres flexible-server show \
  --resource-group $RESOURCE_GROUP \
  --name openspp-db \
  --query fullyQualifiedDomainName \
  --output tsv)

# Deploy container
az container create \
  --resource-group $RESOURCE_GROUP \
  --name openspp-app \
  --image ghcr.io/openspp/openspp:17.0-latest \
  --cpu 2 \
  --memory 4 \
  --ports 8069 \
  --dns-name-label openspp-app \
  --environment-variables \
    PGHOST=$DB_HOST \
    PGDATABASE=openspp_prod \
    PGUSER=openspp \
  --secure-environment-variables \
    PGPASSWORD=$DB_PASSWORD
```

### 6. Create Load Balancer

```shell
# Create public IP
az network public-ip create \
  --resource-group $RESOURCE_GROUP \
  --name openspp-pip \
  --sku Standard

# Create load balancer
az network lb create \
  --resource-group $RESOURCE_GROUP \
  --name openspp-lb \
  --sku Standard \
  --public-ip-address openspp-pip \
  --frontend-ip-name openspp-frontend \
  --backend-pool-name openspp-backend
```

### 7. Configure DNS and SSL

```shell
# Get public IP
az network public-ip show \
  --resource-group $RESOURCE_GROUP \
  --name openspp-pip \
  --query ipAddress \
  --output tsv

# Use Azure Front Door for SSL and CDN
az afd profile create \
  --resource-group $RESOURCE_GROUP \
  --profile-name openspp-cdn \
  --sku Standard_AzureFrontDoor
```

## Google Cloud Platform (GCP) Deployment

### Architecture

```
Internet
   ↓
Cloud Load Balancer (HTTPS)
   ↓
GKE Cluster (OpenSPP pods)
   ↓
Cloud SQL PostgreSQL + Cloud Storage
```

### 1. Install gcloud CLI

```shell
# Ubuntu/Debian
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# macOS
brew install google-cloud-sdk

# Initialize
gcloud init
```

### 2. Create Project

```shell
# Set variables
PROJECT_ID="openspp-prod"
REGION="us-central1"
ZONE="us-central1-a"

# Create project
gcloud projects create $PROJECT_ID

# Set project
gcloud config set project $PROJECT_ID

# Enable APIs
gcloud services enable \
  container.googleapis.com \
  sqladmin.googleapis.com \
  storage.googleapis.com
```

### 3. Create Cloud SQL Instance

```shell
# Create PostgreSQL instance
gcloud sql instances create openspp-db \
  --database-version=POSTGRES_15 \
  --tier=db-custom-2-7680 \
  --region=$REGION \
  --root-password="<generate-strong-password>" \
  --storage-size=100GB \
  --storage-type=SSD \
  --backup \
  --backup-start-time=03:00

# Create database
gcloud sql databases create openspp_prod \
  --instance=openspp-db

# Create user
gcloud sql users create openspp \
  --instance=openspp-db \
  --password="<generate-strong-password>"
```

### 4. Create GKE Cluster

```shell
# Create cluster
gcloud container clusters create openspp-cluster \
  --zone=$ZONE \
  --num-nodes=2 \
  --machine-type=n1-standard-2 \
  --disk-size=50 \
  --enable-autoscaling \
  --min-nodes=2 \
  --max-nodes=5 \
  --enable-autorepair \
  --enable-autoupgrade

# Get credentials
gcloud container clusters get-credentials openspp-cluster --zone=$ZONE
```

### 5. Create Storage Bucket

```shell
# Create bucket
gsutil mb -l $REGION gs://openspp-filestore-$PROJECT_ID/

# Enable versioning
gsutil versioning set on gs://openspp-filestore-$PROJECT_ID/
```

### 6. Deploy to GKE

Create `k8s/deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: openspp
spec:
  replicas: 2
  selector:
    matchLabels:
      app: openspp
  template:
    metadata:
      labels:
        app: openspp
    spec:
      containers:
      - name: openspp
        image: ghcr.io/openspp/openspp:17.0-latest
        ports:
        - containerPort: 8069
        env:
        - name: PGHOST
          value: "127.0.0.1"
        - name: PGDATABASE
          value: "openspp_prod"
        - name: PGUSER
          valueFrom:
            secretKeyRef:
              name: openspp-secrets
              key: db-user
        - name: PGPASSWORD
          valueFrom:
            secretKeyRef:
              name: openspp-secrets
              key: db-password
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
      - name: cloud-sql-proxy
        image: gcr.io/cloudsql-docker/gce-proxy:latest
        command:
          - "/cloud_sql_proxy"
          - "-instances=PROJECT_ID:REGION:openspp-db=tcp:5432"
---
apiVersion: v1
kind: Service
metadata:
  name: openspp-service
spec:
  type: LoadBalancer
  selector:
    app: openspp
  ports:
  - port: 80
    targetPort: 8069
```

**Deploy:**

```shell
# Create secrets
kubectl create secret generic openspp-secrets \
  --from-literal=db-user=openspp \
  --from-literal=db-password='<your-password>'

# Apply deployment
kubectl apply -f k8s/deployment.yaml

# Get external IP
kubectl get service openspp-service
```

## Monitoring and Logging

### AWS CloudWatch

```shell
# View logs
aws logs tail /ecs/openspp --follow

# Create alarm for high CPU
aws cloudwatch put-metric-alarm \
  --alarm-name openspp-high-cpu \
  --alarm-description "Alarm when CPU exceeds 80%" \
  --metric-name CPUUtilization \
  --namespace AWS/ECS \
  --statistic Average \
  --period 300 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold
```

### Azure Monitor

```shell
# Enable diagnostics
az monitor diagnostic-settings create \
  --resource /subscriptions/SUB_ID/resourceGroups/openspp-rg/providers/Microsoft.ContainerInstance/containerGroups/openspp-app \
  --name openspp-diagnostics \
  --logs '[{"category": "ContainerInstanceLog", "enabled": true}]' \
  --metrics '[{"category": "AllMetrics", "enabled": true}]'
```

### GCP Stackdriver

```shell
# View logs
gcloud logging read "resource.type=k8s_container AND resource.labels.pod_name=openspp" --limit 50

# Create uptime check
gcloud monitoring uptime create openspp-check \
  --resource-type=uptime-url \
  --host=openspp.example.com \
  --path=/web/health
```

## Backup Strategies

### AWS Backup

```shell
# Enable automated RDS snapshots (already configured in Terraform)
# Manual snapshot
aws rds create-db-snapshot \
  --db-instance-identifier openspp-db \
  --db-snapshot-identifier openspp-manual-$(date +%Y%m%d)

# S3 versioning (already configured)
# Export database to S3
aws rds start-export-task \
  --export-task-identifier openspp-export-$(date +%Y%m%d) \
  --source-arn arn:aws:rds:us-east-1:ACCOUNT:snapshot:openspp-snapshot \
  --s3-bucket-name openspp-backups \
  --iam-role-arn arn:aws:iam::ACCOUNT:role/rds-s3-export
```

### Azure Backup

```shell
# PostgreSQL automated backups (enabled by default)
# Manual backup
az postgres flexible-server backup create \
  --resource-group openspp-rg \
  --name openspp-db \
  --backup-name manual-$(date +%Y%m%d)

# Storage account backup
az storage blob snapshot \
  --account-name opensppfilestore \
  --container-name filestore \
  --name filestore.tar.gz
```

### GCP Backup

```shell
# Cloud SQL automated backups (enabled in creation)
# Manual backup
gcloud sql backups create \
  --instance=openspp-db \
  --description="Manual backup $(date +%Y%m%d)"

# Storage bucket backup
gsutil -m cp -r gs://openspp-filestore-$PROJECT_ID gs://openspp-filestore-backup-$PROJECT_ID
```

## Cost Optimization

### AWS Cost Optimization

| Strategy | Savings |
|----------|---------|
| Use Reserved Instances for RDS | 30-50% |
| Use Spot Instances for non-critical tasks | 60-80% |
| Enable S3 Intelligent Tiering | 20-40% |
| Right-size ECS tasks | 20-30% |

```shell
# View cost by service
aws ce get-cost-and-usage \
  --time-period Start=2025-01-01,End=2025-01-31 \
  --granularity MONTHLY \
  --metrics BlendedCost \
  --group-by Type=DIMENSION,Key=SERVICE
```

### Azure Cost Optimization

```shell
# View costs
az consumption usage list \
  --start-date 2025-01-01 \
  --end-date 2025-01-31

# Resize VM
az vm resize \
  --resource-group openspp-rg \
  --name openspp-vm \
  --size Standard_B2s
```

### GCP Cost Optimization

```shell
# View costs
gcloud billing accounts list

# Enable committed use discounts
gcloud compute commitments create \
  --plan=12-month \
  --region=$REGION \
  --resources=vcpu=4,memory=16
```

## Are You Stuck?

### Terraform deployment fails

**Check AWS credentials:**
```shell
aws sts get-caller-identity
```

**Check Terraform state:**
```shell
terraform state list
terraform state show aws_db_instance.openspp
```

### Container fails to start

**Check logs:**
```shell
# AWS
aws ecs describe-tasks --cluster openspp-cluster --tasks TASK_ID

# Azure
az container logs --resource-group openspp-rg --name openspp-app

# GCP
kubectl logs -l app=openspp
```

### Database connection fails

**Check security groups (AWS):**
```shell
aws ec2 describe-security-groups --group-ids sg-xxxxx
```

**Test connection:**
```shell
# AWS
psql -h openspp-db.xxxxx.us-east-1.rds.amazonaws.com -U openspp -d openspp_prod

# Azure
psql -h openspp-db.postgres.database.azure.com -U openspp -d openspp_prod

# GCP
gcloud sql connect openspp-db --user=openspp --database=openspp_prod
```

### High costs

**Review resources:**
```shell
# AWS
aws resourcegroupstaggingapi get-resources

# Azure
az resource list --output table

# GCP
gcloud asset search-all-resources
```

**Stop unused resources:**
```shell
# Downsize during off-hours
# Use auto-scaling policies
# Delete unused snapshots and backups
```

## Next Steps

- {doc}`/ops_guide/security/access_control` - Secure your deployment
- {doc}`/ops_guide/monitoring` - Set up monitoring
- {doc}`/ops_guide/backup_recovery` - Configure backups
- {doc}`/get_started/first_program/index` - Create your first program

## Support

- **Documentation:** https://docs.openspp.org
- **AWS:** https://github.com/OpenSPP/openspp-docker/discussions
- **Azure:** https://github.com/OpenSPP/openspp-docker/discussions
- **GCP:** https://github.com/OpenSPP/openspp-docker/discussions
- **Security Issues:** security@openspp.org
