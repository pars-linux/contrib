#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir= "kfuseiso-%s" % get.srcVERSION().split('_')[-1]

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    pisitools.domo("po/tr/iso_image_plugin.po", "tr", "iso_image_plugin.mo")
    pisitools.domo("po/tr/kfile_iso_image.po", "tr", "kfile_iso_image.mo")
    pisitools.domo("po/tr/kfuseisomount.po", "tr", "kfuseisomount.mo")
    pisitools.domo("po/tr/kio_isomedia.po", "tr", "kio_isomedia.mo")
