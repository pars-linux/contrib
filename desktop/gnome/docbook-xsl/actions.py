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
    for i in ['common', 'eclipse', 'fo', 'html', 'htmlhelp', \
              'images', 'javahelp', 'lib', 'manpages', 'params', \
              'profiling', 'slides', 'template', 'website', 'xhtml']:
        pisitools.insinto('/usr/share/sgml/docbook/xsl-stylesheets-1.70.1', i)

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README", "RELEASE-NOTES.txt", "TODO", "VERSION")
    pisitools.dohtml("doc")
