#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = 'glew'

def build():
    autotools.make()

def install():
    autotools.rawInstall("GLEW_DEST=%s/usr" % get.installDIR())

    # No static libraries
    pisitools.remove("/usr/lib/libGLEW.a")

    pisitools.dodoc("README.txt", "doc/*.txt")
    pisitools.dohtml("doc/*")
