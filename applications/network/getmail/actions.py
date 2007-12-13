#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def install():
    pythonmodules.install()

    pisitools.dodoc("docs/*.txt", "docs/getmailrc-examples", "docs/CHANGELOG", "docs/COPYING", "README")
    pisitools.dohtml("docs/configuration.html", "docs/documentation.html", "docs/troubleshooting.html")

    pisitools.removeDir("/usr/share/doc/getmail-%s/" % get.srcVERSION())
