Role Name
=========

A role to troubleshoot connectivity issues between AWS resources in different Amazon VPCs within the same AWS Region that are connected using VPC peering.

Requirements
------------

N/A

Role Variables
--------------

**connectivity_troubleshooter_peering_destination_ip**: (Required) The IPv4 address of the resource you want to connect to.
**connectivity_troubleshooter_peering_destination_port**: (Required) The port number you want to connect to on the destination resource.
**connectivity_troubleshooter_peering_destination_vpc**: (Optional) The ID of the Amazon VPC you want to test connectivity to.
**connectivity_troubleshooter_peering_source_ip**: (Required) The private IPv4 address of the AWS resource in your Amazon VPC you want to test connectivity from.
**connectivity_troubleshooter_peering_source_vpc**: (Optional) The ID of the Amazon VPC you want to test connectivity from.

Dependencies
------------

N/A

Example Playbook
----------------

    - hosts: localhost

      roles:
        - role: cloud.aws_roles.connectivity_troubleshooter_peering:
          cconnectivity_troubleshooter_peering_destination_ip: 172.31.2.8
          connectivity_troubleshooter_peering_destination_port: 443
          connectivity_troubleshooter_peering_source_ip: 172.31.2.7

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_roles/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
