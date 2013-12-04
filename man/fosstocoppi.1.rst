===========
fosstocoppi
===========

-----------------------------
Retrieve open source licenses
-----------------------------

:Author: Eric Le Bihan <eric.le.bihan.dev@free.fr>
:Copyright: 2013 Eric Le Bihan
:Manual section: 1

SYNOPSIS
========

fosstocoppi [OPTIONS] <command> [<arg>, ...]

fosstocoppi [OPTIONS] list

fosstocoppi [OPTIONS] get <alias>, [<alias, ...]

OPTIONS
=======

-o FILE, --output FILE    set output filename

DESCRIPTION
===========

`fosstocoppi(1)` retrieves open source licenses.

LIST COMMAND
============

  To get a list of known licenses, use the *list* command. This command will
  display the alias of the license (as defined by SPDX) and its complete name.

GET COMMAND
===========

  To retrieve the text of one or more licences, use the *get* command. The
  license is specified using its alias, as returned by the *list* command.

OPTIONS
+++++++

-s, --scissors    add a delimiter between licenses

EXAMPLES
++++++++

  To get the text of the GNU Public License version 2.0::

    $ fosstocoppi get GPL-2.0+ LGPL-2.1+

  To get the text of multiple licenses, concatenated in a PDF file, use
  `paps(1)` combined with `ps2pdf(1)`::

    $ fosstocoppi -o /tmp/licenses.txt get GPL-2.0+ LGPL-2.1+
    $ paps /tmp/licenses.txt | ps2pdf - licenses.pdf

.. vim: ft=rst
