#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def build():
    kde.make()

def install():
    kde.install()

    pythonmodules.fixCompiledPy("%s/share/apps/lilykde/"% get.kdeDIR())
    pisitools.remove("%s/share/apps/katepart/syntax/lilypond.xml"% get.kdeDIR())
