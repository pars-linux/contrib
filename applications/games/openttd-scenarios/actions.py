#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir="openttd-0.4.8-RC1-scenarios"

def setup():
    pass

def build():
    pass

def install():
    pisitools.insinto("/usr/share/openttd/scenario", "*")
