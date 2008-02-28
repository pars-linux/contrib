#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

NoStrip = "/"

def setup():
    #disable unnecessary enter/return shortcut
    pisitools.dosed("eric/ViewManager/ViewManager.py", "QApplication\.translate\('ViewManager', 'Enter'\)")
    pisitools.dosed("eric/ViewManager/ViewManager.py", "QKeySequence\(QApplication\.translate\('ViewManager', 'Return'\)", "QKeySequence(QApplication.translate('ViewManager', 'Enter')")

def install():
    bdir = "/usr/bin"
    idir = get.installDIR()
    ddir = "/usr/lib/%s/site-packages" % get.curPYTHON()

    pythonmodules.run("install.py -b %s -i %s -d %s -c" % (bdir, idir, ddir))
    pythonmodules.fixCompiledPy()

    #add icon
    pisitools.insinto("/usr/share/pixmaps", "eric/icons/default/eric.png", "eric4.png")

    pisitools.dodoc("ChangeLog", "LICENSE.GPL", "THANKS", "README*")
