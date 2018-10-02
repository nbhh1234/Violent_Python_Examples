# _*_coding:utf8-
import optparse
import socket
import  threading
from socket import gethostbyaddr, gethostbyname

banner_lock = threading.Lock()

def connScan(tgtHost, tgtPort):
    '''
    First:we create easy socket,and create TCP, use socket.AF_INET,socket.SOCK_STREAM
    Second: we try connection target Host and send some message,note,
            we need set max data size, This example,we set 100,of course,you can set other max data size
            and then,if target Host Port is open,we can accept result,so,we print this port is open,else,
            this port is closed.

    :param tgtHost: target Hostname
    :param tgtPort: target HostPort
    :return: None
    '''
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')  # Send spicy chicken information
        results = connSkt.recv(100)  # s.recv(bufsize[,flag]),accept max data size
        banner_lock.acquire() # lock threading
        print '[+]%d/tcp open' % tgtPort
        print '[+] ' + str(results)
    except:
        banner_lock.acquire()
        print '[-]%d/tcp closed' % tgtPort
    finally:
        banner_lock.release()
        connSkt.close()


def portScan(tgtHost, tgtPorts):
    '''
    Docstring:
    ----------
    First: we try get target Host ip(this ip possibly ipv4 or ipv6)
            and we get hostname, aliaslist, ipaddrlist
    Second:we set socket timeout,because,sometime the network will be very very slowly,

    Third: we use for loop try every port in connScan function


    '''
    try:
        tgtIp = gethostbyname(tgtHost)
        print '[+] hostname ipv4 is :' + str(tgtIp)
    except:
        print '[-] Cannot resolve \'%s\': Unkonwn host' % tgtHost

    try:
        tgtName = gethostbyaddr(tgtIp)
        print '[+] Scan Results for: ' + tgtName[0]
    except:
        print '[+] Scan Results for: ' + tgtIp
    socket.setdefaulttimeout(1)



    for tgtPort in tgtPorts:
        thread = threading.Thread(target=connScan,args=(tgtHost, int(tgtPort)))
        print 'threading {} start to Scanning port {}'.format(threading.Thread.getName(thread),tgtPort)
        thread.start()

    '''
    Note:
        if we use this method to create threading,then,we have a problem.
        this prob is:
            if we have  many  many (maybe 5000) test port,then,  so many threading will be create,
            your computer will be die.~~
        So, follow me, let's look "Correct thread creation method"
    '''



def main():
    '''
    Docstring:
    ---------
    create option Parser, the -H means target Hostname(or ip),-P means target host'ip
    we use ".split(',')", cause,we try run many port as same time and return list type in Python.
    Finally,we run portScan function,star Scan target Host !!

    Note:
        make sure your test Host have open port right?
    Good Luck!~~~
    '''
    parser = optparse.OptionParser('usage %prog -H' + '<target host> -p <target port>')

    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port')

    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort.split(',')

    if (tgtHost == None) and (tgtPort == None):
        print parser.usage
        exit(0)
    else:
        portScan(tgtHost, tgtPort)


if __name__ == '__main__':
    main()

