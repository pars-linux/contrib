#!/usr/bin/python
# -*- coding: utf-8 -*-
# This script checks OpenTTD data files and gives an error message if it can't find them

# script author: Uğur Çetin <jnmbk@users.sourceforge.net>
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

import os

def showWarning(text):
    os.system("kdialog --title OpenTTD --error \"%s\"&" % text)

if __name__ == "__main__":
    turkishText = u"OpenTTD'yi çalıştırmadan önce oyunun veri dosyalarını /usr/share/openttd/data/ dizinine koymalısınız. OpenTTD, çalışabilmek için TTD'nin orjinal resimlerine ihtiyaç duyar. Gerekli dosyaların adları şöyledir:\n\n"
    englishText = "Before you run OpenTTD, you need to put the game's data files into /usr/share/openttd/data/ directory. You need the following files from the original version of TTD as OpenTTD makes use of the original TTD artwork:\n\n"
    dataFiles = "sample.cat\ntrg1r.grf\ntrgcr.grf\ntrghr.grf\ntrgir.grf\ntrgtr.grf"
    i = 0
    for file in dataFiles.split("\n"):
        if os.path.exists("/usr/share/openttd/data/%s" % file):
            i+=1
    if i < len(dataFiles.split("\n")):
        if "tr" in os.environ.get("LANG"):
            text = turkishText + dataFiles
        else:
            text = englishText + dataFiles
        showWarning(text)
    else:
        os.system("/usr/bin/openttd&")
