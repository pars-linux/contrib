#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

WorkDir="LimeWire"

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/opt/limewire","*")