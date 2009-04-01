#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

WorkDir="Miro-2.0.4_svn"

def build():
    pisitools.dosed("platform/gtk-x11/setup.py", ".\/miro.real", "/usr/bin/miro.real")
    shelltools.cd("platform/gtk-x11")
    pythonmodules.compile()

def install():
    shelltools.cd("platform/gtk-x11")
    pythonmodules.install()

    for i in ("24x24", "72x72", "128x128"):
        pisitools.insinto("/usr/share/icons/hicolor/%s/apps" % i, "miro-%s.png" %i, "miro.png")

    pisitools.dodoc("../../README", "../../license.txt", "../../CREDITS")
