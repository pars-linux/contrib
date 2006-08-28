#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "gnome-python-2.15.91"

def setup():
    autotools.configure("--prefix=/usr --disable-glibtest --disable-gtktest")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")


