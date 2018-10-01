# _*_coding:utf8-

import zipfile
import optparse

from threading import  Thread

def extractFile(zFile,password):
    '''

    :param zFile: it's function in Python
    :param password: password in password.txt,and try use it to extract with zip file
    :return: None
    '''
    try:
        zFile.extractall(pwd=password)
        print '[+] Found password:' + password + '\n'
    except :
        pass
def main():
    '''
    this code we need know what is threading?
    And what is optparse,if you don't know,don't worry about it, we will
    explain in the next Chapter.

    Expansion:
    --------
    the optparse is like "argparse" in python

    what is exit(0)  ?
    https://blog.csdn.net/geekleee/article/details/52794826
    '''

    parser = optparse.OptionParser('usage%prog' + '-f <zipfile> -d <dictionary>')
    parser.add_option('-f',dest = 'zname',type='string',
                      help = 'specify zip file')
    parser.add_option('-d',dest = 'dname',type='string',
                      help = 'specify dictionary file')
    (options,args) = parser.parse_args()

    if (options.zname == None) or (options.dname == None):
        print parser.usage
        exit(0)

    else:
        zname = options.zname
        dname = options.dname
        zFile = zipfile.ZipFile(zname)
        passFile = open(dname)
        for line in passFile.readlines():
            password = line.strip('\n')
            t = Thread(target=extractFile,args=(zFile,password))
            t.start()
            print  Thread.getName(t) + 'is start'

if __name__ == '__main__':
    main()


