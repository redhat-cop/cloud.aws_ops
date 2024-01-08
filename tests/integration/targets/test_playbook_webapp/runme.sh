#!/usr/bin/env bash

# generate inventory with access_key provided through a templated variable
ansible-playbook create_aws_credentials.yml "$@"
source access_key.sh

set -eux

function cleanup() {
    set +x
    source access_key.sh
    set -x
    ansible-playbook webapp.yaml -e "operation=delete" "$@"
    exit 1
}

trap 'cleanup "${@}"'  ERR

# Create web application
ansible-playbook webapp.yaml "$@"

# Delete web application
ansible-playbook webapp.yaml -e "operation=delete" "$@"