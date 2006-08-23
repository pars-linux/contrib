#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Eren Türkay <turkay.eren@gmail.com>

from pisi.actionsapi import pisitools

def setup():
    pass

def build():
    pass

def install():
    pisitools.dobin("bin/apacheconv")
    pisitools.dobin("bin/generate.cgi")
    pisitools.dobin("bin/squid-graph")
    pisitools.dobin("bin/timeconv")
    pisitools.insinto("/usr/share/squid-graph-3.1","images/logo.png")

    pisitools.dodoc("docs/CHANGELOG", "docs/README")
    pisitools.dohtml("docs/html/*")