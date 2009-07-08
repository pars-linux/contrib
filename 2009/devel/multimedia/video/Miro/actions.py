#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

WorkDir="Miro-%s" % get.srcVERSION().replace("_","-")

shelltools.export("HOME", "%s" % get.workDIR())

def build():
    shelltools.cd("platform/gtk-x11")
    pythonmodules.compile()

def install():
    shelltools.cd("platform/gtk-x11")
    pythonmodules.install()

    #Fix xulrunner dir
    pisitools.dosed("%s/usr/bin/miro" % get.installDIR(), "1.9.1", "1.9")

    pisitools.dodoc("README", "../../README", "../../license.txt", "../../CREDITS", "../../ADOPTERS")
