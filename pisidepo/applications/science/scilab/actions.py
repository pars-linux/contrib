#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=%s/usr \
                         --with-local-xaw \
                         --with-pvm \
                         --with-tk \
                         --with-addedf2c \
                         --with-ocaml \
                         --with-java \
                         --with-atlas-library=/usr/lib \
                         --with-x" % get.installDIR())

def build():
    autotools.make("all")

def install():
    pisitools.dodir("/usr/share/pixmaps")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.copy("%s/usr/share/scilab-4.0/X11_defaults/scilab.xpm" % get.installDIR(), "%s/usr/share/pixmaps/" % get.installDIR())
    pisitools.insinto("/usr/share/applications", "scilab.desktop")
    shelltools.copytree("examples/", "%s/usr/share/scilab-4.0/examples" % get.installDIR())

    for files in ("Blpr", "BEpsf", "Blatexpr2", "Blatexprs", "Blatexpr", "scilab"):
        pisitools.dosed("%s/usr/share/scilab-4.0/bin/%s" % (get.installDIR(), files),"/var/tmp/pisi/scilab-4.0-1/work/scilab-4.0","/usr/share/scilab-4.0")

    for h in ("eng", "fr"):
        pisitools.dosed("%s/usr/share/scilab-4.0/man/%s/*.h*" % (get.installDIR(), h),"/var/tmp/pisi/scilab-4.0-1/work/scilab-4.0","/usr/share/scilab-4.0")

    for docs in ("Blatdoc", "Blatdocs"):
        pisitools.dosed("%s/usr/share/scilab-4.0/util/%s" % (get.installDIR(), docs),"/var/tmp/pisi/scilab-4.0-1/work/scilab-4.0","/usr/share/scilab-4.0")

    pisitools.dodoc("ACKNOWLEDGEMENTS", "CHANGES", "README_Unix", "RELEASE_NOTES")


