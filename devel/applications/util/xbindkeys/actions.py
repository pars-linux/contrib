#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    # there is no rpl_mallock function and gives error
    # configure script will act as if AC_FUNC_MALLOCK check has passed.
    shelltools.export("ac_cv_func_malloc_0_nonnull", "yes")

    # a flag used by guile, configure script doesn't add this veriable.
    shelltools.export("CFLAGS", "%s -pthread" % get.CFLAGS())

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS","BUGS","COPYING","ChangeLog","TODO")

