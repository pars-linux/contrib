#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import autotools


def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()