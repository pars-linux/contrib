#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-x \
                                  --with-ImageMagick \
                                  --with-libxml2 \
                                  --with-zlib \
                                  --with-libpng \
                                  --with-popt \
                                  --with-fribidi \
                                  --enable-scripting \
                                  --enable-printing \
                                  --enable-gnomeui")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("docs/Abi*", "docs/NonLatin1UnixLocales.abw")
