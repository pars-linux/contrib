#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="I18Nv2-0.11.4"

def install():
    pisitools.insinto("/usr/share/php5/PEAR", "I18Nv2.php")
    pisitools.insinto("/usr/share/php5/PEAR/I18Nv2/DecoratedList", "DecoratedList/*")
    pisitools.insinto("/usr/share/php5/PEAR/I18Nv2/Language", "Language/*")
    pisitools.insinto("/usr/share/php5/PEAR/I18Nv2/Country", "Country/*")
    pisitools.insinto("/usr/share/php5/PEAR/I18Nv2/Locale", "Locale/*")
    pisitools.insinto("/usr/share/php5/PEAR/I18Nv2/Currency", "Currency/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/I18Nv2", "docs/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/I18Nv2", "tests/*")
    items = ['AreaCode.php', 'Currency.php', 'Negotiator.php', 'CommonList.php', 'DecoratedList.php', 'Language.php', 'Timezone.php', 'Country.php', 'Encoding.php', 'Locale.php']
    for item in items:
        pisitools.insinto("/usr/share/php5/PEAR/I18Nv2", item)