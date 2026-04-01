# Continuous Integration (CI)

## AWS Operations Collection Testing

GitHub Actions are used to run the CI for the `cloud.aws_ops` collection. The workflows used for the CI can be found in the [.github/workflows](.github/workflows) directory.

### PR Testing Workflows

The following tests run on every pull request:

| Job | Description | Python Versions | ansible-core Versions |
| --- | ----------- | --------------- | --------------------- |
| [Changelog](.github/workflows/changelog.yml) | Checks for the presence of changelog fragments | 3.12 | N/A |
| [Linters](.github/workflows/linters.yml) | Runs `black`, `flake8`, `yamllint`, and `ansible-lint` on plugins and tests | 3.10 | 2.17 |
| [Sanity](.github/workflows/sanity.yml) | Runs ansible sanity checks | See compatibility table below | devel, stable-2.17, stable-2.18, stable-2.19, stable-2.20 |
| [Integration](.github/workflows/integration.yml) | Executes integration test suites on AWS (split across 2 jobs, requires "safe to test" label) | 3.12 | milestone |

### Python Version Compatibility by ansible-core Version

These are outlined in the collection's [tox.ini](tox.ini) file (`envlist`) and GitHub Actions workflow exclusions.

| ansible-core Version | Sanity Tests |
| -------------------- | ------------ |
| devel | 3.12, 3.13, 3.14 |
| stable-2.20 | 3.10, 3.11, 3.12, 3.13, 3.14 |
| stable-2.19 | 3.11, 3.12, 3.13, 3.14 |
| stable-2.18 | 3.11, 3.12, 3.13, 3.14 |
| stable-2.17 | 3.10, 3.11, 3.12, 3.14 |

### Integration Test Security and "Safe to Test" Label

Integration tests run on real AWS infrastructure and require the "safe to test" label to prevent unauthorized resource creation and ensure security.

**Label Assignment:**
- **Automatically added** for PRs from users with write, maintain, or admin permissions
- **Manually added** by a maintainer for external contributors after code review

**Security Model:**
- Uses `pull_request_target` event (runs in base repository context)
- Prevents untrusted code from automatically accessing AWS credentials
- Label acts as an approval gate before tests consume AWS resources

**Test Execution:**
- Tests trigger when PRs are opened, reopened, synchronized (new commits), or when the label is added/removed
- Tests will **not run** if the label is missing
- Removing the label stops tests from running on subsequent pushes until re-added

**Job Organization:**
- Integration targets are automatically split across 2 parallel jobs
- Split is determined by `ansible_test_splitter` action based on changed files
- Each job runs the subset of tests relevant to the PR's changes
