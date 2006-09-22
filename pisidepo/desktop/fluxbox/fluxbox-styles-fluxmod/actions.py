#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pass
    ### applied in new file in pisidepo
    # comment out every rootcommand
    # find . -name '*.cfg' -exec \
    # sed -i "{}" -e 's-^\(rootcommand\)-!!! \1-i' \;
    # weird tarball...
    # find . -exec chmod a+r '{}' \;
    ###
    
def build():
    pass

def install():
    pisitools.dodir("/usr/share/fluxbox/fluxmod/styles")
    pisitools.insinto("/usr/share/fluxbox/fluxmod/styles/", "*")
