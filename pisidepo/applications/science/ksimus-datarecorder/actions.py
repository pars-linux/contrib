#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "ksimus-datarecorder-0.3.6"

def setup():
    kde.configure()

def build():
    kde.make()


def install():
    kde.install()