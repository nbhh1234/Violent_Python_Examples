# _*_coding:utf8-

import dpkt
import socket
import pygeoip
import optparse

'''
This code we learning resolve "pcap" files in dpkt
First, we using dpkt.pcap.Reader() to open "pcap" file.
and for loop variable pcap, but it result is garbled.so we need use socket.inet_ntoa() to 
get get string.

Note:
-----
    every package, we will split two part: "Ethernet and ip". The ip  dose not exist,so we
    use "try-except".

Expansion:
---------
    1. if you want to know how to use wireshak,you can view this Url:
        http://www.qingpingshan.com/pc/fwq/386061.html
    2. give you dpkt docstring:
        https://dpkt.readthedocs.io/en/latest/
    3.pcap:
        https://www.cnblogs.com/caoguoping100/p/3658792.html
'''

gi = pygeoip.GeoIP('/opt/GeoIP/GeoLiteCity.dat')

def retGeoStr(ip):
    try:
        rec = gi.record_by_name(ip)
        city = rec['city']
        country = rec['country_code3']
        if city != '':
            geoLoc = city + ', ' + country
        else:
            geoLoc =  country
        return geoLoc
    except Exception as e:
        return 'Unregistered'


def printPcap(pcap):
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print '[+] Source:{}({}) --> Destination:{}({})'.format(src,retGeoStr(src),dst,retGeoStr(dst))
        except Exception as e:
            print e


def main():
    parse = optparse.OptionParser('usage%porg -p <pcap file>')
    parse.add_option('-p',dest = 'pcapFile',type='string',help='specify pcap filename')
    (options,args) = parse.parse_args()
    pcapFile = options.pcapFile
    if pcapFile is None:
        print parse.usage
        exit(0)

    f = open(pcapFile)
    pcap = dpkt.pcap.Reader(f)

    printPcap(pcap)


if __name__ == '__main__':
    main()
