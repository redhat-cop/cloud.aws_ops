Role Name
=========

A role to validate input parameters for troubleshoot_connectivity_* roles and return connection next hop.

Requirements
------------

N/A

Role Variables
--------------

**connectivity_troubleshooter_validate_destination_ip**: (Required) The IPv4 address of the resource you want to connect to.
**connectivity_troubleshooter_validate_destination_port**: (Required) The port number you want to connect to on the destination resource.
**connectivity_troubleshooter_validate_source_ip**: (Required) The private IPv4 address of the AWS resource in your Amazon VPC you want to test connectivity from.
**connectivity_troubleshooter_validate_source_vpc**: (Optional) The ID of the Amazon VPC you want to test connectivity from.


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

  - hosts: localhost
    
    roles
      - role: connectivity_troubleshooter_validate
        connectivity_troubleshooter_validate_destination_ip: 172.31.2.8
        connectivity_troubleshooter_validate_destination_port: 443
        connectivity_troubleshooter_validate_source_ip: 172.31.2.7

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_roles/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
