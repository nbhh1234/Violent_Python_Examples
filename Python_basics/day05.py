# _*_coding:utf8-

# class
# simple class
# class Joker:
#     print '[+] Joker is a good man'

# initialize class
class joker:
    # initialization,"self",initialization class joker or "yourself"
    # actually, self can be changed, but default using "self"
    # enjoin local variables
    def __init__(self):
        self.shuai = 'lalalal'  # self, means: shuai is joker classes self variable.
        self.chou = 'hahahah'
    def fuc(self):  # self, fuc function is joker class
        print self.shuai
        print self.chou

    '''
    if "self" in __init__(),means: initialization joker self
    if "self" in variable, means: this variable is joker class,else not in joker class
    if "self" in function,means: this function is joker class
    '''
class ep1:
    def __init__(self):
        self.num = 10000
    def check(self):
        if self.num % 2 == 0:
            print '[+] ou'
        else:
            print '[+] ji'




class ep2:
    def __init__(self,num):
        self.num = num
        print '[+] init over!'
    def num_2(self,b):
        # NUM2 = self.num ** 2  # NUM2 is in num_2 function,not in __init__
        # self.num = NUM2
        self.num = self.num ** 2  + b
        print self.num
        print b
    def num_3(self):
        self.num = self.num ** 3
        print self.num

if __name__ == '__main__':

    # "()" means running __init__(self)
    huwang = ep2(1)
    huwang.num_2('num_2 very handsome')
    huwang.num_3()
