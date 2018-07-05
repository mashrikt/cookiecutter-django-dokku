import os
import shutil


def remove_email_user():
    shutil.rmtree(os.path.join("{{cookiecutter.app_name}}", "core"))


def main():
    if "{{ cookiecutter.email_user }}".lower() == "n":
        remove_email_user()


if __name__ == "__main__":
    main()
