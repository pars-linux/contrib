#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# by Serkan Avci <killer@wolke7.net>

from pisi.actionsapi import pisitools

WorkDir = "fmodapi375linux"

def install():
    pisitools.insinto("/usr/include", "api/inc/*")
    pisitools.insinto("/usr/lib", "api/libfmod-3.75.so")
    pisitools.insinto("/usr/share/doc/fmod-3.75-1", "documentation/*")