[![dtJgFol.png](https://iili.io/dtJgFol.png)](https://freeimage.host/)
[![dZqREOB.jpg](https://iili.io/dZqREOB.jpg "Packing Tutorial")](https://freeimage.host/)

# A sample Python project

A sample project that exists as an aid to the [Python Packaging User
Guide][packaging guide]'s [Tutorial on Packaging and Distributing
Projects][distribution tutorial].

This project does not aim to cover best practices for Python project
development as a whole. For example, it does not provide guidance or tool
recommendations for version control, documentation, or testing.

[The source for this project is available here][src].

The metadata for a Python project is defined in the `pyproject.toml` file,
an example of which is included in this project. You should edit this file
accordingly to adapt this sample project to your needs.

The file should use UTF-8 encoding and can be written using
[reStructuredText][rst] or [markdown][md use] with the appropriate [key set][md use]. It will be used to generate the project webpage on PyPI and will be
displayed as the project homepage on common code-hosting services, and should be
written for that purpose.

Typical contents for this file would include an overview of the project, basic
usage examples, etc. Generally, including the project changelog in here is not a
good idea, although a simple “What's New” section for the most recent version
may be appropriate.

[packaging guide]: https://packaging.python.org
[distribution tutorial]: https://packaging.python.org/tutorials/packaging-projects/
[src]: https://github.com/julioaranajr/sample_project_template
[rst]: http://docutils.sourceforge.net/rst.html
[md]: https://tools.ietf.org/html/rfc7764#section-3.5 "CommonMark variant"
[md use]: https://packaging.python.org/specifications/core-metadata/#description-content-type-optional

## Table of Contents

- [A sample Python project](#a-sample-python-project)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Installing](#installing)
  - [Initializing a Project](#initializing-a-project)
  - [Uploading a Project](#uploading-a-project)

## Description

This sample project template is a starting point for creating a new project. It includes a basic project structure, a README template, and a GitHub Actions workflow for running tests.

We use the following tools to create this project:

- [pyproject-generator](https://pypi.org/project/pyproject-generator/)

## Features

- Initialize a new project with a single command
- Automatically setup a package structure
- Automatically setup a virtual environment
- Automatically install packages
- Upload your package to PyPI with a single command
- Automatically run tests on GitHub Actions
- Automatically generate a README file
- Automatically generate a LICENSE file

## Installing

The easiest way is to install pyproject is from PyPI using pip:

```bash
pip install pyproject-generator
```

Afterwards, a pyproject command will be exposed on your system.

## Initializing a Project

Simply run

```bash
pyproject init {project_name}
```

to create your project folder. It will automatically setup a package structure, virtual environment, and install packages.

[![dtdgC21.gif](https://iili.io/dtdgC21.gif)](https://freeimage.host/)

The final project structure looks like:

[![dt2o1ZF.png](https://iili.io/dt2o1ZF.png)](https://freeimage.host/)

## Uploading a Project

**pyproject** also supplies an upload function. Run

```bash
pyproject upload
```

to build and upload your package to PyPI.

<!-- ![Tests](https://github.com/mCodingLLC/SlapThatLikeButton-TestingStarterProject/actions/workflows/tests.yml/badge.svg) -->
