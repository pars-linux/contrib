#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "dynamips-0.2.8-RC1"
NoStrip = "/"

def build():
    shelltools.system("make")

def install():
    autotools.rawInstall("DESTDIR=%s/usr" % get.installDIR())

    pisitools.dodoc("CHANGELOG", "COPYING", "README", "README.hypervisor", "TODO")
