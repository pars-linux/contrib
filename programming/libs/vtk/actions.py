#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

WorkDir="VTK"

def setup():
    shelltools.system("cmake -DCMAKE_INSTALL_PREFIX=%s/usr \
                          -DBUILD_SHARED_LIBS=ON \
                          -DVTK_USE_SYSTEM_JPEG=ON \
                          -DVTK_USE_SYSTEM_PNG=ON \
                          -DVTK_USE_SYSTEM_TIFF=ON \
                          -DVTK_USE_SYSTEM_ZLIB=ON \
                          -DVTK_USE_SYSTEM_EXPAT=ON \
                          -DVTK_WRAP_PYTHON=ON \
                          -DPYTHON_INCLUDE_PATH:PATH=/usr/include/python2.4 \
                          -DVTK_USE_GUISUPPORT=ON \
                          -DVTK_USE_QVTK=ON \
                          -DQT_WRAP_CPP=ON \
                          -DQT_WRAP_UI=ON \
                          -DVTK_INSTALL_QT_DIR:PATH=/qt/3/plugins \
                          -DDESIRED_QT_VERSION:STRING=3 \
                          -DQT_MOC_EXECUTABLE=/usr/qt/3/bin/moc \
                          -DQT_UIC_EXECUTABLE=/usr/qt/3/bin/uic \
                          -DQT_INCLUDE_DIR:PATH=/usr/qt/3/include \
                          -DQT_QMAKE_EXECUTABLE:PATH=/usr/qt/3/bin/qmake" % get.installDIR())


def build():
    cmaketools.make()


def install():
    cmaketools.install()

    #remove compiled py
    pythonmodules.fixCompiledPy()

    #add examples
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "Examples")
