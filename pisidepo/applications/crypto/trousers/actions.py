#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    #pisitools.dosbin("src/tcsd/tcsd")
    #pisitools.dolib_a("src/tddl/*.a")
    #pisitools.dolib("src/tspi/libtspi.*")
    #pisitools.insinto("/usr/include/","src/include/tss")
    #pisitools.insinto("/usr/include/","src/include/trousers")
    autotools.install()
    pisitools.dobin("tools/ps_convert","/usr/share/doc/%s/tools" % get.srcTAG())
    pisitools.dobin("tools/ps_inspect","/usr/share/doc/%s/tools" % get.srcTAG())
    pisitools.dodoc("README","AUTHORS","ChangeLog","NICETOHAVES","TODO")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "doc/*")