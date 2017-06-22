#!/usr/bin/env python
import nmap


def scan_ports(ips, ports):
    info = nmap.PortScanner()

    info.scan(ips, ports)
    info.command_line()
    info.scaninfo()

    for host in info.all_hosts():

        print('---------------------------------------------------------')
        print('Host  : %s (%s)' % (host, info[host]['hostname']))
        print('State : %s' % info[host].state())

        for proto in info[host].all_protocols():
            print('Protocol : %s' % proto)

            if proto == 'tcp':

                lport = info[host][proto].keys()
                lport.sort()

                for port in lport:

                    print('  port %s' % (port))
                    # print ('port : %s\tstate : %s' % (port, info[host][proto][port]['state']))
                    # print ('port : %s\tproduct : %s' % (port, info[host][proto][port]['product']))

                    port = info[host][proto][port]
                    items = port.keys()

                    for item in items:
                        print('    {: <12}: {: <24}'.format(item, port[item]))

    print


scan_ports('192.168.1.1-9', '16-1024')
# scan_ports('192.168.1.10-14', '16-9999')
# scan_ports('192.168.1.15-29', '16-2000 ')
