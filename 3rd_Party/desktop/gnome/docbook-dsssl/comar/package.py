#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/install-catalog --add /etc/sgml/dsssl-docbook-stylesheets.cat \
    /usr/share/sgml/docbook/dsssl-stylesheets-1.79/catalog")
    os.system("/usr/bin/install-catalog --add /etc/sgml/sgml-docbook.cat /etc/sgml/dsssl-docbook-stylesheets.cat")
