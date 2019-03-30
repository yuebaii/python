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

mht = 0
mlt = 50
mhd = 0
mld = 0
for j in range(len(l1)):
    if(l1[j] > mht):
        mht = l1[j]
        mhd = j
print('这周第%d天最热'%mhd,'最高为%d度'%mht)
for k in range(len(l2)):
    if(l2[k] < mlt):
        mlt = l2[k]
        mld = k
print('这周第%d天最冷'%mld,'最低为%d度'%mlt)

    
    
                
