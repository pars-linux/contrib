#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.rawConfigure()

def build():
    autotools.make()

def install():
    pisitools.dobin("herrie")
    pisitools.domo("lang/nl.po", "nl", "herrie.mo")
    pisitools.domo("lang/tr.po", "tr", "herrie.mo")

    pisitools.doman("herrie.1")
    pisitools.dodoc("COPYING", "ChangeLog", "README")
