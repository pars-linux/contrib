#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "tex -ini", "latex -ini")
#   autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.doman("*.1")
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog*", "COPYING*", "INSTALL", "NEWS", "README", "TODO")    
    pisitools.dodir("/usr/bin")
    pisitools.dosym("/usr/bin/latex", "/usr/bin/jadetex")
    pisitools.dosym("/usr/bin/pdftex", "/usr/bin/pdfjadetex")
