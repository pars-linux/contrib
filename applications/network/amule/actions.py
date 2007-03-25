#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get

# for stable versions
# WorkDir = "aMule-%s" % get.srcVERSION()

# for snapshots
WorkDir = "amule-cvs"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
