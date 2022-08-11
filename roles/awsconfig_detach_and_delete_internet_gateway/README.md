awsconfig_detach_and_delete_internet_gateway
==================

A role to detach and delete the internet gateway you specify from virtual private cloud. If any Amazon EC2 instances in your virtual private cloud (VPC) have elastic IP addresses or public IPv4 addresses associated with them, the role fails.

Requirements
------------

AWS User Account with the following permission:

* ec2:DeleteInternetGateway
* ec2:DescribeInternetGateways
* ec2:DetachInternetGateway

Role Variables
--------------

* **internet_gateway_id**: (Required) The ID of the internet gateway that you want to delete.

Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

Example Playbook
----------------

    - hosts: localhost
      roles:
        - role: cloud.aws_roles.awsconfig_detach_and_delete_internet_gateway
          internet_gateway_id: "igw-053865b26102549d1"

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.azure_roles/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team