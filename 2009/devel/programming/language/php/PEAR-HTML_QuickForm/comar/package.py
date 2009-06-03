#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("chmod -R 0755 /usr/share/php5/PEAR/doc/HTML_QuickForm")