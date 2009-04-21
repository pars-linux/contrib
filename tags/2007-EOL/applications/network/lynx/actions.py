#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="lynx2-8-6"

def setup():
    autotools.configure("--libdir=/etc/lynx \
                         --enable-ipv6 \
                         --enable-widec \
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
                         --with-bzlib \
                         --with-zlib \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGES","COPYHEADER","PROBLEMS","README","docs/*","lynx_help/*.txt")
