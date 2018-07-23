import os
import shutil


def remove_file(filename):
    try:
        os.remove(filename)
    except OSError:
        pass


def remove_dir(dir_name):
    try:
        shutil.rmtree(dir_name)
    except OSError:
        pass


def remove_celery():
    remove_file(filename=os.path.join("{{cookiecutter.app_name}}", "celery.py"))


def remove_rest_auth():
    remove_file(os.path.join("{{cookiecutter.app_name}}", "users", "serializers.py"))
    remove_file(os.path.join("{{cookiecutter.app_name}}", "users", "conftest.py"))
    remove_file(os.path.join("{{cookiecutter.github_repository_name}}", "pytest.ini"))
    remove_dir(os.path.join("{{cookiecutter.app_name}}", "users", "tests"))


def remove_email_user():
    remove_file(os.path.join("{{cookiecutter.app_name}}", "users", "serializers.py"))
    remove_file(os.path.join("{{cookiecutter.app_name}}", "users", "forms.py"))
    remove_file(os.path.join("{{cookiecutter.app_name}}", "users", "managers.py"))


def main():
    if "{{ cookiecutter.use_celery }}".lower() == "n":
        remove_celery()

    if ("{{ cookiecutter.use_auth_endpoints }}".lower() == "y" and
            "{{ cookiecutter.use_rest_framework }}".lower() == "n"):
        remove_rest_auth()

    if "{{ cookiecutter.email_user }}".lower() == "n":
        remove_email_user()


if __name__ == "__main__":
    main()
