# _*_coding:utf8-

from socket import *  # include any func or method
'''
This code,we will create connScan func and port Scan
portScan: accept Host address and Port
connScan: output Ip address and try links every port
'''

def connScan(tgtHost, tgtPort):
    '''
    :param tgtHost: target host address
    :param tgtPort: target Port
    :return: None
    Expansion:
    ---------
    what is socket in Python?
        https://gist.github.com/kevinkindom/108ffd675cb9253f8f71
    '''
    try:
        # Create TCP socket
        connSkt = socket(AF_INET, SOCK_STREAM)
        # connect Socket
        connSkt.connect((tgtHost, tgtPort))
        print '[+]%d/tcp open' % tgtPort
        connSkt.close()

    except Exception as e:
        print '[-]%d/tcp closed:' % tgtPort


def portScan(tgtHost, tgtPorts):
    '''

    :param tgtHost: target host address
    :param tgtPorts: target Ports
    :return: None

    Expansion:
    ----------
    0.https://docs.python.org/2/library/socket.html#socket.gethostbyname
    what is gethostbyname function?
        Note: you can try gethostname("your host name or use localhost")
        Translate a host name to IPv4 address format.
        The IPv4 address is returned as a string,
        If the host name is an IPv4 address itself it is returned unchanged.
    what is gethostbyaddr function?
        Return a triple (hostname, aliaslist, ipaddrlist)
        hostname:the primary host name responding to the given ip_address
        aliaslist: alternative host names for the same address, possibly empty
        ipaddrlist: list of IPv4/v6 addresses
    '''
    try:

        tgtIP = gethostbyname(tgtHost)
    except:
        print '[-] Cannot resolve \'%s\':Unknown host' % tgtHost
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '[+] Scan Results for: ' + tgtName[0]
    except:
        print '[-] Scan Results for: ' + tgtIP

    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        print 'Scanning port ' + tgtPort
        connScan(tgtHost, tgtPort)
