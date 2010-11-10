#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008- 2010  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "cinelerra-cv"

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")  

#   fails due to ‘UINT64_C’ was not declared in this scope - ffmpeg svn related  
    shelltools.export("CXXFLAGS", "%s -D__STDC_CONSTANT_MACROS" % get.CXXFLAGS())

    autotools.autoreconf("-fiv")
    autotools.configure("--enable-mmx \
                         --enable-alsa \
                         --with-external-ffmpeg \
                         --disable-opengl \
                         --enable-esd \
                         --disable-rpath \
                         --disable-static \
                         --with-buildinfo=cust/GIT\ Pardus\ build")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/include")

    pisitools.rename("/usr/bin/mpeg3cat", "mpeg3cat.hv")
    pisitools.rename("/usr/bin/mpeg3dump", "mpeg3dump.hv")
    pisitools.rename("/usr/bin/mpeg3toc", "mpeg3toc.hv")
    
    pisitools.dosym("/usr/bin/mpeg2enc", "/usr/lib/cinelerra/mpeg2enc") 

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "LICENSE", "NEWS", "TODO")
