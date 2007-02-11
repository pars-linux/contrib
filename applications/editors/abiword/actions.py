#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="%s/abi" % get.srcDIR()

def setup():
    autotools.configure("--with-x \
                                  --with-ImageMagick \
                                  --with-libxml2 \
                                  --with-sys-wv \
                                  --with-zlib \
                                  --with-libpng \
                                  --with-popt \
                                  --with-builtin-plugins")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("docs/Abi*")