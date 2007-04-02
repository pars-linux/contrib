#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

WorkDir="VTK"

def setup():
    cmaketools.configure("-DBUILD_SHARED_LIBS=ON \
                          -DVTK_WRAP_PYTHON=ON \
                          -DVTK_USE_SYSTEM_JPEG=ON \
                          -DVTK_USE_SYSTEM_PNG=ON \
                          -DVTK_USE_SYSTEM_TIFF=ON \
                          -DVTK_USE_SYSTEM_ZLIB=ON \
                          -DVTK_USE_SYSTEM_EXPAT=ON \
                          -DVTK_USE_SYSTEM_FREETYPE=ON \
                          -DVTK_WRAP_PYTHON=ON \
                          -DPYTHON_INCLUDE_PATH=/usr/include/python2.4 \
                          -DVTK_USE_GUISUPPORT=ON \
                          -DVTK_USE_QVTK=ON \
                          -DQT_WRAP_CPP=ON \
                          -DQT_WRAP_UI=ON \
                          -DVTK_INSTALL_QT_DIR=/qt/3/plugins \
                          -DDESIRED_QT_VERSION:STRING=3 \
                          -DQT_MOC_EXECUTABLE=/usr/qt/3/bin/moc \
                          -DQT_UIC_EXECUTABLE=/usr/qt/3/bin/uic \
                          -DQT_INCLUDE_DIR=/usr/qt/3/include \
                          -DQT_QMAKE_EXECUTABLE=/usr/qt/3/bin/qmake")


def build():
    cmaketools.make()



def install():
    cmaketools.rawInstall("DESTDIR=%s root=%s" % (get.installDIR(), get.installDIR()))

    #add examples
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "Examples")

    #remove Win32 examples
    pisitools.removeDir("/usr/share/doc/%s/Examples/GUI/Win32" % get.srcTAG())

    #remove Win32 header
    pisitools.remove("/usr/include/vtk-5.0/vtkWin32Header.h")

    #install python modul
    shelltools.cd("Wrapping/Python")
    pythonmodules.install()
