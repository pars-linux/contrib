#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir= "AcetoneISO-6.7"

def install():
    pisitools.dodir('/opt/acetoneiso')
    fileList= [('AcetoneISO-6.7/acetone.png', '/usr/share/pixmaps/'),
               ('AcetoneISO-6.7/aiso.png', '/usr/share/pixmaps/'),
               ('AcetoneISO-6.7/playiso-unmount.sh', '/opt/acetoneiso'),
               ('AcetoneISO-6.7/turbo.sh', '/opt/acetoneiso'),
               ('AcetoneISO-6.7/acetoneiso-mount.desktop', '/usr/kde/3.5/share/apps/konqueror/servicemenus'),
               ('AcetoneISO-6.7/acetoneiso-umount.desktop', '/usr/kde/3.5/share/apps/konqueror/servicemenus'),
               ('AcetoneISO-6.7/cdi2iso', '/opt/acetoneiso/bin'),
               ('AcetoneISO-6.7/mdf2iso', '/opt/acetoneiso/bin'),
               ('AcetoneISO-6.7/nrg2iso', '/opt/acetoneiso/bin'),
               ('AcetoneISO-6.7/xbiso', '/opt/acetoneiso/bin'),
               ('AcetoneISO-6.7/b5i2iso', '/opt/acetoneiso/bin'),
               ('AcetoneISO-6.7/pdi2iso', '/opt/acetoneiso/bin'),
               ('AcetoneISO-6.7/poweriso', '/opt/acetoneiso/bin'),
               ('AcetoneISO-6.7/AcetoneISO.kmdr', '/opt/acetoneiso')]
    for file in fileList:
        pisitools.insinto("%s" % file[1], "%s" % file[0])
    pisitools.dobin('AcetoneISO-6.7/acetoneiso')
