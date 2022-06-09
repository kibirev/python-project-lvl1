# Makefile

env-prepare:
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    source $HOME/.poetry/env

install:
    poetry install

start:
    poetry run brain-games