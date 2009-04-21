#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "aMule-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-amulecmd \
                         --enable-webserver \
                         --enable-amule-daemon \
                         --with-wx-prefix=/usr/wx/2.8 \
                         --with-wx-config=/usr/wx/2.8/bin/wx-config")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
