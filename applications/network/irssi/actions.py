#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="irssi-0.8.10"

def setup():
    autotools.configure("--enable-ipv6")

def build():
    autotools.make()

def install():
    autotools.install()
    #fix conflict with pilot-link
    pisitools.remove("/usr/lib/perl5/5.8.8/i686-linux/perllocal.pod")