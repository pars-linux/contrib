#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    kde.configure("--with-lame \
                   --with-vorbis \
                   --with-faad \
                   --with-flac \
                   --with-ffmpeg \
                   --without-mp4v2")

def build():
    kde.make()

def install():
    kde.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "NEWS", "TODO")
