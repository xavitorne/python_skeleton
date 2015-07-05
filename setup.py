import os

from setuptools import find_packages
from setuptools import setup

version = '0.1'
project = 'project_name'

install_requires=[
    'Babel',
    'lingua',
    'sqlalchemy-i18n',
],

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(name=project,
      version=version,
      description="description",
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: ",
        "License :: ",
        ],
      keywords='',
      author='Xavi',
      author_email='xavitorne@gmail.com',
      url='http://pypi.python.org/pypi/',
      license='bsd',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=[],
      entry_points={},
      extras_require={},
      message_extractors={'project_name': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
            ]},
      )
