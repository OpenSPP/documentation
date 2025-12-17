---
openspp:
  doc_status: unverified
---

# Release Management

## Agile Release Planning and Scheduling

OpenSPP's development process operates through the scrum methodology, a framework widely used in Agile software development. This involves two-week sprints, at the end of which a new version of the solution is released. The use of scrum methodology fosters iterative progress, rapid feedback, and efficient resolution of issues.

In terms of release frequency, internal releases are planned every two/three weeks in alignment with the sprint durations. Public releases, incorporating more extensive changes or new features. This schedule strikes a balance between introducing new functionalities and maintaining system stability.

## Risk Management and Release Safeguards

Risk management is a crucial aspect of OpenSPP's development process. The platform is equipped with mechanisms to manage the risk of releases, such as rollback plans. These include automated deployment pipelines, a continuous integration process, and automated testing and validation of code changes.

OpenSPP uses these features to ensure that every new release is stable and reliable. In the event of a failed deployment or the emergence of other issues, a rollback feature allows users to restore a previous version of their code. This safeguard ensures that system functionality can be quickly recovered, minimizing disruption to users.

## Automated Testing and Continuous Integration

The platform's engineering rigor includes the application of automated testing and Continuous Integration/Continuous Delivery (CI/CD). This ensures a consistent delivery of high-quality software, faster problem detection, and more productive development cycles. However, it should be noted that while the solution supports automated deployment, it currently does not provide an automatic rollback mechanism.

OpenSPP also supports blackbox testing, a method wherein the functionality of an application is tested without knowledge of its internal structures or workings. This helps identify discrepancies in the system's behavior against expected outcomes. Along with this, the solution ensures high test coverage, guaranteeing that all aspects of the software have been thoroughly tested.

## Deployment Models and Scalability

OpenSPP is equipped to handle various deployment models, including containers and virtual machines. The platform's versatility allows it to adapt to various infrastructure needs, thereby offering more options to organizations in terms of how they wish to run the solution.

The solution is designed with scalability at its core, making it an ideal choice for growing organizations. It can scale up and down with ease to accommodate varying requirements while maintaining the same level of reliability. OpenSPP supports deployment across multiple platforms, such as cloud, on-premise, and hybrid deployments. Moreover, it can manage multiple deployments from a single interface, simplifying the process and increasing efficiency. It also provides tools for monitoring and managing performance across all deployments, ensuring consistent and reliable service levels.

## Integration with CI/CD Tools

OpenSPP integrates seamlessly with popular CI/CD tools through Github Actions. This empowers developers to automate their workflows, making the software development process more efficient. Github Actions facilitates a range of tasks, including building, testing, and deploying software, directly from Github.
