#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="qwtplot3d"

def setup():
    shelltools.system("qmake")

def build():
    autotools.make()


def install():
    pisitools.insinto("/usr/lib/","lib/*")
    pisitools.insinto("/usr/include/","include/*")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "examples")