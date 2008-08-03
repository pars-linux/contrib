#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

# since upstream did not release a tarball, we made it by hand
# to get the same tarball checkout the svn revision 3197. There is a rumour
# that revision 3098 will be released as 0.7.0 but since it is not released
# and it is not tagged, we are now going for latest a.k.a. rev 3197
#
# svn co -r3197 https://svn.sourceforge.net/svnroot/hugin/hugin/trunk hugin-svn
#
# and make a source tarball with
#
# cmake .
# make package_source

def setup():
    cmaketools.configure("--enable-shared \
                          --with-unicode \
                          --with-wx-config=/usr/bin/wx-config \
                          --disable-desktop")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("AUTHORS", "BUGS", "README", "TODO")
