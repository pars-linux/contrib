#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoconf()
    autotools.configure("--disable-vanity        \
                         --disable-gtk           \
             --enable-dbus           \
                         --enable-gnome          \
             --enable-lirc           \
             --with-x                \
             --enable-debug          \
                  --enable-nautilus       \
                         --disable-mozilla")
#                        MOZILLA_PLUGINDIR=/usr/lib/MozillaFirefox/include \
#                        --enable-nvtv          \
#                        --enable-gstreamer=0.10 \
#                        --with-mozilla \
#/usr/lib/MozillaFirefox/idl/nsISupports.idl
#                         MOZILLA_PLUGINDIR=/usr/lib/nsbrowser
#                        --enable-firefox        \

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #fixme: why does it need write access here, probably need to set up a fake
    #home in /var/tmp like other pkgs do
#    addpredict "/root/.gconfd"
#    addpredict "/root/.gconf"
#    addpredict "/root/.gnome2"
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "INSTALL", "NEWS", "README", "TODO")
