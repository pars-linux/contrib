#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import scons

WorkDir="linden"

def build():
    shelltools.cd("indra")

    shelltools.export("TEMP_BUILD_DIR", "build")

    scons.make("DISTCC=no \
                BTARGET=client \
                BUILD=release \
                MOZLIB=no \
                GRID=firstlook \
                FMOD=yes \
                ELFIO=no \
                STANDALONE=yes")

def install():
    for data in ["secondlife-i686-bin-globalsyms", "featuretable.txt", "gpu_table.txt", "app_settings", "skins", "fonts", "character", "help", "res-sdl"]:
        pisitools.insinto("/usr/share/secondlife", "indra/newview/%s" % data)

    pisitools.insinto("/usr/share/secondlife/app_settings", "scripts/messages/message_template.msg")
    pisitools.insinto("/usr/share/secondlife", "indra/newview/linux_tools/launch_url.sh")

    pisitools.dosym("/usr/share/fonts/dejavu/DejaVuSerif.ttf", "/usr/share/secondlife/unicode.ttf")

    pisitools.dohtml("indra/newview/lsl_guide.html")
    pisitools.dodoc("indra/newview/releasenotes.txt", "indra/newview/licenses-linux.txt")
