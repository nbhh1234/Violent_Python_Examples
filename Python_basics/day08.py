# import random
# def youhuiquan():
#     list_ = [1,2,3,4,5,6,7,8,9,0,10,11,12,13]
#     list_2 =['红桃','黑桃','梅花','方块']
#     rest_list = []
#     count = 0
#     while len(rest_list) != 4:
#         count +=1
#         random_1 = random.randint(0,12)
#         random_2 = random.randint(0,3)
#         if list_2[random_2] not in rest_list:
#             print('获得牌: {}{}'.format(list_2[random_2],list_[random_1]))
#             rest_list.append(list_2[random_2])
#     print('Pick: '+ str(count))
# youhuiquan()
#
# import random
#
#
# def shuffle(lst):
#     # 创建一个新的列表
#     rest_list = []
#     #     count = 0
#     #     while len(rest_list) != len(lst):
#     #         count +=1
#     #         index = random.randint(0,len(lst)-1)
#     #         if lst[index] not in rest_list:
#     #             rest_list.append(lst[index])
#     #     print(rest_list,count)
#
#     # For + pop
#
#     for i in range(len(lst)):
#         print(len(lst))
#         index = random.randint(0, len(lst) - 1)
#         res = lst.pop(index)
#         rest_list.append(res)
#     print(rest_list)
#
#
# shuffle([1, 2, 3, 4, 5])
#
# a = 1235555
#
# a = 1235555
#
#
#
# def isConsecutiveFour(values):
#     values_list = list(str(values))  # [1,2,3,5,5,5,5] [1,2,3,2,4,2,6,2]
#     if len(values_list) >= 4:
#         for i in range(len(values_list) - 3):
#             if values_list[i] == values_list[i + 1] and values_list[i] == values_list[i + 2] and values_list[i] == values_list[i + 3]
#                 print('成功')
#                 break
#     else:
#         print('失败')
#
#
#
