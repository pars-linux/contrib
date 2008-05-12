#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Coin-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-optimization \
                         --enable-3ds-import \
                         --enable-vrml97 \
                         --enable-man  \
                         --disable-html-help \
                         --disable-html \
                         --without-mesa \
                         --without-simage \
                         --with-doxygen \
                         --with-freetype \
                         --with-bzip2 \
                         --with-fontconfig \
                         --with-openal \
                         --with-opengl \
                         --with-opengl-glu \
                         --with-x \
                         --with-zlib \
                         --disable-java-wrapper \
                         --disable-javascript-api \
                         --without-spidermokey")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "NEWS", "README*", "RELNOTES", "THANKS")

    # Waiting for a maintainer to fix, see #117756. on bugs.gentoo.org, remove conflict file  with openssl 
    pisitools.remove("/usr/share/man/man3/_var_pisi_coin-*")
    pisitools.remove("/usr/share/man/man3/threads.3")
