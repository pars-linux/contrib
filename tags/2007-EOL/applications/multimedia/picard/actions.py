#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed('picard/ui/options/cdlookup.py', '""', '"/dev/cdrom"')
    pythonmodules.run('setup.py config')

def install():
    pythonmodules.install('--disable-autoupdate')

    pisitools.dodoc('AUTHORS.txt', 'COPYING.txt', 'NEWS.txt')
