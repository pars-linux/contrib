#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "compiz"

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--disable-static \
                         --disable-metacity \
                         --disable-gnome \
                         --disable-gnome-keybindings \
                         --disable-libtool-lock \
                         --disable-gconf \
                         --enable-kconfig \
                         --enable-fuse \
                         --enable-gtk \
                         --enable-inotify \
                         --enable-glib \
                         --enable-kde \
                         --enable-dbus \
                         --enable-annotate \
                         --enable-place \
                         --enable-schemas-install \
                         --enable-dbus-glib \
                         --enable-librsvg")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
