#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir= "kfuseiso-%s" % get.srcVERSION().split('_')[-1]

def setup():
    autotools.configure()

def make():
    autotools.make()

def install():
    autotools.install()

    pisitools.domo("po/tr/iso_image_plugin.po", "tr", "iso_image_plugin.mo")
    pisitools.domo("po/tr/kfile_iso_image.po", "tr", "kfile_iso_image.mo")
    pisitools.domo("po/tr/kfuseisomount.po", "tr", "kfuseisomount.mo")
    pisitools.domo("po/tr/kio_isomedia.po", "tr", "kio_isomedia.mo")
