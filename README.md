# armada-sde-rest

[![Build Status](https://travis-ci.org/kriberg/armada-sde-rest.svg?branch=master)](https://travis-ci.org/kriberg/armada-sde-rest)
[![Coverage Status](https://coveralls.io/repos/github/kriberg/armada-sde-rest/badge.svg?branch=master)](https://coveralls.io/github/kriberg/armada-sde-rest?branch=master)


armada-sde-rest is a pluggable app for Django which provides [Django REST framework](https://www.django-rest-framework.org/) 
endpoints for the models generated by [armada-sde](https://github.com/kriberg/armada-sde.git).

## Usage

Install the latest version of armada-sde-rest from PyPI:

```commandline
pip install armada-sde-rest
```

Follow the installation instructions for [armada-sde](https://github.com/kriberg/armada-sde.git), then 
add armada-sde-rest and its dependencies to Django's settings.py:

```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'armada_sde',
    'armada_sde_rest',
]
```

Add the routes to your urls.py:

```python
from django.urls import path, include


urlpatterns = [
    path('sde/', include('armada_sde_rest.urls')),
]
```
