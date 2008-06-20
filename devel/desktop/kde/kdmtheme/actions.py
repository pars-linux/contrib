#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    autotools.aclocal()
    kde.configure("--disable-rpath")


def build():
    kde.make("-f Makefile.cvs")


def install():
    kde.install()

    pisitools.dodoc("AUTHORS", "README", "ChangeLog", "TODO")
