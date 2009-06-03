#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile.in", "DESTDIR=", "DESTDIR=%s" % get.installDIR())

    autotools.configure("--enable-shared \
                         --disable-static \
                         --with-tk \
                         --without-gtk2 \
                         --with-ocaml \
                         --with-java \
                         --with-atlas-library=/usr/lib \
                         --with-x")

def build():

    autotools.make("all")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps/", "X11_defaults/scilab.xpm")
    pisitools.insinto("/usr/share/applications", "scilab.desktop")
