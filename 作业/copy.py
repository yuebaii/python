filename1 = "C:/Users/Administrator/Desktop/sample12.txt"
filename2 = "C:/Users/Administrator/Desktop/sample12_copy.txt"
fp1 = open(filename1, "r+")
fp2 = open(filename2, "w+")

str1 =fp1.readline()
while(len(str1) != 0):
    
    str2 = str1.upper()
    fp2.write(str2)
    
    str1 =fp1.readline()
        
fp1.close()
fp2.close()
    
