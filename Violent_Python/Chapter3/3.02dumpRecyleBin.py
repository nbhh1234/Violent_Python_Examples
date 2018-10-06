# _*_ coding:utf8-

import os
from winreg import *

'''
This code we learning "How to find files and user in Trash" with Windows System.

Docstring:
---------
we build three function in this code:
    1.returnDir:
        this function,we will find difference trash path in different Windows system,
        for example,  Windows 98 system the trash path is "C:\Recycled", Windows 7 and Windows 10 is 
        "C:\$Recycle.Bin\"..
        Once we find it,then we use next function "findRecycled".
    2.findRecycled:
        this function,we views  directory in we found trash path.
        actually,this directory is Unique ID in our Windows system.we can call it "SID".
        then,we can use SID to find true user in regedit's ProfileImagePath.
        of course,we can use SID to find "delete files" using "os.listdir()"
    3.sid2user:
        this function, we using SID to search true user.
        same as before, "OpenKey()" function can open "regedit" in Windows, and find target path.
        This example, target path is "ProfileImagePath"
        
Note:
-----
    if your windows system in virtual machine, then, you will same as mine,the true trash path is
    "\\vmware-host\", and "CMD" not support this path.
    
Anyway, Good Luck. :)
    
'''


def sid2user(sid):
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, 'SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList' + '\\' + sid)
        (value, type) = QueryValueEx(key, 'ProfileImagePath')
        user = value.split('\\')[-1]
        return user
    except:
        print('[-] File Does Not Exist: ' + sid + ' It will skip.')
        return None


def returnDir():
    dirs = ['C:\\Recycler\\', 'C:\\Recycled', 'C:\\$Recycle.Bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            print('[+] Found Dirs: ' + recycleDir)
            return recycleDir

    return None


def findRecycled(recycleDir):
    dirList = os.listdir(recycleDir)
    for sid in dirList:
        files = os.listdir(recycleDir + sid)
        user = sid2user(sid)
        if user is not None:
            print('[*] Listing Files For User: ' + str(user))
            for file in files:
                print('[+] Found File: ' + str(file))


def main():
    recycledDir = returnDir()
    findRecycled(recycledDir)


if __name__ == '__main__':
    main()
