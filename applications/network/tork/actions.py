#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools


def setup():
    kde.configure("--with-external-geoip \
                   --with-conf=/etc/tor/tor-tsocks.conf")

def build():
    kde.make()

def install():
    kde.install()

    # remove files conflicts
    pisitools.removeDir("/usr/kde/3.5/share/icons/crystalsvg")

    # for using tsocks add  needed programs
    pisitools.dobin("src/tsocks/torkify")

    # remove unused executable,library, configfile and man's
    pisitools.remove("/usr/kde/3.5/lib/libtorksocks.*")
    pisitools.remove("/usr/kde/3.5/local/etc/tork-tsocks.conf")
    pisitools.remove("/usr/kde/3.5/bin/torksocks")
    pisitools.removeDir("/usr/kde/3.5/man/")
