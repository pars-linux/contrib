#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "gtk-smooth-engine-0.6.0.1"

def setup():
    autotools.configure("--enable-gtk-1 \
                         --disable-gtk-2")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
