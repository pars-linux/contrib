#!/usr/bin/python
# -*- coding: utf-8 -*-
# This script checks OpenTTD data files and gives an error message if it can't find them

# script author: Uğur Çetin <jnmbk@users.sourceforge.net>
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from qt import *
import sys, os

class openttdError(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("openttdError")

        self.setSizeGripEnabled(1)

        openttdErrorLayout = QGridLayout(self,1,1,11,6,"openttdErrorLayout")

        layout5 = QVBoxLayout(None,0,6,"layout5")

        self.textLabel1 = QLabel(self,"textLabel1")
        self.textLabel1.setAlignment(QLabel.WordBreak | QLabel.AlignVCenter)
        layout5.addWidget(self.textLabel1)

        self.textLabel2 = QLabel(self,"textLabel2")
        self.textLabel2.setPaletteForegroundColor(QColor(255,0,0))
        self.textLabel2.setFrameShape(QLabel.Box)
        self.textLabel2.setFrameShadow(QLabel.Sunken)
        layout5.addWidget(self.textLabel2)
        spacer4 = QSpacerItem(20,21,QSizePolicy.Minimum,QSizePolicy.Minimum)
        layout5.addItem(spacer4)

        layout4 = QHBoxLayout(None,0,6,"layout4")
        Horizontal_Spacing2 = QSpacerItem(248,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout4.addItem(Horizontal_Spacing2)

        self.Ok = QPushButton(self,"Ok")
        self.Ok.setAutoDefault(1)
        self.Ok.setDefault(1)
        layout4.addWidget(self.Ok)

        self.Help = QPushButton(self,"Help")
        self.Help.setAutoDefault(1)
        layout4.addWidget(self.Help)
        layout5.addLayout(layout4)

        openttdErrorLayout.addLayout(layout5,0,0)

        self.languageChange()

        self.resize(QSize(350,250).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.Ok,SIGNAL("clicked()"),self.accept)
        self.connect(self.Help,SIGNAL("clicked()"),self.gotoSite)


    def languageChange(self):
        self.setCaption(self.__tr("OpenTTD"))
        self.textLabel1.setText(self.__tr("    Before you run OpenTTD, you need to put the game's datafiles into the /usr/share/openttd/data/ directory. You need the following files from the original version of TTD as OpenTTD makes use of the original TTD artwork:"))
        self.textLabel2.setText(self.__tr("<p align=\"center\">sample.cat trg1r.grf trgcr.grf trghr.grf trgir.grf trgtr.grf</p>"))
        self.Ok.setText(self.__tr("&OK"))
        self.Ok.setAccel(QKeySequence(QString.null))
        self.Help.setText(self.__tr("&Help"))
        self.Help.setAccel(QKeySequence(self.__tr("Alt+H")))


    def gotoSite(self):
        import os
        os.system("firefox http://www.openttd.org &")

    def __tr(self,s,c = None):
        return qApp.translate("openttdError",s,c)

    def toggleTurkish(self):
        self.textLabel1.setText(u"    OpenTTD'yi çalıştırmadan önce oyunun veri dosyalarını /usr/share/openttd/data/ dizinine koymalısınız. OpenTTD, çalışabilmek için TTD'nin orjinal resimlerine ihtiyaç duyar. Gerekli dosyaların adları şöyledir:")
        self.Ok.setText(u"&Tamam")
        self.Help.setText(u"&Yardım")
        self.Help.setAccel(QKeySequence(self.__tr("Alt+Y")))

if __name__ == "__main__":
    datafiles = ["sample.cat", "trg1r.grf", "trgcr.grf", "trghr.grf", "trgir.grf", "trgtr.grf"]
    i = 0
    for file in datafiles:
        if os.path.exists("/usr/share/openttd/data/%s" % file): i+=1
    if i < datafiles.__len__():
        app = QApplication(sys.argv)
        f = openttdError()
        if "tr" in os.environ.get("LANG"): f.toggleTurkish()
        f.show()
        app.setMainWidget(f)
        app.exec_loop()
    else:
        os.system("/usr/share/openttd/run")
