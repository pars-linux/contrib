#!/usr/bin/python

import os

def postInstall():
    os.system("sed -i 's/pardus/circles/g' /usr/kde/3.5/share/config/kdm/kdmrc")
    os.system("e17genmenu -k")
    os.system("e17genmenu -d=/usr/kde/3.5/share/applications/kde")
    os.system("e17genmenu -d=/usr/kde/3.5/share/applnk")
def preRemove():
    os.system("sed -i 's/circles/pardus/g' /usr/kde/3.5/share/config/kdm/kdmrc")