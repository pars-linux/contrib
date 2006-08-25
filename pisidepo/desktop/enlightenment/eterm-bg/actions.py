#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import pisitools

WorkDir="bg"

def setup():
    pass

def build():
    pass

def install():
    pisitools.insinto("/usr/share/Eterm/pix/scale", "scale/*")
    pisitools.insinto("/usr/share/Eterm/pix/tile", "tile/*")

   #remove the files to avoid the file conflicts
    pisitools.remove("/usr/share/Eterm/pix/scale/Neopolis-horizon.jpg")
    pisitools.remove("/usr/share/Eterm/pix/tile/circuit.jpg")
    pisitools.dodoc("README.backgrounds")

