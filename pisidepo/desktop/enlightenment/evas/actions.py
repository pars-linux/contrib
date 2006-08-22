#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="evas-0.9.9.027"

def setup():
    autotools.configure("--prefix=/usr \
                         --enable-x \
                         --enable-directfb \
                         --enable-software-x11 \
                         --enable-software-xcb \
                         --enable-software-qtopia \
                         --enable-fbcon-fb \
                         --enable-buffer \
                         --enable-opengl \
                         --enable-xrender \
                         --enable-png-image-loader-png \
                         --enable-image-loader-gif \
                         --enable-jpeg-image-loader-jpeg \
                         --enable-image-loader-eet \
                         --enable-font-loader-eet \
                         --enable-image-loader-edb \
                         --enable-image-loader-tiff \
                         --enable-cpu-mmx \
                         --enable-cpu-sse \
                         --enable-altivec-cpu-altivec \
                         --with-enable-cairo \
                         --enable-cpu-c \
                         --enable-scale-sample \
                         --enable-scale-smooth \
                         --enable-convert-yuv \
                         --enable-small-dither-mask \
                         --enable-convert-8-rgb-332 \
                         --enable-convert-8-rgb-666 \
                         --enable-convert-8-rgb-232 \
                         --enable-convert-8-rgb-222 \
                         --enable-convert-8-rgb-221 \
                         --enable-convert-8-rgb-121 \
                         --enable-convert-8-rgb-111 \
                         --enable-convert-16-rgb-565 \
                         --enable-convert-16-rgb-555 \
                         --enable-convert-16-rgb-444 \
                         --enable-convert-16-rgb-rot-0 \
                         --enable-convert-16-rgb-rot-270 \
                         --enable-convert-16-rgb-rot-90 \
                         --enable-convert-24-rgb-888 \
                         --enable-convert-24-bgr-888 \
                         --enable-convert-32-rgb-8888 \
                         --enable-convert-32-rgbx-8888 \
                         --enable-convert-32-bgr-8888 \
                         --enable-convert-32-bgrx-8888 \
                         --enable-convert-32-rgb-rot-0 \
                         --enable-convert-32-rgb-rot-270 \
                         --enable-convert-32-rgb-rot-90")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "README*")

