#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    # edit prefix for sandbox error
    pisitools.dosed("gdist/shortcuts.py", "self.prefix", "'%s/usr'" % get.installDIR())
    pisitools.dosed("gdist/man.py", "self.prefix", "'%s/usr'" % get.installDIR())
    pisitools.dosed("gdist/po.py", "self.install_base", "'%s/usr'" % get.installDIR())

    # install quodlibet and exfalso
    pythonmodules.install()

    # and then, copy images for desktop files' icons
    pisitools.insinto("/usr/share/pixmaps", "quodlibet/images/quodlibet.png")
    pisitools.insinto("/usr/share/pixmaps", "quodlibet/images/exfalso.png")

    # there is no need to extensions
    pisitools.dosed("%s/usr/share/applications/quodlibet.desktop" % get.installDIR(),
                    "Icon=quodlibet.png",
                    "Icon=quodlibet")
    pisitools.dosed("%s/usr/share/applications/exfalos.desktop" % get.installDIR(),
                    "Icon=exfalso.png",
                    "Icon=exfalso")

    # don't forget to include this documents
    pisitools.dodoc("COPYING", "HACKING", "NEWS", "README")
