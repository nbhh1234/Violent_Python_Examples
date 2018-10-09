# _*_coding:utf8-

def B(func):  # func == A
    def warp(*args,**kwargs):
        print 'huwang'
        print args,kwargs
        func(*args,**kwargs)  # A(name='yyyy')
    return warp

@B
def A(name):
    print 'hahahah1' + name

A(name='yyyyy')
# @B
# def C():
#     print 'heieheiehi1'
# A()
# C()
#
#
# def b(func):
#     def war():
#         func()
#         print 'lalala2'
#     return war()   # == a()
# def a():
#     print 'hahaha2'
#
# b(a)