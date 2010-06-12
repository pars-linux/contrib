#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure("--sysconfdir=/etc/X11/ \
                         --with-pam-prefix=/etc \
                         --disable-scrollkeeper \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/lib/gdm")

    pisitools.domove("/usr/share/gdm/applications/","/usr/share")

    remove = ["/usr/sbin/gdm","/usr/sbin/gdm-restart","/usr/sbin/gdm-safe-restart",
              "/usr/sbin/gdm-stop", "/usr/share/applications/gdmflexiserver.desktop",
              "/usr/share/gdm/BuiltInSessions/*"]
    for r in remove:
        pisitools.remove(r)
    pisitools.removeDir("/usr/share/xsessions")

    pisitools.remove("/etc/X11/gdm/Xsession")
    pisitools.removeDir("/etc/X11/dm")
    pisitools.dosym("/usr/lib/X11/xinit/Xsession", "/etc/X11/gdm/Xsession")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
