#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="HTML_TreeMenu-1.2.0"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTML", "TreeMenu*")
    pisitools.insinto("/usr/share/php5/PEAR/HTML/images", "images/*")
    pisitools.insinto("/usr/share/php5/PEAR/HTML/imagesAlt", "imagesAlt/*")
    pisitools.insinto("/usr/share/php5/PEAR/HTML/imagesAlt2", "imagesAlt2/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/HTML_TreeMenu", "docs/*")