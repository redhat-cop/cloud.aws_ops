## cloud.aws_ops.upload_file_to_s3

A playbook to upload a local file to S3. When running this playbook the file to upload is expected to be located on the remote host, the controller host is responsible of the PUT operation on the S3 bucket.

## Variables

* **aws_access_key**: The AWS access key to use. _type_: **str**
* **aws_secret_key**: The AWS secret key that corresponds to the access key. _type_: **str**
* **aws_session_token**: The AWS session token if using temporary access and secret keys.  _type_: **str**
* **aws_profile**: A named AWS profile to use for authentication.  _type_: **str**

* **upload_file_to_s3_bucket_name**: (Required) Name of an existing bucket to upload file in. _type_: **str**
* **upload_file_to_s3_file_path**: (Required) Path to a local file to upload. _type_: **path**
* **upload_file_to_s3_object_name**: Object name inside the bucket. Default to file basename. _type_: **str**
* **upload_file_to_s3_object_permission**: This option lets the user set the canned permissions on the object that is created. _type_: **str**, valid values are: _private_, _public-read_, _public-read-write_, _aws-exec-read_, _authenticated-read_, _bucket-owner-read_, _bucket-owner-full-control_
* **upload_file_to_s3_object_overwrite**: Force overwrite remotely with the object/key. _type_: **bool**.

## Dependencies

- NA

## Example

__vars.yaml__
```yaml
---
aws_profile: sample-profile
upload_file_to_s3_bucket_name: my-test-bucket
upload_file_to_s3_file_path: /path/to/file/on/remote/host
```

__playbook.yaml__
```yaml
---
ansible.builtin.import_playbook: cloud.aws_ops.upload_file_to_s3
```

__inventory.ini__
```
[all]
sample_host ansible_ssh_user=some_user ansible_host=xxx.xxx.xxx.xxx
```

Run the following command:

```shell
ansible-playbook ./playbook.yaml -e "@./vars.yaml" -i inventory.ini
```

## License

GNU General Public License v3.0 or later

See [LICENSE](https://github.com/ansible-collections/cloud.aws_troubleshooting/blob/main/LICENSE) to see the full text.

## Author Information

- Ansible Cloud Content Team
