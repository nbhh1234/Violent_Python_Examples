# _*_coding:utf8

import crypt


def testPass(cryptPass):
    '''
    for loop in every word with every cryptPass
    :param cryptPass: the crypt Password in password.txt
    :return: None
    :Docstring:
    ------
    0.what is content in /etc/password? or /etc/shadow
    1.test  my Ubuntu (joker) in the /etc/shadow
        ctype = "1" #for sha512 (see man crypt)
        salt = "V3AOSVeo"
        insalt = '${}${}$'.format(ctype, salt)
        password = "woaij100"

        ctype is 1,the salt is V3AOSVeo so, the insalt is $1$V3AOSVeo'
        a = crypt.crypt('woaij100','$1$V3AOSVeo')
    2.Expansion:
        1.http://www.cnblogs.com/leoo2sk/archive/2010/10/01/hash-and-encrypt.html
        2.https://www.cnblogs.com/heart-runner/archive/2011/11/29/2268340.html
        3.https://blog.csdn.net/matrix65537/article/details/53788681
    '''
    salt = cryptPass[0:2]
    dictFile = open('../../data/dictionary.txt','r')
    for word in dictFile.readlines():
        word = word.strip('\n')   # delete '\n'
        cryptWord = crypt.crypt(word,salt)
        if cryptWord == cryptPass:
            print "[+] Found Password:" +word
        else:
            print "[-] Password {} Not Found.".format(word)

def main():
    passFile = open('../../data/passwords.txt')
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print "[*] Cracking Password For:" + user
            testPass(cryptPass)


if __name__ == "__main__":
    main()




