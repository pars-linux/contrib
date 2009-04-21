#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-pcmcia")

def build():
    autotools.make()

def install():
    pisitools.doexe("comedi/drivers/*.ko", "/lib/modules/%s/extra/comedi/" % get.curKERNEL())
    pisitools.doexe("comedi/comedi.ko", "/lib/modules/%s/extra/comedi/" % get.curKERNEL())
    pisitools.doexe("comedi/kcomedilib/kcomedilib.ko", "/lib/modules/%s/extra/comedi/" % get.curKERNEL())

    pisitools.dodoc("README", "COPYING", "NEWS", "TODO","AUTHORS")
