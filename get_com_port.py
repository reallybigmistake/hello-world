from serial.tools.list_ports_windows import comports
port_list = comports()
if port_list:
    for port in port_list:
        print(port[0], end=',')
input()