#!/usr/bin/python

import os

def postInstall():
    # Set Amaya language
    lang = open("/etc/env.d/03locale").readline().strip("LANG=")[:5]

    # Set lang as Turkish
    if lang == "tr_TR":
        os.system("sed -i -e 's/LANG=en/LANG=tr/g' /usr/share/Amaya-9.54/config/unix-thot.rc")
    # Set lang as Spanish
    elif lang == "es_ES":
        os.system("sed -i -e 's/LANG=en/LANG=es/g' /usr/share/Amaya-9.54/config/unix-thot.rc")
    # Set lang as German
    elif lang == "de_DE":
        os.system("sed -i -e 's/LANG=en/LANG=de/g' /usr/share/Amaya-9.54/config/unix-thot.rc")
    # Set lang as French
    elif lang == "fr_FR":
        os.system("sed -i -e 's/LANG=en/LANG=fr/g' /usr/share/Amaya-9.54/config/unix-thot.rc")
    # Set lang as Italian
    elif lang == "it_IT":
        os.system("sed -i -e 's/LANG=en/LANG=it/g' /usr/share/Amaya-9.54/config/unix-thot.rc")
    # Set lang as Finnish
    elif lang == "fi_FI":
        os.system("sed -i -e 's/LANG=en/LANG=fi/g' /usr/share/Amaya-9.54/config/unix-thot.rc")
    # Set lang as Russian
    elif lang == "ru_RU":
        os.system("sed -i -e 's/LANG=en/LANG=ru/g' /usr/share/Amaya-9.54/config/unix-thot.rc")
    # Set lang as Portuguese
    elif lang == "pt_PT":
        os.system("sed -i -e 's/LANG=en/LANG=pt/g' /usr/share/Amaya-9.54/config/unix-thot.rc")