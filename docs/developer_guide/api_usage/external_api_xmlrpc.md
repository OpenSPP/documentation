---
review-status: needs-review
review-date: 2025-08-26
reviewer: technical-writer
migration-notes: "Rewritten for clarity and practical usage, following REST API documentation structure"
---

# External API using XML-RPC

This guide explains how to connect to and interact with OpenSPP using the XML-RPC API, with practical examples in Python, Ruby, PHP, and Java.

## Prerequisites

- OpenSPP server running and accessible.
- User credentials or API key with appropriate permissions.
- Basic knowledge of your chosen programming language.
- Required libraries installed (see language-specific notes below).

## 1. Understanding XML-RPC in OpenSPP

OpenSPP exposes much of its data and functionality via XML-RPC endpoints. You can use these endpoints to authenticate, read, create, update, and delete records from external applications.

**Endpoints:**
- `/xmlrpc/2/common` — Authentication and meta-calls
- `/xmlrpc/2/object` — Model methods (CRUD operations)

## 2. Authentication

You must authenticate before accessing most data. You can use your password or an API key (recommended for security).

### Authentication Examples

<!-- tabs:start -->

#### **Python**

```python
import xmlrpc.client

url = "http://localhost:8069"
db = "my_database"
username = "admin"
password = "your_password_or_api_key"

common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})
print("Authenticated UID:", uid)
```

#### **Ruby**

```ruby
require "xmlrpc/client"

url = "http://localhost:8069"
db = "my_database"
username = "admin"
password = "your_password_or_api_key"

common = XMLRPC::Client.new2("#{url}/xmlrpc/2/common")
uid = common.call('authenticate', db, username, password, {})
puts "Authenticated UID: #{uid}"
```

#### **PHP**

```php
require_once('ripcord.php');

$url = "http://localhost:8069";
$db = "my_database";
$username = "admin";
$password = "your_password_or_api_key";

$common = ripcord::client("$url/xmlrpc/2/common");
$uid = $common->authenticate($db, $username, $password, array());
echo "Authenticated UID: $uid\n";
```

#### **Java**

```java
import org.apache.xmlrpc.client.*;
import java.net.URL;
import java.util.*;

final String url = "http://localhost:8069";
final String db = "my_database";
final String username = "admin";
final String password = "your_password_or_api_key";

XmlRpcClientConfigImpl config = new XmlRpcClientConfigImpl();
config.setServerURL(new URL(url + "/xmlrpc/2/common"));
XmlRpcClient client = new XmlRpcClient();
client.setConfig(config);

int uid = (Integer) client.execute("authenticate", Arrays.asList(db, username, password, new HashMap<>()));
System.out.println("Authenticated UID: " + uid);
```

<!-- tabs:end -->

## 3. Calling Model Methods (CRUD Operations)

Once authenticated, use the `/xmlrpc/2/object` endpoint to interact with OpenSPP models.

### Read Records

<!-- tabs:start -->

#### **Python**

```python
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
partners = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['name', 'country_id'], 'limit': 5})
print(partners)
```

#### **Ruby**

```ruby
models = XMLRPC::Client.new2("#{url}/xmlrpc/2/object")
partners = models.call(
  'execute_kw',
  db,
  uid,
  password,
  'res.partner',
  'search_read',
  [ [ ['is_company', '=', true] ] ], # domain as an array of arrays
  { fields: ['name', 'country_id'], limit: 5 } # options as a separate hash
)
puts partners
```

#### **PHP**

```php
$models = ripcord::client("$url/xmlrpc/2/object");
$partners = $models->execute_kw($db, $uid, $password, 'res.partner', 'search_read', array(array(array('is_company', '=', true))), array('fields'=>array('name','country_id'), 'limit'=>5));
print_r($partners);
```

#### **Java**

```java
XmlRpcClientConfigImpl objectConfig = new XmlRpcClientConfigImpl();
objectConfig.setServerURL(new URL(url + "/xmlrpc/2/object"));
client.setConfig(objectConfig);

List<Object> domain = Arrays.asList(Arrays.asList("is_company", "=", true));
Map<String, Object> kwargs = new HashMap<>();
kwargs.put("fields", Arrays.asList("name", "country_id"));
kwargs.put("limit", 5);

Object[] partners = (Object[]) client.execute("execute_kw", Arrays.asList(db, uid, password, "res.partner", "search_read", Arrays.asList(domain), kwargs));
System.out.println(Arrays.toString(partners));
```

<!-- tabs:end -->

## 4. Creating, Updating, and Deleting Records

### Create a Record

<!-- tabs:start -->

#### **Python**

```python
new_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "New Partner"}])
print("Created Partner ID:", new_id)
```

#### **Ruby**

```ruby
new_id = models.call('execute_kw', db, uid, password, 'res.partner', 'create', [{name: "New Partner"}])
puts "Created Partner ID: #{new_id}"
```

#### **PHP**

```php
$new_id = $models->execute_kw($db, $uid, $password, 'res.partner', 'create', array(array('name' => "New Partner")));
echo "Created Partner ID: $new_id\n";
```

#### **Java**

```java
Object newId = client.execute("execute_kw", Arrays.asList(db, uid, password, "res.partner", "create", Arrays.asList(Collections.singletonMap("name", "New Partner"))));
System.out.println("Created Partner ID: " + newId);
```

<!-- tabs:end -->

### Update a Record

<!-- tabs:start -->

#### **Python**

```python
models.execute_kw(db, uid, password, 'res.partner', 'write', [[new_id], {'name': "Updated Partner"}])
```

#### **Ruby**

```ruby
models.call('execute_kw', db, uid, password, 'res.partner', 'write', [[new_id], {name: "Updated Partner"}])
```

#### **PHP**

```php
$models->execute_kw($db, $uid, $password, 'res.partner', 'write', array(array($new_id), array('name' => "Updated Partner")));
```

#### **Java**

```java
client.execute("execute_kw", Arrays.asList(db, uid, password, "res.partner", "write", Arrays.asList(Arrays.asList(newId), Collections.singletonMap("name", "Updated Partner"))));
```

<!-- tabs:end -->

### Delete a Record

<!-- tabs:start -->

#### **Python**

```python
models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[new_id]])
```

#### **Ruby**

```ruby
models.call('execute_kw', db, uid, password, 'res.partner', 'unlink', [[new_id]])
```

#### **PHP**

```php
$models->execute_kw($db, $uid, $password, 'res.partner', 'unlink', array(array($new_id)));
```

#### **Java**

```java
client.execute("execute_kw", Arrays.asList(db, uid, password, "res.partner", "unlink", Arrays.asList(Arrays.asList(newId))));
```

<!-- tabs:end -->

## 5. Security: Using API Keys

- **API keys** are recommended over passwords for scripts and integrations.
- Generate API keys in your OpenSPP user profile under **Account Security**.
- Use the API key in place of your password in all XML-RPC calls.

## 6. Best Practices

1. **Use API Keys**: Safer than passwords; revoke if compromised.
2. **Limit Permissions**: Create dedicated users for API access with only necessary rights.
3. **Validate Responses**: Always check for errors or unexpected results.
4. **Secure Connections**: Use HTTPS for all API traffic.
5. **Log and Monitor**: Track API usage for auditing and troubleshooting.

## References

- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- [OpenSPP Developer Guide](https://docs.openspp.org/)
- [XML-RPC Specification](https://en.wikipedia.org/wiki/XML-RPC)

---

*For more advanced usage, including model introspection and dynamic model creation, see the full documentation.*