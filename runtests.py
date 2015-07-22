# -*- coding: utf-8 -*-
# Source: https://stackoverflow.com/questions/3841725/how-to-launch-tests-for-django-reusable-app
#         https://github.com/dokterbob/django-newsletter/blob/master/runtests.py

import sys
import os

import django


def runtests():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'

    # Django >= 1.7
    if hasattr(django, 'setup'):
        django.setup()

    try:
        # Django <= 1.8
        from django.test.simple import DjangoTestSuiteRunner
        test_runner = DjangoTestSuiteRunner(verbosity=1)
    except ImportError:
        # Django >= 1.8
        from django.test.runner import DiscoverRunner
        test_runner = DiscoverRunner(verbosity=1)

    failures = test_runner.run_tests(['pandasjsonfield'])
    sys.exit(failures)

if __name__ == '__main__':
    runtests()
