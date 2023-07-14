awsconfig_multiregion_cloudtrail
==================

A role to create/delete a Trail for multiple regions.

Requirements
------------

AWS User Account with the following permission:

* s3:HeadBucket
* s3:GetBucketOwnershipControls
* s3:ListObjectsV2
* s3:ListBucket

Role Variables
--------------

* **moving_buckets_src**: source bucket
* **moving_bucket_dest**: destination (receiving) bucket

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
          src: "mytaeho-src"
          dest: "mytaeho-dst"
    
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