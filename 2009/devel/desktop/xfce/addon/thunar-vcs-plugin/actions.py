#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("xdt-autogen")
    autotools.configure("--enable-subversion \
                         --enable-git")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # remove empty dir
    pisitools.removeDir("/usr/share/icons/hicolor/16x16")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
