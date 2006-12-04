#!/usr/bin/python

import os

def postInstall():
#    os.system("/usr/bin/xmlcatalog --noout --add \
#               /usr/share/xml/libglade/glade-2.0.dtd /etc/xml/catalog")
     os.system("/usr/bin/install-catalog --add \
                /etc/xml/catalog /usr/share/xml/libglade/glade-2.0.dtd")
		
def preRemove():
#    os.system("/usr/bin/xmlcatalog --noout --del \
#               /usr/share/xml/libglade/glade-2.0.dtd /etc/xml/catalog")
     os.system("/usr/bin/install-catalog --remove \
                /etc/xml/catalog /usr/share/xml/libglade/glade-2.0.dtd")
