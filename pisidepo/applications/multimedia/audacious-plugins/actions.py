#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="audacious-plugins-1.2.2"

def setup():
    autotools.configure("--enable-ipv6 \
                         --enable-chardet \
                         --enable-gconf \
                         --enable-gnome-vfs \
                         --enable-esd \
                         --enable-mp3 \
                         --enable-lirc \
                         --enable-adplug \
                         --enable-vorbis \
                         --enable-aac \
                         --enable-notify \
                         --enable-sndfile \
                         --enable-modplug \
                         --enable-flac \
                         --enable-wma \
                         --enable-oss \
                         --enable-jack \
                         --enable-arts \
                         --enable-sid \
                         --enable-musepack \
                         --enable-alsa \
                         --enable-paranormal \
                         --enable-amidiplug \
                         --enable-amidiplug-alsa \
                         --enable-amidiplug-flysn \
                         --enable-amidiplug-dummy \
                         --enable-timidity \
                         --enable-xspf \
                         --disable-xmltest")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ChangeLog", "COPYING", "AUTHORS", "INSTALL", "NEWS")

