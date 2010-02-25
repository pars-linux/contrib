#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="HTML_Template_IT-1.3.0a2"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTML/Template", "HTML/Template/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/HTML_Template_IT", "examples/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/HTML_Template_IT", "tests/*")
