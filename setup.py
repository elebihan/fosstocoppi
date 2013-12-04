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

import os
from distutils.core import setup, Extension
from disthelpers import build, build_trans, build_man, install_data
from fosstocoppi import __version__

setup(name='fosstocoppi',
      version=__version__,
      description='Retrieve Open Source licenses',
      long_description='''
      This tool can retrieve the text of Open Source licenses, using
      information from the http://spdx.org website.
      ''',
      license='GPLv3+',
      url='https://github.com/elebihan/fosstocoppi/',
      platforms=['linux'],
      classifiers=('Programming Language :: Python :: 3',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Development Status :: 2 - Pre-Alpha',
                   'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',),
      keywords=['FOSS', 'licensing', 'SPDX'],
      requires=['docutils (>=0.11)'],
      packages=['fosstocoppi'],
      scripts=['scripts/fosstocoppi'],
      data_files=[('share/man/man1', ['build/man/man1/fosstocoppi.1'])],
      author='Eric Le Bihan',
      author_email='eric.le.bihan.dev@free.fr',
      cmdclass = {'build': build,
                  'build_man': build_man,
                  'build_trans': build_trans,
                  'install_data': install_data})

# vim: ts=4 sts=4 sw=4 sta et ai
