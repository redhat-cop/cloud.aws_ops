# cloud.amazon_roles roles/playbook to demo ansible on aws

This repository hosts the `cloud.aws_ops` Ansible Collection.

The collection includes a variety of Ansible roles and playbook to help automate the management of resources on AWS.

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.17**.

## Included content

Click on the name of a plugin or module to view that content's documentation:

<!--start collection content-->

### Playbooks
Name | Description
--- | ---
cloud.amazon_roles.webapp|A playbook to create a webapp on AWS.
<!--end collection content-->

## Installation and Usage

### Installing the Collection from Ansible Galaxy

Before using the amazon_roles collection, you need to install it with the Ansible Galaxy CLI:

    ansible-galaxy collection install cloud.amazon_roles

You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: cloud.amazon_roles
    version: 0.1.0
```

## License

GNU General Public License v3.0 or later

See [LICENSE](https://github.com/ansible-collections/cloud.aws_ops/blob/main/LICENSE) to see the full text.
