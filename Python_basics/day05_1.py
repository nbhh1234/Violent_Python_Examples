# _*_coding:utf8-
def B1(name3):
    def B(func):
        def warp(*args, **kwargs):
            print name3
            print 'hahahah'
            print args
            print kwargs
            func(*args, **kwargs)  # A()

        return warp

    return B


@B1('huwang3')
def A(name, name2):
    print 'lalalal' + name + name2


A(name='huwang', name2='huwang2')


@B1('huwang4')
def C():
    print 'kkkkkk'
