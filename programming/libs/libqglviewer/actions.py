#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="libQGLViewer-%s" % get.srcVERSION().replace("_", "-")

def setup():
    shelltools.cd("QGLViewer")
    shelltools.system("qmake PREFIX=%s/usr" % get.installDIR())

def build():
    shelltools.cd("QGLViewer")
    autotools.make("QMAKE=qmake")

def install():
    shelltools.cd("QGLViewer")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.insinto("/usr/share/doc/%s/html" % get.srcTAG(), "doc/images")
    pisitools.insinto("/usr/share/doc/%s/html" % get.srcTAG(), "doc/refManual")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "examples" )
    pisitools.dohtml("doc/*")
    pisitools.dodoc("CHANGELOG", "LICENCE", "README")
