#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="evidence"

def setup():
    autotools.system("./autogen.sh --prefix=/usr \
                         --with-dbus \
                         --with-dcop \
                         --enable-evas \
                         --enable-epeg \
                         --enable-ecore \
                         --enable-ecore-ipc \
                         --enable-edb \
                         --enable-eet \
                         --enable-edje \
                         --enable-imlib2 \
                         --enable-libpng \
                         --enable-curl \
                         --enable-attr \
                         --enable-acls \
                         --enable-libmagic \
                         --enable-libsharedmime \
                         --enable-canvas-evas2 \
                         --enable-extra-themes \
                         --enable-extra-iconsets \
                         --disable-thumbnailer-avi \
                         --enable-thumbnailer-xine \
                         --enable-thumbnailer-mpeg3 \
                         --enable-pcre \
                         --enable-x \
                         --enable-freetype \
                         --enable-plugin-vorbis \
                         --enable-plugin-ttf \
                         --enable-debug \
                         --with-kde")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/applications", "evidence.xpm")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPING", "evidence.1", "HELP_DEVELOP", "NEWS", "README")
    shelltools.system("/usr/bin/mv %s/usr/man %s/usr/share/man" % (get.installDIR(),get.installDIR())