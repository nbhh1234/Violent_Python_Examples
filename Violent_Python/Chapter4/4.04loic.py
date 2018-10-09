# _*_coding:utf8-

import dpkt
import socket

'''
Find LOIC(Low Orbit Ion Cannon).
1. we open tcpdump in your terminal "tcpdump -i eth0 -A 'port 80'", for more information,
    you can see: https://www.cnblogs.com/ggjucheng/archive/2012/01/14/2322659.html
2. and we using dpkt.http.Request() to get some message in http packet header,if we find '.zip' and
    'loic',then we can be sure this  ip  download 'loic.zip'.was
'''

def findDownload(pcap):
    for ts,buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            tcp = ip.data
            http = dpkt.http.Request(tcp.data)
            if http.method == 'GET':
                uri = http.uri.lower()
                if '.zip' in uri and 'loic' in uri:
                    print '[!] ' + src + ' Download LOIC'
        except:
            print '[-] Not Find'

f = open('geotest.pcap')
pcap = dpkt.pcap.Reader(f)
findDownload(pcap)

'''
Example:
--------
    test your ip, and  download loic.zip from http://sourceforge.net/projects/loic/
    you maybe need Wireshark.
'''


