#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    autotools.autoconf()
    libtools.libtoolize("--force")
    # with gtk-doc parameter gives error!!
    autotools.rawConfigure("--host=%s  \
                            --prefix=/usr \
                            --libdir=/usr/lib \
                            --mandir=/usr/share/man \
                            --infodir=/usr/share/info \
                            --sysconfdir=/etc \
                            --localstatedir=/var/lib \
                            --with-kde-datadir=%s/share \
                            --disable-gtk-doc  \
                            --enable-prefer-db1 \
                            --enable-compat185" % (get.HOST(), get.kdeDIR()))


def build():
    autotools.make("-j1")
    shelltools.cd("devel-docs")
    autotools.make()
    shelltools.cd("..")

def install():
    autotools.install()

    paket = "get.srcTAG()"
    
#    autotools.rawInstall("DESTDIR=%s prefix=%s/usr \
#                          libdir=%s/usr/lib \
#                          mandir=%s/usr/share/man \
#                          infodir=%s/usr/share/info \
#                          sysconfdir=%s/etc \
#                          localstatedir=%s/var/lib \
#                          docdir=%s/usr/share/doc/" + paket +
#                          "HTML_DIR=%s/usr/share/gnome/html" % get.installDIR())
    
    #mess clean up
    pisitools.remove("/usr/share/gtkrc*")
    #
    pisitools.domove("/usr/doc", "/usr/share/doc", "%s" % get.srcTAG())
    #
    pisitools.domove("/usr/share/doc/gnome-doc", "/usr/share/doc/%s" % get.srcTAG())
    pisitools.domove("/usr/share/doc/gnome-doc.1", "/usr/share/doc/%s" % get.srcTAG())
    pisitools.domove("/usr/share/doc/gnome-doc.el", "/usr/share/doc/%s" % get.srcTAG())
    pisitools.domove("/usr/share/doc/gnome-mkstub.1", "/usr/share/doc/%s" % get.srcTAG())
    pisitools.domove("/usr/share/doc/mkstub", "/usr/share/doc/%s" % get.srcTAG())
    ####

    ####
    #Conflict with libgnomeui
    #/usr/share/pixmaps/gnome-error.png from libgnomeui package
    #/usr/share/pixmaps/gnome-default-dlg.png from libgnomeui package
    #/usr/share/pixmaps/gnome-question.png from libgnomeui package
    #/usr/share/pixmaps/gnome-warning.png from libgnomeui package
    #/usr/share/pixmaps/gnome-info.png from libgnomeui package    
    pisitools.remove("/usr/share/pixmaps/gnome-error.png")
    pisitools.remove("/usr/share/pixmaps/gnome-default-dlg.png")
    pisitools.remove("/usr/share/pixmaps/gnome-question.png")
    pisitools.remove("/usr/share/pixmaps/gnome-warning.png")
    pisitools.remove("/usr/share/pixmaps/gnome-info.png")    
    ####
    
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "INSTALL", "NEWS", "README", "HACKING", "TODO")
