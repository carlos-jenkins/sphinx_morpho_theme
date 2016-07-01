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

"""
sphinx_morpho_theme module entry point.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

from os.path import abspath, dirname

__author__ = 'Carlos Jenkins'
__email__ = 'carlos@jenkins.co.cr'
__version__ = '0.1.0'


def html_theme_path():
    """
    Get the absolute path to the parent directory to where the theme is
    located.

    :return: The absolute path to the folder containing the theme.
    :rtype: str
    """
    return abspath(dirname(__file__))


__all__ = ['html_theme_path']
