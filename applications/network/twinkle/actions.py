#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2007, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools


def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
    pisitools.dodoc("README","ChangeLog","AUTHORS","NEWS","TODO")

