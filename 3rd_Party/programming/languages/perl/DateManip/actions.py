#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules

def setup():
    perlmodules.configure("/usr")

def build():
    perlmodules.make()

def install():
    perlmodules.install()
