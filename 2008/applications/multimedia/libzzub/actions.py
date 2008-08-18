#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import scons
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():

    pisitools.dosed("SConstruct", "share/doc/zzub", "share/doc/%s" % get.srcTAG())

    scons.make('DEBUG=False \
                DESTDIR="%s" \
                PREFIX="/%s" configure' % (get.installDIR(), get.defaultprefixDIR()))

def build():
    scons.make('LINKFLAGS="%s"' % get.LDFLAGS())

    shelltools.cd("src/pyzzub")
    pythonmodules.compile()

def install():
    scons.install()

    shelltools.cd("src/pyzzub")
    pythonmodules.install()

    shelltools.cd("../..")
    pisitools.dodoc("LICENCE", "CREDITS.txt", "ChangeLog")

