# 解决除零异常
i = input('请输入数字:')
n = 8888

try:
    i2 = int(i)
    try:
        result = n / int(i2)
        print('{0}除以{1}等于{2}'.format(n,i2,result))
    except ZeroDivisionError as e1:
        print("不能除以0，异常:{}".format(e1))
except (ZeroDivisionError,ValueError) as e2:
    print("输入的是无效数字，异常:{}".format(e2))
