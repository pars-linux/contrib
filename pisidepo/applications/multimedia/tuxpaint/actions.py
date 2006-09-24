#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="tuxpaint-0.9.15b"

def setup():
    pass

def build():
    autotools.make()

def install():
    pisitools.insinto("/etc/tuxpaint", "src/tuxpaint.conf")
    pisitools.dobin("tuxpaint")
    pisitools.insinto("/usr/bin", "src/tuxpaint-import.sh", "tuxpaint-import")
    pisitools.insinto("/usr/share/tuxpaint/", "data/*")
    pisitools.insinto("/usr/share/tuxpaint/fonts/", "fonts/*")
    pisitools.insinto("/usr/share/tuxpaint/stamps/", "stamps/*")
    pisitools.insinto("/usr/share/tuxpaint/starters/", "starters/*")
    pisitools.insinto("/usr/share/applications", "src/tuxpaint.desktop")
    pisitools.insinto("/usr/share/pixmaps", "data/images/icon.png", "tuxpaint.png")
    pisitools.doman("src/manpage/*")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "docs/*")

    #Very strange error..! One of the files in captures/ doesn't support utf-8 and when the actions.py is saved, the name of the file will be changed so better to remove captures/
    pisitools.removeDir("/usr/share/doc/%s/fr/html/images/captures" % get.srcTAG())

    #icon files
    for res in ("192x192", "128x128", "96x96", "64x64", "48x48", "32x32", "22x22", "16x16"):
         pisitools.insinto("/usr/share/icons/hicolor/%s/apps/" % res, "data/images/icon%s.png" % res, "tuxpaint.png")

    pisitools.insinto("/usr/share/icons/hicolor/scalable/apps/", "data/images/tuxpaint-icon.svg", "tuxpaint.svg")

    #localedata files
    for locale_data in ("af", "ca", "de", "es_MX", "fr", "he", "id", "ka", "nb", "pt_BR", "rw", "sr", "th", "vi", "be", "cs", "el", "et", "ga", "hi", "is", "ko", "nl", "pt_PT", "sk", "sv", "tlh", "wa", "bg", "cy", "en_GB", "eu", "gl", "hr", "it", "lt", "nn", "ro", "sl", "sw", "tr", "zh_CN", "br", "da", "es", "fi", "gos", "hu", "ja", "ms", "pl", "ru", "sq", "ta", "uk", "zh_TW"):
         pisitools.insinto("/usr/share/locale/%s/LC_MESSAGES/" % locale_data, "trans/%s.mo" % locale_data, "tuxpaint.mo")


