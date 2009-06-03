#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import perlmodules

def setup():
    pisitools.dosed("hamlib.pc.in", r"^(includedir=.*)$", r"\1/hamlib")

    autotools.configure("--without-rpc-backends \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s pythondir=/usr/lib/%s" % (get.installDIR(), get.curPYTHON()))

    pythonmodules.fixCompiledPy()
    perlmodules.fixLocalPod()

    pisitools.dodoc("AUTHORS", "README", "README.betatester", "README.developer", "NEWS", "TODO")
