#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "ipfdevlib_linux"

def install():
    pisitools.dobin("examples/i686/ipfinfo")

    pisitools.insinto("/usr/include/caps", "include/caps/capsimage.h")

    pisitools.dolib_so("lib/i686/libcapsimage.so.2.0")
    pisitools.dosym("/usr/lib/libcapsimage.so.2.0", "/usr/lib/libcapsimage.so.2")
    pisitools.dosym("/usr/lib/libcapsimage.so.2.0", "/usr/lib/libcapsimage.so")

    pisitools.dodoc("HISTORY", "LICENSE", "README")
