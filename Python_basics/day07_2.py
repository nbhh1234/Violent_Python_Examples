# _*_coding:utf8-

# Tuple
# a = ()
# print type(a)
# b = (1,2,3,4,'a','b',True,(1,2,3))
# print b
# b1 = [1,2,3,4]
# b1[0] = 100
#
# b2 = (100,200)
# print b[:-1]
# print tuple([x for x in range(10)])
# # str,list,tuple
#
# # b3 = (1,2,4,'a')
# # print sum(b3)
# print (1,2,3) < (1,3,22)
# a = (1,)
# # set
# b = {1,2,3}
# b1 = set([1,2,3,5,6])
# b2 = set()
# print type(b2)
# for i in b:
#     print i
#
# b3 = [1,1,1,2,2]
# b3 = set(b3)
# print list(b3)

# a_1 = {1,2,3,4,'a'}
# # a_1.add('100')
# # print a_1
# a_1.remove(1)
# a_1.discard(100)  # if ele not in set ,don't crash but remove crash
# print a_1

# a_2 = {1,2,3}
# a_3 = {2,1}
# print a_2 > a_3

# dictionary,veli zhongyao
# key: single ele
# value: sui,bian
# suxu !!!
# 一切操作都要通过键名操作键值
a = {'key':'value',100:100,19:{1,2},'dict':{1,2}}  # key-value
# print a
# print a['key'],a[1]
# b = {'key':'value','key':'VALUE'}
# print b['key']

# get value
print a['key']
# xiu,gai
a['key'] = 100
print a
# delete
# del a['key']
# print a
# len() -- > number of keys
print len(a)

# == !=  ---> key and value
#>,<,>=,<= Python2 OK,Python3 no OK
# 先比字典长度，若相等就比 key 值，若再相等就比 value。
# a2 = {2:1000,3:200}
# a3 = {2:100,3:200}
# # print a2 == a3
# print a2 < a3

# keys
a1 = {'1':1,'2':2,'aa':{1,2}}
# print a1.keys()
# for i in a1:  # return keys
#     print i
#
# for i in a1.keys(): # for i in ['1', 'aa', '2']:
#     print i

# values
# print a1.values()
# for i in a1.values():  # in fact,for loop "[]"
#     print i

# item  return [(key,value)]
# for i in a.items():
#     print i

# for i,j in a.items():  # i,j = (a,b)
#     print i,j

# get
# print a['bb']
# print a.get('bb','Joker') # get(key,obj) if get return value,else return obj,obj default None
# print a.get('bb',[1,2,3])

# pop
# print a1.pop('aa')
# print a1

# popitem
# print a1.popitem()
# add key - value
a2 = {}
a2['Joker'] = 100
print a2