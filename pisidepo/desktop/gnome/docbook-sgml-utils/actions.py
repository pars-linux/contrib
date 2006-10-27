#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "docbook-utils-0.6.14"

def setup():
#    autotools.autoconf()
    autotools.configure("--disable-tetex")

def build():
    pass

def install():
    autotools.install()
#"-e -f --makefile=Makefile --prefix=%s/usr" % get.installDIR())
                    #htmldir=/usr/share/doc/%s/html" % (get.installDIR(), get.srcTAG()))
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
