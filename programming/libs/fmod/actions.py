#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="fmodapi375linux"

def install():
    pisitools.insinto("/usr/lib","api/libfmod-3.75.so")
    pisitools.dosym("/usr/lib/libfmod-3.75.so","/usr/lib/libfmod.so")

    pisitools.insinto("/usr/include","api/inc/*.h")

    pisitools.dohtml("documentation/*.html")
    pisitools.insinto("/usr/share/doc/fmod-%s-%s/html" % (get.srcVERSION(),get.srcRELEASE()),"documentation/HTML")
