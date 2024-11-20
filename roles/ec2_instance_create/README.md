# ec2_instance_create

A role to create an EC2 instance in AWS.

Users can specify various parameters for instance configuration, including instance type, AMI ID, key pair, tags, and VPC/subnet configuration.

This role also supports the creation of optional networking resources, such as a security group and an Elastic IP (EIP). You can choose to wait for the EC2 instance to finish booting before continuing.

## Role Variables

The following variables can be set in the role to customize EC2 instance creation and networking configurations:

### EC2 Instance Configuration

* **ec2_instance_create_aws_region**: (Required)
  The AWS region in which to create the EC2 instance.

* **ec2_instance_create_instance_name**: (Required)
  The name of the EC2 instance to be created.

* **ec2_instance_create_instance_type**: (Required)
  The instance type for the EC2 instance (e.g., `t2.micro`, `m5.large`).

* **ec2_instance_create_ami_id**: (Required)
  The AMI ID for the EC2 instance.

* **ec2_instance_create_key_name**: (Required)
  The name of the key pair to use for SSH access to the EC2 instance.

* **ec2_instance_create_vpc_subnet_id**: (Required)
  The ID of the VPC subnet in which the instance will be launched.

* **ec2_instance_create_tags**: (Optional)
  A dictionary of tags to assign to the EC2 instance.

* **ec2_instance_create_wait_for_boot**: (Optional)
  Whether to wait for the EC2 instance to be in the "running" state before continuing. Default is `true`.

### Optional Networking Resources

* **ec2_instance_create_associate_eip**: (Optional)
  Whether to create an Elastic IP (EIP) and associate it with the EC2 instance. Default is `false`.

* **ec2_instance_create_associate_sg**: (Optional)
  Whether to create and associate a security group with the EC2 instance for external access. Default is `false`.
  If set to `true`, a security group will be created or associated with the instance.

* **ec2_instance_create_sg_name**: (Optional)
  The name of the security group to create. Default is `default-external-sg`.

* **ec2_instance_create_sg_description**: (Optional)
  A description for the security group. Default is `Security group for external access`.

* **ec2_instance_create_sg_ssh_port**: (Optional)
  The SSH port to open in the security group. Default is `22`.

* **ec2_instance_create_sg_http_port**: (Optional)
  The HTTP port to open in the security group. Default is `80`.

* **ec2_instance_create_sg_https_port**: (Optional)
  The HTTPS port to open in the security group. Default is `443`.

* **ec2_instance_create_sg_tags**: (Optional)
  Tags to assign to the security group.

### Example:

Here’s an example of how to use the role in a playbook.

```yaml
---
- name: Playbook for creating EC2 instance using cloud.aws_ops.ec2_instance_create role
  hosts: localhost
  gather_facts: false
  roles:
    - role: cloud.aws_ops.ec2_instance_create
      vars:
          ec2_instance_create_aws_region: us-west-2
          ec2_instance_create_instance_name: my-test-instance
          ec2_instance_create_instance_type: t2.micro
          ec2_instance_create_ami_id: ami-066a7fbaa12345678
          ec2_instance_create_vpc_subnet_id: subnet-071443aa123456789
          ec2_instance_create_tags:
            Component: my-test-instance
            Environment: Testing
          ec2_instance_create_wait_for_boot: true
          # Optionally, enable security group creation
          ec2_instance_create_associate_sg: true
          ec2_instance_create_sg_name: my-custom-sg
          ec2_instance_create_sg_description: Security group for my custom access
          ec2_instance_create_sg_ssh_port: 22
          ec2_instance_create_sg_http_port: 80
          ec2_instance_create_sg_https_port: 443
          ec2_instance_create_sg_tags:
            Component: my-custom-sg
            Environment: Testing
          # Optionally, enable Elastic IP association
          ec2_instance_create_associate_eip: true
          ec2_instance_create_eip_release_on_disassociation: true
              ec2_instance_create_eip_tags:
                Component: my-test-eip
                Environment: Testing

License
-------

GNU General Public License v3.0 or later

See [LICENSE](../../LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team