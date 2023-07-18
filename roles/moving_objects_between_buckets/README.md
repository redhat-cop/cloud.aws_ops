moving_objects_between_buckets
==================

A role to move objects from one S3 Bucket to another.
Objects have two options: all objects can be transferred or specific objects are transferred through key prefix.

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

Role Variables
--------------

* **source_bucket**: The name of the Amazon S3 bucket that will have its objects retrieved and then emptied. **Required**
* **dest_bucket**: The name of the Amazon S3 bucket that will receive the objects. **Required**
* **key_prefix**: limits objects that begin with the specified prefix. Default value is **""**.

Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

## Example:
```
---
- name: Playbook for moving objects between buckets using cloud.aws_ops.moving_objects_between_buckets role
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Define bucket name used for tests
      set_fact:
        moving_buckets:
          src: "mybucket-src"
          dest: "mybucket-dst"
    
    - name: Create source s3 bucket
      amazon.aws.s3_bucket:
        name: "{{ moving_buckets.src }}"
        state: present
      
    - slurp:
        src: "test.png"
      register: put_binary
    
    - name: Put object in source s3 bucket
      amazon.aws.s3_object:
        bucket: "{{ moving_buckets.src }}"
        object: put-binary.bin
        content_base64: "{{ put_binary.content }}"
        mode: put
    
    - name: Put object in source s3 bucket
      amazon.aws.s3_object:
        bucket: "{{ moving_buckets.src }}"
        object: /template/test.txt
        content: "{{ lookup('png', 'test.png') }}"
        mode: put
    
    - name: Create destination s3 bucket
      amazon.aws.s3_bucket:
        name: "{{ moving_buckets.dest }}"
        state: present
    
    - name: Transferring source bucket's objects to destination bucket
      ansible.builtin.include_role:
        name: cloud.aws_ops.moving_objects_between_buckets
      vars:
        moving_buckets_src: "{{ moving_buckets.src }}"
        moving_bucket_dest: "{{ moving_buckets.dest }}"
```

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team