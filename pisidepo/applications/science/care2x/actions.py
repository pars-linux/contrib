#!/usr/bin/python
# -*- coding: utf-8 -*- 
#

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="htdocs"

def setup():
    pass

def build():
    pass

def install():
    pisitools.dodir("/var/www/localhost/htdocs/care2x")
    shelltools.move("%s/htdocs" % get.workDIR(),"%s/var/www/localhost/htdocs/care2x" % get.installDIR())