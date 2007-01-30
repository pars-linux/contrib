#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "sidplay-libs-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("libsidutils/src/ini/ini.cpp", "#include <malloc.h>", "#include <stdlib.h>")
    libtools.libtoolize("--copy --force")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Dirty way to install docs
    for dirs in ("libsidplay", "libsidutils", "resid"):
        for files in ("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "TODO", "README"):
            shelltools.cd(dirs)
            pisitools.insinto("/usr/share/doc/%s/%s" % (get.srcTAG(), dirs), "%s" % files)
            shelltools.cd("..")