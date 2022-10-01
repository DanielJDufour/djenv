from unittest import TestCase
from subprocess import check_output

class TestEnvSettings(TestCase):
    def test_loading_string(self):
        statement = 'DJANGO_STATIC_URL="/assets/" pipenv run python3 test/mysite/manage.py diffsettings | grep STATIC_URL'
        output = check_output(statement, shell=True, text=True)
        self.assertEqual(output.strip(), "STATIC_URL = '/assets/'")

    def test_loading_number(self):
        statement = 'DJANGO_EMAIL_PORT="23" pipenv run python3 test/mysite/manage.py diffsettings | grep EMAIL_PORT'
        output = check_output(statement, shell=True, text=True)
        self.assertEqual(output.strip(), "EMAIL_PORT = 23")

    def test_loading_boolean(self):
        statement = 'DJANGO_SECURE_CONTENT_TYPE_NOSNIFF="false" pipenv run python3 test/mysite/manage.py diffsettings | grep SECURE_CONTENT_TYPE_NOSNIFF'
        output = check_output(statement, shell=True, text=True)
        self.assertEqual(output.strip(), "SECURE_CONTENT_TYPE_NOSNIFF = False")

    def test_loading_nested_json_values(self):
        statement = '''DJANGO_DATABASES='{ "default": { "ENGINE": "django.db.backends.sqlite3", "NAME": "test.sqlite3" } }' pipenv run python3 test/mysite/manage.py diffsettings | grep DATABASES'''
        output = check_output(statement, shell=True, text=True)
        self.assertEqual(output.strip(), "DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'test.sqlite3', 'ATOMIC_REQUESTS': False, 'AUTOCOMMIT': True, 'CONN_MAX_AGE': 0, 'OPTIONS': {}, 'TIME_ZONE': None, 'USER': '', 'PASSWORD': '', 'HOST': '', 'PORT': '', 'TEST': {'CHARSET': None, 'COLLATION': None, 'MIGRATE': True, 'MIRROR': None, 'NAME': None}}}")

    def test_loading_json_list_values(self):
        statement = '''DJANGO_ALLOWED_HOSTS='["127.0.0.1", "localhost"]' pipenv run python3 test/mysite/manage.py diffsettings | grep ALLOWED_HOSTS'''
        output = check_output(statement, shell=True, text=True)
        self.assertEqual(output.strip(), "ALLOWED_HOSTS = ['127.0.0.1', 'localhost']")

    def test_loading_python_path(self):
        statement = '''DJANGO_EMAIL_BACKEND='django.core.mail.backends.filebased.EmailBackend' pipenv run python3 test/mysite/manage.py diffsettings | grep EMAIL_BACKEND'''
        output = check_output(statement, shell=True, text=True)
        self.assertEqual(output.strip(), "EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'")

    def test_unused(self):
        statement = '''pipenv run python3 test/mysite/manage.py diffsettings'''
        check_output(statement, shell=True, text=True)
