#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "kvirc-3.4.2"

def setup():
    kde.configure("--with-aa-fonts \
                   --with-big-channels \
                   --with-pizza \
                   --with-ix86-asm \
                   --with-optimisation=-o2 \
                   --mandir=/%s" % get.manDIR())

def build():
    kde.make("kvirc -j1")

def install():
    kde.install()

    pisitools.remove("%s/share/services/irc.protocol"% get.kdeDIR())
