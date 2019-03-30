a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if(a >= b):
    if(a > c):
        print('a是最大数')
    else:
        print('c是最大值')
else:
    if(b > c):
        print('b是最大数')
    else:
        print('c是最大值')
