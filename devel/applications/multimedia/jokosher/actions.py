#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools


def install():
    pisitools.dosed("bin/jokosher.desktop", "AudioVideoEditing;GTK;Recorder", "GTK;AudioVideo;Recorder")
    pythonmodules.install()
    pisitools.removeDir("/usr/share/gnome")

    pisitools.dodoc("AUTHORS", "COPYING", "PKG-INFO", "README")
