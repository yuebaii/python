#filename = "C:/Users/Administrator/Desktop/class_score.txt"

def average(mylist1, mylist2):
    sums = 0
    for i in range(0,len(mylist1)):
        sums += int(mylist1[i])
    scores = float(sums/len(mylist1))
    print('此班数学成绩平均分为%f'%scores)
    
    sums = 0
    for i in range(0,len(mylist2)):
        sums += int(mylist2[i])
    scores = float(sums/len(mylist2))
    print('此班语文成绩平均分为%f'%scores) 


def findnotok(mylist0, mylist1, mylist2):
	flag = 0
    for i in range(0, len(mylist0)):
        if(int(mylist1[i])<60 and int(mylist2[i])<60):
            print('不及格学生学号为：%d  '%(int(mylist0[i])),'语文%d  '%(int(mylist2[i])),'数学%d'%(int(mylist1[i])))     
            
    if flag == 0:
		 print('没有不及格的学生！')
  
def findveryok(mylist0, mylist1, mylist2):
	flag = 0 
    for i in range(0, len(mylist0)):
        if((int(mylist1[i])+int(mylist2[i]))/2 > 90):
			flag = 1
            print('平均分90以上学生学号为：%d  '%(int(mylist0[i])),'语文%d  '%(int(mylist2[i])),'数学%d'%(int(mylist1[i])))    
            
	if flag == 0:
		print('没有90分以上的学生！')
		
def main():
    filename = "C:/Users/Administrator/Desktop/class_score.txt"
    fp = open(filename)
    
    l0 = []
    l1 = []
    l2 = []
    str1 = fp.readline()
    str1 = fp.readline()
    while(len(str1) != 0):
        lists = str1.split()
        
        l0.append(lists[0])
        l1.append(lists[1])
        l2.append(lists[2])
     
        str1 = fp.readline()

    average(l1,l2)
    findnotok(l0,l1,l2)
    findveryok(l0,l1,l2)

       
if __name__ == "__main__":
    main()
  
