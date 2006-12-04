#!/usr/bin/python
#-*- coding: UTF-8 -*-

import os

def postInstall():
   os.system("/usr/bin/gconftool-2 --direct --config-source \
             `/usr/bin/gconftool-2 --get-default-source` --load=/etc/gconf/schemas/panel-default-setup.entries")