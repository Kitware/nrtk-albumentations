Pending Release Notes
=====================

Updates / New Features
----------------------

* Build System & Project Configuration:

  - Migrated from ``setuptools`` to Poetry build system (``poetry.core.masonry.api``)
  - Converted ``pyproject.toml`` structure: ``[project]`` to ``[tool.poetry]``
  - Migrated all project metadata (name, version, description, authors, license, keywords, classifiers)
  - Converted runtime dependencies to ``[tool.poetry.dependencies]`` including numpy, scipy, PyYAML, pydantic, albucore, opencv-python-headless
  - Migrated optional dependencies to ``[tool.poetry.extras]`` (hub, pytorch, text)
  - Created ``[tool.poetry.group.dev.dependencies]`` for development tools from requirements-dev.txt
  - Updated package configuration to Poetry's packages format


* CI/CD:

  - Converted ``.github/workflows/ci.yml`` to use Poetry for all operations
  - Replaced ``uv`` package installer with ``poetry install``
  - Updated all test and check commands to use ``poetry run`` prefix
  - Changed caching strategy from pip cache to Poetry virtualenvs (``${cache-dir}/virtualenvs``)
  - Migrated to ``snok/install-poetry@v1`` action for Poetry installation
  - Maintained multi-platform testing across Ubuntu, Windows, and macOS
  - Preserved Python 3.9-3.12 test matrix
  - Retained OpenCV headless replacement logic for CI environments
  - Organized workflow into separate jobs: core tests, pre-commit hooks, defaults checking, and documentation checks

Fixes
-----
