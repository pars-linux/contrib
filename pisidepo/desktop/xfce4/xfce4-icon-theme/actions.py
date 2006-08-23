#!/usr/bin/python
#
#Ertugrul Erata ertugrulerata at gmail.com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import get


def setup():
    autotools.configure("--with-sound=alsa")

def build():
    autotools.make()


def install():
    autotools.install()