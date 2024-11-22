# Create EC2 Instance Experience

## Description

This experience is designed to help get an EC2 instance up and running.

## What This Experience Covers

### Project Templates

- **Create EC2 Instance Template**: Defined in `setup.yml`, this template helps organize and manage all necessary components for the ec2 creation experience. It ensures that relevant files, roles, and configurations are logically arranged, making it easier to maintain and execute automation tasks.

### Job Templates

- **Create EC2 Instance Job Template**: This template is designed to streamline the process of creating and EC2 instance.

### Playbooks

- **Playbooks**:

### Surveys

- **Create EC2 Instance Survey**: This survey provides an interactive way to specify parameters for creating the EC2 instance.

## Resources Created by This Experience

1. **Project Templates**
   - Ensure that all relevant files, roles, and configurations are logically arranged, facilitating easier maintenance and execution of automation tasks.

2. **Job Templates**
    - Outline the necessary parameters and configurations to perform network backups using the provided playbooks.

## How to Use

1. **Use Seed Red Hat Experience Job**
    - Ensure the custom EE is correctly built and available in your Ansible Automation Platform. Execute the "Seed Red Hat Experience" job within the Ansible Automation Platform, and select the "AWS Operations" category to load this experience.

2. **Use the Job Templates**
    - In the `Create EC2 Instance Automation Experience Project` execute the required job template to create the EC2 instance. Monitor the job execution and verify that the instance has been successfully created.

## Contribution

Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text. This project is licensed under the MIT License. See the [LICENSE](https://github.com/redhat-cop/cloud.aws_ops/blob/main/LICENSE) file for details.
