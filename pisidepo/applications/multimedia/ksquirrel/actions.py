#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import kde

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()