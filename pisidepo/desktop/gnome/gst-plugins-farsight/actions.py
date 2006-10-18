#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Eren Türkay <turkay.eren@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("/usr/bin/sed -i -e \"s:GST.*LOCK://\\0:\" ext/jpeg2000/gstj2kdec.c")
    shelltools.system("./autogen.sh")
    autotools.configure("--enable-jingle-p2p \
                                            --disable-debug \
                                            --with-plugins=rtpdemux,rtpjitterbuffer")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README")