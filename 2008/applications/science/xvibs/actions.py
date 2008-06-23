#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.unlink("xvibs.jar")
    shelltools.unlinkDir("classes")

def build():
    shelltools.system("ant")

def install():
    pisitools.insinto("/usr/share/java", "xvibs.jar")
    pisitools.insinto("/usr/share/doc/%s/samples" % get.srcTAG(), "samples/*")

    pisitools.dohtml("index.html")
    pisitools.dodoc("documentation/License.txt")
