#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

WorkDir = "ExtUtils-PkgConfig-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()
