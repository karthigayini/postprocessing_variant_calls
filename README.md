# Post-processing of variant calls

This hosts multiple scripts necessary for filtering and processing of variant calls in the vcfs/txt file generated by callers.

## Callers Supported

### VarDictJava

See `example_calls.sh` for example calls of how VarDict filtering works for single and two sample input vcfs via the command line. 

## How the repo was made

Template used: https://github.com/yxtay/python-project-template

### Features

- environment management with Conda
- project metadata and dependency management with Poetry
- preconfigured continuous integration tasks
  - code formatting with isort and Black
  - code linting with isort, Black, Flake8, Bandit and Mypy
  - unit tests with pytest
  - pre-commit hooks
  - CICD pipelines with GitHub Actions
- application
  - logging with standard logging and python-json-logger
  - configuration with standard configparser, python-dotenv and pydantic
  - command line with Typer
  - web service with FastAPI, Uvicorn and Gunicorn
- deployment with Docker images
  - development image based on `python:latest`
  - lightweight production image based on `python:slim` using multi-stage build
- Make formula for common development tasks
  - install dependencies
  - run continuous integration tasks
  - run application
  - build Docker images

### Usage

Clone this repository or [use it as a template][generate] to generate a new repository.

Update the project name and metadata in `pyproject.toml` and `configs/main.ini`.

#### External dependencies

- [Conda][conda]
- [Docker][docker]
- [Make][make]

#### Create environment

Use Conda to create a virtual environment and activate it for the project.

```bash
conda env create -f environment.yml
conda activate vardict
```

#### Install dependencies

Then install project dependencies with Poetry.

```bash
make deps-install
```

#### Updating Environment

To update the environment after initial setup up run: 

```bash
conda env update -f environment.yml
```

instead of `conda create`, and then re-run `poetry lock --no-update` and `make deps-install`

### Tools

- Environment management
  - [Conda][conda]
  - [Poetry][poetry]
  - [Docker][docker]
- Linting & Testing
  - [isort][isort]
  - [Black][black]
  - [Flake8][flake8]
  - [Bandit][bandit]
  - [Mypy][mypy]
  - [pytest][pytest]
  - [pre-commit][pre-commit]
- Application
  - [logging][logging]
  - [python-json-logger][python-json-logger]
  - [configparser][configparser]
  - [python-dotenv][python-dotenv]
  - [pydantic][pydantic]
  - [Typer][typer]
  - [FastAPI][fastapi]
  - [Uvicorn][uvicorn]
  - [Gunicorn][gunicorn]
  - [Make][make]

[conda]: https://docs.conda.io/en/latest
[poetry]: https://python-poetry.org
[isort]: https://timothycrosley.github.io/isort
[black]: https://black.readthedocs.io/en/stable
[flake8]: https://flake8.pycqa.org/en/latest
[bandit]: https://github.com/PyCQA/bandit
[mypy]: http://www.mypy-lang.org
[pytest]: https://docs.pytest.org/en/stable
[pre-commit]: https://pre-commit.com
[logging]: https://docs.python.org/3/library/logging.html
[python-json-logger]: https://github.com/madzak/python-json-logger
[configparser]: https://docs.python.org/3/library/configparser.html
[python-dotenv]: https://saurabh-kumar.com/python-dotenv
[pydantic]: https://pydantic-docs.helpmanual.io
[typer]: https://typer.tiangolo.com
[fastapi]: https://fastapi.tiangolo.com
[uvicorn]: https://www.uvicorn.org
[gunicorn]: https://gunicorn.org
[make]: https://www.gnu.org/software/make
[docker]: https://www.docker.com
[generate]: https://github.com/yxtay/python-project-template/generate
