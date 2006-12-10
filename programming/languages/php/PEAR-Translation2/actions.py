#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Translation2-2.0.0beta11"

def install():
    pisitools.insinto("/usr/share/php5/PEAR", "Translation2.php")
    pisitools.insinto("/usr/share/php5/PEAR/Translation2", "Admin*")
    pisitools.insinto("/usr/share/php5/PEAR/Translation2", "Container*")
    pisitools.insinto("/usr/share/php5/PEAR/Translation2", "Decorator*")
    pisitools.insinto("/usr/share/php5/PEAR/Translation2/scripts", "scripts/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Translation2", "docs/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Translation2", "tests/*")