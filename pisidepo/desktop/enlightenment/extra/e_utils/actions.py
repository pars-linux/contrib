#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="e_utils-20060926"

def setup():
    autotools.configure("--with-ecore \
                         --with-ecore-exec \
                         --with-evas \
                         --with-evas-exec \
                         --with-esmart \
                         --with-esmart-exec \
                         --with-edje \
                         --with-edje-exec \
                         --with-ewl \
                         --with-ewl-exec \
                         --with-eet \
                         --with-eet-exec \
                         --with-engrave \
                         --with-engrave-exec \
                         --with-imlib2 \
                         --with-enlightenment \
                         --with-enlightenment-exec \
                         --with-epsilon \
                         --with-epsilon-exec")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING", "NEWS", "README", "TODO")