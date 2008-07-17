#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "tomcat-connectors-%s-src" % get.srcVERSION()

def setup():
    shelltools.cd("native") # Change to build directory
    autotools.configure("--with-apxs=/usr/sbin/apxs")

def build():
    shelltools.cd("native") # Change to build directory
    autotools.make()

def install():
    pisitools.insinto("/usr/lib/apache2/modules", "native/apache-2.0/mod_jk.so")

    pisitools.dohtml("docs/*")
