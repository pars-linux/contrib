#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde

def setup():
    kde.configure("--disable-camera \
                   --disable-djvu \
                   --disable-jpeg2000 \
                   --disable-gif \
                   --disable-mng \
                   --disable-svg \
                   --disable-ttf \
                   --disable-xcf \
                   --disable-dxf \
                   --disable-wmf \
                   --enable-final")

def build():
    kde.make()

def install():
    kde.install()
