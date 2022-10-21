# Pre-commit hooks

## About

These are checks which automatically run before you make a commit. You can only commit if the checks pass.

You can set them up manually, or use the python [pre-commit framework](https://pre-commit.com/) to automate the process.

## Why?

![xkcd comic on code quality](https://imgs.xkcd.com/comics/code_quality.png)

## Instructions

Create a file `.pre-commit-config.yaml` describing which hooks you want to use:

```yaml
repos:
-   repo: https://github.com/psf/black
    rev: 22.6.0
    hooks:
    - id: black
      language_version: python3
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v1.2.3
    hooks:
    - id: flake8
      args: [--ignore=E501]
```

`black` is a formatter, and `flake8` is a wrapper around various PEP8 linting tools.

```shell
pip install pre-commit
pre-commit install
```

This installs the hook at `.git/hooks/pre-commit`, and the tools in an environment at `~/.cache/pre-commit/`.

I found the pre-commit workflow above on a [blog](https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/) and it works like this:

![black then flake8 diagram](https://ljvmiranda921.github.io/assets/png/tuts/precommit_pipeline.png)

## Non-standard configuration of flake8

I've set flake8 to ignore long line errors in `.pre-commit-config.yaml`, because black doesn't format comment lines which then trigger flake8 errors.

## Other pre-commit hooks

[Full list](https://pre-commit.com/hooks.html) of pre-commit hooks available in this framework.
