#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Author: Gökmen Görgen, <gkmngrgn@gmail.com>

import pygtk, gtk
import os

def main(widget = None):
    if os.getenv("LANG").startswith("tr"):
        msg = "Wicd servisi şuan etkin değil! Servis Yöneticisi'nden\nWicd ağ yöneticisini çalıştırın ve tekrar deneyin."

    else:
        msg = "Service Wicd is not started! Please run Wicd connection\nmanager from Service Manager and try again."

    warning = gtk.MessageDialog(None,
                                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                                gtk.MESSAGE_INFO,
                                gtk.BUTTONS_OK,
                                str(msg))
    warning.run()
    warning.destroy()
