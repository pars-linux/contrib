#!/usr/bin/python

import os

def postInstall():
    os.system("chmod -R 0755 /usr/share/php5/PEAR/doc/HTML_Template_Sigma")
    os.system("chmod -R 0755 /usr/share/php5/PEAR/tests/HTML_Template_Sigma")