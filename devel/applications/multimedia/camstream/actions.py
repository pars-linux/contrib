#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="camstream-070511"

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--with-qt=/usr/qt/3")

def build():
    autotools.make()

def install():
    autotools.install()

    # No libs and headers needed
    pisitools.removeDir("/usr/lib")
    pisitools.removeDir("/usr/include")

    pisitools.dohtml("docs/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
