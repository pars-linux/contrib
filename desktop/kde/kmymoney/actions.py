#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde

WorkDir = "kmymoney2-0.8.6"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
