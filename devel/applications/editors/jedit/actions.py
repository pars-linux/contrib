#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "jEdit"

jedit_home = "/usr/share/jEdit"
build_properties = """
build.directory = .
xsltproc.executable = /usr/bin/xsltproc
docbook.catalog = /usr/share/sgml/docbook/xml-dtd-4.5/docbook.cat
docbook.xsl = /usr/share/sgml/docbook/xsl-stylesheets-1.72.0
"""

def setup():
    shelltools.echo("build.properties", build_properties)

    pisitools.dosed("package-files/linux/jedit", "@jar.filename@", "jedit.jar")

def build():
    shelltools.system("ant")

    shelltools.cd("jars/LatestVersion")
    shelltools.system("ant")

    shelltools.cd("../../jars/QuickNotepad")
    shelltools.system("ant")

    shelltools.cd("../..")
    shelltools.system("ant userdocs")

def install():
    pisitools.dobin("package-files/linux/jedit")

    files = shelltools.ls("build")
    files.remove("classes")

    for f in files:
        pisitools.insinto(jedit_home, "build/%s" % f)

    pisitools.insinto("%s/jars" % jedit_home, "jars/*.jar")

    pisitools.dosym("%s/jedit.jar" % jedit_home, "/usr/share/java/jedit.jar")

    pisitools.doman("package-files/linux/jedit.1")
