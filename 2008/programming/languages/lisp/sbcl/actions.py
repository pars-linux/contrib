#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

# we have patch number in package version but not in source package version
# so WorkDir does not include any patch number.
WorkDir = "sbcl-%s-pardus/" % ".".join(get.srcVERSION().split(".")[:3])

def setup():
    # correct doc directory : /usr/share/doc/sbcl-{srcVERSION}
    pisitools.dosed("install.sh", '/share/doc/sbcl}', '/share/doc/sbcl-%s}' % get.srcVERSION())

    # personalize lisp-implementation-version for pardus
    pisitools.dosed("version.lisp-expr", '^"(.*)"$', '\\1.pardus.%s' % get.srcRELEASE())

def build():
    host_compiler = "%s/sbcl-binary/sbcl --core %s/sbcl-binary/sbcl.core \
                                         --noinform \
                                         --end-runtime-options \
                                         --disable-debugger \
                                         --no-sysinit \
                                         --no-userinit" % (get.curDIR(), get.curDIR())
    shelltools.system("sh make.sh '%s'" % host_compiler)
    shelltools.system("cd doc/manual && make html")

def install():
    shelltools.system("SBCL_HOME=\"\" INSTALL_ROOT=%s/usr sh install.sh" % get.installDIR())

