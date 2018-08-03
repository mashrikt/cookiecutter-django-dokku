import pytest


@pytest.fixture
def context():
    return {
        "github_repository_name": "my-project",
        "app_name": "my_project",
        "description": "My Project",
        "email_user": "y",
        "use_celery": "y",
        "use_sentry": "n",
        "use_rest_framework": "y",
        "use_rest_auth": "y",
        "use_restframework_documentation": "y"
    }


def test_default_configuration(cookies, context):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["github_repository_name"]
    assert result.project.isdir()
