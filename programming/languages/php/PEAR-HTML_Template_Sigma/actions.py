#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="HTML_Template_Sigma-1.1.5"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTML/Template", "Sigma.php")
    pisitools.insinto("/usr/share/php5/PEAR/doc/HTML_Template_Sigma", "docs/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/HTML_Template_Sigma", "tests/*")