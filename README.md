
[![codecov](https://codecov.io/gh/amakarudze/to-do/graph/badge.svg?token=HPslvKVFkW)](https://codecov.io/gh/amakarudze/to-do)

![Code Coverage Graph](https://codecov.io/gh/amakarudze/to-do/graphs/tree.svg?token=HPslvKVFkW)

# to-do
A simple to-do app. This app was developed as a fulfillment to PA2552-Group Project
## Group members
Anna Makarudze - anmk24@student.bth.se
Payel Mahapatra - pamh24@student.bth.se
Jammithri Kotapati - jako22@student.bth.se
Meenakshi Arakkal Sudesh - meaa24@student.bth.se

## Prerequisites
Visual Studio Code
Python 3.12
Git

## Set Up
To set up this project in your local environment do the following steps:

Fork this repository to your own account.

Copy the link to the repository and type in your shell/command line:

```git clone git@github.com:your_repository/to-do.git```

Navigate into to-do by typing the following command:
```cd to-do```

Run the following command to create a virtual environment. The Python version used to create this project is Python 3.12
```python3 -m venv .venv```

Activate the virtual environment by running the following command on Mac OSX and Linux
```source .venv/bin/activate```

or on Windows

```.venv\Scripts\activate```

## Installations

### Install Poetry
Install latest version of poetry by running the below command in the virtual environment

```pipx install poetry```


Install all the required dependencies using poetry

```poetry install```


Run migrations to create a local copy of the database:
```python manage.py migrate```

*Note:*- This project uses SQLite database so there is no need to install any database software or plugins.

## Configuring your local environment
For security reasons, some important and secret configuration values have been removed from the project `settings.py`
file. For your project to work properly, create an empty file in the root of your project called `.env`. Copy the
contents of `sample_env_file` into your `.env` file and write some values for everything that has a `blank` or `""` value.

### Setting up pre-commit
The project uses `ruff` as a `linter` and `format`. It also uses `pre-commit` to ensure that code is linted and
formatted properly before being committed.
However, you will need to run the following command to ensure that all files are properly linted and formatted before
being pushed to GitHub:

```pre-commit install```

## Testing your setup
With your virtual environment activated, run the following commands:

To run all tests:

```pytest``` or ```coverage run pytest```
To run individual test files provide the whole path of the test file following the pytest command. For example:

```pytest tests/unit_tests/test_tasks/test_views.py```


To see if your development server is set up correctly:

```python manage.py runserver```


and open this URL in the browser to see the homepage ```http://127.0.0.1:8000```.

## Contributing to this project
To contribute to this project, create a branch in your local development environment. After you are finished with your changes, push the changes to your fork and make a pull request to the main repo `git@github.com:amakarudze/to-do.git` where you forked this project.
