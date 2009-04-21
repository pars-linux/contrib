#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--enable-shm \
                         --enable-spell=gtkspell")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.chmod("%s/usr/lib/xchat/plugins/*" % get.installDIR(),0644)

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "HACKING", "README")
