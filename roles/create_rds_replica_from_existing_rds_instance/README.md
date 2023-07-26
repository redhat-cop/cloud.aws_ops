move_objects_between_buckets
==================

A role to set up an RDS read replica from an existing RDS instance.

Requirements
------------

AWS User Account with the following permission:

* s3:HeadBucket
* s3:GetBucketOwnershipControls
* s3:ListObjectsV2
* s3:ListBucket
* s3:DeleteObject
* s3:HeadObject
* s3:PutObjectAcl
* s3:CopyObject
* s3:GetObjectTagging
* s3:DeleteBucket

Role Variables
--------------

* **source_bucket**: The name of the Amazon S3 bucket that will have its objects retrieved and then emptied. **Required**
* **dest_bucket**: The name of the Amazon S3 bucket that will receive the objects. **Required**
* **key_prefix**: limits objects that begin with the specified prefix. Default value is **""**.
* **delete_empty_source_bucket**: deletes source bucket after all objects have been transferred to destination bucket. Default value is **false**.

Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

## Example:
```
---
- name: Playbook for move objects between buckets using cloud.aws_ops.move_objects_between_buckets role
  hosts: localhost
  gather_facts: false
  tasks:
```

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team