#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir ="kvm"

def install():
    pisitools.insinto("/usr/bin", "src/kvm")
    pisitools.insinto("%s/share/apps/konqueror/servicemenus" % get.kdeDIR(), "src/kvm*.desktop")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
