#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Author: Gökmen Görgen, <gkmngrgn@gmail.com>

import pygtk, gtk

def main(widget = None):
    lang = file("/etc/mudur/language").read().rstrip("\n")

    if lang == "tr":
        msg = "Wicd servisi şuan etkin değil! Servis Yöneticisi'nden\nWicd ağ yöneticisini çalıştırın ve tekrar deneyin."

    else:
        msg = "Wicd daemon isn't active! Please run Wicd\nconnection manager from Service Manager and try again."

    warning = gtk.MessageDialog(None,
                                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                                gtk.MESSAGE_INFO,
                                gtk.BUTTONS_OK,
                                str(msg))
    warning.run()
    warning.destroy()
