# _*_coding:utf8-

def checkISBN(str_):
    str_list = list(str_)
    SUM = 0
    for i in range(len(str_list)):
        if i % 2 == 0:
            res = int(str_list[i]) * 3
        else:
            res = int(str_list[i])
        SUM += res

    RES = 10 - SUM % 10
    if RES == 10:
        RES = 0
    print(RES)

str_ = input('>>')
checkISBN(str_)

def checkCard(card_num):
    card_list = list(card_num) # 将字符串转为列表方便计算
    Res = 0
    Res_2 = 0
    for i in range(len(card_list)):
        res = int(card_list[i]) * 2  # 将所有位数*2
        if res >= 10:
            res_1 = res % 10  # 拿到的个位
            res_2 = res // 10# 拿到的十位
            res_3 = res_2 + res_1
            Res += res_3
        else:
            Res += res

        if i % 2 !=0: # 加和所有奇数位置
            Res_2 += int(card_list[i])

    RES = Res + Res_2
    if RES % 10 == 0:
        print('合法')
    else:
        print('不合法')
card_num = '438857601840707'
checkCard(card_num)
# Deepcopy
# http://www.pythontutor.com/visualize.html#mode=display
import copy
a = [100,1,2,3,[1000,200]]
b =copy.deepcopy(a)
print(b)
a[4][0] = -1
print(b)