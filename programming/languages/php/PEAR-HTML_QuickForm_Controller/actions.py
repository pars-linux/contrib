#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="HTML_QuickForm_Controller-1.0.7"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTML/QuickForm", "Action*")
    pisitools.insinto("/usr/share/php5/PEAR/HTML/QuickForm", "Page.php")
    pisitools.insinto("/usr/share/php5/PEAR/HTML/QuickForm", "Controller.php")
    pisitools.insinto("/usr/share/php5/PEAR/doc/HTML_QuickForm_Controller", "examples/*")
    # set permissions
    items = ['*', '*/*']
    for item in items:
        shelltools.chmod("%s/usr/share/php5/PEAR/doc/HTML_QuickForm_Controller/%s" % (get.installDIR(), item))