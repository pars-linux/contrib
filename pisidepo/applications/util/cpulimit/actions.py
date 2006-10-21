#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pass

def build():
    autotools.make()

def install():
    pisitools.dobin("cpulimit")
