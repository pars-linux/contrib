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

