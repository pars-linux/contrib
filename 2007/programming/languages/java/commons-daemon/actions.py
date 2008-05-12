#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="daemon-%s" % get.srcVERSION()

def setup():
    shelltools.cd("src/native/unix")
    autotools.autoconf()
    autotools.configure("--with-java=/opt/sun-jdk")
    autotools.make()

    shelltools.cd("../../..")
    shelltools.system("ant jar")

def install():
    pisitools.dobin("src/native/unix/jsvc")
    pisitools.insinto("/usr/share/java","dist/*.jar")

    pisitools.dodoc("README","RELEASE-NOTES.txt")
    pisitools.dohtml("*.html")
