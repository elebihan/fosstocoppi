===========
fosstocoppi
===========

Tool to retrieve Open Source licenses, using a bicycle.

Description
===========

`fosstocoppi` retrieves the text of open source licenses thanks to information
from `SPDX website <http://spdx.org/>`_.

Several commands are available:

- list: retrieve a list of all the known Open Source licenses.
- get: retrieve the text of one or more licenses.

Installation
============

To build and install for current user::

  $ PYTHONPATH=. python3 setup.py sdist
  $ pip install --user dist/fosstocoppi*.tar.gz

To build and install globally (may require superuser privileges)::

  $ PYTHONPATH=. python3 setup.py install

Usage
=====

To get the list of known licenses::

  $ fosstocoppi list

To retrieve the text of the GNU General Public License v2.0 and the Ruby
License and output them in a file::

  $ fosstocoppi -o licenses.txt get --scissors GPL-2.0+ Ruby

License
=======

Released under the GNU General Public License v3 or later. See ``COPYING`` for
details.
