#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="HTML_AJAX-0.5.0"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTML","AJAX.php")
    items = ['AJAX', 'js']
    for item in items:
        pisitools.insinto("/usr/share/php5/PEAR/HTML/%s" % item, "%s/*" % item)
    pisitools.insinto("/usr/share/php5/PEAR/doc/HTML_AJAX", "docs/*"
    pisitools.insinto("/usr/share/php5/PEAR/doc/HTML_AJAX/examples", "examples/*")