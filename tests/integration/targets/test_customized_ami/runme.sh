#!/usr/bin/env bash

set -eux

function cleanup() {
    ansible-playbook playbooks/manage_ami.yml -e "custom_ami_operation=delete" "$@"
    exit 1
}

trap 'cleanup "${@}"'  ERR

# Create custom AMI with default settings
ansible-playbook playbooks/manage_ami.yml -e "ami_architecture=x86_64" "$@"

# Validate custom AMI creation
ansible-playbook playbooks/validate_ami.yml -e "ami_architecture=x86_64" "$@"

# Trying to update existing AMI with custom_ami_recreate_if_exists=false
ansible-playbook playbooks/manage_ami.yml -e "ami_architecture=arm64" -e "update_when_exists=false" "$@"

# Validate custom AMI did not changed
ansible-playbook playbooks/validate_ami.yml -e "ami_architecture=x86_64" "$@"

# Delete Existing AMI
ansible-playbook playbooks/manage_ami.yml -e "custom_ami_operation=delete" -e "ami_architecture=x86_64" "$@"

# Ensure custom AMI was deleted
ansible-playbook playbooks/validate_ami.yml -e "ami_should_exists=false" "$@"
