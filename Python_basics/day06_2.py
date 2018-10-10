# _*_coding:utf8-

# a ='haha'
#
# # max Method1: input iter,method2: single args
# print max(a)
# print max('1','2','a','b') # ASCII value
# print min(a),min('1','2','a','b')

# c = 'Joker'
# print c[-1]   # -1 equals len(c) - 1
# print c[-2]
# print c[2],c[-3]
# print c[0:2]   # [star:end,[step])
# print c[-3:-1],c[2:4]
# print c[0:],c[:]   # ":" last element
# print c[::-1]  # reverse c
# print c[-5:]

a = 'Joker '
b = 'is a bad man ~~~'
print a + b # a plus b
print ''.join((a,b))  # pra:: iter,"()" tuple.
'''
for i in (a,b):
    i = a
    i = b
    res = a + '' + b
'''
print '!'.join(a)   #!Joker
'''
for i in a:
    i = J
    i = o
    i = k.....
    res = i + '!' + i + '!' + i
'''
# EP1:
url = 'http://www.baidu.com/?page=?wd=xiaopangzi' # GET
# for i in range(100):
#     part1 = 'http://www.baidu.com/?page='
#     res = part1 + str(i) + '?wd=xiaopangzi'
#     print res
# i = 0
# while i < 100:
#     part1 = 'http://www.baidu.com/?page='
#     res = part1 + str(i) + '?wd=xiaopangzi'
#     print res
#     i +=1


a = 'abcEdda'
print   a.endswith('cd')
print a.startswith('ab')
print a.find('dd')  # return index (first element index)
print a.rfind('a') # return index (right find, left index)
print a.find('e')  # No find !  return -1
print a.lower()  # lower
print a.upper() # upper
print a.replace('a','S')  # replace
print a.strip('da')  # strip
print a.strip()  # strip " " a.strip(' '), left and right

aa = 'joker aa joker joker aaa '
print aa.strip('a')
print aa.rsplit(' ')
print aa.lstrip(' ')
print aa.replace(' ','')