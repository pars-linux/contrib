#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system('xdt-autogen')
    autotools.configure("--disable-static \
                         --enable-gnome \
                         --enable-libgnome-keyring \
                         --enable-final \
                         --enable-session-screenshots \
                         --disable-legacy-sm")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # It's also in pardus-default-settings-xfce package.
    pisitools.remove("/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-session.xml")

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog*", "NEWS", "README", "TODO")
