#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static")

    shelltools.cd("src/qttestrunner")
    shelltools.system("qmake qttestrunnerlib.pro")

def build():
    autotools.make()

    shelltools.cd("src/qttestrunner")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dolib("lib/libqttestrunner.so*")

    # remove md5 files move html's
    pisitools.remove("/usr/share/cppunit/html/*.md5")
    pisitools.domove("/usr/share/cppunit/html/", "/usr/share/doc/%s/html/" % get.srcTAG())

    pisitools.dodoc("ChangeLog","COPYING","THANKS","TODO")
