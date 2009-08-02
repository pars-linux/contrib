#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "gdm-pardus-theme"

def install():
    pisitools.insinto("/usr/share/gdm/themes", "pardus-air/")

    pisitools.dodoc("ChangeLog", "COPYING", "README")
