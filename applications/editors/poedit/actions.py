#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--with-wx-config=/usr/bin/wx-config-2.8 --prefix %s/usr" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc('COPYING', 'README', 'AUTHORS', 'NEWS', 'TODO')
