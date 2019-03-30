
for num in range(2,1001):
    L1 = []
    i = 1
    sums = 0
    while(i < num):
        if num%i ==0:
            sums += i
            L1.append(i)
        i += 1
            
    if sums == num:
        print('完数为%d因子为'%num,end="")
        for j in range(1,len(L1)):
            print("%d"%L1[j],end=",")
        print('\n')
