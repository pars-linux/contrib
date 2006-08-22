#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import kde
from pisi.actionsapi import get


def setup():
    kde.configure("--with-showimgdb --enable-libexif --enable-libkipi --with-postgres")

def build():
    kde.make()


def install():
    kde.install()