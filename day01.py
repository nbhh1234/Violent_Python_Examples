'''
# num = 1000 or num = "hahah" and so on ....
# 
num = raw_input(">>") # return str type, raw_input == input(python3), its input,
int_num = int(num) #int :: change to int type,it's class type inpython
float_num = float(num) # change to float
aera = int_num * int_num * 3.14

print(aera)'''
'''
width,height = 100,50 
print(width,height)
area = width * height
'''
# EP:1
'''
time_ = int(raw_input(">>"))# change int,raw_input returns string.
min_ = time_ // 60 # get mins
times = time_ % 60 # get times
print(min_,times)'''
'''
# EP:2
x,y,a,b,c = 1,1,0,0,0
part1 =( 3 + 4 * x) / 5
part2 = 10 * (y-5) * (a + b + c )/ x
part3 = 9 * ((4/x) + (9+x)/y)

res = part1 - part2 + part3
print(res)
'''

a,b = eval(raw_input('>>'))
print(a,b)

