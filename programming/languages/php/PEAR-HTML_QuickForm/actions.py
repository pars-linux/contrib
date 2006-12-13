#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="HTML_QuickForm-3.2.7"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTML", "QuickForm*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/HTML_QuickForm", "docs/*")