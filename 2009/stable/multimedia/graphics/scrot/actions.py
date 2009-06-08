#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    pisitools.dosed("Makefile", "docsdir = .*", "docsdir = %s/usr/share/doc/%s" % (get.installDIR(), get.srcTAG()))
    autotools.make()

def install():
    autotools.install()
