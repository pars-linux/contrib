#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="amaroK-0.2"

def install():
    pisitools.insinto("/usr/share/amsn/plugins/amaroK", "*")