#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-plugin-scintilla \
                         --disable-scrollkeeper ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("-j1 GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("TODO", "AUTHORS", "ChangeLog", "README", "ROADMAP", "THANKS", "FUTURE")
