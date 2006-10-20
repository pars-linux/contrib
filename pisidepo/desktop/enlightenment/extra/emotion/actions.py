#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="emotion-0.0.1.004"

def setup():

    autotools.system("./autogen.sh --prefix=/usr \
                                   --with-eet \
                                   --with-eet-exec \
                                   --with-evas \
                                   --with-evas-exec \
                                   --with-edje \
                                   --with-edje-exec \
                                   --with-ecore \
                                   --with-ecore-exec \
                                   --with-embryo \
                                   --with-embryo-exec \
                                   --with-xine \
                                   --with-xine-exec")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "NEWS", "README", "TODO")