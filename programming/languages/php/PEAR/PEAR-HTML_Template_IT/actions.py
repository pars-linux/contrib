#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="HTML_Template_IT-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTML/Template", "IT*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/HTML_Template_IT", "examples/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/HTML_Template_IT", "tests/*")
