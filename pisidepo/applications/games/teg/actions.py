#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# muratasenel@gmail.com
#######################

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "teg-0.11.1"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "INSTALL", "README", "Changelog", "COPYING" "NEWS", "PEOPLE", "HACKING", "ABOUT-NLS")
