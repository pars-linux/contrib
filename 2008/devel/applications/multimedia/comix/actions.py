#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pythonmodules.run("install.py install --no-mime --dir %s/usr" % get.installDIR())

    pisitools.insinto("/etc/gconf/schemas", "mime/comicbook.schemas")

    pisitools.dodoc("ChangeLog", "COPYING", "README")
