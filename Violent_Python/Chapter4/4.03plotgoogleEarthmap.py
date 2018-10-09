# _*_coding:utf8-

import dpkt
import socket
import pygeoip
import optparse


'''
Actually,we can cast ip onto the Google Earth map. let's to see how to achieve.
Note:
------
make sure you have VPN, then login to Google Earth.
Docstring:
----------
    1.First,you need know what is "Google KML",for more information please see:
        https://developers.google.com/kml/documentation/kml_tut
    2.Second,we can use "Google KML" to create ".kml" file.
        A:same as before, we get ip in geotest.pcap,using dpkt and socket packages.
        B:get  longitude and latitude of ip, using pygeoip package.
        C:write ".kml" file in your location directory.
'''
gi = pygeoip.GeoIP('/opt/GeoIP/GeoLiteCity.dat')
def retKML(ip):
    print ip
    try:
        rec = gi.record_by_name(ip)
        longitude = rec['longitude']
        latitude = rec['latitude']
        kml = '''
        <Placemark>
 <name>%s</name>
 <description>you can Write something by Joker</description>
 <Point>
 <coordinates>%6f,%6f</coordinates>
 </Point>
 </Placemark>
        ''' % (ip, longitude, latitude)
        return kml
    except Exception as e:
        print e



def plotIPs(pcap):
    kmlPts = ''
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            srcKML = retKML(src)
            dstKML = retKML(dst)
            kmlPts += srcKML + dstKML
        except Exception as e:
            print e
    return kmlPts


def Writekml(kmldoc):
    # remember close file !!
    file = open('geotest.kml', 'w')
    file.write(kmldoc)
    file.close()


def main():
    parse = optparse.OptionParser('usage%porg -p <pcap file>')
    parse.add_option('-p', dest='pcapFile', type='string', help='specify pcap filename')
    (options, args) = parse.parse_args()
    pcapFile = options.pcapFile
    if pcapFile is None:
        print parse.usage
        exit(0)

    f = open(pcapFile)
    pcap = dpkt.pcap.Reader(f)

    kmlheader = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>'''
    kmlfooter = '''</Document></kml>'''
    kmldoc = kmlheader + plotIPs(pcap) + kmlfooter

    Writekml(kmldoc)


if __name__ == '__main__':
    main()


'''
HomeWork:
    1.if you have courage, you can using Precise Position of ip.
        https://www.cnblogs.com/niuniuc/p/7244874.html
        
'''