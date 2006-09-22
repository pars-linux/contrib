#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "bbsload-0.2.8"

def setup():
#   needs automake 1.7. breaks with emake.
    shelltools.export("WANT_AUTOMAKE", "1.7")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("README", "COPYING", "AUTHORS", "BUGS", "INSTALL", "ChangeLog", "NEWS", "TODO", "data/README.bbsload")