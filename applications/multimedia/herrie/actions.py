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
    pisitools.doman("herrie.1")
    
    locales = ['nl','tr','de','pl']
    for locale in locales:
        pisitools.insinto("/usr/share/locale/%s/LC_MESSAGES" % locale, "%s.mo" % locale, "herrie.mo")

    pisitools.dodoc("COPYING", "ChangeLog", "README")
