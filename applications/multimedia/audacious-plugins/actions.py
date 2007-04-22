#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-nls \
                         --enable-rpath \
                         --enable-ipv6 \
                         --enable-chardet \
                         --disable-gconf \
                         --enable-esd \
                         --enable-mp3 \
                         --enable-rocklight \
                         --enable-lirc \
                         --enable-evdevplug \
                         --enable-statusicon \
                         --enable-aosd \
                         --enable-adplug \
                         --enable-vorbis \
                         --enable-wavpack \
                         --enable-aac \
                         --enable-sndfile \
                         --enable-modplug \
                         --enable-flac \
                         --enable-musepack \
                         --enable-wma \
                         --enable-jack \
                         --enable-arts \
                         --enable-sid \
                         --enable-oss \
                         --enable-alsa \
                         --enable-amidiplug \
                         --enable-amidiplug-alsa \
                         --enable-amidiplug-flysn \
                         --enable-amidiplug-dummy \
                         --enable-timidity \
                         --enable-mms \
                         --enable-paranormal \
                         --enable-xspf \
                         --disable-xmltest \
                         --enable-projectm \
                         --enable-tta \
                         --enable-lame \
                         --with-sidplay2=/usr \
                         --with-sidbuilders=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING", "AUTHORS", "NEWS")
