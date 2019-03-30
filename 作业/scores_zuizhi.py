def calcute_score(l1, l2):
    num_max = 0
    num_min = 0
    max = 0
    min = 100
    for i in range(0, len(l2)):
        if(int(l2[i]) >= max):
            max = int(l2[i])
            num_max = int(l1[i])
        if(int(l2[i]) <= min):
            min = int(l2[i])
            num_min = int(l1[i])

    print("总评成绩最高的同学学号是%d：分数为%d"%(num_max, max))
    print("总评成绩最低的同学学号是%d：分数为%d"%(num_min, min))
    print("时间复杂度为O(n)")

if __name__ == '__main__':
    fd = open("C:/Users/Administrator/Desktop/score2.txt.txt")
    strs = fd.readline()
    strs = fd.readline()
    l1 = []
    l2 = []

    while len(strs) != 0:
        l3 = strs.split()

        l1.append(l3[0])
        l2.append(l3[1])

        strs = fd.readline()
    calcute_score(l1, l2)


