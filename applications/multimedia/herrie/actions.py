#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.rawConfigure("alsa")

def build():
    autotools.make()

def install():
    pisitools.dobin("herrie")
    pisitools.doman("herrie.1")

    locales = ['nl','tr','de','pl', 'sv', 'ga']
    for locale in locales:
        pisitools.insinto("/usr/share/locale/%s/LC_MESSAGES" % locale, "%s.mo" % locale, "herrie.mo")

    pisitools.dodoc("COPYING", "ChangeLog", "README")
    pisitools.insinto("/etc", "herrie.conf.sample")
