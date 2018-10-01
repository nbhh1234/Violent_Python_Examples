# _*_ coding:utf8-
'''
print('GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOd')
a = raw_input('>>')
print(a)
# python day03.py > test.txt   output
# python day03.py < test.txt   input if you have "raw_input() or input()" code
'''

# 1 method:: open()
# Python3
'''
path = 'testJoker.txt'
file_ = open(path,'w',encoding = 'utf8')
file_.write('Joker is a good man')
file_.close()  close the file ,must !!!!

'''
'''
# 2. with opne()  as f:
path = 'testJoker.txt'
with open(path,'w',encoding='utf-8') as Joker:
    Joker.write('Joker is a bad man')
'''
#Homework 8
'''
text = '''
#good 
#bad
#good bad
'''
new_text = ''
for i in text:
    new = chr(ord(i)+1)
    new_text = new_text + new
print(new_text)
with open('textJoker.txt','w') as f:
    f.write(new_text)

'''
'''
while 

while condition:
    do something!!
while 1:
    print('Good')
'''
'''
i = 0
while i  < 10:
    print('Good')
    i +=1
'''
'''
for i in 'abcgd':
    print(i)
'''
'''
a = 'abcgd'
i = 0
while i < 5:
    print(a[i])  # index get elements
    i += 1
'''
# EP1
'''
import random
num = random.randint(1,5)
input_num = int(raw_input('input>>'))
if num == input_num:
    print('Good')
else:
    while num != input_num:
        input_num = int(raw_input('again:>>'))
        if num == input_num:
            print('Good')
        else:
            print('Error')
--------------------------------
import random
num = random.randint(1,5)
whlie 1:
    input_num = int(raw_input('>>'))
    if num == input_num:
        print('Good')
        break
'''
'''
# range(a,b,setp)  [a,b)
for i in range(1,10,2):
    print('Good')
'''
# [x for x in range(1,10)]
'''
EP2
i = 0
sum_ = 0
while i < 1001:
    sum_ +=i
    i +=1
'''


'''
def function_name():
    do something
'''
'''
def test():
    print('hahahah')
if __name__ == "__main__":
    test()
'''

def test2(name):
    print(name)
