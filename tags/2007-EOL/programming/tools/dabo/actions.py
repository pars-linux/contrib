#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "dabo"

def install():
    pythonmodules.install()

    pisitools.insinto("/usr/lib/%s/site-packages/dabo/ide" % get.curPYTHON(), "ide/*")
    pisitools.insinto("/usr/share/pixmaps", "ide/sampleDaboIcon.png", "daboide.png")

    pisitools.domove("/usr/dabo/*", "/usr/lib/%s/site-packages/dabo" % get.curPYTHON())

    pisitools.dodoc("ANNOUNCE", "AUTHORS", "ChangeLog", "dabo/LICENSE.TXT", "README", "TODO")
