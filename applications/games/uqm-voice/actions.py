#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/uqm/content/packages", "uqm-%s-voice.uqm" % get.srcVERSION())

