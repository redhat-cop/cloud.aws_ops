backup_create_plan
==================

A role to create a backup plan and optionally a vault. A set of variables for plan rules is included for use as-is or as examples for modification. This role can be combined with the backup_select_resources role to back up a selection of resources.

Requirements
------------

AWS User Account with the following permission:

* backup:CreateBackupVault
* backup:CreateBackupPlan
* backup:DescribeBackupVault
* backup:ListBackupPlans
* backup:ListTags
* backup-storage:MountCapsule
* kms:CreateGrant
* kms:GenerateDataKey
* kms:Decrypt
* kms:RetireGrant
* kms:DescribeKey

Role Variables
--------------

* **plan_name**: (Required) The name of the backup plan you want to create
* **plan_rules**: (Required) A set of rules for the backup, as a list of dicts
* **plan_windows_vss_settings**: Optional settings for Windows VSS backup, see [AdvancedBackupSetting object in the AWS Backup API documentation](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_AdvancedBackupSetting.html) for details
* **plan_tags**: Optional tags to apply to all backups created with the plan
* **vault_name**: The name of the vault you want to use or create. If not provided, will use the default backup vault for the account
* **vault_encryption_key_arn**: Optional ARN of key to use for vault encryption
* **vault_tags**: Optional tags to apply to the vault

Dependencies
------------

* role: [aws_setup_credentials](../aws_setup_credentials/README.md)

Example Playbook
----------------

    - hosts: localhost
      roles:
        - role: cloud.aws_ops.backup_create_plan
          plan_name: my-backup-plan
          plan_rules: "{{ daily_backup }}"

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

* Ansible Cloud Content Team
