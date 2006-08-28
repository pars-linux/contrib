#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-aka-test \
                         --with-madwifi-path=/usr/include/madwifi/include/")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("README", "CHANGELOG", "COPYING", "AUTHORS", "etc/*.conf")