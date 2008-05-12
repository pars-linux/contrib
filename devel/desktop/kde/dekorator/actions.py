#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    theme_dir = "%s/share/apps/deKorator/themes" % get.kdeDIR()
    pisitools.dodir(theme_dir)

    for theme in shelltools.ls("themesStuff/*-theme.tar.*"):
        shelltools.system("tar -xvf '%s' -C %s%s" % (theme, get.installDIR(), theme_dir))

    pisitools.dodoc("AUTHORS", "CHANGELOG", "README", "gpl.txt")
