#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Multimedia Converter %s" % get.srcVERSION()

def install():
    shelltools.system("tar xvf mconverter-1.5.tgz")
    pisitools.insinto("/usr/kde/3.5/bin", "usr/local/LinConverter/LinConverter.kmdr", "mconverter.kmdr")

    pisitools.dodoc("usr/share/doc/license.txt")
