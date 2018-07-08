import os
import shutil


def remove_celery():
    os.remove(os.path.join("{{cookiecutter.app_name}}", "celery.py"))


def remove_rest_auth():
    os.remove(os.path.join("{{cookiecutter.app_name}}", "users", "serializers.py"))
    os.remove(os.path.join("{{cookiecutter.app_name}}", "users", "urls.py"))


def remove_email_user():
    shutil.rmtree(os.path.join("{{cookiecutter.app_name}}", "users"))


def main():
    if "{{ cookiecutter.use_celery }}".lower() == "n":
        remove_celery()

    if "{{ cookiecutter.use_rest_auth }}".lower() == "n":
        remove_rest_auth()

    if "{{ cookiecutter.email_user }}".lower() == "n":
        remove_email_user()


if __name__ == "__main__":
    main()
