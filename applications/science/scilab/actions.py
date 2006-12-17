#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile.in", "DESTDIR=", "DESTDIR=%s" % get.installDIR())
    autotools.rawConfigure("--prefix=/usr \
                            --bindir=/usr/bin \
                            --datadir=/usr/share \
                            --docdir=/usr/share/doc \
                            --with-local-xaw \
                            --with-pvm \
                            --with-tk \
                            --with-addedf2c \
                            --with-ocaml \
                            --with-java \
                            --with-atlas-library=/usr/lib \
                            --with-x")

def build():
    autotools.make("all")

def install():
    autotools.install()

    pisitools.insinto("/usr/share/pixmaps/", "X11_defaults/scilab.xpm")
    pisitools.insinto("/usr/share/applications", "scilab.desktop")