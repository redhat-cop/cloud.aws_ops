ec2_instance_terminate_by_id
==================

A role to terminate the ec2_instances having a specific tag.
User can specify a tag key-value pair for which the ec2 instances with matching tag key-value pair
will be terminated.

Instances with termination_protection enabled will not be terminated.
To terminate instances with termination_protection enabled, please set `terminate_termination_protected_instances` to `True`.

Specify following values in role vars

tag_key_to_terminate_instances
tag_value_to_terminate_instances
terminate_termination_protected_instances

example:

---
- name: Playbook for testing cloud.aws_roles.ec2_instance_terminate_by_tag role
  hosts: localhost
  gather_facts: false
  roles:
    - role: cloud.aws_roles.ec2_instance_terminate_by_tag
      vars:
          tag_key_to_terminate_instances: instances-to-terminate
          tag_value_to_terminate_instances: "True"
          terminate_termination_protected_instances: True
