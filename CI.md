# Continuous Integration (CI)

## AWS Operations Collection Testing

GitHub Actions are used to run the CI for the cloud.aws_ops collection. The workflows used for the CI can be found [here](https://github.com/redhat-cop/cloud.aws_ops/tree/main/.github/workflows). These workflows include jobs to run the sanity tests, linters, integration tests, and changelog checks.

The collection uses reusable workflows from [ansible-network/github_actions](https://github.com/ansible-network/github_actions) for standardized testing.

### PR Testing Workflows

The following tests run on every pull request:

| Job | Description | Configuration |
| --- | ----------- | ------------- |
| Changelog | Checks for the presence of changelog fragments | ubuntu-latest |
| Linters | Runs `ansible-lint`, `black`, `flake8`, `yamllint` | Python 3.10 (via tox) |
| Sanity | Runs ansible sanity checks across multiple Python and ansible-core versions | Determined by [ansible-network reusable workflows](https://github.com/ansible-network/github_actions) |
| Integration tests | Executes integration test suites on AWS (split across 2 parallel jobs) | Python 3.12, ansible-core milestone, requires "safe to test" label |

For the official Ansible core support matrix, see the [Ansible Release and Maintenance documentation](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix).

### Collection Dependencies

The collection depends on several other collections for integration testing. These dependencies are defined in:
- [`galaxy.yml`](galaxy.yml) - Production dependencies
- [`tests/integration/requirements.yml`](tests/integration/requirements.yml) - Test-time dependencies

### Security Model

Integration tests use `pull_request_target` trigger and require explicit approval:
- PRs from external contributors require the "safe to test" label to be added by a maintainer
- This prevents unauthorized execution of tests that create AWS resources
- The `safe-to-test` job validates authorization before any AWS resources are created
