# ec2_create_instance

A role to create an EC2 instance in AWS.

Users can specify various parameters for instance configuration, including instance type, AMI ID, key pair, tags, and VPC/subnet configuration.

This role also supports the creation of optional networking resources, such as a VPC, subnet, security group, and Elastic IP. You can choose to wait for the EC2 instance to finish booting before continuing.

## Specify the following values in role vars

### Role Variables
--------------

* **ec2_create_instance_aws_region**: (Required)
  The AWS region in which to create the EC2 instance.

* **ec2_create_instance_instance_name**: (Required)
  The name of the EC2 instance to be created.

* **ec2_create_instance_instance_type**: (Required)
  The instance type for the EC2 instance (e.g., `t2.micro`, `m5.large`).

* **ec2_create_instance_ami_id**: (Required)
  The AMI ID for the EC2 instance.

* **ec2_create_instance_key_name**: (Required)
  The name of the key pair to use for SSH access to the EC2 instance.

* **ec2_create_instance_vpc_subnet_id**: (Required)
  The ID of the VPC subnet in which the instance will be launched.

* **ec2_create_instance_tags**: (Optional)
  A dictionary of tags to assign to the EC2 instance.

* **ec2_create_instance_wait_for_boot**: (Optional)
  Whether to wait for the EC2 instance to be in the "running" state before continuing. Default is `true`.

* **ec2_create_instance_associate_eip**: (Optional)
  Whether to create an Elastic IP (EIP) and associate it with the EC2 instance. Default is `false`.


Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

## Example:
```
---
- name: Playbook for creating ec2 instances using cloud.aws_ops.ec2_create_instance role
  hosts: localhost
  gather_facts: false
  roles:
    - role: cloud.aws_ops.ec2_create_instance
      vars:
          ec2_create_instance_aws_region: us-west-2
          ec2_create_instance_instance_name: my-test-instance
          ec2_create_instance_instance_type: t2.micro
          ec2_create_instance_ami_id: ami-066a7fbaa12345678
          ec2_create_instance_vpc_subnet_id: subnet-071443aa123456789
          ec2_create_instance_tags:
            Environment: Testing
          ec2_create_instance_wait_for_boot: true
```

License
-------

GNU General Public License v3.0 or later

See [LICENSE](../../LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
