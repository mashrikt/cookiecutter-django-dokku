import pytest


@pytest.fixture
def context():
    return {
        "github_repository_name": "myproject",
        "app_name": "myproject",
        "description": "My Project",
        "email_user": "y",
        "use_celery": "y",
        "use_sentry": "n",
        "use_rest_framework": "y",
        "use_auth_endpoints": "y",
        "use_restframework_documentation": "n"
    }


@pytest.fixture(params=["email_user", "use_celery", "use_rest_framework", "use_auth_endpoints"])
def feature_context(request, context):
    context.update({request.param: "n"})
    return context
