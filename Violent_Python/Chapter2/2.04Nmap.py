# _*_coding:utf8-
import optparse
import nmap
'''
This code, we known the namp package is very strong with port is 1720
and we learning other port scan in Chapter5
'''

def nmapScan(tgtHost, tgtPort):

    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print " [*] " + tgtHost + ' tcp/ ' + tgtPort + " " + state


def main():
    parser = optparse.OptionParser('usage %prog -H' + '<target host> -p <target port>')

    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port')

    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = options.tgtPort.split(',')

    if tgtHost is None and tgtPorts is None:
        print parser.usage
        exit(0)
    else:
        for tgtPort in tgtPorts:
            nmapScan(tgtHost, tgtPort)


if __name__ == '__main__':
    main()

