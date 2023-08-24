# cloud.aws_ops.aws_manage_cloudtrail_encryption

A rulebook to ensure continuously running and encrypted Cloudtrail trails using Event Driven Ansible.

This rulebook includes four rules:

1. A rule that matches Cloudtrail events indicating the provided KMS key was deleted or disabled, and re-enables it.
2. A rule that matches Cloudtrail events indicating the provided trail was deleted, and recreates it with encryption using the provided KMS key.
3. A rule that matches Cloudtrail events indicating the provided trail encryption was disabled, and re-enables it with the provided KMS key.
4. A rule that matches Cloudtrail events indicating the provided S3 bucket was deleted, and prints the full event data.

## Requirements

AWS User Account with the following permissions:

* cloudtrail:CreateTrail
* cloudtrail:DescribeTrails
* cloudtrail:GetTrail
* cloudtrail:GetTrailStatus
* cloudtrail:ListTags
* cloudtrail:StartLogging
* cloudtrail:UpdateTrail
* kms:CancelKeyDeletion
* kms:DescribeKey
* kms:EnableKey
* kms:GetKeyPolicy
* kms:GetKeyRotationStatus
* kms:ListAliases
* kms:ListGrants
* kms:ListKeyPolicies
* kms:ListResourceTags
* s3:PutObject
* s3:GetBucketAcl
* s3:PutBucketLogging
* s3:ListBucket

## Rulebook Variables

* **cloudtrail_name** (str): (Required) Name of the Cloudtrail trail to monitor.
* **kms_key_alias** (str): (Required) Alias for the KMS key used to encrypt the trail.
* **s3_bucket_name** (str): (Required) Name of the s3 bucket used to store trail logs.
* **s3_key_prefix** (str): Optional s3 key prefix for trail logs.

## Example Usage

Create an `inventory.yaml` file with the following contents:

```yaml
---
all:
  hosts:
    localhost:
      ansible_connection: local
```

Create a `vars.yaml` file with the required variables:

```yaml
---
cloudtrail_name: your-trail-name
kms_key_alias: your-kms-key
s3_bucket_name: your-s3-bucket
```

With AWS credentials set via ENV or AWS config, run:

```bash
ansible-rulebook -r cloud.aws_ops.aws_manage_cloudtrail_encryption -i inventory.yml -e vars.yml -vv
```

Perform one of the above monitored actions in the AWS console or via CLI or API (delete or disable the KMS key, delete the trail, disable trail encryption, or delete the S3 bucket) and observe the ansible-rulebook runner output to see that the corrective action is taken. Note: it can take some time, up to a few minutes, for the matching Cloudtrail event to be received and processed by the queue.
