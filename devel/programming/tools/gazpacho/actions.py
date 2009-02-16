#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pythonmodules.install()

    # when the doc files are not under /usr/share/doc/gazpacho , gazpacho do not start
    # that's why all docs are unified under /usr/share/doc/gazpacho
    pisitools.removeDir("/usr/share/doc/%s/" % get.srcTAG() )
    pisitools.insinto("/usr/share/doc/gazpacho", "doc/*")
