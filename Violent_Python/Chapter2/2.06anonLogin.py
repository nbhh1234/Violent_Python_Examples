# _*_coding:utf8-
import ftplib
'''
This code we need learning how to connect anonymous FTP in Python

Note:
----
    1.Make sure you have ftp server in your computer and open anonymous
    2. if you have not ,you can view URL below, they can help you. !
        https://blog.csdn.net/xinguan1267/article/details/47751137
        https://blog.csdn.net/soslinken/article/details/79304076   create ftpuser !
        https://askubuntu.com/questions/413677/vsftpd-530-login-incorrect
    3. if you have 530 Error, checking  anonymous = No? in your /etc/vsftpd.conf
    
'''
def annonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous','Joker@edu.com')
        print '[+] ' + str(hostname) + ' FTP Anonymous Logon Succeeded.'
        ftp.quit()
        return  True
    except Exception as e:
        print e
        print '[-] ' + str(hostname) + ' FTP Anonymous Logon Failed.'
        return  False


if __name__ == '__main__':

    host = '127.0.0.1'
    annonLogin(host)