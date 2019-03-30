filename = "C:/Users/Administrator/Desktop/temp.txt"
fp = open(filename)

ht = fp.readline()
l1 = list(ht.split())
lt = fp.readline()
l2 = list(lt.split())

fp.close()

for i in range(len(l1)):
    l1[i] = int(l1[i])
    l2[i] = int(l2[i])

dat = 0
wat = 0
tem = 0
n = 0

for j in range(len(l1)):
    dat = (l1[j]+l2[j])/2
    if(dat > 10):
        n += 1
    tem += dat
    
wat = tem/7
print('全周平均气温是%d'%wat,'度')
if(n >= 5):
    print('上海已入春')
else:
    print('上海未入春')

