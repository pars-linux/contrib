#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoconf()
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # Documentation install for each of the games
#    for game in \
#    $(find . -maxdepth 1 -type d ! -name po ! -name libgames-support); do
#    	docinto ${game}
#	for doc in AUTHORS ChangeLog NEWS README TODO; do
#		[ -s ${game}/${doc} ] && dodoc ${game}/${doc}
#	done
#    done
    
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "INSTALL", "NEWS", "README", "TODO")