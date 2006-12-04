#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --with-logdir=/var/log/dansguardian \
                         --with-piddir=/var/run \
                         --enable-pcre \
                         --enable-fancydm \
                         --enable-clamd=yes \
                         --with-proxyuser=clamav \
                         --with-proxygroup=clamav")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/dansguardian/scripts")
