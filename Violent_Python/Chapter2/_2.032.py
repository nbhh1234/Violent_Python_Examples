import optparse
import socket

import threading


class connScan(threading.Thread):
    '''
    Note:
        This code we use Thread division, so we not use for loop in portScan
    '''

    def __init__(self, start_index, end_index, tgtHost, tgtPorts):
        threading.Thread.__init__(self)
        self.start_index = start_index
        self.end_index = end_index
        self.tgtHost = tgtHost
        self.tgtPorts = tgtPorts

    def run(self):
        '''
        Docstring:
        ----------
        Rewrite threading's run function
        '''
        print 'Start' + self.getName() + ' is running...'
        for i in range(self.start_index, self.end_index):

            self.portScan(self.tgtHost, self.tgtPorts[i])

    def portScan(self, tgtHost, tgtPort):

        try:
            tgtIp =  socket.gethostbyname(tgtHost)
            print '[+] hostname ipv4 is :' + str(tgtIp)
        except:
            print '[-] Cannot resolve \'%s\': Unkonwn host' % tgtHost

        try:
            tgtName = socket.gethostbyaddr(tgtIp)
            print '[+] Scan Results for: ' + tgtName[0]
        except:
            print '[+] Scan Results for: ' + tgtIp

        socket.setdefaulttimeout(1)
        # start connScan ~~
        self.connScan(tgtHost, int(tgtPort))

    def connScan(self, tgtHost, tgtPort):
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:

            connSkt.connect((tgtHost, tgtPort))
            connSkt.send('ViolentPython\r\n')  # Send spicy chicken information
            results = connSkt.recv(100)  # s.recv(bufsize[,flag]),accept max data size
            banner_lock.acquire()  # lock threading
            print '[+]%d/tcp open' % tgtPort
            print '[+] ' + str(results)
        except:
            banner_lock.acquire()
            print '[-]%d/tcp closed' % tgtPort
        finally:
            banner_lock.release()
            connSkt.close()




def main():
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
        '''
        Start threading division:
        ------------------------
            1. we set total number of thread(tnt:This example we set 4)
            2. use "tnt" division,its may produce two  result:
                A: your input port can be divisible
                B: your input port can not be divisible,then,we need create other one thread to handle the final part.
            3. we need create threading list to input create new thread
            4. .py thread must be waite all thread execution completed !! use "join()"
        Let's look how to create ~  
        '''
        tnt = 4
        Len_tgtPort = len(tgtPort)
        divisible_part = Len_tgtPort // tnt

        thread_list = []
        for num in range(tnt):
            star_index = num * divisible_part
            end_index = (num + 1) * divisible_part
            t = connScan(star_index, end_index, tgtHost, tgtPort)
            t.start()
            thread_list.append(t)  # append thread,then,execution thread wait.

        if Len_tgtPort % tnt != 0:
            t1 = connScan(end_index, Len_tgtPort, tgtHost, tgtPort)
            t1.start()
            thread_list.append(t1)

        for thread in thread_list:
            thread.join()  # Unified thread waiting


if __name__ == '__main__':
    banner_lock = threading.Lock()  # create global threading Lock

    main()
