#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.rawConfigure("alsa")

def build():
    autotools.make()

def install():
    # move herrie to herrie-bin for wrapper script
    pisitools.insinto("/usr/bin", "herrie", "herrie-bin")

    pisitools.doman("herrie.1")

    locales = ['ca', 'da', 'de', 'es', 'fi', 'ga', 'nl', 'pl', 'ru', 'sv', 'tr', 'vi']
    for locale in locales:
        pisitools.insinto("/usr/share/locale/%s/LC_MESSAGES" % locale, "%s.mo" % locale, "herrie.mo")

    pisitools.insinto("/etc", "herrie.conf.sample")
    pisitools.dodoc("COPYING", "ChangeLog", "README")
