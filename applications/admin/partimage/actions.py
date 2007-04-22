#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Fahri Tuğrul Gürkaynak <ftugrul@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    shelltools.system("useradd partimag -g root")
    
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README*")