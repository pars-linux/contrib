#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import kde

WorkDir="soundkonverter-0.2.80"

def setup():
    kde.configure("--with-lame \
                   --with-vorbis \
                   --with-faad \
                   --with-flac \
                   --with-ffmpeg")

def build():
    kde.make()

def install():
    kde.install()