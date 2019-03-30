filename1 = "C:/Users/Administrator/Desktop/score1.txt"
filename2 = "C:/Users/Administrator/Desktop/score2.txt"

fp1 = open(filename1)
fp2 = open(filename2, 'w+')
fp2.write('学号       总评成绩\n')

text = fp1.readline()
text = fp1.readline()
count = 0
l2 = [0,0,0,0,0]
sums = 0
while(len(text) != 0):
  #  text = fp1.readline()
    l1 = text.split()
    score = int(int(l1[1])*0.4+int(l1[2])*0.6)
    fp2.write(l1[0]+"   ")
    fp2.write(l1[1]+'\n')
    if(score >= 90):
        l2[0] += 1
    elif score >= 80:
        l2[1] += 1
    elif score >= 70:
        l2[2] += 1
    elif score >= 60:
        l2[3] += 1
    else:
        l2[4] += 1
    count += 1
    sums += score
    text = fp1.readline()
fp1.close()
fp2.close()
avescore = sums/count
print('班级人数为%d\n'%count, '90分以上%d  '%l2[0],'80-89分%d  '%l2[1],'70-79分%d  '%l2[2],'60-69分%d  '%l2[3],'60分以下%d  '%l2[4])
print('班级总平均分为%d'%avescore)


          
        
