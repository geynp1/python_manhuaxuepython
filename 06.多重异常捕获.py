# 解决除零异常
i = input('请输入数字:')
n = 8888

try:
    result = n / int(i)
    print(result)
    print('{0}除以{1}等于{2}'.format(n,i,result))
except (ZeroDivisionError,ValueError) as e:
    print("异常发生:{}".format(e))
