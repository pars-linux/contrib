#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #Fixme !!! 
    #shelltools.sym("%s/gal-2.4.3/docs/gal-decl.txt", "%s/gal-2.4.3/docs/gal-2.4-decl.txt" % get.workDIR())
    #shelltools.sym("%s/gal-2.4.3/docs/gal-sections.txt", "%s/gal-2.4.3/docs/gal-2.4-sections.txt" % get.workDIR())
    autotools.configure("--enable-static")

def build():
    autotools.make("-j1")

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "MAINTAINERS", "NEWS", "README")
