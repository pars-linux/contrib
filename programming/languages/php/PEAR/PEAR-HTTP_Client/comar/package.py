#!/usr/bin/python

import os

def postInstall():
    os.system("chmod 0755 /usr/share/php5/PEAR/doc/HTTP_Client/link-checker.php")