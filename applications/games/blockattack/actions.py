#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import scons
from pisi.actionsapi import get

def setup():
    pass

def build():
    pass

def install():
    scons.make("install blockattack destdir=%s prefix=/usr" % get.installDIR())