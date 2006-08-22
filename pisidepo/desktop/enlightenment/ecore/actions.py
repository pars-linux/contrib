#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="ecore-0.9.9.027"

def setup():
    autotools.configure("--prefix=/usr \
                         --enable-ecore-txt \
                         --enable-ecore-x \
                         --enable-ecore-job \
                         --enable-ecore-fb \
                         --enable-ecore-dfb \
                         --enable-ecore-evas \
                         --enable-ecore-evas-gl \
                         --enable-evas-xrender \
                         --enable-evas-dfb \
                         --enable-ecore-evas-dfb \
                         --enable-ecore-evas-fb \
                         --enable-ecore-evas-buffer \
                         --enable-ecore-con \
                         --enable-openssl \
                         --enable-ecore-ipc \
                         --enable--ecore-dbus \
                         --enable-ecore-config \
                         --enable-ecore-file")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "NEWS", "README*")
    # Syntax Error Fix
    pisitools.dosed("%s/usr/lib/libecore_txt.la","dependency_libs='","dependency_libs=''")