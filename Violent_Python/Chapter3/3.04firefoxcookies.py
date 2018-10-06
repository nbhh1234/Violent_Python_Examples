# _*_ coding:utf8-

import sqlite3
'''
This code we learning use sqlite3 package to connect sqlite.
What is sqlite?
---------------
    http://www.runoob.com/sqlite/sqlite-intro.html
Note:
-----
    1.upgrade your sqlite3.
    2.have a SQL is important:'select [ ] from sqlite_master where type="table"'
        and the [ ] can set "sql,table.. and so on"
    3. sqlite_master can Record all operations. so, you can use it to search anything.
    4. run 'find ./ -name "*.sqlite"' in your terminal. then ,return search result.
        use "cd"  to this directory.
        use "sqlite3 xxx.sqlite" enter sqlite environment.
        try SQL in "2."
'''
def printCookies(CookiesDB):
    conn = sqlite3.connect(CookiesDB)
    c = conn.cursor()
    c.execute('SELECT baseDomain,value,host FROM moz_cookies;')
    conn.commit()

    print '[*] ---Files Cookies ---'
    for row in c:
        print 'Name: ' + row[0] + ' Value: ' + row[1] + 'host: ' + row[2]


if __name__ == '__main__':
    printCookies('/root/.mozilla/firefox/3tiw8wev.default/cookies.sqlite')


'''
HomeWork:
        1. try other sqlite, using this code.
        2. find all history website in your Firefox and write your computer.
            Friendly Reminder:"moz_places"
        3. try connect 'Mysql' and perform "add, delete, change,search".
            Reminder:using 'pymysql' package.
'''