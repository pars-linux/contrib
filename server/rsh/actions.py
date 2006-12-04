#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "netkit-rsh-0.17"

def setup():
    autotools.rawConfigure()

def build():
    autotools.make()

def install():
    pisitools.dobin("rcp/rcp")
    pisitools.doman("rcp/rcp.1")
    pisitools.dobin("rexec/rexec")
    pisitools.doman("rexec/rexec.1")
    pisitools.dobin("rlogin/rlogin")
    pisitools.doman("rlogin/rlogin.1")
    pisitools.doman("rlogin/rhosts.5")
    pisitools.dobin("rsh/rsh")
    pisitools.doman("rsh/rsh.1")

    pisitools.dosbin("rexecd/rexecd")
    pisitools.domove("/usr/sbin/rexecd", "/usr/sbin", "in.rexecd")
    pisitools.doman("rexecd/rexecd.8")
    pisitools.dosym("/usr/share/man/man8/rexecd.8.gz", "/usr/share/man/man8/in.rexecd.8.gz")
    pisitools.dosbin("rlogind/rlogind")
    pisitools.domove("/usr/sbin/rlogind", "/usr/sbin", "in.rlogind")
    pisitools.doman("rlogind/rlogind.8")
    pisitools.dosym("/usr/share/man/man8/rlogind.8.gz", "/usr/share/man/man8/in.rlogind.8.gz")
    pisitools.dosbin("rshd/rshd")
    pisitools.domove("/usr/sbin/rshd", "/usr/sbin", "in.rshd")
    pisitools.doman("rshd/rshd.8")
    pisitools.dosym("/usr/share/man/man8/rshd.8.gz", "/usr/share/man/man8/in.rshd.8.gz")
    pisitools.dodoc("BUGS", "ChangeLog", "README")
