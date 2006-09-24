#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "bbmail-0.8.3"

def setup():
    autotools.configure()
def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "BUGS", "COPYING", "ChangeLog", "INSTALL", "NEWS", "README", "TODO")