#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir="qgis_sample_data"

def setup():
    pass

def build():
    pass

def install():
    pisitools.dodir("/usr/share/qgis/sample")
    pisitools.insinto("/usr/share/qgis/sample", "*")
