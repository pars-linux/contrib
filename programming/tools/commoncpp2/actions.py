#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2007, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
    autotools.configure("--with-gnutls \
                         --with-openssl \
                         --enable-debug \
                         --with-ipv6")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS","NEWS","ChangeLog","README","THANKS","TODO","COPYING")

