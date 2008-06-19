#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Manencode-%s" % get.srcVERSION()

def setup():
    shelltools.system("/usr/bin/qmake-qt4 Manencode.pro")

def build():
    autotools.make()

def install():
    for data in ["Manencode","Interface","*.qm"]:
        pisitools.insinto("/usr/share/manencode",data)

    pisitools.dosym("/usr/share/manencode/Manencode","/usr/bin/manencode")
