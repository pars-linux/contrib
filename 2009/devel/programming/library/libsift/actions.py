#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="libsift-1.8/src"


def build():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())

    autotools.make("lib")

def install():
    pisitools.insinto("/usr/lib","libsift.dll")

    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "TODO")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "VERSION")