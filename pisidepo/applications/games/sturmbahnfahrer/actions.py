#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Serkan Avcı <killer@wolke7.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#def setup():
#    autotools.configure()

def build():
    autotools.make()

def install():
	    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
#	    autotools.install()
