#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Calendar-0.5.3"

def install():
    items = ['Calendar.php', 'Minute.php', 'Week.php', 'Day.php', 'Year.php', 'Factory.php', 'Month.php', 'Decorator.php', 'Hour.php', 'Second.php', 'Validator.php']
    for item in items:
        pisitools.insinto("/usr/share/php5/PEAR/Calendar", item)
    
    pisitools.insinto("/usr/share/php5/PEAR/Calendar/Decorator", "Decorator/*")
    pisitools.insinto("/usr/share/php5/PEAR/Calendar/Engine", "Engine/*")
    pisitools.insinto("/usr/share/php5/PEAR/Calendar/Month", "Month/*")
    pisitools.insinto("/usr/share/php5/PEAR/Calendar/Util", "Util/*")
    pisitools.insinto("/usr/share/php5/PEAR/Calendar/Table", "Table/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Calendar", "docs/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Calendar", "tests/*")