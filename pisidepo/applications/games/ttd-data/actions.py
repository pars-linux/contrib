#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="Transport Tycoon Deluxe Windows"

def setup():
    pass

def build():
    pass

def install():
    shelltools.chmod("*", 0644)
    shelltools.chmod("gm/*", 0644)
    pisitools.insinto("/usr/share/openttd/data", "sample.cat")
    pisitools.insinto("/usr/share/openttd/data", "trg*")
    pisitools.insinto("/usr/share/openttd/gm", "gm/*")