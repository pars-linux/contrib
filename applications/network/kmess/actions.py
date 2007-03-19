#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

WorkDir="kmess-1.5pre2"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
    pisitools.dosym("%s/share/apps/kmess/eventsrc" % get.kdeDIR(), "%s/share/config/kmess.eventsrc" % get.kdeDIR())

