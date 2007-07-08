#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir="geda-symbols-%s" % get.srcVERSION().split('_')[-1]

def setup():
    autotools.configure()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
