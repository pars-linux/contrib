#!/usr/bin/python
#-*- coding: UTF-8 -*-
#
# Uğur Çetin
# jnmbk@users.sourceforge.net

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
#from pisi.actionsapi import shelltools

def setup():
    autotools.configure()

def build():
    #TODO: --enable-gtk-doc
    #shelltools.move("docs/gal-sections.txt", "docs/gal-2.4-sections.txt")
    #shelltools.move("docs/gal-decl.txt", "docs/gal-2.4-decl.txt")
    #shelltools.touch("docs/html/book1.html")
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "MAINTAINERS", "NEWS", "README")