#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="HTML_TreeMenu-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTML", "TreeMenu*")
    pisitools.insinto("/usr/share/php5/PEAR/HTML/images", "images/*")
    pisitools.insinto("/usr/share/php5/PEAR/HTML/imagesAlt", "imagesAlt/*")
    pisitools.insinto("/usr/share/php5/PEAR/HTML/imagesAlt2", "imagesAlt2/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/HTML_TreeMenu", "docs/*")
