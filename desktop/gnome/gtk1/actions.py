#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "gtk+-1.2.10"

def setup():
    libtools.libtoolize()

    autotools.configure("--with-xinput=xfree --with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    libtools.preplib()

    # Don't use helvetica, we don't have it
    pisitools.dosed("%s/etc/gtk/*" % get.installDIR(), "helvetica", "dejavu sans mono")

    pisitools.dodoc("AUTHORS", "README", "COPYING")
