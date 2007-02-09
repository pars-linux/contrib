#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-win32 \
                         --with-opengl \
                         --with-bzip2 \
                         --with-vorbis \
                         --with-theora \
                         --with-mikmod \
                         --with-mng")

def build():
    autotools.make()

def install():
    pisitools.dobin("stratagus")

    pisitools.dodoc("COPYING", "README", "doc/*")
    pisitools.dohtml("doc/*.html")
