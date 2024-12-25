import network
ap = network.WLAN(network.AP_IF) #access point mode, change to STA_IF for station mode
ap.active(True)
ap.config(essid='picotest',password='goodPassword23')
