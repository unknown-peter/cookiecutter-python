# cookiecutter-python

Cookiecutter template for python project

## Quickstart

generate project from template
```bash
pip install cookiecutter

cookiecutter gh:unknown-peter/cookiecutter-python
```
<br>

enter project config values
```text
$ cookiecutter gh:unknown-peter/cookiecutter-python
  [1/5] project_name (New Project):
  [2/5] package_name (new_project):
  [3/5] project_description (new project description):
  [4/5] author_name (unknown-peter):
  [5/5] Select license
    1 - NONE
    2 - MIT
    Choose from [1/2] (1):
```
<br>

project layout (file or directory in bracket is optional)
```text
new_project
├── (LICENSE)
├── README.md
├── src
│   └── new_project
│       └── __init__.py
└── tests
    └── __init__.py
```
