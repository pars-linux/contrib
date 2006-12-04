#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import get


def setup():
    kde.configure("--with-showimgdb --enable-libexif --enable-libkipi --with-postgres")

def build():
    kde.make()


def install():
    kde.install()