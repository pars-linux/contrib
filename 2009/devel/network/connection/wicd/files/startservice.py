#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# @author: Gökmen Görgen, <gkmngrgn_gmail.com>
#

import comar

link = comar.Link()
link.setLocale()
link.useAgent()

def startService(service):
    link.System.Service[service].start()

def infoService(service):
    # return 'on' or 'stopped'.
    return link.System.Service[service].info()[2]

def warningWidget():
    import gtk
    import os

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
