#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Eren Türkay <turkay.eren@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="lynx2-8-5"

def setup():
    autotools.configure("--libdir=/etc/lynx \
                                           --enable-cgi-links \
                                           --enable-EXP_PERSISTENT_COOKIES \
                                           --enable-prettysrc \
                                           --enable-nls-fork \
                                           --enable-file-upload \
                                           --enable-read-eta \
                                           --enable-libjs \
                                           --enable-color-style \
                                           --enable-scrollbar \
                                           --enable-included-msgs \
                                           --with-zlib \
                                           --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("CHANGES","COPYHEADER","PROBLEMS","README","docs/*","lynx_help/*.txt")