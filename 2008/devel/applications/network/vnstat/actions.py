#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('CC="%s" CFLAGS="%s"' % (get.CC(), get.CFLAGS()))

def install():
    pisitools.dobin("src/vnstat")
    pisitools.insinto("/etc", "cfg/vnstat.conf")
    pisitools.dodir("/var/lib/vnstat")

    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "cron/vnstat", "vnstat.cron")
    pisitools.doman("man/*")
    pisitools.dodoc("CHANGES", "COPYING", "README", "FAQ")
