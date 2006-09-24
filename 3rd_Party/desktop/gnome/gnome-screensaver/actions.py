#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-pam --enable-xinerama --enable-debug \
                         --enable-locking --with-libexif --with-dpms-ext \
                         --with-xscreensaverdir=/usr/share/xscreensaver/config  \
                         --with-xscreensaverhackdir=/usr/lib/misc/xscreensaver")
#                        --with-gdm-config=/usr/share/gdm/defaults.conf   \

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.chmod("%s/usr/libexec/gnome-screensaver-dialog" % get.installDIR(), 0755)
    pisitools.dodoc("data/migrate-xscreensaver-config.sh", "data/xscreensaver-config.xsl", "xss-conversion.txt")
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "INSTALL", "NEWS", "README", "TODO")
    #Conversion information
    #shelltools.system("/usr/bin/sed -e 's:\${PF}:%s:' < xss-conversion.txt > xss-conversion.txt" % get.srcTAG())
