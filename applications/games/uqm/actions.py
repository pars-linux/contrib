#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "%s-%s/sc2" % (get.srcNAME(), get.srcVERSION())

def build():
    shelltools.system("sh build.sh uqm")

def install():
    pisitools.dobin("uqm", "/usr/share/uqm")
    pisitools.insinto("/usr/share/uqm/content", "content/version")
    pisitools.dodoc("README", "COPYING", "AUTHORS", "doc/users/manual.txt")
