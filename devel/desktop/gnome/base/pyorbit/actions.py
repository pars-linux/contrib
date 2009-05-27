#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import libtools
def setup():
    autotools.aclocal("-I m4")
    autotools.automake("-fi")
    autotools.autoconf()
    libtools.libtoolize("--copy --force")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pythonmodules.fixCompiledPy(lookInto="/usr/lib/%s/site-packages" % get.curPYTHON())

    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "INSTALL", "MAINTAINERS", "NEWS", "README", "TODO")
