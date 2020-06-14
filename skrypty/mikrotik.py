#!/bin/python37

from netmiko import ConnectHandler
import getpass
import datetime
import time


miktotik= { 
    'device_type': 'mikrotik_routeros', 
    'host': '172.16.200.1', 
    'port': 2111, 
    } 

all_devices = [ miktotik ]


for a_dev in all_devices:
    try:
        inUsername=input("Username: ")
        inPassword=getpass.getpass()
        
        if (len(inUsername) != 0 and len(inPassword) != 0):
            a_dev.update({ 'password' : inPassword })
            a_dev.update({ 'username' : inUsername })
            
            net_connect = ConnectHandler(**a_dev)
            net_connect.find_prompt()
            
            if a_dev['device_type'] == 'mikrotik_routeros':
                print("=============================================\n" \
                    + a_dev['host'] + " " + net_connect.send_command("system identity print") \
                    + "\n=============================================")

                output = net_connect.send_command("ip route print")
                print(output)
                output = net_connect.send_command("user active print")
                print(output)
                output = net_connect.send_command("ip dhcp-server lease print")
                print(output)

                net_connect.disconnect()
        else:
            print("\n\nUsername and Password cannot be empty")
    except ValueError:
        print(a_dev['host']+" Error")