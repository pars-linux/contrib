#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # Set Amaya language

    lang = open("/etc/env.d/03locale").readline().strip("LANG=")[:5]
    for i in ["tr_TR", "es_ES", "de_DE", "fr_FR", "it_IT", "fi_FI", "ru_RU", "pt_PT"]:
        if lang == i:
            os.system("sed -i -e 's/LANG=en/LANG=%s/g' /usr/share/Amaya/config/unix-thot.rc" % i.split("_")[0])
