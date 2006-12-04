from comar.service import *

serviceType = 'local'
serviceDesc = 'WPA Supplicant Service'

pidfile = '/var/run/wpa_supplicant.pid'

''' wpa_supplicant communication interfaces '''
global_iface = '/var/run/wpa_supplicant-global'
wpa_iface = '/var/run/wpa_supplicant'

def start():
    ''' Load configuration settings '''
    try:
        opts = '-P %s %s' % (pidfile, config['opts'])
        driver = config['wireless_driver']
    except:
        fail('Error in wpa_supplicant configuration file')

    interface = getWirelessInterface()

    ''' Start daemon '''
    ret = run('/sbin/start-stop-daemon --start --quiet --pidfile %s --exec /usr/sbin/wpa_supplicant -- %s' % (pidfile, opts))
    if ret == 0:
        notify('System.Service.changed', 'started')
    else:
       fail('Failed to start wpa_supplicant daemon')

    # Automatic device registration for IEEE 802.1x

    ## FIXME: Enable this later, when we support IEEE 802.1x auth. on wired networks in net-kga

    ## Add all wired interfaces with "wired" driver
    #for interface in getWiredInterfaces():
        #os.system('/usr/bin/wpa_cli -g %s interface_add %s "" wired %s' % (global_iface, interface, wpa_iface))

    # FIXME: Wireless drivers should automatically detect (madwifi, wext, atmel, hostap, prism54, ndiswrapper..)

    # Now, default driver in the configuration file is "wext" (Generic linux wireless extension driver)
    # Add wireless interface
    os.system('/usr/bin/wpa_cli -g %s interface_add %s "" %s %s' % (global_iface, interface, driver, wpa_iface))

def stop():
    ret = run('/sbin/start-stop-daemon --stop --quiet --pidfile %s --exec /usr/sbin/wpa_supplicant' % pidfile)
    if ret == 0:
        notify('System.Service.changed', 'stopped')
    else:
       fail('Failed to stop wpa_supplicant daemon')

def status():
    return checkDaemon(pidfile)

import os

def getWirelessInterface():
    ''' Find wireless interface '''
    for interface in os.listdir('/sys/class/net'):
        if os.path.exists(os.path.join('/sys/class/net', interface, 'wireless')):
            return interface
    fail('Unable to find wireless interface')

from comar.device import sysValue

def getWiredInterfaces():
    import csapi
    ARPHRD_ETHER = 1
    ''' Find wired interfaces '''
    list = []
    for interface in os.listdir('/sys/class/net'):
        if not os.path.exists(os.path.join('/sys/class/net', interface, 'wireless')):
            if csapi.atoi(sysValue('class/net', interface, 'type')) == ARPHRD_ETHER:
                list.append(interface)
    return list
