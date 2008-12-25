#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

flags="%s \
      -msse \
      -mfpmath=sse \
      -ffast-math" % get.CXXFLAGS()

def setup():
    autotools.configure("--with-qt=/usr/qt/4 \
                         --disable-librubberband \
                         --disable-vst \
                         --enable-ladspa \
                         --enable-dssi \
                         --disable-debug")

def build():
    autotools.make('CXXFLAGS="%s" \
                    CXX="%s"' % (flags, get.CXX()))

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "TODO", "README*")
