#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --disable-dependency-tracking")

def build():
    autotools.make("html")

def install():
    autotools.install()

    pisitools.dohtml("doc/reference/html_files/*")

    for i in ["doc/examples/*.cpp", "doc/examples/ginac-examples.html/index.html"]:
        pisitools.insinto("/usr/share/doc/%s/examples" % get.srcNAME(), i)

    pisitools.dodoc("ChangeLog","NEWS","README","COPYING","AUTHORS")
