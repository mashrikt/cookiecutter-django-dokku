#!/bin/sh
# this is a very simple script that tests the docker configuration for cookiecutter-django-dokku
# it is meant to be run from the root directory of the repository, eg:
# sh tests/test_docker.sh

# install test requirements
pip install -r requirements.txt

# create a cache directory
mkdir -p .cache/docker
cd .cache/docker

# create the project using the default settings in cookiecutter.json
cookiecutter ../../ --no-input
cd myproject

# run the project's tests
docker-compose -f docker-compose.yml run web pytest

# return non-zero status code if there are migrations that have not been created
docker-compose -f docker-compose.yml run web python manage.py makemigrations --dry-run --check || { echo "ERROR: there were changes in the models, but migration listed above have not been created and are not saved in version control"; exit 1; }
