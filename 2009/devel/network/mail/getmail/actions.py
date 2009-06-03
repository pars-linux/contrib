#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def install():
    pisitools.dosed("setup.py", "'./getmail.spec'", "#'./getmail.spec'")
    pythonmodules.install()

    pisitools.dodoc("docs/*.txt", "docs/getmailrc-examples", "docs/CHANGELOG", "docs/COPYING", "README")
    pisitools.dohtml("docs/*")

    pisitools.removeDir("/usr/share/doc/getmail-%s/" % get.srcVERSION())
