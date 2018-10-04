# _*_coding:utf8-

import ftplib

'''
https://docs.python.org/2/library/ftplib.html
'''
def returnDefault(tfp):

    try:
        dirList = tfp.nlst()
        print dirList
    except Exception as e:
        print e
        print '[-] Could not lost directory contents'
        print '[-] Skipping To Next Target'
    else:
        retList = []

        for fileName in dirList:
            # dirList2 = tfp.nlst(fileName)
            # print dirList2
            fn = fileName.lower()
            if ('.php' in fn) or ('.htm' in fn) or ('.asp' in fn):
                print '[+] Found default page: ' + fileName
        return retList


host = '127.0.0.1'
userName = 'root'
passWord = 'toor'

tfp = ftplib.FTP(host)
tfp.login(userName, passWord)
returnDefault(tfp)

'''
HomeWork:
    use ftp.nlst to traverse all directories. 
'''