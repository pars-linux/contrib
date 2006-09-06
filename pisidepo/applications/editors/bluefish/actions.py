#!/usr/bin/python
# -*- coding: utf-8 -*-
#Murat Şenel <> muratasenel@gmail.com <>

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()