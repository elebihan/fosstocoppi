# -*- coding: utf-8 -*-
#
# fosstocoppi - Retrieve Open Source licenses
#
# Copyright (c) 2013 Eric Le Bihan <eric.le.bihan.dev@free.fr>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
Helpers
"""

import os
import sys
from gettext import bindtextdomain, textdomain

def lookhead(iterable):
    """Iterates over a sequence and indicates if last element has been
    reached.
    """
    it = iter(iterable)
    last = next(it)
    for val in it:
        yield last, False
        last = val
    yield last, True

class Printer(object):
    """Print some data to standard output or a file.

    :param filename: path to the output file.
    :type filename: str
    """
    def __init__(self, filename=None):
        self._fn = filename

    def __enter__(self):
        if self._fn is None:
            self._file = sys.stdout
        else:
            self._file = open(self._fn, 'w')
        return self

    def __exit__(self, type, value, traceback):
        if self._fn is not None:
            self._file.close()

    def print(self, data):
        print(data, file=self._file)


def setup_i18n():
    """Set up internationalization."""
    root_dir = os.path.dirname(os.path.abspath(__file__))
    if 'lib' not in root_dir:
        return
    root_dir, mod_dir = root_dir.split('lib', 1)
    locale_dir = os.path.join(root_dir, 'share', 'locale')

    bindtextdomain('fosstocoppi', locale_dir)
    textdomain('fosstocoppi')

def create_printer(filename):
    """Creates a printer"""
    return Printer(filename)

# vim: ts=4 sts=4 sw=4 sta et ai
