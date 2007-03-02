#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools

WorkDir="xarchiver-0.4.2rc2"

def setup():
    autotools.configure()

def build():
    autotools.make()


def install():
    autotools.install()
