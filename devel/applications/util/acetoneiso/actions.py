#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

WorkDir= "AcetoneISO-6.7"

def build():
    scons.make()

def install():
    scons.install("%s/opt/acetoneiso/bin" % get.installDIR())
    fileList= [('AcetoneISO-6.7/acetone.png', '/usr/share/pixmaps/'),
               ('AcetoneISO-6.7/aiso.png', '/usr/share/pixmaps/'),
               ('AcetoneISO-6.7/playiso-unmount.sh', '/opt/acetoneiso'),
               ('AcetoneISO-6.7/turbo.sh', '/opt/acetoneiso'),
               ('AcetoneISO-6.7/acetoneiso-mount.desktop', '/usr/kde/3.5/share/apps/konqueror/servicemenus'),
               ('AcetoneISO-6.7/acetoneiso-umount.desktop', '/usr/kde/3.5/share/apps/konqueror/servicemenus'),
               ('AcetoneISO-6.7/xbiso', '/opt/acetoneiso/bin'),
               ('AcetoneISO-6.7/AcetoneISO.kmdr', '/opt/acetoneiso')]
    for file in fileList:
        pisitools.insinto("%s" % file[1], "%s" % file[0])
    pisitools.dobin('AcetoneISO-6.7/acetoneiso')
