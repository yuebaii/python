num = 44
nums = 0

while(1):
    nums = int(input('请输入所猜的数:'))
    if(nums > num):
        print('太大了！')
    elif nums < num:
        print('太小了！')
    else:
        print('恭喜你，猜中了！')
        break
