#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="enlightenment-0.16.999.035"

def setup():
    autotools.configure("--enable-nls \
                         --enable-rpath \
                         --enable-x \
                         --with-gnu-ld \
                         --enable-libiconv \
                         --enable-libintl \
                         --enable-esd-sound \
                         --enable-xinerama \
                         --enable-xrandr \
                         --enable-upgrade \
                         --enable-hints-ewmh \
                         --enable-fsstd \
                         --enable-zoom \
                         --with-imlib2 \
                         --enable-evas-config \
                         --enable-ecore-config \
                         --enable-edje-cc \
                         --enable-edje \
                         --enable-eet-config \
                         --enable-embryo-config")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domo("po/tr.po","tr","enlightenment.mo")
    pisitools.dodoc("AUTHORS", "ChangeLog", "INSTALL", "NEWS", "README*", "docs/README*")

