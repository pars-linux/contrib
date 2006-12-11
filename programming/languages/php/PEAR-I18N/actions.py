#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="I18N-0.8.6"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/I18N/Common", "Common/*")
    pisitools.insinto("/usr/share/php5/PEAR/I18N/Messages", "Messages/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/I18N", "docs/*")
    items = ['Country.php', 'DateTime.php', 'Format.php', 'Number.php', 'Common.php', 'Currency.php', 'Language.php', 'Negotiator.php']
    for item in items:
        pisitools.insinto("/usr/share/php5/PEAR/I18N", item)