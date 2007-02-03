#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools


def setup():
    autotools.configure("--enable-xkb-support --enable-xmm-support --enable-doc --enable-doxygen")

def build():
    autotools.make()

def install():
    autotools.install()
