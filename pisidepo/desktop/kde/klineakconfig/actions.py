#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

WorkDir="klineakconfig-0.8-beta2"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
    pisitools.domo("po/tr.po", "tr", "klineakconfig.mo")
    pisitools.dodir("/usr/kde/3.5/share/locale/tr/LC_MESSAGES")
    pisitools.domove("/usr/share/locale/tr/LC_MESSAGES/klineakconfig.mo", "/usr/kde/3.5/share/locale/tr/LC_MESSAGES")