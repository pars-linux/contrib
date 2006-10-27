#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
    autotools.configure()

def build():
    autotools.make()


def install():
    autotools.install()
    pisitools.remove("/usr/share/xfce4/*.az")
    pisitools.remove("/usr/share/xfce4/*.ca")
    pisitools.remove("/usr/share/xfce4/*.de")
    pisitools.remove("/usr/share/xfce4/*.es")
    pisitools.remove("/usr/share/xfce4/*.eu")
    pisitools.remove("/usr/share/xfce4/*.fi")
    pisitools.remove("/usr/share/xfce4/*.fr")
    pisitools.remove("/usr/share/xfce4/*.ja")
    pisitools.remove("/usr/share/xfce4/*.lt")
    pisitools.remove("/usr/share/xfce4/*.ro")
    pisitools.remove("/usr/share/xfce4/*.ru")
    pisitools.remove("/usr/share/xfce4/*.sk")
    pisitools.remove("/usr/share/xfce4/*.vi")
    pisitools.remove("/usr/share/xfce4/*.zh_TW")
    pisitools.remove("/usr/share/xfce4/*.he")
    pisitools.remove("/usr/share/xfce4/*.it")
    pisitools.remove("/usr/share/xfce4/*.uk")
    pisitools.removeDir("/usr/share/xfce4/doc/fr")
    pisitools.removeDir("/usr/share/xfce4/doc/he")
    pisitools.domo("po/tr.po","tr","xfce-utils.mo")
    pisitools.insinto("/etc/xdg/xfce4","scripts/xinitrc")