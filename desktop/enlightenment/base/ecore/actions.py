#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="ecore-0.9.9.036"

def setup():
    autotools.configure("--enable-ecore-txt \
                         --enable-ecore-x \
                         --enable-ecore-job \
                         --enable-ecore-dfb \
                         --enable-ecore-fb \
                         --enable-ecore-evas \
                         --enable-ecore-evas-gl \
                         --enable-ecore-evas-buffer \
                         --enable-ecore-evas-xrender \
                         --enable-ecore-evas-dfb \
                         --enable-ecore-evas-fb \
                         --enable-ecore-con \
                         --enable-openssl \
                         --enable-ecore-ipc \
                         --enable-ecore-dbus \
                         --enable-ecore-config \
                         --enable-ecore-file \
                         --enable-inotify \
                         --enable-poll \
                         --enable-ecore-desktop \
                         --enable-curl \
                         --enable-pthreads \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "NEWS", "README*")
