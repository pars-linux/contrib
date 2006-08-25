#!/usr/bin/python

from pisi.actionsapi import shelltools

def postInstall():
    os.system("e17genmenu -k")
    os.system("e17genmenu -d /usr/kde/3.5/share/applications")
    os.system("e17genmenu -d /usr/share/applications")
    os.system.("e17genmenu -d=/usr/kde/3.5/share/applnk")
    os.system("e17genmenu -d=/usr/share/applnk")