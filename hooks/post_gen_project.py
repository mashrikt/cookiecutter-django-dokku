import os
import shutil


def remove_celery():
    os.remove(os.path.join("{{cookiecutter.app_name}}", "celery.py"))


def remove_email_user():
    shutil.rmtree(os.path.join("{{cookiecutter.app_name}}", "core"))


def main():
    if "{{ cookiecutter.use_celery }}".lower() == "n":
        remove_celery()

    if "{{ cookiecutter.email_user }}".lower() == "n":
        remove_email_user()


if __name__ == "__main__":
    main()
