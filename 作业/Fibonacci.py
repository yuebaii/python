'''
def Fibonacci(items):
    if(items <= 2):
        return 1
    return Fibonacci(items-1)+Fibonacci(items-2)
'''


def Fibonacci(items):
    num1 = 1
    num2 = 1
    num3 = 1
    i = 3
    while i<=items:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        i = i+1
    return num3

if __name__ == '__main__':
    items = int(input('请输入项数：'))
    print('第%d项和为:%d,'%(items,Fibonacci(items)),'时间复杂度为O(n)')



