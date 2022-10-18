awsconfig_multiregion_cloudtrail
==================

A role to create/delete a Trail for multiple regions.

Requirements
------------

AWS User Account with the following permission:

* cloudtrail:CreateTrail
* cloudtrail:StartLogging
* cloudtrail:GetTrail
* s3:PutObject
* s3:GetBucketAcl
* s3:PutBucketLogging
* s3:ListBucket

Role Variables
--------------

* **operation**: Whether to create or delete the Trail. Choices: 'create', 'delete'. Default: 'create'.
* **bucket_name**: The name of the Amazon S3 bucket you want to upload logs to. Required when **operation** is set to **create**.
* **key_prefix**: The Amazon S3 key prefix that comes after the name of the bucket you designated for log file delivery.
* **trail_name**: The name of the CloudTrail trail to be created.

Dependencies
------------

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

Example Playbook
----------------

    - hosts: localhost
      roles:
        - role: cloud.aws_ops.awsconfig_multiregion_cloudtrail
          aws_profile: xxxxxxxxxxx
          aws_access_key: xxxxxxxxxxx
          aws_secret_key: xxxxxxxxxxx
          operation: create
          bucket_name: mys3bucket
          key_prefix: The Amazon S3 key prefix that comes after the name of the bucket you designated for log file delivery.
          trail_name: mytrail

License
-------

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team