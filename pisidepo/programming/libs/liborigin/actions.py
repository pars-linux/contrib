#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make("-f Makefile.LINUX")


def install():
    pisitools.dolib("liborigin.so")
    pisitools.dosym("/usr/lib/liborigin.so","/usr/lib/liborigin.so.0")
    pisitools.dobin("opj2dat")
    pisitools.insinto("/usr/include","OPJFile.h")