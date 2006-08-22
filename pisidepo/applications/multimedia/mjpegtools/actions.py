#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# turkay.eren@gmail.com
#######################

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-x \
                        --disable-xfree-ext \
                        --with-quicktime \
                        --with-v4l \
                        --without-gtk \
                        --with-sdl \
                        --with-dv=/usr \
                        --enable-largefile \
                        --with-dv-yv12 \
                        --enable-simd-accel \
                        --with-jpeg-mmx=/usr/include/jpeg-mmx \
                        --enable-cmov-extension")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("mjpeg_howto.txt", "README", \
                    "PLANS", "NEWS", "README.AltiVec", \
                    "README.avilib", "README.DV", "README.glav", \
                    "README.lavpipe", "README.transist", "TODO", \
                    "HINTS", "BUGS", "ChangeLog", "AUTHORS", "CHANGES")