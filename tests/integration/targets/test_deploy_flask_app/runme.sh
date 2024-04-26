#!/usr/bin/env bash

set -eux

function cleanup() {
    ansible-playbook run.yaml -e "run_deploy_flask_app_operation=delete" "$@"
    exit 1
}

trap 'cleanup "${@}"'  ERR

# Create web application
ansible-playbook run.yaml -e "run_deploy_flask_app_operation=create" "$@"

# Delete web application
 ansible-playbook run.yaml -e "run_deploy_flask_app_operation=delete" "$@"
