#!/usr/bin/env bash

set -eux

function cleanup() {
    ansible-playbook test_webapp.yaml -e "operation=delete" "$@"
    exit 1
}

trap 'cleanup "${@}"'  ERR

# Create web application
ansible-playbook test_webapp.yaml "$@"

# Delete web application
ansible-playbook test_webapp.yaml -e "operation=delete" "$@"