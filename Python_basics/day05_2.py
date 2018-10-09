# _*_coding:utf8-

class mayun:
    def __init__(self):
        self.__caichan = 10000000000
    def __showmayun(self):
        print '[+] mayun',self.__caichan

class mahuateng:
    def __init__(self):
        self.cai = 50
    def showmahuateng(self):
        print self.cai
# Web !
class huwang(mayun,mahuateng):  # 告诉Python我即将要继承马云
    def __init__(self):
        mayun.__init__(self) # 马云的证明
        mahuateng.__init__(self)
        # self.caichan = 100000000
        self.huwang = 10
    # def showmayun(self):
        # print '[+] mayun',self.caichan
    def showhuwang(self):
        print '[+] huwangcaichan',self._mayun__caichan

huwang()._mayun__showmayun()
print dir(mayun())

# _classname__var(funcname)