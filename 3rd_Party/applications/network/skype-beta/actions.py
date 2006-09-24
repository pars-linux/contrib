#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir = "skype-1.3.0.30"

def install():    
    pisitools.dodir("/opt/skype")
    pisitools.dodir("/opt/skype/sound")
    pisitools.dodir("/opt/skype/lang")
    
    pisitools.doexe("skype", "/opt/skype")
    pisitools.doexe("skype-callto-handler", "/opt/skype")
    
    pisitools.insinto("/opt/skype/sound", "sound/*.wav")
    pisitools.insinto("/opt/skype/lang", "lang/*.qm")
    pisitools.insinto("/usr/kde/3.5/share/icons/default.kde/16x16/apps", "icons/skype_16_32.png", "skype.png")
    pisitools.insinto("/usr/kde/3.5/share/icons/default.kde/32x32/apps", "icons/skype_32_32.png", "skype.png")
    pisitools.insinto("/usr/kde/3.5/share/icons/default.kde/48x48/apps", "icons/skype_48_32.png", "skype.png")
    pisitools.insinto("/usr/share/applications", "skype.desktop")
    
    pisitools.dosym("/opt/skype/skype.sh", "/usr/bin/skype")
    pisitools.dodoc("README", "LICENSE")
