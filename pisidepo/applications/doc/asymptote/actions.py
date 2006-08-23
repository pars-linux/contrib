#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Ertuğrul Erata

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():

    autotools.configure()

def build():

    autotools.make()

def install():
    pisitools.dobin("asy")
    pisitools.insinto("/usr/share/asymptote/","base/*.asy")
    pisitools.insinto("/usr/share/doc/asymptote-%s-%s/examples" % (get.srcVERSION(),get.srcRELEASE()),"examples/*")
    pisitools.doman("doc/asy.1")