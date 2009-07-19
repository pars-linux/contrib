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
    shelltools.system("qmake-qt4 PREFIX=%s/usr DOC_DIR=%s/usr/share/doc/%s/html" %
            (get.installDIR(), get.installDIR(), get.srcTAG()))

def build():
    shelltools.cd("QGLViewer")
    autotools.make("QMAKE=qmake")

def install():
    shelltools.cd("QGLViewer")
    autotools.rawInstall("PREFIX=%s/usr DESTDIR=%s" % (get.installDIR(), get.installDIR()))

    shelltools.cd("..")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "examples" )
    pisitools.dodoc("CHANGELOG", "LICENCE", "README")
