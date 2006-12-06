#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="trml2pdf"

def install():
    pisitools.insinto("/usr/lib/python2.4/site-packages/trml2pdf","trml2pdf/*")
    pisitools.dosym("/usr/lib/python2.4/site-packages/trml2pdf/trml2pdf.py","/usr/bin/trml2pdf")
    pisitools.insinto("/usr/share/doc/trml2pdf-%s-%s/examples" % (get.srcVERSION(),get.srcRELEASE()),"rmls/*.rml")
