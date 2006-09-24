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

WorkDir = "SGMLSpm"

def setup():
#   pisitools.dosed("Makefile", "${D}", "%s" % get.installDIR())
#   pisitools.dosed("Makefile", "${P}", "%s" % get.srcTAG())
    pass 

def build():
    pass    


def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/lib/perl5/vendor_perl/5.8.8")
    pisitools.dodir("/usr/share/SGMLS")
    shelltools.system("make install -f %s/SGMLSpm/Makefile" % get.workDIR())
    shelltools.system("make docs -f %s/SGMLSpm/Makefile" % get.workDIR())
    pisitools.dodoc("BUGS", "ChangeLog", "COPYING", "README", "TODO")
