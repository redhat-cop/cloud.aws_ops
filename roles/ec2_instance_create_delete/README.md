# ec2_instance_create

A role to create an EC2 instance in AWS.

Users can specify various parameters for instance configuration, including instance type, AMI ID, key pair, tags, and VPC/subnet configuration.

This role also supports the creation of optional networking resources, such as an external security group and an Elastic IP (EIP). You can choose to wait for the EC2 instance to finish booting before continuing.

## Role Variables

The following variables can be set in the role to customize EC2 instance creation and networking configurations:

### Role Operation

* **ec2_instance_create_delete_operation**: (Optional)
  - Goal state for the instances.
  - "O(state=present): ensures instances exist, but does not guarantee any state (e.g. running). Newly-launched instances will be run by EC2."
  - "O(state=running): O(state=present) + ensures the instances are running."
  - "O(state=started): O(state=running) + waits for EC2 status checks to report OK if O(wait=true)."
  - "O(state=stopped): ensures an existing instance is stopped."
  - "O(state=rebooted): convenience alias for O(state=stopped) immediately followed by O(state=running)."
  - "O(state=restarted): convenience alias for O(state=stopped) immediately followed by O(state=started)."
  - "O(state=terminated): ensures an existing instance is terminated."
  - "O(state=absent): alias for O(state=terminated)."
  choices are [present, terminated, running, started, stopped, restarted, rebooted, absent]
  Default is `present`.

### EC2 Instance Configuration

* **ec2_instance_create_delete_aws_region**: (Required)
  The AWS region in which to create the EC2 instance.

* **ec2_instance_create_delete_instance_name**: (Required)
  The name of the EC2 instance to be created.

* **ec2_instance_create_delete_instance_type**: (Required)
  The instance type for the EC2 instance (e.g., `t2.micro`, `m5.large`).

* **ec2_instance_create_delete_ami_id**: (Required)
  The AMI ID for the EC2 instance.

* **ec2_instance_create_delete_key_name**: (Optional)
  The name of the key pair to use for SSH access to the EC2 instance.
  If the key does not exist, a key pair will be created with the name.

* **ec2_instance_create_delete_vpc_subnet_id**: (Optional)
  The ID of the VPC subnet in which the instance will be launched.
  If not provided, instance might get created with `default` subnet in the AWS region if present.

* **ec2_instance_create_delete_tags**: (Optional)
  A dictionary of tags to assign to the EC2 instance.

* **ec2_instance_create_delete_wait_for_boot**: (Optional)
  Whether to wait for the EC2 instance to be in the "running" or "terminated" state before continuing. Default is `true`.

### Optional Networking Resources

#### Elastic IP

* **ec2_instance_create_delete_vpc_id**: (Optional)
  The ID of the VPC used for security group and internet gateway.
  Required if `ec2_instance_create_delete_associate_igw` or `ec2_instance_create_delete_associate_eip` is `true`.

* **ec2_instance_create_delete_associate_eip**: (Optional)
  Whether to create an Elastic IP (EIP) and associate it with the EC2 instance. Default is `false`.
  If set to `true` and the provided VPC doesn't have an Internet Gateway (IGW) attached, set `ec2_instance_create_delete_associate_igw` to `true` to avoid failure.

* **ec2_instance_create_delete_eip_tags**: (Optional)
  Tags to assign to the elastic IP.

#### Internet Gateway

* **ec2_instance_create_delete_associate_igw**: (Optional)
  Whether to create and associate an internet gateway with the EC2 instance. Default is `false`.
  If set to `true`, an internet gateway will be created or associated with the instance.

* **ec2_instance_create_delete_igw_tags**: (Optional)
  Tags to assign to the internet gateway.

#### External Security Group

* **ec2_instance_create_delete_associate_external_sg**: (Optional)
  Whether to create and associate an security group with the EC2 instance. Default is `false`.
  If set to `true`, an security group will be created or associated with the instance.

* **ec2_instance_create_delete_external_sg_name**: (Required)
  The name of the security group to use for the EC2 instance.
  The role will check if an SG with this name exists. If not, it will create a new one.
  Default is `ec2_instance_create-default-external-sg`.

* **ec2_instance_create_delete_external_sg_description**: (Optional)
  A description for the security group. Default is `Security group for external access`.

* **ec2_instance_create_delete_external_sg_rules**: (Optional)
  A list of custom rules to add to the security group. Each rule is a dictionary with `proto`, `ports`, and `cidr_ip` keys. Default is to allow SSH (port 22) from `0.0.0.0/0`.

* **ec2_instance_create_delete_external_sg_tags**: (Optional)
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
          ec2_instance_create_delete_operation: present
          ec2_instance_create_delete_aws_region: us-west-2
          ec2_instance_create_delete_instance_name: my-test-instance
          ec2_instance_create_delete_instance_type: t2.micro
          ec2_instance_create_delete_ami_id: ami-066a7fbaa12345678
          ec2_instance_create_delete_vpc_subnet_id: subnet-071443aa123456789
          ec2_instance_create_delete_tags:
            Component: my-test-instance
            Environment: Testing
          ec2_instance_create_delete_wait_for_boot: true
          ec2_instance_create_delete_vpc_id: vpc-xxxx
          # Optionally, enable security group creation
          ec2_instance_create_delete_associate_external_sg: true
          ec2_instance_create_delete_external_sg_name: my-custom-sg
          ec2_instance_create_delete_external_sg_description: Security group for my custom access
          ec2_instance_create_delete_external_sg_rules:
            - proto: tcp
              ports: "80"
              cidr_ip: "0.0.0.0/0"
          ec2_instance_create_delete_external_sg_tags:
            Component: my-custom-sg
            Environment: Testing
          # Optionally, enable Elastic IP association
          ec2_instance_create_delete_associate_eip: true
          ec2_instance_create_delete_eip_tags:
            Component: my-custom-eip
            Environment: Testing
          # Optionally, enable Internet Gateway association
          ec2_instance_create_delete_associate_igw: true
          ec2_instance_create_delete_igw_tags:
            Environment: Testing
            Name: "{{ resource_prefix }}-igw"

---
- name: Playbook for deleting EC2 instance and other role resources using cloud.aws_ops.ec2_instance_create role
  hosts: localhost
  gather_facts: false
  roles:
    - role: cloud.aws_ops.ec2_instance_create
      vars:
          ec2_instance_create_delete_operation: absent
          ec2_instance_create_delete_aws_region: us-west-2
          ec2_instance_create_delete_instance_name: my-test-instance
          ec2_instance_create_delete_wait_for_boot: true
          ec2_instance_create_delete_associate_external_sg: true
          ec2_instance_create_delete_external_sg_name: my-custom-sg
          ec2_instance_create_delete_associate_igw: true
          ec2_instance_create_delete_vpc_id: vpc-xxxx

License
-------

GNU General Public License v3.0 or later

See [LICENSE](../../LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
