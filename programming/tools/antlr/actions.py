#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-java \
                         --enable-cxx \
                         --enable-python \
                         --enable-csharp \
                         --enable-examples")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.rename("/usr/share/doc/antlr-%s" % get.srcVERSION(), get.srcTAG())
