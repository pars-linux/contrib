#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
    autotools.configure("--disable-scrollkeeper")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS","ChangeLog","HACKING","MAINTAINERS","NEWS","README","TODO")