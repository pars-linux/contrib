#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "mozilla"

def setup():
    shelltools.export("JAVA_HOME","/opt/sun-jdk")
    shelltools.export("MOZCONFIG","xulrunner-mozconfig")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    executable = ["xpcshell","xpidl","xpt_dump","xpt_link","xulrunner-bin","xulrunner-stub"]
    for a in executable:
        pisitools.dosym("/usr/lib/xulrunner-1.9/%s" % a,"/usr/bin/%s" % a)

    files = ["/usr/include/xulrunner-sdk-1.9/stable/nsDirectoryServiceDefs.h","/usr/include/xulrunner-sdk-1.9/stable/nsTPtrArray.h",
             "/usr/include/xulrunner-sdk-1.9/stable/nsVersionComparator.h","/usr/include/nsDirectoryServiceDefs.h",
             "/usr/lib/xulrunner-1.9/LICENSE","/usr/include/nsTPtrArray.h","/usr/include/nsTPtrArray.h","/usr/include/nsVersionComparator",
             "/usr/lib/xulrunner-1.9/icons/mozicon50.xpm","/usr/lib/xulrunner-1.9/icons/mozicon16.xpm",
             "/usr/lib/xulrunner-1.9/icons/document.png","/usr/lib/xulrunner-1.9/README.txt",
             "/usr/lib/xulrunner-1.9/chrome/icons/default/default48.png","/usr/lib/xulrunner-1.9/chrome/icons/default/default16.png"
             "/usr/lib/xulrunner-1.9/chrome/icons/default/default32.png","/etc/gre.d/1.9.0.1.system.conf"]

    for a in files:
        shelltools.chmod("%s/%s" % (get.installDIR(),a),0644)
