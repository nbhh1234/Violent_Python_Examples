# # _*_coding:utf8-
#
# # Ep1:
# class Account:
#     '''
#     Implement XXXXXXXX..
#     function:
#     --------
#         1.getMonthlyIntersetRate():
#             asdfsdfasjhgkasj
#         Return xxxxx
#         2.getMonthlyInterset():
#             sdfasdf
#     Note:
#     -----
#         1.axxxxx
#         2.xxxxxx
#     Expansion:
#     ----------
#         1.dcccsss
#     '''
#
#     def __init__(self, id_=0, balance=100, annualInterstRate=0):
#         self.id_ = id_
#         self.balance = balance
#         self.annualInterstRate = annualInterstRate / 100
#
#     def getMonthlyIntersetRate(self):
#         MonthlyIntersetRate = self.annualInterstRate / 12
#         print(MonthlyIntersetRate)
#
#         return MonthlyIntersetRate
#
#     def getMonthlyInterset(self):
#         MonthlyIntersetRate = self.getMonthlyIntersetRate()
#         MonthlyInterset = self.balance * MonthlyIntersetRate
#         print(MonthlyInterset)
#
#     def withdraw(self, Money):
#         if Money < self.balance:
#             print('[+] withdraw {}'.format(Money))
#             self.balance -= Money
#             print('[+] balance: ' + str(self.balance))
#         else:
#             print('[-] No Money !')
#
#     def deposit(self, Money):
#         self.balance += Money
#         print('[+] balance: ' + str(self.balance))
#
# accoune = Account(id_=1112, balance=20000, annualInterstRate=4.5)
# accoune.deposit(10000)
#
# #Ep2
# class Fan:
#
#     def __init__(self, speed, radius, color, on):
#         self.__speed = speed
#         self.__radius = radius
#         self.__color = color
#         self.__on = on
#
#     def show(self):
#         print('[+] speed: ', self.__speed)
#         print('[+] radius: ', self.__radius)
#         print('[+] color: ', self.__color)
#         print('[+] on: ', self.__on)
#
# #EP3
# class RegularPloygon:
#     def __init__(self, n=3, side=1, x=0, y=0):
#         self.__n = n
#         self.__side = side
#         self.__x = x
#         self.__y = y
#
#     def getPerimeter(self):
#         print('[+] Perimeter: ' + str(self.__n * self.__side))
#
#     def getArea(self):
#         import math
#         area = (self.__n * math.pow(self.__side, 2.0)) / (4.0 * math.tan(math.pi / self.__n))
#         print('[+] Area is : ', area)
#
# #Ep4
# class LinearEquation:
#     def __init__(self, a, b, c, d, e, f):
#         self.__a = a
#         self.__b = b
#         self.__c = c
#         self.__d = d
#         self.__e = e
#         self.__f = f
#         if self.__a * self.__d - self.__b * self.__c == 0:
#             print('[-] 该方程无解')
#             exit(0)  # 无报错结束当前脚本
#
#     def isSolvable(self):
#         print('[+] True')
#
#     def getX(self):
#         x = (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
#         print('[+] X: ', x)
# #EP5
# class Test:
#
#     def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#         self.x3 = x3
#         self.y3 = y3
#         self.x4 = x4
#         self.y4 = y4
#
#     def Result(self):
#         # Method1:
#         # k1x + b1y + c1 = 0  (x1,y1,x2,y2)
#         # k2x + b2y + c2 = 0  (x3,y3,x4,y4)
#
#         # Method2:
#         # (y - y1)/(y1- y2) = (x - x1)/ (x1- x2)
#
#         k1 = (y1 - y2) / (x1 - x2)
#         k2 = (y3 - y4) / (x3 - x4)
#         if k1 == k2:
#             print('[+] 没有交点')
#         else:
#             X =
#
