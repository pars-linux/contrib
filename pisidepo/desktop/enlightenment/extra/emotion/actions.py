#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="emotion-20060926"

def setup():
    autotools.configure("--with-eet \
                        --with-eet-exec \
                        --with-evas \
                        --with-evas-exec \
                        --with-edje \
                        --with-edje-exec \
                        --with-ecore \
                        --with-ecore-exec \
                        --with-embryo \
                        --with-embryo-exec \
                        --enable-xine \
                        --enable-gstreamer \
                        --with-xine-exec")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "NEWS", "README", "TODO")