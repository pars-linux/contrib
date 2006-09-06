#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import kde

def setup():
    kde.configure("--with-lame \
                   --with-vorbis \
                   --with-flac \
                   --with-ffmpeg")

def build():
    kde.make()

def install():
    kde.install()