#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pisitools.insinto("/usr/bin", "anytowav")
    pisitools.insinto("/usr/bin", "audioconvert")
    pisitools.insinto("/usr/bin", "movie2sound")
    pisitools.insinto("/usr/bin", "oggdrop-lx")
    pisitools.insinto("%s/share/apps/konqueror/servicemenus" % get.kdeDIR(), "*.desktop")

    pisitools.dodoc("ChangeLog", "COPYING", "README")
