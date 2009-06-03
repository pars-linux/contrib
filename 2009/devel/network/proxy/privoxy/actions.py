#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "privoxy-3.0.10-stable"

def setup():
    autotools.autoheader()
    autotools.autoconf()

    autotools.configure("--enable-dynamic-pcre \
                         --enable-zlib")

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/sbin", "privoxy")
    pisitools.doman("privoxy.1")
