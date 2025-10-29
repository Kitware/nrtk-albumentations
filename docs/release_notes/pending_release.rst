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

Fixes
-----
