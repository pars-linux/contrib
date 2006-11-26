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
    pisitools.dobin("opj2dat")