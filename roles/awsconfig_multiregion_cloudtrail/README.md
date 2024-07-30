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

* **awsconfig_multiregion_cloudtrail_operation**: Whether to create or delete the Trail. Choices: 'create', 'delete'. Default: 'create'.
* **awsconfig_multiregion_cloudtrail_bucket_name**: The name of the Amazon S3 bucket you want to upload logs to. Required when **operation** is set to **create**.
* **awsconfig_multiregion_cloudtrail_key_prefix**: The Amazon S3 key prefix that comes after the name of the bucket you designated for log file delivery.
* **awsconfig_multiregion_cloudtrail_trail_name**: The name of the CloudTrail trail to be created.

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
          awsconfig_multiregion_cloudtrail_operation: create
          awsconfig_multiregion_cloudtrail_bucket_name: mys3bucket
          awsconfig_multiregion_cloudtrail_key_prefix: The Amazon S3 key prefix that comes after the name of the bucket you designated for log file delivery.
          awsconfig_multiregion_cloudtrail_trail_name: mytrail

License
-------

GNU General Public License v3.0 or later

See [LICENSE](https://github.com/ansible-collections/cloud.aws_ops/stable-3/main/LICENSE) to see the full text.

Author Information
------------------

- Ansible Cloud Content Team