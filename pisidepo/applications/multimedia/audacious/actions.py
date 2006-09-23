#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="audacious-1.2.0-rc1"

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
                         --enable-amidiplug \
                         --enable-timidity \
                         --with-dev-dsp=/dev/sound/dsp \
                         --with-dev-mixer=/dev/sound/mixer")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ABOUT-NLS", "ChangeLog", "COPYING", "AUTHORS", "INSTALL", "NEWS", "README")

