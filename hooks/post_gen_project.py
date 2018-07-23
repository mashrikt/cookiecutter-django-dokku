import os
import shutil


def remove_celery():
    os.remove(os.path.join("{{cookiecutter.app_name}}", "celery.py"))


def remove_rest_auth():
    os.remove(os.path.join("{{cookiecutter.app_name}}", "users", "serializers.py"))


def remove_email_user():
    os.remove(os.path.join("{{cookiecutter.app_name}}", "users", "serializers.py"))
    os.remove(os.path.join("{{cookiecutter.app_name}}", "users", "forms.py"))
    os.remove(os.path.join("{{cookiecutter.app_name}}", "users", "managers.py"))


def main():
    try:
        if "{{ cookiecutter.use_celery }}".lower() == "n":
            remove_celery()

        if "{{ cookiecutter.use_rest_auth }}".lower() == "n":
            remove_rest_auth()

        if "{{ cookiecutter.email_user }}".lower() == "n":
            remove_email_user()
    except OSError:
        pass


if __name__ == "__main__":
    main()
