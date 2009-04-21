#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-python \
                         --disable-3rdparty")

def build():
    autotools.make()

def install():
    autotools.install()

    pythonmodules.fixCompiledPy()

    pisitools.dohtml("doc/fitykhelp.html", "doc/html.css")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "TODO", "NEWS")
