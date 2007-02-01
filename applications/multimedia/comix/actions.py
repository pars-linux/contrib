#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def install():
     pythonmodules.run("install.py install --no-mime --installdir /usr 1>/dev/null")

     pisitools.dobin("mime/comicthumb")

     pisitools.insinto("/usr/share/mime/packages/", "mime/comix.xml")
     pisitools.insinto("/etc/gconf/schemas/", "mime/comicbook.schemas")

     pisitools.dodoc("ChangeLog", "COPYING", "README")