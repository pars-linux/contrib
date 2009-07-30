#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "stardict-essential-turkish-0.2"

def install():
    pisitools.insinto("/usr/share/stardict/dic", "*")
