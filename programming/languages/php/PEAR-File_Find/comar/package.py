#!/usr/bin/python

import os

def postInstall():
    os.system("chmod 0755 /usr/share/php5/PEAR/File/Find.php")