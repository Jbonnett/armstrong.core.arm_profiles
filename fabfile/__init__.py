from ._utils import *

@task
def pep8():
    local('find ./armstrong -name "*.py" | xargs pep8', capture=False)


@task
def test():
    settings = {
        'INSTALLED_APPS': (
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'armstrong.core.arm_profiles',
            'armstrong.core.arm_profiles.tests.arm_profiles_support',
            'idios',
        ),
        'TEMPLATE_CONTEXT_PROCESSORS': (
            'django.core.context_processors.request',
        ),
        'ROOT_URLCONF': 'armstrong.core.arm_profiles.tests.arm_profiles_support.urls',
        'ABSOLUTE_URL_OVERRIDES': {
            "auth.user": lambda o: "/profiles/profile/%s/" % o.username
        },
        'AUTH_PROFILE_MODULE': 'arm_profiles.UserProfile',
    }
    with html_coverage_report():
        run_tests(settings, 'arm_profiles', 'arm_profiles_support')
