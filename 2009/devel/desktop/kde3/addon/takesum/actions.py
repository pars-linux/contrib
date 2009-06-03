#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "takesum_%s/src" % get.srcVERSION()

def install():
    pisitools.dobin("takesum")
    pisitools.insinto("%s/share/apps/konqueror/servicemenus" % get.kdeDIR(), "takesum_check.desktop")
    pisitools.insinto("%s/share/apps/konqueror/servicemenus" % get.kdeDIR(), "takesum_sha1.desktop")
    pisitools.insinto("%s/share/apps/konqueror/servicemenus" % get.kdeDIR(), "takesum_md5.desktop")
