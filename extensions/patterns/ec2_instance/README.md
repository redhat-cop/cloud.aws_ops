# Create EC2 Instance Pattern

## Description

This pattern is designed to help get an EC2 instance up and running.

## What This Pattern Covers

### Projects

- **AWS Operations / EC2 Instance Patterns**: Defined in `setup.yml`, this project helps organize and manage all necessary components for the ec2 creation pattern. It ensures that relevant files, roles, and configurations are logically arranged, making it easier to maintain and execute automation tasks.

### Job Templates

- **AWS Operations / Create EC2 Instance**: This job template is designed to streamline the process of creating an EC2 instance.
- **AWS Operations / Terminate EC2 Instance**: This job template is designed to streamline the process of terminating (deleting) an EC2 instance.

### Playbooks

- **Create EC2 Instance Playbook**: This playbook creates an EC2 instance with optional configurations.
- **Terminate EC2 Instance Job Template**: This playbook terminates (deletes) an existing EC2 instance.

### Surveys

- **Create EC2 Instance Survey**: This survey provides an interactive way to specify parameters for creating the EC2 instance.
- **Terminate EC2 Instance Survey**: This survey provides an interactive way to specify parameters for terminating the EC2 instance.

## Resources Created by This Pattern

1. **Project**
   - Ensures that all relevant files, roles, and configurations are logically arranged, facilitating easier maintenance and execution of automation tasks.

2. **Job Templates**
    - Outline the necessary parameters and configurations to perform network backups using the provided playbooks.
    - Provide surveys for specifying parameters needed to run the job templates.

## How to Use

1. **Use Seed Red Hat Pattern Job**
    - Ensure the custom EE is correctly built and available in your Ansible Automation Platform. Execute the "Seed Red Hat Pattern" job within the Ansible Automation Platform, and select the "AWS Operations" category to load this pattern.

2. **Use the Job Templates**
    - In the `AWS Operations / EC2 Instance Patterns` execute the required job template to create the EC2 instance. Monitor the job execution and verify that the instance has been successfully created.

## Contribution

Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text. This project is licensed under the MIT License. See the [LICENSE](https://github.com/redhat-cop/cloud.aws_ops/blob/main/LICENSE) file for details.
