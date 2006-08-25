#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="ecore-0.9.9.032"

def setup():
    autotools.configure("--enable-ecore-txt \
                         --enable-ecore-x \
                         --enable-ecore-job \
                         --enable-ecore-evas \
                         --enable-ecore-evas-gl \
                         --enable-ecore-evas-buffer \
                         --enable-ecore-con \
                         --enable-openssl \
                         --enable-ecore-dbus \
                         --enable-ecore-config \
                         --enable-ecore-file \
                         --enable-inotify \
                         --enable-poll \
                         --enable-curl \
                         --enable-pthreads")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "NEWS", "README*")
