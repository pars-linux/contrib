#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed('picard/ui/options/cdlookup.py', '""', '"/dev/cdrom"')
    pythonmodules.run('setup.py config')

def install():
    shelltools.export("CFLAGS", "%s -I/usr/include/libavcodec -I/usr/include/libavformat" % get.CFLAGS())
    pythonmodules.install('--disable-autoupdate')

    pisitools.dodoc('AUTHORS.txt', 'COPYING.txt', 'NEWS.txt')
