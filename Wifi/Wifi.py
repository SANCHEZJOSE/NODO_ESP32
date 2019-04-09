import network
sta_if = network.WLAN(network.STA_IF) #modo conexión a rourter
ap_if = network.WLAN(network.AP_IF) #modo acess point
sta_if.active() #verificar modo activo
ap_if.active() #verificar modo activo
#.ifconfig() #devuelve IP addres,netmask,gateway,DNS
"""conectarse a una red"""
sta_if.active(True)#activacion
sta_if.connect('nombre', '12345')#conexion a red
sta_if.isconnected()#verificar conexion
"""Sockets(puentes de conexion a travez de puertos)"""
#TCP socket
