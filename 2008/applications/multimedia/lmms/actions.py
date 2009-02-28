#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DWANT_CAPS=TRUE -DWANT_PORTAUDIO=FALSE -DWANT_SYSTEM_SR=TRUE -DWANT_STK=FALSE -DWANT_VST_NOWINE=FALSE", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "/usr/share/lmms/themes/default/icon.png", "lmms.png")

    pisitools.dodoc("../AUTHORS", "../COPYING", "../ChangeLog", "../TODO", "../README")
