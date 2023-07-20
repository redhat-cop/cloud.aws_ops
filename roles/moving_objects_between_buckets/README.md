moving_objects_between_buckets
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
- name: Playbook for moving objects between buckets using cloud.aws_ops.moving_objects_between_buckets role
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Define bucket name
      set_fact:
        bucket:
          src: "mybucket-src"
          dest: "mybucket-dest"
    
    - name: Create source s3 bucket
      amazon.aws.s3_bucket:
        name: "{{ bucket.src }}"
        state: present

    - name: Create destination s3 bucket
      amazon.aws.s3_bucket:
        name: "{{ bucket.dest }}"
        state: present
    
    - name: Put object (text) in source bucket
      amazon.aws.s3_object:
        bucket: "{{ bucket.src }}"
        object: /template/test.txt
        content: "{{ lookup('file', 'test.txt') }}"
        mode: put

    - name: Put object (python) in source bucket
      amazon.aws.s3_object:
        bucket: "{{ bucket.src }}"
        object: test.py
        content: "{{ lookup('file', 'test.py') }}"
        mode: put

    - slurp:
        src: "{{ role_path }}/files/test.png"
      register: put_binary

    - name: Put object (image) in source s3 bucket
      amazon.aws.s3_object:
        bucket: "{{ bucket.src }}"
        object: put-binary.bin
        content_base64: "{{ put_binary.content }}"
        mode: put
    
    - name: Moving one object between buckets
      ansible.builtin.include_role:
        name: cloud.aws_ops.moving_objects_between_buckets
      vars:
        source_bucket: "{{ bucket.src }}"
        dest_bucket: "{{ bucket.dest }}"
        key_prefix: "template"
    
    - name: Moving all objects between buckets and deleting the empty source bucket
      ansible.builtin.include_role:
        name: cloud.aws_ops.moving_objects_between_buckets
      vars:
        source_bucket: "{{ bucket.src }}"
        dest_bucket: "{{ bucket.dest }}"'
        delete_empty_source_bucket: true
```

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team