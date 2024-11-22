# ec2_instance_create

A role to create an EC2 instance in AWS.

Users can specify various parameters for instance configuration, including instance type, AMI ID, key pair, tags, and VPC/subnet configuration.

This role also supports the creation of optional networking resources, such as an external security group and an Elastic IP (EIP). You can choose to wait for the EC2 instance to finish booting before continuing.

## Role Variables

The following variables can be set in the role to customize EC2 instance creation and networking configurations:

### Role operation

* **ec2_instance_create_operation**: (Required)
  Whether to create or delete resources using the role. Default is `create`.
  Choices are `create` and `delete`.

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

  * **ec2_instance_create_vpc_id**: (Optional)
  The ID of the VPC used for security group and internet gateway.
  Required if `ec2_instance_create_associate_external_sg` is `true` or `ec2_instance_create_associate_igw` is `true`.

* **ec2_instance_create_external_sg_id**: (Optional)
  The ID or name of the existing security group to be associated with EC2 instance.
  Mutually exclusive with `ec2_instance_create_associate_external_sg`.

* **ec2_instance_create_tags**: (Optional)
  A dictionary of tags to assign to the EC2 instance.

* **ec2_instance_create_wait_for_boot**: (Optional)
  Whether to wait for the EC2 instance to be in the "running" state before continuing. Default is `true`.

### Optional Networking Resources

#### Elastic IP

* **ec2_instance_create_associate_eip**: (Optional)
  Whether to create an Elastic IP (EIP) and associate it with the EC2 instance. Default is `false`.
  If set to `true` and provided VPC doesn't have an Internet Gateway (IGW) attached, please set `ec2_instance_create_associate_igw` to true to avoid failure due to VPC not having IGW attached.

* **ec2_instance_create_eip_tags**: (Optional)
  Tags to assign to the elastic IP.

#### Internet Gateway

* **ec2_instance_create_associate_igw**: (Optional)
  Whether to create and associate an internet gateway with the EC2 instance. Default is `false`.
  If set to `true`, an internet gateway will be created or associated with the instance.

* **ec2_instance_create_igw_tags**: (Optional)
  Tags to assign to the internet gateway.

#### External Security Group

* **ec2_instance_create_associate_external_sg**: (Optional)
  Whether to create and associate a security group with the EC2 instance for external access. Default is `false`.
  If set to `true`, a security group will be created or associated with the instance.
  Mutually exclusive with `ec2_instance_create_external_sg_id`.

* **ec2_instance_create_external_sg_name**: (Optional)
  The name of the security group to create. Default is `ec2_instance_create-default-external-sg`.

* **ec2_instance_create_external_sg_description**: (Optional)
  A description for the security group. Default is `Security group for external access`.

* **ec2_instance_create_external_sg_rules**: (Optional)
  A list of custom rules to add to the security group. Each rule is a dictionary with `proto`, `ports`, and `cidr_ip` keys. Default is to allow SSH (port 22) from `0.0.0.0/0`.

* **ec2_instance_create_sg_tags**: (Optional)
  Tags to assign to the security group.

### Example:

Here's an example of how to use the role in a playbook.

```yaml
---
- name: Playbook for creating EC2 instance using cloud.aws_ops.ec2_instance_create role
  hosts: localhost
  gather_facts: false
  roles:
    - role: cloud.aws_ops.ec2_instance_create
      vars:
          ec2_instance_create_operation: create
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
          ec2_instance_create_associate_external_sg: true
          ec2_instance_create_external_sg_name: my-custom-sg
          ec2_instance_create_external_sg_description: Security group for my custom access
          ec2_instance_create_external_sg_rules:
            - proto: tcp
              ports: "80"
              cidr_ip: "0.0.0.0/0"
          ec2_instance_create_sg_tags:
            Component: my-custom-sg
            Environment: Testing
          # Optionally, enable Elastic IP association
          ec2_instance_create_associate_eip: true
          ec2_instance_create_eip_tags:
            Component: my-custom-eip
            Environment: Testing

License
-------

GNU General Public License v3.0 or later

See [LICENSE](../../LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
