#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "SHERPA-MC-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-clhep \
                         --enable-hepmc2 \
                         --enable-root \
                         --enable-lhapdf \
                         --enable-gzip")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
