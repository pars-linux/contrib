#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall():
    os.system("/usr/bin/xmlcatalog --noout --add \"delegatePublic\" \
               \"-//Robby Stephenson/DTD Tellico V9.0//EN\" \
               \"file:///usr/share/apps/tellico/tellico.dtd\" \
               /etc/xml/catalog")

    os.system("/usr/bin/xmlcatalog --noout --add \"delegateSystem\" \
               \"http://www.periapsis.org/tellico/dtd/v9/tellico.dtd\" \
               \"file:///usr/share/apps/tellico/tellico.dtd\" \
               /etc/xml/catalog")

    os.system("/usr/bin/xmlcatalog --noout --add \"delegateURI\" \
               \"http://www.periapsis.org/tellico/dtd/v9/tellico.dtd\" \
               \"file:///usr/share/apps/tellico/tellico.dtd\" \
               /etc/xml/catalog")

def preRemove():
    os.system("/usr/bin/xmlcatalog --noout --del \
               \"file:///usr/share/apps/tellico/tellico.dtd\" \
               /etc/xml/catalog")