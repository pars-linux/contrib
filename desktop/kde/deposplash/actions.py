#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir = "deposplash"

def install():
    pisitools.insinto("/usr/kde/3.5/share/apps/ksplash/Themes/deposplash",  "*")
