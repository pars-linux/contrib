#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="File_Gettext-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/File", "Gettext*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/File_Gettext", "LICENSE")
