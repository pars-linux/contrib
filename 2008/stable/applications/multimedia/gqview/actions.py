#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("%s/%s" % (get.docDIR(), get.srcDIR()))

    pisitools.dohtml("doc/*.html")
    pisitools.dohtml("doc/*.txt")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "NEWS", "COPYING", "TODO")
