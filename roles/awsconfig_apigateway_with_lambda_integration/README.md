# awsconfig_apigateway_with_lambda_integration

A role to create/delete an API gateway with lambda function integration.
the role produces variables **awsconfig_apigateway_with_lambda_integration\_\_invoke_url** that contains the URL to invoke API gateway and **awsconfig_apigateway_with_lambda_integration\_\_id** that contains the id of the API gateway created.

## Requirements

AWS User Account with permission to create API gateway, lambda function and IAM role.

## Role Variables

- **awsconfig_apigateway_with_lambda_integration_operation**: Whether to create or delete the API gateway. Choices: 'create', 'delete'. Default: 'create'.
- **awsconfig_apigateway_with_lambda_integration_api_name**: The name of the API gateway to create/delete.
- **awsconfig_apigateway_with_lambda_integration_id**: string identifier of the API gateway to update/delete.
- **awsconfig_apigateway_with_lambda_integration_tags**: collection of tags associated to the API gateway, this is used to ensure unique API gateway is created/deleted while running multiple times. Provided as dictionnary.
- **awsconfig_apigateway_with_lambda_integration_lambda_runtime**: The lambda function runtime. e.g: 'python3.8'
- **awsconfig_apigateway_with_lambda_integration_lambda_function_file**: The path to a valid file containing the code of the lambda function.
- **awsconfig_apigateway_with_lambda_integration_lambda_handler**: The lambda function handler. e.g: 'hello.lambda_handler'
- **awsconfig_apigateway_with_lambda_integration_stage_name**: The name for the Stage resource. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.

## Dependencies

- role: [aws_setup_credentials](../aws_setup_credentials/README.md)

## Example Playbook

    - hosts: localhost
      roles:
        - role: cloud.aws_ops.awsconfig_apigateway_with_lambda_integration
          aws_access_key: xxxxxxxxxxx
          aws_secret_key: xxxxxxxxxxx
          aws_region: xxxxxxxx
          awsconfig_apigateway_with_lambda_integration_operation: create
          awsconfig_apigateway_with_lambda_integration_api_name: hello
          awsconfig_apigateway_with_lambda_integration_tags:
            automation: ansible
          awsconfig_apigateway_with_lambda_integration_lambda_runtime: 'python3.8'
          awsconfig_apigateway_with_lambda_integration_lambda_handler: 'hello.lambda_handler'
          awsconfig_apigateway_with_lambda_integration_lambda_function_file: hello.py

## License

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.

## Author Information

- Ansible Cloud Content Team
