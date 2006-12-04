#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "firebird-1.5.3.4870"

def setup():
    shelltools.export("NOCONFIGURE", "1")
    # Configure Super server
    # FIXME: Add support for embedded db?
    # FIXME: Add editline
    shelltools.system("./autogen.sh --prefix=/opt/firebird --enable-superserver --without-editline")
    autotools.configure("--prefix=/opt/firebird --enable-superserver --without-editline")

def build():
    autotools.make()
    # Build installable tar file
    shelltools.cd("gen")
    autotools.make("-f Makefile.install tarfile")

def install():
    # Create install directory
    shelltools.makedirs(get.installDIR())
    # Extract tar file    
    shelltools.system("tar zxpf gen/FirebirdSS-*/buildroot.tar.gz -C %s" % get.installDIR())

    # Fix libib_util.so's symlink
    pisitools.remove("/usr/lib/libib_util.so")
    pisitools.dosym("/opt/firebird/lib/libib_util.so", "/usr/lib/libib_util.so")

    # Add support for old client's
    pisitools.dosym("/usr/lib/libfbclient.so", "/usr/lib/libgds.so")
    pisitools.dosym("/usr/lib/libfbclient.so", "/usr/lib/libgds.so.0")
    pisitools.dosym("/opt/firebird/lib/libfbclient.so", "/opt/firebird/lib/libgds.so")
    pisitools.dosym("/opt/firebird/lib/libfbclient.so", "/opt/firebird/lib/libgds.so.0")

    # Create log file's symlink
    pisitools.dodir("/var/log/")
    shelltools.touch("%s/var/log/firebird.log" % get.installDIR())
    pisitools.dosym("/var/log/firebird.log", "/opt/firebird/firebird.log")

    # Make all files readonly.
    shelltools.system("chmod a-w -R %s/opt/firebird/" % get.installDIR())

    # For your security.fdb's security :)
    shelltools.chmod("%s/opt/firebird/security.fdb" % get.installDIR(), 0600)
