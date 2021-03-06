#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DENABLE_SHARED=ON", installPrefix="%s/usr" % get.installDIR())

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall()

    pisitools.dodoc("ChangeLog", "COPYING", "README")
