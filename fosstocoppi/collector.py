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
Collects open source licenses
"""

import urllib.request
from bs4 import BeautifulSoup
from gettext import gettext as _

_SPDX_URL = 'http://spdx.org/licenses/'

class LicenseNotFoundError(Exception):
    """Error raised when a license can not be found"""

class MalformedLicenseError(Exception):
    """Error raised when license text can not be parsed"""

class LicenseCollector(object):
    """
    Collects open source licenses
    """

    def __init__(self):
        pass

    def _list_licenses(self):
        licenses = {}
        response = urllib.request.urlopen(_SPDX_URL)
        doc = BeautifulSoup(response.read().decode('utf-8'))
        for row in doc.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) == 4:
                name = cols[0].string.strip()
                alias = cols[1].code.string.strip()
                url = _SPDX_URL + cols[3].a['href'][2:]
                licenses[alias] = (name, url)
        return licenses

    def list_licenses(self):
        """Lists all the known licenses.


        :returns: a mapping between license alias and full name.
        :rtype: dict.
        """
        return dict([(a, n) for a, (n, u) in self._list_licenses().items()])

    def get_license(self, alias):
        """Returns the text of a license.

        :param alias: alias of the license.
        :type: str.

        :returns: the text of the license.
        :rtype: str
        """
        licenses = self._list_licenses()
        try:
            name, url = licenses[alias]
        except KeyError:
            msg = _("{} is not a valid license alias")
            raise LicenseNotFoundError(msg.format(alias))

        response = urllib.request.urlopen(url)
        doc = BeautifulSoup(response.read().decode('utf-8'))
        divs = doc.find_all('div', 'license-text')
        if divs:
            return divs[0].get_text()
        else:
            msg = _("{} text is malformed")
            raise MalformedLicenseError(msg.format(alias))

# vim: ts=4 sts=4 sw=4 sta et ai
