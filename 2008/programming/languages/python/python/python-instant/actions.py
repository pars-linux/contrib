#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#(c) TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "instant-%s" % get.srcVERSION()

def install():
    pythonmodules.install()
    #fix .gz files in /usr/share/man when bug #8426 is reflected to pisi.
    pisitools.dodoc("ChangeLog", "RELEASENOTES", "AUTHORS", "LICENSE", "TODO")
