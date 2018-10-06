# _*_ coding:utf8-*-

from winreg import  *
'''
This code we will learning where is "wifi MAC" in Windows.
Unfortunately:
-------------
    1.this code is failed,because,the "wigle.net" is closed.
    2.in fact,now we use ip to search location,so don't worry.
    3.Despite this, we still need to learn how to extract "wifi MAC" and i trust, the following URLs can help you.
        https://blog.csdn.net/weixin_38233274/article/details/80791030
        https://blog.csdn.net/crylearner/article/details/38521685
        https://blog.csdn.net/joeblackzqq/article/details/38960659
Note:
----
    1.the package winreg is in Windows Python.
    2.and this example, I use Python3 in Windows, so this package is "winreg" but "_winreg" in Python2.
    Finally:
        remember, run this code need "Administrator mode" in Windows cmd.
    Try it.!!!
'''


import binascii

def va12addr(val):
    val_list = list(val)
    res_val = ''
    for i in range(len(val_list)):
        if i % 2==0:
            res = ''.join(val_list[i:i+2])
            res_val += res + ':'

    return res_val[:-1]

def printNets():
    net = 'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\NetworkList\\Signatures\\Unmanaged'
    key = OpenKey(HKEY_LOCAL_MACHINE,net)
    print('[*] Networks You have Joined.')

    for i in range(100):
        try:
            guid  = EnumKey(key,i)
            netKey = OpenKey(key,str(guid))
            (name1,value1,type1) = EnumValue(netKey,5)
            print('[+] name: {}, addr: {}, type:{} '.format(name1,value1,type1))
            (name2,value2,type2) = EnumValue(netKey,4)
            print('[+] name: {}, addr: {}, type:{} '.format(name2,value2,type2))

            value1=str(binascii.b2a_hex(value1))[2:-1]
            macAddr = va12addr(value1)   # Python3 返回的是字节，需要字节转16进制,并且valaddr需要改变
            netName = str(name2)
            print('[+] ' + netName + ' ' + macAddr)
            CloseKey(netKey)
        except Exception as e:print(e)

def main():
    printNets()

if __name__ == '__main__':
    main()


'''
HomeWork:
        1. try find 'wifi Mac' map 'GPS' website. and use this website'API to complete the unfinished operation.
        Come On....~~~
'''

