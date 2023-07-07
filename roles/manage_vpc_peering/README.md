# manage_vpc_peering

A role to create, delete and accept existing VPC peering connections.

## Specify following values in role vars

- region - Region of the requester VPC.

- requester_vpc - ID of the VPC requesting the peering connection.

- accepter_vpc - ID of the VPC accepting the peering connection.

- accepter_vpc_region - Region of the accepter VPC (Required if requester and accepter VPCs are in different regions or performing cross-account peering.)

- accepter_vpc_account_id - The AWS account ID of accepter VPC account for cross-account peering.

- accepter_account_profile - A Named AWS profile of accepter VPC account for cross-account peering.

- vpc_peering_operation - Choices include 'create', 'delete', and 'accept'.

- vpc_peering_conn_id - ID of the VPC peering connection request (only provide to delete a VPC peering connection).

Return Value
------------
On successful creation of peering connection request, the peering connection ID can be accessed using the variable `peering_request_id` set during the role execution.

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

    - name: Set variable for peering connection ID for above task
      ansible.builtin.set_fact:
        peering_id_1: "{{ peering_request_id }}"

    - name: Peer VPCs in same account and different region (local cross-region)
      ansible.builtin.include_role:
        name: cloud.aws_ops.manage_vpc_peering
      vars:
        region: us-west-1
        requester_vpc: vpc-12345
        accepter_vpc: vpc-98765
        accepter_vpc_region: ap-northeast-3
        vpc_peering_operation: create

    - name: Peer VPCs in different accounts and different region (cross-account)
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
