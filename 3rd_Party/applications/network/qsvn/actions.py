#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("/usr/qt/4/bin/qmake qsvn.pro")
        
def build():
    autotools.make()
	    
def install():
    shelltools.chmod("%s/qsvn-0.4.0/images/qsvn.png" % get.workDIR(), 0755)
    pisitools.dodir("/usr/share/qsvn")
    shelltools.move("bin/qsvn" ,"%s/usr/share/qsvn/qsvn" % get.installDIR())
    pisitools.insinto("/usr/share/qsvn/","images")
    pisitools.insinto("/usr/share/qsvn/","licenses")
    pisitools.dosym("/usr/share/qsvn/qsvn","/usr/bin/qsvn")
    pisitools.dodoc("ChangeLog", "INSTALL", "README")
