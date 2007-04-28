#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir="3gpconverter-0.4"

def install():
    pisitools.insinto("/usr/kde/3.5/bin", "3gpconverter-0.4.kmdr","3gpconverter.kmdr")
