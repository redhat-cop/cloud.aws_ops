backup_select_resources
==================

A role to configure backups for selected resources. The role requires an existing backup vault and plan, and adds selected resources to the provided plan. A set of variables for resource selections is included for use as-is or as examples for modification. This role can be combined with the backup_plan_create role to create or update a backup plan if one does not already exist.

Requirements
------------

AWS User Account with the following permission:

* backup:CreateBackupSelection
* backup:DeleteBackupSelection
* backup:GetBackupPlan
* backup:GetBackupSelection
* backup:ListBackupSelections
* iam:GetRole

Role Variables
--------------

* **plan_name**: (Required) The name of the backup plan you want to use for the selected resources.
* **selection_name**: (Required) The display name of the resource selection you want to back up.
* **selection_resources**: (Required) List of resources selected for backup. Can use wild cards and/or combine with selection options below to precisely restrict resources based on various conditions. See included vars for examples.
* **selection_excluded_resources**: List of resources to exclude from backup
* **selection_tags**: List of resource tags selected for backup
* **selection_conditions**: Conditions for resources to back up
* **backup_role_name**: The name of an IAM role with permissions to perform all needed backup actions for the selected resources. If not provided, the role will use the AWSBackupDefaultServiceRole for the account (note: this will fail if the default role has not been created in the AWS console).

Dependencies
------------

* role: [aws_setup_credentials](../aws_setup_credentials/README.md)

Example Playbook
----------------

    - hosts: localhost
      roles:
        - role: cloud.aws_ops.backup_select_resources
          vars:
            plan_name: daily-backup
            selection_name: s3_buckets
            selection_resources:
              - "{{ all_s3_buckets }}"

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

* Ansible Cloud Content Team
