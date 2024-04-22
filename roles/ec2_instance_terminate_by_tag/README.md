# ec2_instance_terminate_by_tag

A role to terminate the ec2_instances having a specific tag.
User can specify a tag key-value pair for which the ec2 instances with matching tag key-value pair will be terminated.

Instances with termination_protection enabled will not be terminated.
To terminate instances with termination_protection enabled, please set `terminate_protected_instances` to `True`.

## Specify following values in role vars
- ec2_instance_terminate_by_tag_tag_key_to_terminate_instances
- ec2_instance_terminate_by_tag_tag_value_to_terminate_instances
- ec2_instance_terminate_by_tag_terminate_protected_instances

## Role and instances in a AutoScalingGroup (ASG)

This role will terminate the instances with the specified tag even if they are a part of an ASG.

## Role and instances with attached EBS volumes

The attached EBS volumes to the instances are deleted when instance is terminated if `Delete on Termination` is set to `True`.
If `Delete on Termination` is set to `False`, the volume will be detached from the instance and will not be deleted.

Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

## Example:
```
---
- name: Playbook for terminating instances using cloud.aws_ops.ec2_instance_terminate_by_tag role
  hosts: localhost
  gather_facts: false
  roles:
    - role: cloud.aws_ops.ec2_instance_terminate_by_tag
      vars:
          ec2_instance_terminate_by_tag_tag_key_to_terminate_instances: instances-to-terminate
          ec2_instance_terminate_by_tag_tag_value_to_terminate_instances: "True"
          ec2_instance_terminate_by_tag_terminate_protected_instances: True
```

License
-------

GNU General Public License v3.0 or later

See [LICENCE](../../LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team
