# _*_ conding:utf8-
'''
# 如果要有默认参数，那么一定统一塞到最后面
def test(name1,name2='Joker',name3='Joker2'):
    print(name1,name2,name3)
test('h','h','j')


# * 强制命名,*后面的所有参数，在传参过程中必须要带上
# 参数名防止传参错误
def NB(name1,*,name2='Joker',name3='Joker2'):
    print(name1,name2,name3)
#  1. 位置参数，可以不带参数名
#  2. 带参数名的传参方式
NB('Joker3',name2='hahah',name3='heihei')

# 匿名函数,装逼函数,只能完成一些简单的问题
# : 前面，是装逼函数的输入量，后面是装逼函数的输出量
func = lambda x,y,z=1000:print(x+y+z)
func(100,100)
# 装逼函数完全体
(lambda x,y,z=1000:print(x+y+z))(100,100)

# 不定长参数 *args  下水道::你来多少，我装多少
# * 只是一个标示，意味着后面的参数是一个不定长参数,所以args可以更改成别的你喜欢的参数名
# 但是约定俗成的是args
# 传参的方式是：单个元素，不能带参数名
def AGS(*args):
    print(args)  # 返回的叫元组
# AGS(1,2,3,4,5,7,89,0,43,2,4,67,8,5,123,1,231)
# ---------------------
# ** 也是一个标示，所以kwargs也是可以更换的，但是约定俗成是kwargs
# 传参形式一定要是带参数名的(实际上是一个键值对)
# 返回的是一个字典
def KWargs(**kwargs):
    print(kwargs)
# KWargs(a = '100',b = 100,c = True)

# 终极用法在Python中,完整的不定长函数
#----------------
def argsKw(*args,**kwargs):
    print(args)
    print(kwargs)
# 全局变量 Mist
# 使用全局变量的时候，必须要声明全局变量，
# 否则无法更改全局变量
Mist = 0
def test4():
    global Mist
    Mist += 10
    print(Mist)

test4()
print(Mist)
globals()   #返回运行开始到现在为止所有的全局变量表
locals()  # 返回运行开始到现在为止所有的局部变量表

'''
