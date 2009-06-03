#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dosym("/usr/lib/%s/site-packages/takenote/images/takenote-icon.png" % get.curPYTHON(), "/usr/share/pixmaps/takenote.png")

    pisitools.dodoc("COPYING", "CHANGES", "README", "LICENSE")
