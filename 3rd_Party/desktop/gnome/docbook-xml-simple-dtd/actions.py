#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.


from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def setup():
    pass

def build():
    pass

def install():
    pisitools.insinto("/usr/share/sgml/docbook/xml-simple-dtd-%s" % get.srcVERSION(), "*.dtd")
    pisitools.insinto("/usr/share/sgml/docbook/xml-simple-dtd-%s" % get.srcVERSION(), "*.mod")
    pisitools.insinto("/usr/share/sgml/docbook/xml-simple-dtd-%s" % get.srcVERSION(), "*.css")
#   pisitools.insinto("/usr/share/sgml/docbook/xml-simple-dtd-%s/ent" % get.srcVERSION(), "ent/*.ent")
    
#   pisitools.newdoc("ent/README", "README.ent")
#   pisitools.dodoc("README", "ChangeLog", "LostLog", "COPYRIGHT")

