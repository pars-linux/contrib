#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "bbrun-1.6/bbrun"

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dobin("bbrun")
    shelltools.cd("..")
    pisitools.dodoc("Changelog", "COPYING", "README")