#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "YouGrabber-%s" % get.srcVERSION()

def build():
    shelltools.cd("src")
    shelltools.system("make")
    shelltools.cd("..")

def install():
    pisitools.insinto("/usr/bin", "src/yg", "yougrabber")

    pisitools.dodoc("doc/LICENSE", "doc/README", "doc/CHANGELOG", "yg.conf.sample")
