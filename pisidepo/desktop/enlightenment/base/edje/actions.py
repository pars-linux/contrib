#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir="edje-0.5.0.032"

def setup():
    autotools.configure("--enable-edje-cc \
                         --with-eet \
                         --with-eet-exec \
                         --with-evas \
                         --with-evas-exec \
                         --with-ecore \
                         --with-ecore-exec \
                         --with-embryo \
                         --with-embryo-exec \
                         --with-vim")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "NEWS", "README")