#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="compiz-%s" % get.srcVERSION()

def setup():
    autotools.configure("--disable-static \
                         --disable-metacity \
                         --disable-gnome \
                         --disable-gnome-keybindings \
                         --disable-libtool-lock \
                         --disable-gconf \
                         --enable-fuse \
                         --enable-gtk \
                         --enable-inotify \
                         --enable-glib \
                         --enable-kde \
                         --enable-kde4 \
                         --enable-kconfig \
                         --enable-dbus \
                         --enable-annotate \
                         --enable-dbus-glib \
                         --enable-place \
                         --enable-librsvg")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
