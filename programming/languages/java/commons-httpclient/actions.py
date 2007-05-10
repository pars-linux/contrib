#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="commons-httpclient-%s" % get.srcVERSION()

def setup():
    shelltools.makedirs("lib") # ant script looks for this dir
    shelltools.copy("build.properties.sample", "build.properties")
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant dist")

def install():
    pisitools.insinto("/usr/lib/java","dist/commons-httpclient.jar","commons-httpclient.jar")
    #TODO: docs

    pisitools.dodoc("LICENSE")
    pisitools.dodoc("README")
    pisitools.dodoc("RELEASE_NOTES")
