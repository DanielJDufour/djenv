# DjEnv: Django + Environment
Load Django Settings Directly from Environmental Variables

# features
- modify django configuration without modifying source code
- prevent hard-coding of Django settings
- works great with Docker

# install
### with pip
```bash
pip install djenv
```
### with pipenv
```bash
pipenv install djenv
```

# basic usage
```python3
# inside settings.py

# import settings from environment
from djenv.settings import *
```

Prepend Settings with `DJANGO_` to import them.  For example:
```bash
DJANGO_DEBUG=False python3 manage.py runserver
```
Will set DEBUG=False in the settings.py

# advanced usage
You can also replace nested settings like DATABASES by setting a JSON file
```bash
DJANGO_DATABASES='{ "default": { "ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3" } }'  python3 manage.py runserver
```
