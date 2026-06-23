# SonarCloud

Dashboard:

[SonarCloud project overview](https://sonarcloud.io/project/overview?id=redhat-cop_cloud.aws_ops)

## CI integration

Sonar analysis and **coverage collection** live in **[.github/workflows/sonarcloud.yml](.github/workflows/sonarcloud.yml)** only. They are **not** part of **[.github/workflows/integration.yml](.github/workflows/integration.yml)** or an **`all_green`** aggregator.

| Workflow | Role |
| -------- | ---- |
| [integration.yml](.github/workflows/integration.yml) | Standard integration tests (`ansible_test_integration`, no coverage) |
| [sonarcloud.yml](.github/workflows/sonarcloud.yml) | Same PR gates and targets, but `ansible-test integration --coverage`; **`coverage`** job emits `coverage.xml`; **`finalize`** runs the Sonar scanner |

Both workflows use **`pull_request_target`**, the **safe to test** label, and the same splitter/AWS setup. A labeled PR therefore runs integration tests twice (once per workflow); only the SonarCloud workflow produces coverage for Sonar.

### SonarCloud workflow jobs

- **`coverage-test`** (matrix) — integration tests with `--coverage`; uploads **`coverage-raw-*`** artifacts
- **`coverage`** — `ansible-test coverage combine` / `coverage xml`, path rewrite, upload artifact **`coverage`**
- **`finalize`** — downloads **`coverage`**, sets **`sonar.python.coverage.reportPaths`**, runs **`SonarSource/sonarqube-scan-action`** (same-repo PRs only, when org secret is set)

Scanner configuration: [sonar-project.properties](sonar-project.properties) (`sonar.projectKey=redhat-cop_cloud.aws_ops`, `sonar.tests=tests/integration`).

**`finalize`** uses org secret **`ANSIBLE_COLLECTIONS_ORG_SONAR_TOKEN_CICD_BOT`** and is gated so the token is not used for fork-head PRs. See GitHub [secrets in Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).

## Branch protection (repository settings)

If **SonarCloud** / **finalize** should block merges, add the check under **Settings** > **Branches** > **Required status checks**. That is not configured in YAML.
