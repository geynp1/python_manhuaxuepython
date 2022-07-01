# 替换符号lambda表达式
def calc(opr):
    if opr == '+':
        return lambda a,b:(a+b) # 替代add()函数
    else:
        return lambda a,b:(a-b) # 替代sub()函数

f1 = calc('+')
f2 = calc('-')
print("10 + 5 = {0}".format(f1(10,5)))
print("10 - 5 = {0}".format(f2(10,5)))

# lambda的过滤函数
data1 = [66,15,91,28,98,50,7,80,99]

filtered = filter(lambda x:(x>50),data1)
data2 = list(filtered)
print(data2)

mapped = map(lambda x:(x*2),data1)
data3 = list(mapped)
print(data3)