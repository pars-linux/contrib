#!/usr/bin/python
#
#Ertugrul Erata ertugrulerata at gmail.com
#

from pisi.actionsapi import autotools

WorkDir="exo-0.3.1.8beta2"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

