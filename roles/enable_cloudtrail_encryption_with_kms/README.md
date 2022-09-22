Role Name
=========

A role to encrypts an AWS CloudTrail (CloudTrail) trail using the AWS Key Management Service (AWS KMS) customer managed key you specify.

Requirements
------------

N/A

Role Variables
--------------

**enable_cloudtrail_encryption_with_kms_trail_name**: (Required) The ARN or name of the trail you want to update to be encrypted.
**enable_cloudtrail_encryption_with_kms_kms_key_id**: (Required) The ARN, key ID, or the key alias of the of the customer managed key you want to use to encrypt the trail you specify in the TrailName parameter.
**enable_cloudtrail_encryption_with_kms_automation_assume_role**: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf.

Dependencies
------------

- role: aws_setup_credentials

Example Playbook
----------------

    - hosts: localhost

      roles:
        - role: enable_cloudtrail_encryption_with_kms:
          enable_cloudtrail_encryption_with_kms_trail_name: ""
          enable_cloudtrail_encryption_with_kms_kms_key_id: ""
          enable_cloudtrail_encryption_with_kms_automation_assume_role: ""

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.azure_roles/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team