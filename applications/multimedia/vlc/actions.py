#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

NoStrip = "/"

def setup():
    autotools.configure("--enable-x11 \
                         --enable-xvideo \
                         --disable-gtk \
                         --enable-sdl \
                         --enable-ffmpeg \
                         --with-ffmpeg-mp3lame \
                         --enable-mad \
                         --enable-libdvbpsi \
                         --enable-a52 \
                         --enable-dts \
                         --enable-libmpeg2 \
                         --enable-dvdnav \
                         --enable-faad \
                         --enable-vorbis \
                         --enable-ogg \
                         --enable-theora \
                         --enable-faac \
                         --enable-mkv \
                         --enable-freetype \
                         --enable-fribidi \
                         --enable-speex \
                         --enable-flac \
                         --enable-livedotcom \
                         --with-livedotcom=/usr/lib/libliveMedia.a \
                         --enable-caca \
                         --enable-skins \
                         --enable-skins2 \
                         --enable-alsa \
                         --disable-kde \
                         --disable-qt \
                         --enable-wxwindows \
                         --enable-ncurses \
                         --enable-release \
                         --enable-debug")
    libtools.libtoolize("--copy --force")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #icons vlc128x128.png  vlc16x16.png  vlc32x32.png  vlc48x48.png
    for res in ("128x128", "64x64", "48x48", "32x32", "16x16"):
         pisitools.insinto("/usr/share/icons/hicolor/%s/apps/" % res, "share/vlc%s.png" % res, "vlc.png")

    pisitools.removeDir("/usr/share/doc/vlc")

    pisitools.insinto("/usr/share/applications/", "debian/vlc.desktop")

    #Firefox plugins compile clean up --enable-mozilla=firefox --with-mozilla-sdk-path=/usr/lib/MozillaFirefox
    pisitools.removeDir("/usr/lib/mozilla") 

    pisitools.dodoc("doc/*", "AUTHORS", "ABOUT-NLS", "ChangeLog", "COPYING", "INSTALL", "MAINTAINERS", "README.MacOSX.rtf",  "NEWS", "HACKING", "THANKS", "README")