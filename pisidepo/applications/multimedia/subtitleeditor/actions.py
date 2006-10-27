#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools

WorkDir="subtitleeditor-0.11-alpha1"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
