#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="evas-0.9.9.035"

def setup():
    autotools.configure("--enable-fontconfig \
                         --enable-software-x11 \
                         --enable-software-xcb \
                         --enable-directfb \
                         --enable-fb \
                         --enable-buffer \
                         --enable-software-qtopia \
                         --enable-gl-x11 \
                         --enable-xrender-x11 \
                         --enable-xrender-xcb \
                         --enable-image-loader-gif \
                         --enable-image-loader-png \
                         --enable-image-loader-jpeg \
                         --enable-image-loader-eet \
                         --enable-font-loader-eet \
                         --enable-image-loader-edb \
                         --enable-image-loader-tiff \
                         --enable-image-loader-xpm \
                         --enable-image-loader-svg \
                         --enable-cpu-mmx \
                         --enable-cpu-sse \
                         --enable-cpu-altivec \
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
                         --enable-convert-16-rgb-ipq \
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
                         --enable-convert-32-rgb-rot-90 \
                         --with-x \
                         --with-eet-config=/usr/bin/eet-config \
                         --with-edb-config=/usr/bin/edb-config")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "README*")

