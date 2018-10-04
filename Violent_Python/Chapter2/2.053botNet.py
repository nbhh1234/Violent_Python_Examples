# _*_coding:utf8-
from pexpect import pxssh
import Violent_Python._Config as hnp
'''
This we use "class" in Python to Control multiple computers. We can call it a "botnet"
Note:
-----
    1."uname -v": get linux system version
    2."/etc/issue": login to the system,displayed message.
    3.pxssh documents:
        https://pexpect.readthedocs.io/en/stable/api/pxssh.html
'''

class Client:
    '''
    Create client classes, and initialization.
    parameters:
    ----------
        host: target host
        user: target user
        password: target password
    Note:
    ----
        This code ,we try login in initial function,means:
        when we transfer Client Class, it running ~~
    '''
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        '''
        build a session using pxssh.pxssh,and try login,if failed ,then print Error connecting
        '''
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print e
            print '[-] Error Connecting'

    def send_command(self, cmd):
        '''
        send command to target linux computer.
        :param cmd: send linux command
        '''
        self.session.sendline(cmd)
        self.session.prompt()  # match the prompt
        return self.session.before  # return everything before the prompt.


def botnetCommand(command):
    '''
    For loop botNet list to send command , use Client class
    '''
    for client in botNet:
        output = client.send_command(command)
        print '[*] Output from ' + client.host
        print '[+] ' + output


def addClient(host, user, password):
    '''
    This function, we add target client to boNet list,than, we can use it to For loop and achieved
    multiple computers.
    '''
    client = Client(host, user, password)
    botNet.append(client)


botNet = []


if __name__ == '__main__':

    addClient(hnp.TenCent['host'], hnp.TenCent['user'], hnp.TenCent['password'])
    addClient(hnp.Ali['host'], hnp.Ali['user'],hnp.Ali['password'])
    botnetCommand('uname -v')
    botnetCommand('cat /etc/issue')
