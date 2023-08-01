move_objects_between_buckets
==================

A role to move objects from one S3 Bucket to another.
Objects have two options: all objects can be transferred or specific objects are transferred through key prefix.
If the source bucket is empty, the user has two options: source bucket is deleted or source bucket is kept as an empty bucket.

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

* **move_objects_between_buckets_source_bucket**: The name of the Amazon S3 bucket that will have its objects retrieved and then emptied. **Required**
* **move_objects_between_buckets_dest_bucket**: The name of the Amazon S3 bucket that will receive the objects. **Required**
* **move_objects_between_buckets_key_prefix**: limits objects that begin with the specified prefix. Default value is **""**.
* **move_objects_between_buckets_delete_empty_source_bucket**: deletes source bucket after all objects have been transferred to destination bucket. Default value is **false**.

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
    - name: Move objects that have prefix "template" between buckets
      ansible.builtin.include_role:
        name: cloud.aws_ops.move_objects_between_buckets
      vars:
        move_objects_between_buckets_source_bucket: mybucket_name-src
        move_objects_between_buckets_dest_bucket: mybucket_name-dest
        move_objects_between_buckets_key_prefix: "template"
    
    - name: Move all objects between buckets
      ansible.builtin.include_role:
        name: cloud.aws_ops.move_objects_between_buckets
      vars:
        move_objects_between_buckets_source_bucket: mybucket_name-src
        move_objects_between_buckets_dest_bucket: mybucket_name-dest
    
    - name: Move all objects between buckets and deleting the empty source bucket
      ansible.builtin.include_role:
        name: cloud.aws_ops.move_objects_between_buckets
      vars:
        move_objects_between_buckets_source_bucket: mybucket_name-src
        move_objects_between_buckets_dest_bucket: mybucket_name-dest
        move_objects_between_buckets_delete_empty_source_bucket: true
```

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team