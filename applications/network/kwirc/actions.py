#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools

WorkDir="kwirc-0.1.0"

def install():
	autotools.install()
    
def build():
	autotools.make()
	
def setup():
	autotools.configure() 
