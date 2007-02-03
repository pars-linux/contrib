#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
#   since multiple bbtools packages provide this file, install
#   it in /usr/share/doc/
    pisitools.domove("/usr/share/bbtools/bbtoolsrc.in", "/usr/share/doc/%s" % get.srcTAG(), "bbtoolsrc.example")    
    pisitools.dodoc("README", "COPYING", "AUTHORS", "INSTALL", "ChangeLog", "NEWS", "TODO", "data/README.bbweather")
