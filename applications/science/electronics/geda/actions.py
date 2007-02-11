#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools

WorkDir = "geda-gattrib-20061020"

def setup():
    autotools.configure("--disable-dependency-tracking \
                         --with-docdir=/usr/share/doc \
                         --with-pcbconfdir=/usr/share/pcb \
                         --with-pcbm4dir=/usr/share/pcb/m4")

def build():
    autotools.make()

def install():
    autotools.install()
