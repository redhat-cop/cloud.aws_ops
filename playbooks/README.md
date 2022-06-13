### cloud.amazon_roles.webapp

A playbook to create a webapp on AWS. The webapp consists in mutiple resources

How to create a web application ?

```
ansible-playbook webapp.yaml -e "@credentials.yaml"
```
with `credentials.yaml` describe as below:

```
aws_access_key: "xxxxxxxxxxxxxxxxxxxx"
aws_secret_key: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
aws_region: "us-east-1"
resource_prefix: sample-prefix
```

To delete resources created above use:

```
ansible-playbook webapp.yaml -e "@credentials.yaml" -e "operation=delete"
```