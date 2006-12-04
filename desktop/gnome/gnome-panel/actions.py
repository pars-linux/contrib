#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    # We should patch in a switch here and send it upstream
    pisitools.dosed("gnome-panel/Makefile.in", "--load", "-v")
    
    # Calling this late so it doesn't process the GConf schemas file we already in comar
    # took care of it.
    autotools.configure("--disable-scrollkeeper --enable-eds")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.removeDir("/var/lib/scrollkeeper")
    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "NEWS", "README")
