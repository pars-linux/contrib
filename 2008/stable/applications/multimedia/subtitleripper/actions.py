#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenes/gpl-2.0.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="subtitleripper"

def setup():
    pisitools.dosed("Makefile", "ppm", "netpbm")
    pisitools.dosed("Makefile", "CC = gcc", "CC = %s" % get.CC())
    pisitools.dosed("Makefile", "CFLAGS = \\$\\(COPT\\) \\$\\(WARN\\) \\$\\(DEFINES\\) \\$\\(INCLUDES\\)", "CFLAGS = %s $(DEFINES)" % get.CFLAGS())

    pisitools.dosed("pgm2txt", "~/sourceforge/subtitleripper/src/", "/usr/share/subtitleripper")

def build():
    autotools.make()

def install():
    binfiles = ["pgm2txt", "srttool", "subtitle2pgm", "subtitle2vobsub", "vobsub2pgm" ]

    for i in binfiles:
        pisitools.dobin(i)

    pisitools.insinto("/usr/share/subtitleripper", "gocrfilter_*")

    pisitools.dodoc("ChangeLog", "README*")
