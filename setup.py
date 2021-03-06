#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Carlos Jenkins
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from setuptools import setup, find_packages


def read(filename):
    """
    Read a file relative to setup.py location.
    """
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, filename)) as fd:
        return fd.read()


def find_version(filename):
    """
    Find package version in file.
    """
    import re
    content = read(filename)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", content, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


def find_requirements(filename):
    """
    Find requirements in file.
    """
    import string
    content = read(filename)
    requirements = []
    for line in content.splitlines():
        line = line.strip()
        if line and line[:1] in string.ascii_letters:
            requirements.append(line)
    return requirements


def find_data(package, path):
    """
    Find all data files in a folder.
    """
    from os import walk
    from pprint import pprint
    from os.path import join, relpath

    data_path = join(package, path)
    data_files = []
    for root, folders, files in walk(data_path):
        if files:
            data_files.extend(
                [relpath(join(root, f), package) for f in files]
            )

    print('Data files found:')
    pprint(data_files)

    return data_files


setup(
    name='sphinx_morpho_theme',
    version=find_version('lib/sphinx_morpho_theme/__init__.py'),
    package_dir={'': 'lib'},
    packages=find_packages('lib'),
    package_data={
        'sphinx_morpho_theme': find_data(
            'lib/sphinx_morpho_theme', 'sphinx_morpho_theme'
        )
    },

    # Dependencies
    install_requires=find_requirements('requirements.txt'),

    # Metadata
    author='Carlos Jenkins',
    author_email='carlos@jenkins.co.cr',
    description=(
        'Clean, materialized theme for Sphinx'
    ),
    long_description=read('README.rst'),
    url='https://sphinx_morpho_theme.readthedocs.org/',
    keywords='sphinx_morpho_theme',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    entry_points={
        'sphinx_themes': [
            'path = sphinx_morpho_theme:html_theme_path',
        ]
    },
)
