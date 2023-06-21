# manage_vpc_peering

A role to create and delete VPC peering connections.

## Specify following values in role vars
- region
- vpc_peering_operation - choices include 'create' and 'delete'
- requester_vpc - ID of the VPC requesting the peering connection.
- accepter_vpc - ID of the VPC accepting the perring connection.
- vpc_peering_conn_id - ID of the VPC peering connection request.

Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

## Example:
```
---
- name: Playbook for managing VPC peering connections using cloud.aws_ops.manage_vpc_peering role
  hosts: localhost
  gather_facts: false
  tasks:
    - ansible.builtin.include_role:
        name: cloud.aws_ops.manage_vpc_peering
      vars:
        region: us-west-1
        requester_vpc: vpc-12345
        accepter_vpc: vpc-98765
        vpc_peering_operation: create

    - ansible.builtin.include_role:
        name: cloud.aws_ops.manage_vpc_peering
      vars:
        region: us-west-1
        vpc_peering_conn_id: pcx-1234567890
        vpc_peering_operation: delete
```

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team