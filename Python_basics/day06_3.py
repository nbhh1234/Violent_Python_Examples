# _*_coding:utf8-

# a = []  # [] list
# b = [1,2,3,4,5,'1',1.0,True,[1,2,3]]
# print b
# c = list('abcgddhdjf') # input iter
# print c

# a1 = [1,20,3,'a']
# b1 = [1,5,6,True]
# print 4 * a1  # just int type
# print a1[2:2] # don't crash,return []
# print len(a1)
# print min(b1)
# # print sum(a1)
# for i in a1:
#     print i
# print a1 < b1

# a2 = [1,2,5]
# b2 = [1,2,3]
# print a2 <= b2

# print [x for x in range(10)]

# a = (x for x in range(10)) # generator-->iter
# print next(a)
# print next(a)


A2 = [1,1,1,1,1,1,2,2,2,2,2,3]

# a2 = []
# for i in A2:
#     if i not in a2:
#         a2.append(i)
# print a2
# print A2.count(1)
#
# A2.extend([[100,200,300]])
# print A2
# for i in [[100,200,300]]:
#     print i
# A3 = [1,2,3]
# # A3.insert(0,'hahaha')  # index,obj
# # print A3
# # A3.remove(3)
# # print A3
# A3.reverse()
# print A3

# sort
# a3 = [0,-1,100,1]
# a3.sort(reverse=True)
# print a3

# a4 = [['liuyanyun',22,['360',100]],['jingjing',12,['baidu',1]],['taotao',-1,['Google',0]]]
# a4.sort(key=lambda x:x[2][1])
# print a4
# for i in a4:
#     print i

# sorted
# a4 = [['liuyanyun',22,['360',100]],['jingjing',12,['baidu',1]],['taotao',-1,['Google',0]]]
# a5 = sorted(a4,key=lambda x:x[2][1])
# print a4
# print a5

# pop
A5 = [1,2,3,'a',True]
pop_ele= A5.pop(0)  # default pop last ele
print pop_ele
print A5

# split
a = 'a,b,c,d'
b = 'a b c d'
print a.split(',')
print b.split(' ')
