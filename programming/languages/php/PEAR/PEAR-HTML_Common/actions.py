#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="HTML_Common-1.2.3"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTML", "Common.php")