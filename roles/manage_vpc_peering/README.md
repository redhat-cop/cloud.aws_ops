# manage_vpc_peering

A role to create and delete VPC peering connections.

currently works for VPCs under same account and same region.

## Specify following values in role vars

- region - Region of the requester VPC (region in which VPC peering connection request resides when performing a delete operation)

- requester_vpc - ID of the VPC requesting the peering connection.

- accepter_vpc - ID of the VPC accepting the perring connection.

- accepter_vpc_region - Region of the accepter VPC (Required if requester and accepter VPCs are in different regions and performing cross-region peering.)

- accepter_vpc_account_id - The AWS account number of accepter VPC account for cross account peering.

- accepter_account_profile - A Named AWS profile of accepter VPC account for cross account peering.

- vpc_peering_operation - Choices include 'create', 'delete', and 'accept'.

- vpc_peering_conn_id - ID of the VPC peering connection request (only provide to delete a VPC peering connection).

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
    - name: Peer VPCs in same account and region (local)
      ansible.builtin.include_role:
        name: cloud.aws_ops.manage_vpc_peering
      vars:
        region: us-west-1
        requester_vpc: vpc-12345
        accepter_vpc: vpc-98765
        vpc_peering_operation: create

    - name: Peer VPCs in same account and different region (local cross-region)
      ansible.builtin.include_role:
        name: cloud.aws_ops.manage_vpc_peering
      vars:
        region: us-west-1
        requester_vpc: vpc-12345
        accepter_vpc: vpc-98765
        accepter_vpc_region: ap-northeast-3
        vpc_peering_operation: create

    - name: Peer VPCs in same account and different region (cross-account)
      ansible.builtin.include_role:
        name: cloud.aws_ops.manage_vpc_peering
      vars:
        region: us-west-1
        requester_vpc: vpc-12345
        accepter_vpc: vpc-98765
        accepter_vpc_region: ap-northeast-3
        accepter_vpc_account_id: 1234567890
        accepter_account_profile: my-account-profile
        vpc_peering_operation: create

    - name: Delete VPC peering request
      ansible.builtin.include_role:
        name: cloud.aws_ops.manage_vpc_peering
      vars:
        region: us-west-1
        vpc_peering_conn_id: pcx-1234567890
        vpc_peering_operation: delete

    - name: Accept existing VPC peering request (local account)
      ansible.builtin.include_role:
        name: cloud.aws_ops.manage_vpc_peering
      vars:
        region: us-west-1
        vpc_peering_conn_id: pcx-1234567890
        vpc_peering_operation: accept

    - name: Accept existing VPC peering request (another account)
      ansible.builtin.include_role:
        name: cloud.aws_ops.manage_vpc_peering
      vars:
        region: us-west-1
        vpc_peering_conn_id: pcx-1234567890
        vpc_peering_operation: accept
        accepter_vpc_account_id: 1234567890
        accepter_account_profile: my-account-profile
```

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
