# aws_setup_credentials

A role to define credentials for aws modules. The role defines a variable named **aws_setup_credentials\_\_output** which contains AWS credentials for Amazon modules based on user input.

## Requirements

N/A

## Role Variables

- **aws_endpoint_url**:
  - URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used.
  - Environment variable:
    - EC2_URL
    - AWS_URL
- **aws_access_key**:
  - The AWS access key to use.
  - Mutually exclusive with option aws_profile.
  - Environment variable:
    - AWS_ACCESS_KEY_ID
    - AWS_ACCESS_KEY
    - EC2_ACCESS_KEY.
- **aws_secret_key**:
  - The AWS secret key that corresponds to the access key.
  - Mutually exclusive with option aws_profile.
  - Environment variable:
    - AWS_SECRET_ACCESS_KEY
    - AWS_SECRET_KEY
    - EC2_SECRET_KEY.
- **aws_security_token**:
  - The AWS security token if using temporary access and secret keys.
  - Mutually exclusive with option aws_profile.
  - Environment variable:
    - AWS_SECURITY_TOKEN
    - EC2_SECURITY_TOKEN
- **aws_ca_bundle**:
  - The location of a CA Bundle to use when validating SSL certificates.
  - Environment variable:
    - AWS_CA_BUNDLE
- **aws_validate_certs**:
  - When set to "false", SSL certificates will not be validated for communication with the AWS APIs.
  - Environment variable:
    - AWS_VALIDATE_CERTS
- **aws_profile**:
  - The AWS profile to use.
  - Mutually exclusive with the aws_access_key, aws_secret_key and aws_security_token options.
  - Environment variable:
    - AWS_PROFILE
    - AWS_DEFAULT_PROFILE.
- **aws_config**:
  - A dictionary to modify the botocore configuration.
  - Parameters can be found at [botocore config](https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config).
- **aws_region**:
  - The AWS region to use.
  - Environment variable:
    - AWS_REGION
    - EC2_REGION.

## Dependencies

- NA

## Example Playbook

    - hosts: localhost

      roles:
        - role: cloud.aws_ops.aws_setup_credentials
          aws_profile: us-profile

      tasks:
        - block:

          - name: list availability zones
            aws_az_info:
              filter:
                zone-name: eu-east-1
        module_defaults:
          group/aws:
            '{{ aws_setup_credentials__output }}'

## License

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_troubleshooting/blob/main/LICENSE) to see the full text.

## Author Information

- Ansible Cloud Content Team
