#!/usr/bin/python

import os

def postInstall():
    os.system('/usr/bin/xmlcatalog --noout --add "public" \
               "-//OMF//DTD Scrollkeeper OMF Variant V1.0//EN" \
               "/usr/share/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd" \
               /etc/xml/docbook')
    os.system("/usr/bin/scrollkeeper-rebuilddb -q -p /var/lib/scrollkeeper")
    os.system("/usr/bin/scrollkeeper-update")

def preRemove():
    os.system('/usr/bin/xmlcatalog --noout --del \
               "/usr/share/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd" \
               /etc/xml/docbook')