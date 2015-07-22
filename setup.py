from setuptools import setup

setup(
    name = 'pandasjsonfield',
    packages = ['pandasjsonfield'],
    version = '0.1',
    description = 'Django model field for pandas objects (Series and DataFrame)',
    author = 'Estelle Scifo',
    author_email = '',
    url = 'https://github.com/stellasia/django-pandasjsonfield',
    download_url = 'https://github.com/stellasia/django-pandasjsonfield/archive/0.1.tar.gz',
    keywords = ['django', 'model field', 'pandas'],
    classifiers = [],
    test_suite='runtests.runtests',
    tests_require=['Django >= 1.8', "pandas>=0.16"],
)
