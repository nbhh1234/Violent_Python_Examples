# _*_coding:utf8-
import pygeoip

'''

This code we learning 'Use Ip search location'
We need download database, you can use "wget:"
     http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
and use linux order "gunzip" to decompression download file. 
you can move "D-F" to you loving directory.I moved in /opt/GeoIp(you cam mkdir this directory)
finally, we need download "pygeoip",same as before using pip install xxx [-i].

Docstring:
---------
    1. loading database to pygeoip.GeoIP()
    2.  use record_by_name to find some we need message. and then return dictionary in Python.
    3. we get city, region , country, longitude(-180,180), latitude(-90,90)
    
    
Come on , take look your boyfriend or girlfriend wifi location :),if you have not 'b,g' 
Don't worry, take look yourself IP,like me !_! 
 
Expansion:
--------
    1.Precise Position: https://ip.rtbasia.com/ or baidu precise position API
    2.test ip remember using Public IP:
        run curl ifconfig.me in your terminal 
'''

gi = pygeoip.GeoIP('/opt/GeoIP/GeoLiteCity.dat')


def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    print rec
    city = rec['city']
    region = rec['continent']
    country = rec['country_name']
    long_ = rec['longitude']
    lat = rec['latitude']
    print '[+] Target: ' + tgt + ' Geo-located'
    print '[+] ' + str(city) + ', ' + str(region) + ', ' + str(country)
    print '[+] Latitude: ' + str(lat) + ', Longitude: ' + str(long_)


tgt = '114.245.20.191'
if __name__ == '__main__':
    printRecord(tgt)
