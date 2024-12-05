# ec2_instance_create

A role to create an EC2 instance in AWS.

Users can specify various parameters for instance configuration, including instance type, AMI ID, key pair, tags, VPC/subnet configuration, and whether to associate an EIP. You can choose to wait for the EC2 instance to finish booting before continuing.

This role can be combined with the [cloud.aws_ops.ec2_networking_resources role](../ec2_networking_resources/README.md) to create networking resources for the instance, see [examples](#examples).

## Requirements

An AWS account with the following permissions:

* ec2:AllocateAddress
* ec2:AssociateAddress
* ec2:CreateKeyPair
* ec2:DeleteKeyPair
* ec2:DescribeAddresses
* ec2:DescribeInstanceAttribute
* ec2:DescribeInstances
* ec2:DescribeInstanceStatus
* ec2:DescribeKeyPairs
* ec2:DescribeSecurityGroups
* ec2:DescribeSubnets
* ec2:DescribeVpcs
* ec2:DisassociateAddress
* ec2:ModifyInstanceAttribute
* ec2:ReleaseAddress
* ec2:RunInstances
* ec2:TerminateInstances

## Role Variables

The following variables can be set in the role to customize EC2 instance creation and networking configurations:

* **ec2_instance_create_delete_operation**: (Optional)
  Target operation for the ec2 instance role. Choices are ["create", "delete"]. Defaults to "create".

* **ec2_instance_create_delete_instance_name**: (Required)
  The name of the EC2 instance to be created.

* **ec2_instance_create_delete_instance_type**: (Optional)
  The instance type for the EC2 instance (e.g., `t2.micro`, `m5.large`). Required when `ec2_instance_create_delete_operation` is `create`

* **ec2_instance_create_delete_ami_id**: (Optional)
  The AMI ID for the EC2 instance. Required when `ec2_instance_create_delete_operation` is `create`

* **ec2_instance_create_delete_key_name**: (Optional)
  The name of the key pair to use for SSH access to the EC2 instance.
  If the key does not exist, a key pair will be created with the name.
  If not provided, instance will not be accessible via SSH.
  If provided when `ec2_instance_create_delete_operation` is `delete`, the keypair will also be deleted.

* **ec2_instance_create_delete_vpc_subnet_id**: (Optional)
  The ID of the VPC subnet in which the instance will be launched.
  If not provided, instance will be created in the default subnet for the default VPC in the AWS region if present.

* **ec2_instance_create_delete_tags**: (Optional)
  A dictionary of tags to assign to the EC2 instance.

* **ec2_instance_create_delete_wait_for_state**: (Optional)
  Whether to wait for the EC2 instance to be in the "running" (if creating an instance) or "terminated" (if deleting an instance) state before continuing. Default is `true`.

* **ec2_instance_create_delete_associate_security_groups**: (Optional)
  List of security group IDs to associate with the EC2 instance.

* **ec2_instance_create_delete_associate_eip**: (Optional)
  Whether to create an Elastic IP (EIP) and associate it with the EC2 instance. Default is `false`.
  If true, EC2 instance must be launched in a VPC with an Internet Gateway (IGW) attached, otherwise this will fail. Use [cloud.aws_ops.ec2_networking_resources role](../ec2_networking_resources/README.md) to create the necessary networking resources.

* **ec2_instance_create_delete_eip_tags**: (Optional)
  Tags to assign to the elastic IP.

## Dependencies

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

## Examples

Using the role on its own in a playbook:

```yaml
---
- name: Create EC2 instance
  hosts: localhost
  gather_facts: false
  roles:
    - role: cloud.aws_ops.ec2_instance_create
      vars:
          ec2_instance_create_delete_operation: present
          ec2_instance_create_delete_aws_region: us-west-2
          ec2_instance_create_delete_instance_name: my-test-instance
          ec2_instance_create_delete_instance_type: t2.micro
          ec2_instance_create_delete_ami_id: ami-066a7fbaa12345678
          ec2_instance_create_delete_vpc_subnet_id: subnet-071443aa123456789
          ec2_instance_create_delete_tags:
            Component: my-test-instance
            Environment: Testing
          ec2_instance_create_delete_wait_for_state: true
```

Combining the role with [cloud.aws_ops.ec2_networking_resources](../ec2_networking_resources/README.md):

```yaml
---
- name: Create EC2 networking resources and EC2 instance
  hosts: localhost
  gather_facts: false
  roles:
    - role: cloud.aws_ops.ec2_networking_resources:
      vars:
        ec2_networking_resources_vpc_name: my-vpc
        ec2_networking_resources_vpc_cidr_block: 10.0.0.0/24
        ec2_networking_resources_subnet_cidr_block: 10.0.0.0/25
        ec2_networking_resources_sg_internal_name: my-internal-sg
        ec2_networking_resources_sg_external_name: my-external-sg
        ec2_networking_resources_create_igw: true
    - role: cloud.aws_ops.ec2_instance_create
      vars:
        ec2_instance_create_delete_operation: present
        ec2_instance_create_delete_instance_name: my-test-instance
        ec2_instance_create_delete_instance_type: t2.micro
        ec2_instance_create_delete_ami_id: ami-066a7fbaa12345678
        ec2_instance_create_delete_vpc_subnet_id: "{{ ec2_networking_resources_subnet_result.subnet.id }}"
        ec2_instance_create_delete_associate_security_groups:
          - my-internal-sg
          - my-external-sg
        ec2_instance_create_delete_associate_eip: true
```

Deleting an EC2 instance:

```yaml
---
- name: Delete EC2 instance
  hosts: localhost
  gather_facts: false
  roles:
    - role: cloud.aws_ops.ec2_instance_create_delete
      vars:
          ec2_instance_create_delete_operation: delete
          ec2_instance_create_delete_instance_name: my-test-instance
          ec2_instance_create_delete_wait_for_state: true
```

## License

GNU General Public License v3.0 or later

See [LICENSE](../../LICENSE) to see the full text.

## Author Information

- Ansible Cloud Content Team
