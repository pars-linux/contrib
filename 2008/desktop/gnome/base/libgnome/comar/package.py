#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.environ['GCONF_CONFIG_SOURCE'] = 'xml:merged:/etc/gconf/gconf.xml.defaults'
    installedSchemas = ['desktop_gnome_accessibility_keyboard.schemas',
                        'desktop_gnome_accessibility_startup.schemas',
                        'desktop_gnome_applications_at_mobility.schemas',
                        'desktop_gnome_applications_at_visual.schemas',
                        'desktop_gnome_applications_browser.schemas',
                        'desktop_gnome_applications_help_viewer.schemas',
                        'desktop_gnome_applications_terminal.schemas',
                        'desktop_gnome_applications_window_manager.schemas',
                        'desktop_gnome_background.schemas',
                        'desktop_gnome_file_views.schemas',
                        'desktop_gnome_interface.schemas',
                        'desktop_gnome_lockdown.schemas',
                        'desktop_gnome_peripherals_keyboard.schemas',
                        'desktop_gnome_peripherals_mouse.schemas',
                        'desktop_gnome_sound.schemas',
                        'desktop_gnome_thumbnailers.schemas',
                        'desktop_gnome_typing_break.schemas']

    for schema in installedSchemas:
        os.system("/usr/bin/gconftool-2 --makefile-install-rule /etc/gconf/schemas/%s" % schema)

def preRemove():
    os.environ['GCONF_CONFIG_SOURCE'] = 'xml:merged:/etc/gconf/gconf.xml.defaults'
    installedSchemas = ['desktop_gnome_accessibility_keyboard.schemas',
                        'desktop_gnome_accessibility_startup.schemas',
                        'desktop_gnome_applications_at_mobility.schemas',
                        'desktop_gnome_applications_at_visual.schemas',
                        'desktop_gnome_applications_browser.schemas',
                        'desktop_gnome_applications_help_viewer.schemas',
                        'desktop_gnome_applications_terminal.schemas',
                        'desktop_gnome_applications_window_manager.schemas',
                        'desktop_gnome_background.schemas',
                        'desktop_gnome_file_views.schemas',
                        'desktop_gnome_interface.schemas',
                        'desktop_gnome_lockdown.schemas',
                        'desktop_gnome_peripherals_keyboard.schemas',
                        'desktop_gnome_peripherals_mouse.schemas',
                        'desktop_gnome_sound.schemas',
                        'desktop_gnome_thumbnailers.schemas',
                        'desktop_gnome_typing_break.schemas']

    for schema in installedSchemas:
        os.system("/usr/bin/gconftool-2 --makefile-uninstall-rule /etc/gconf/schemas/%s" % schema)
