#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # gcc doesn't like mcpu flag while bootstrapping itself
    shelltools.export("CFLAGS", "-march=i686 -O2 -pipe -fomit-frame-pointer -U_FORTIFY_SOURCE")
    shelltools.export("CXXFLAGS", "-march=i686 -O2 -pipe -fomit-frame-pointer -U_FORTIFY_SOURCE")

    conf ="--prefix=/usr/lib/gcc-snapshot \
           --disable-libgcj \
           --disable-libssp \
           --disable-nls \
           --disable-werror \
           --disable-checking \
           --enable-clocale=gnu \
           --enable-__cxa_atexit \
           --enable-languages=c,c++,fortran,objc,obj-c++,treelang \
           --enable-libstdcxx-allocator=new \
           --enable-shared \
           --enable-ssp \
           --enable-threads=posix \
           --enable-version-specific-runtime-libs \
           --without-included-gettext \
           --without-system-libunwind \
           --with-system-zlib"

    shelltools.makedirs("build")
    shelltools.cd("build")

    shelltools.system("../configure %s" % conf)

def build():
    # gcc doesn't like mcpu flag while bootstrapping itself
    shelltools.export("CFLAGS", "-march=i686 -ftree-vectorize -O2 -pipe -fomit-frame-pointer -U_FORTIFY_SOURCE")
    shelltools.export("CXXFLAGS", "-march=i686 -ftree-vectorize -O2 -pipe -fomit-frame-pointer -U_FORTIFY_SOURCE")

    shelltools.cd("build")
    autotools.make('LDFLAGS="%s" BOOT_CFLAGS="%s" profiledbootstrap' % (get.LDFLAGS(), get.CFLAGS()))

def install():
    shelltools.cd("build")

    # Do not allow symlinks in include as this can break the build.
    for file in shelltools.ls("gcc/include/*"):
        if shelltools.isLink(file):
            shelltools.unlink(file)

    # Remove generated headers, as they can cause things to break
    for file in shelltools.ls("gcc/include/*"):
        if shelltools.isFile(file):
            if not shelltools.system("grep -q \"auto-edited\" %s" % file):
                shelltools.unlink(file)
        elif shelltools.isDirectory(file):
            shelltools.unlinkDir(file)

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # This one comes with gdb
    pisitools.remove("/usr/share/gcc-snapshot/lib/libiberty.a")

    # cc symlink
    pisitools.dosym("/usr/lib/gcc-snapshot/bin/gcc","/usr/lib/gcc-snapshot/bin/cc")
