# Virtual environments

## [venv](https://docs.python.org/3/library/venv.html)

Historically this has been done with `virtualenv` or `venv` like this `python3 -m venv .venv`,
and then you install your packages into the (activated) venv e.g.

```
source .venv/bin/activate
pip install numpy
```

You might then create a `requirements.txt` containing the packages (and versions) required for your project,
which can then be used to create a new venv using `pip install -r requirements.txt`.
This is basically fine, except that it's a manual process, and doesn't (usually) define which specific versions of which
packages were used, so you might get the same package versions if you recreate the venv,
but equally you might not.

You can `pip freeze > requirements.txt` which then lists all versions of all packages,
so you should be able to recreate the venv,
but it's still a manual process keeping `requirements.txt` up to date, and now you have loads more packages listed.

### `requirements.in` + `pip compile`

Create a `requirements.in` file and list just the direct dependencies of your app. The same way you’d do with `requirements.txt`.
Then run `pip-compile` and it will create `requirements.txt`, with all the dependencies listed and all the versions locked.

There are other tools which attempt to fix the various shortcomings of `pip` and `venv` but they all
[bring their own problems](https://www.bitecode.dev/p/why-not-tell-people-to-simply-use), and so `pip` + `venv` might still bring the highest rates of success.

## [pipenv](https://pipenv.pypa.io/en/latest/)

This is a tool to manage both virtual environments and package installation, and as such installation is done
at a system or user level. It can be installed with `pip install --user pipenv`, but this won't work if you're
using the Linux system `python`

```error
error: externally-managed-environment
× This environment is externally managed
...
```

so your options are `apt install pipenv` or `pipx install pipenv`.
However, if you can't `pip install --user <package>` then you'll need `apt install pipx`.
Once you've installed it, you create/activate an environment using `pipenv shell`,
or install from `Pipfile.lock` using `pipenv install`
or from a requirements file using `pipenv install -r requirements.txt`.
The virtual environments are by default all put in a central location, so to fix this and put the environment
in the project directory, you need `PIPENV_VENV_IN_PROJECT=1 ` this in your `.bashrc` file.

## [poetry](https://python-poetry.org/)

Another environment and packaging tool which attempts to create a deterministic build. Install with

```
pipx install poetry
```

Create a new project directory and venv using

```
poetry new poetry-demo
```

As with `pipenv`, you need to set a variable in `.bashrc` to create the venv in the project directory:

```
POETRY_VIRTUALENVS_IN_PROJECT=true
```

Poetry creates a skeleton project structure with a `README.md`, `pyproject.toml` `<project_name>` and `tests` directories.

## [pipx](https://pipx.pypa.io/stable/)

This is a way to install python command-line tools in isolated environments that don't affect your system python,
or any of your project venvs.
Install with either

```
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

or

```
sudo apt install pipx
pipx ensurepath
```
