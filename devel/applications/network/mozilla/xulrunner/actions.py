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
    pisitools.remove("/usr/lib/xulrunner-1.9/plugins/*")

    executable = ["xpcshell","xpidl","xpt_dump","xpt_link","xulrunner-bin",\
                  "xulrunner-stub","mozilla-xremote-client"]

    for a in executable:
        pisitools.dosym("/usr/lib/xulrunner-1.9/%s" % a,"/usr/bin/%s" % a)

    files = ["/usr/share/idl/xulrunner-sdk-1.9/unstable/*","/usr/share/idl/xulrunner-sdk-1.9/stable/*",\
             "/usr/lib/xulrunner-sdk-1.9/sdk/lib/*","/usr/lib/xulrunner-1.9/*.so","/usr/lib/xulrunner-1.9/icons/*",\
             "/usr/lib/xulrunner-1.9/components/*","/usr/lib/xulrunner-1.9/README.txt","/usr/lib/xulrunner-1.9/LICENSE",\
             "/usr/lib/xulrunner-1.9/res/html/folder.png","/usr/lib/xulrunner-1.9/chrome/icons/default/*.png",\
             "/usr/include/xulrunner-sdk-1.9/stable/*","/etc/gre.d/1.9.0.6.system.conf"]

    for a in files:
        shelltools.chmod("%s%s" % (get.installDIR(),a),0644)
