#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="HTML_QuickForm_ElementGrid-0.1.0"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTML/QuickForm", "HTML/QuickForm/ElementGrid.php")
    pisitools.insinto("/usr/share/php5/PEAR/doc/HTML_QuickForm_ElementGrid", "examples/*")