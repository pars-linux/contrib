#!/usr/bin/python
# -*- coding: utf-8 -*-·
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir="."
datadir = "/usr/share/%s" % get.srcNAME()

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    #delete GNUmakefile as it's not necessary anymore and messing things up if it's there
    shelltools.unlink("%s/GNUmakefile" % get.workDIR())

    #convert the DOS line endings of data files to unix type
    shelltools.system("dos2unix %s/TestVectors/*" % get.workDIR())
    shelltools.system("dos2unix %s/*.dat" % get.workDIR())

    #create the configure script and configure to create only dynamic library
    for f in ["NEWS", "README", "AUTHORS", "ChangeLog"]:
        shelltools.touch(f)

    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def check():
    shelltools.system("./cryptestcwd v")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #GNU/Linux distributions prefer crypto++ instead of cryptopp, so we do the same by renaming and moving
    #rename and symlink for the .la file
    pisitools.dosym("libcrypto++.la", "/usr/lib/libcryptopp.la")

    #rename and symlink for the .so file
    for file in ["libcryptopp.so", "libcryptopp.so.6", "libcryptopp.so.6.0.0"]:
        pisitools.dosym("libcrypto++.so.6.0.0", "/usr/lib/%s" % file)

    #rename the include and data directories
    pisitools.rename("/usr/include/cryptopp", "crypto++")
    pisitools.rename("/usr/share/cryptopp", "crypto++")

    #We include the TestVectors directory in package as examples for future coders
    pisitools.insinto(datadir, "TestVectors")

    #fix directory and file permissions so that they are readable by users
    fixperms("%s/%s" % (get.installDIR(),datadir))

    pisitools.remove("/usr/bin/cryptestcwd")

    pisitools.dodoc("Readme*", "License*")
