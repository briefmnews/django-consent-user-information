# django-consent-user-information
[![Python 3.7](https://img.shields.io/badge/python-3.6|3.7|3.8-blue.svg)](https://www.python.org/downloads/release/python-270/) 
[![Django 2.x](https://img.shields.io/badge/django-2.2-blue.svg)](https://docs.djangoproject.com/en/2.2/)
![Python CI](https://github.com/briefmnews/django-consent-user-information/workflows/Python%20CI/badge.svg)
[![codecov](https://codecov.io/gh/briefmnews/django-consent-user-information/branch/master/graph/badge.svg?token=OEDGBJ7JT6)](https://codecov.io/gh/briefmnews/django-consent-user-information)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

A simple app to manage consent users information. Sometimes it's important to
store information from the user.

## Installation

Install with pip:
```
pip install -e git://github.com/briefmnews/django-consent-user-information.git@master#egg=django-consent-user-information
```

## Setup
In order to make `django-consent-user-information` works, you'll need to follow the steps below.

### Settings
```python
INSTALLED_APPS = (
    ...
    'django_user_agents',
    'consent_user_information',
    ...
)
```

## Tests
Testing is managed by `pytest`. Required package for testing can be installed with:
```shell
make install
``` 

To run testing locally:
```shell
pytest
``` 