#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-multibyte")

def build():
    autotools.make()

def check():
    autotools.make("test")

def install():
    autotools.install()

    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("COPYING", "CHANGES")
