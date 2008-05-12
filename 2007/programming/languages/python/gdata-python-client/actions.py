#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="gdata.py-%s" % get.srcVERSION()

def install():
    pythonmodules.install()

    # Code samples
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(),"samples")

    pisitools.dodoc("RELEASE_NOTES.txt", "README.txt")
