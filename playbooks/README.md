# cloud.aws_ops playbooks

## EDA playbooks

Playbooks to restore canceled or deleted cloudtrail resources, intended for use with the EDA [aws_manage_cloudtrail_encryption rulebook](../extensions/eda/rulebooks/AWS_MANAGE_CLOUDTRAIL_ENCRYPTION.md)

* **aws_restore_cloudtrail_encryption**: Playbook to restore encryption to an existing AWS Cloudtrail trail using the [enable_cloudtrail_encryption_with_kms role](../roles/enable_cloudtrail_encryption_with_kms/README.md).
* **aws_restore_cloudtrail**: Playbook to re-create and encrypt a deleted AWS Cloudtrail trail using the [awsconfig_multiregion_cloudtrail](../roles/awsconfig_multiregion_cloudtrail/README.md) and [enable_cloudtrail_encryption_with_kms](../roles/enable_cloudtrail_encryption_with_kms/README.md) roles.
* **aws_restore_kms_key**: Playbook to cancel deletion of a KMS key and re-enable it.

## Webapp playbooks

Playbooks to create, delete, or migrate a webapp on AWS. See [webapp playbooks README](webapp/README.md) for details and usage.
