#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="ksquirrel-libs-0.7.0-pre2"

def setup():
    autotools.configure("--disable-camera \
                         --disable-djvu \
                         --disable-jpeg2000 \
                         --disable-mng \
                         --disable-svg \
                         --disable-ttf \
                         --disable-wmf \
                         --enable-final")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
