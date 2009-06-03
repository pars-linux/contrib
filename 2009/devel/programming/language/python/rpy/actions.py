#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import autotools

def build():
    shelltools.cd("doc")
    autotools.make("html")

def install():
    shelltools.export("RHOMES","/usr/lib/R")

    pythonmodules.install()

    pisitools.remove("/usr/lib/python2.4/site-packages/rpy_wintools.py")

    # add docs, examples and tests
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "examples")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "tests")
    pisitools.dohtml("doc/rpy_html")