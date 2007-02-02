#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pass

def build():
    pass

def install():
    pisitools.insinto("/usr/share/sgml/docbook/xsl-stylesheets-1.72.0", "*")
    pisitools.dodoc("AUTHORS", "BUGS", "COPYING", "NEWS", "README", "RELEASE-NOTES.txt", "TODO", "VERSION")
    pisitools.dohtml("doc")