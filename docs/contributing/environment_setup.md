# Setting Up Your Development Environment

> **Note:** This fork is maintained specifically for NRTK integration. We are not accepting general contributions at this time. For issues or questions related to NRTK integration, please open an issue on the [NRTK repository](https://github.com/Kitware/nrtk/issues).

This guide is provided for Kitware developers and NRTK maintainers working on this fork.

## Prerequisites

- Python 3.9 or higher
- Poetry 2.0+
- Git

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Kitware/nrtk-albumentations.git
cd nrtk-albumentations
```

### 2. Install Dependencies with Poetry

```bash
poetry install
```

This will create a virtual environment and install all dependencies.

### 3. Set Up Pre-commit Hooks

Pre-commit hooks help maintain code quality:

```bash
poetry run pre-commit install
```

Run hooks manually on all files:

```bash
poetry run pre-commit run --files $(find albumentations -type f)
```

## Verifying Your Setup

Run the test suite:

```bash
poetry run pytest
```

## Development Workflow

1. Create a new branch for your work
2. Make your changes
3. Run tests: `poetry run pytest`
4. Run pre-commit hooks: `poetry run pre-commit run --all-files`
5. Commit and push your changes
6. Create a pull request

## Getting Help

For questions about this fork or NRTK integration:

- Open an issue on [this repository](https://github.com/Kitware/nrtk-albumentations/issues) for fork-specific questions
- Open an issue on [NRTK repository](https://github.com/Kitware/nrtk/issues) for broader NRTK questions
- Contact the NRTK team at <nrtk@kitware.com>
