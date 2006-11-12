#!/usr/bin/python

import os

def postInstall():
    os.system('wall "Merhaba PiSi paketi sisteme kuruldu!"')

def preRemove():
    os.system('wall "Merhaba PiSi paketi sistemden kaldırılıyor!"') 
