#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "aMule-%s" % get.srcVERSION()

def setup():
    autotools.configure("--with-wx-prefix=/usr/wx/2.8 \
                         --with-wx-config=/usr/wx/2.8/bin/wx-config")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
