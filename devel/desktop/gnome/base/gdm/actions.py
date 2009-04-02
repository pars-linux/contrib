#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-scrollkeeper\
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/lib/gdm")

    pisitools.domove("/usr/share/gdm/applications/","/usr/share/applications/")

    remove = ["/usr/sbin/gdm","/usr/sbin/gdm-restart","/usr/sbin/gdm-safe-restart","/usr/sbin/gdm-stop",
              "/usr/share/gdm/BuiltInSessions/*","/usr/share/xsessions/gnome.desktop",
              "/usr/share/applications/gdmflexiserver*.desktop"]
    for r in remove:
        pisitools.remove(r)

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
