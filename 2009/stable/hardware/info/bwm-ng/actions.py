#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make("CC=%s" % get.CC())

def install():
    autotools.install()

    pisitools.insinto("/etc", "bwm-ng.conf-example", "bwm-ng.conf")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README", "THANKS")
