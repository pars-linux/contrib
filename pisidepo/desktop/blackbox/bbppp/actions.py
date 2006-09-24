#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "bbppp-0.2.3"

def setup():
    autotools.configure()
def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("README", "COPYING", "AUTHORS", "BUGS", "INSTALL", "ChangeLog", "NEWS", "TODO", "data/README.bbppp")