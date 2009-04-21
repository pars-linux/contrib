#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-xvid-prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dosym("/usr/lib/librevel.so.%s" % get.srcVERSION(), "/usr/lib/librevel.so.1")
    pisitools.dosym("/usr/lib/librevel.so.%s" % get.srcVERSION(), "/usr/lib/librevel.so")

    pisitools.dodoc("ChangeLog", "COPYING", "NEWS", "README", "THANKS", "TODO")
