#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-ipv6 \
                         --enable-chardet \
                         --enable-esd \
                         --enable-mp3 \
                         --enable-pulse \
                         --enable-lirc \
                         --enable-coreaudio \
                         --enable-null \
                         --enable-wavpack \
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
                         --with-sidplay2=/usr \
                         --with-sidbuilders=/usr \
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

