customized_ami
=========

A role to create custom AMI on AWS. User can create, update or delete AMI.

Requirements
------------

AWS credentials with valid permission.

Role Variables
--------------

* **custom_ami_operation** (str) - Operation to perform. Valid values are 'create', 'delete'. Default: 'create'.
* **custom_ami_name** (str) - Name of the AMI to create. **Required**
* **custom_ami_packages** (list) - List of packages to install.
* **custom_ami_recreate_if_exists** (bool) - Whether to recreate the AMI if it already exists. Default: False.
* **source_ami_filters** (dict) - A dict of filters to apply to find the source AMI id. See [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html) for possible filters. The following are used by the role, by default:
    **architecture** (str) - Architecture supported by the AMI. Default: 'x86_64'.
    **virtualization-type** (str) - Virtualization supported by the AMI. Default: 'hvm'.
    **root-device-type** (str) - Root Device Type supported by the AMI. Default: 'ebs'
    **name** (str) - Name of the AMI. Default: 'Fedora-Cloud-Base-37-*'
* **source_ami_image_id** (str) - Image id of the AMI to be used as source. When not specified, we will use **source_ami_filters** to determine source AMI image id.
* **source_ami_user_name** (str) - User name to connect to EC2 instance used to create custom AMI. Default value is **ec2-user**. Default: 'fedora'.
* **custom_ami_vpc_cidr** (str) - VPC CIDR for the ec2 instance. Default: '10.1.0.0/16'
* **custom_ami_subnet_cidr** (str) - Subnet CIDR for the ec2 instance. Default: '10.1.0.0/24'
* **custom_ami_ec2_instance_name** (str) - Name of EC2 instance. Default: '{{ custom_ami_name }}-ec2'
* **custom_ami_ec2_instance_type** (str) - EC2 instance type. Default: 't2.large'
* **custom_ami_resource_tags** (dict) - Resouce tags. Default: '{'role': 'customized_ami', 'customized_ami_name': '{{ custom_ami_name }}'}.
* **custom_ami_vpc_name** (str) - Name of VPC. Default: 'vpc-{{ custom_ami_name }}'
* **custom_ami_security_group** (str) - Name of Security Group. Default: 'security-{{ custom_ami_name }}'
* **custom_ami_key_name** (str) - Name of the key pair. Default: 'key-{{ custom_ami_name }}'
* **custom_ami_public_key_file** (str) - Name of the public key file. Default: '~/.ssh/id_rsa.pub'
* **custom_ami_private_key_file** (str) - Name of the private key file. Default: '~/.ssh/id_rsa'
* **custom_ami_security_group_desc** (str) - Description of Security Group. Default: 'Security group allowing SSH connection to EC2 instance'

Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: cloud.aws_ops.customized_ami
           customized_ami_name: my_customized_ami_name
           customized_ami_packages:
            - package1
            - package2
            - package3

License
-------

GNU General Public License v3.0 or later

