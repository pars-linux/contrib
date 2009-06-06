#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008, 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Glib-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

    pisitools.dosed("Makefile", " -shared ", " -lperl -Wl,--as-needed -shared ")

def build():
    perlmodules.make()

def install():
    perlmodules.install()

    pisitools.dodoc("AUTHORS", "README", "TODO", "NEWS")
