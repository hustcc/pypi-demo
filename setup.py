# -*- coding: utf-8 -*-
import setuptools  # noqa
from distutils.core import setup
import io
import re
import os


DOC = 'Document on <https://github.com/hustcc/pypi-demo>'


def read(*names, **kwargs):
    return io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


PACKAGE_NAME = 'pypidemo'


setup(name=PACKAGE_NAME,
      version=find_version('pypidemo/__init__.py'),
      description=PACKAGE_NAME,
      long_description=DOC,
      author='hustcc',
      author_email='i@hust.cc',
      url='https://github.com/hustcc/hust',
      license='MIT',
      install_requires=[
      ],
      classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities'
      ],
      keywords='pypidemo, hustcc, github, %s' % PACKAGE_NAME,
      include_package_data=True,
      zip_safe=False,
      packages=['pypidemo'],
      entry_points={
        'console_scripts': ['%s=pypidemo.cli:run' % PACKAGE_NAME]
      })
