from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
  name = 'djenv',
  packages = ['djenv'],
  package_dir = {'djenv': 'djenv'},
  package_data = {'djenv': ['__init__.py']},
  version = '0.0.6',
  description = 'DjEnv (Django + Environment): Load Django Settings from Environmental Variables',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = 'Daniel J. Dufour',
  author_email = 'daniel.j.dufour@gmail.com',
  url = 'https://github.com/DanielJDufour/djenv',
  download_url = 'https://github.com/DanielJDufour/djenv/tarball/download',
  keywords = ['auto', 'automate', 'conf', 'configure', 'env', 'environment', 'django', 'loader', 'settings'],
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent'
  ],
  install_requires=['simple-env'] # assume have Django already installed
)
