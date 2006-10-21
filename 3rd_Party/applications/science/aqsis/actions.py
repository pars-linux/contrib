#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools

WorkDir = "aqsis-1_1_0"

def build():
    scons.make("no_exr=1")

def install():
    pisitools.dobin("output/bin/aqs*")
    pisitools.dobin("output/bin/*ser")

    pisitools.dolib("output/bin/*.so", "/usr/lib/aqsis")
    pisitools.domove("/usr/lib/aqsis/libaqsis.so", "/usr/lib")

    pisitools.insinto("/etc", "output/etc/aqsisrc")
    pisitools.insinto("/usr/include/aqsis", "output/include/aqsis/*")
    pisitools.insinto("/usr/share/aqsis/shaders", "output/shaders/*")

    pisitools.dodoc("AUTHORS", "COPYING", "README*")

