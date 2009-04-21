#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="qmmp_skins-%s" %get.srcVERSION()

def install():
    for skin in ("parskin", "parskin_v.2", "qmmp_black", "qmmp_black_mod1"):
        pisitools.insinto("/usr/share/qmmp/skins/%s" % skin, "%s/*" % skin)

    pisitools.dodoc("COPYING")
