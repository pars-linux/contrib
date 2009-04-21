#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "abook-0.6.0pre2"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/doc/%s/"% get.srcTAG(), "contrib/")
    pisitools.insinto("/usr/share/doc/%s/"% get.srcTAG(), "sample.abookrc")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "LICENSE")
