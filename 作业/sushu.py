num = int(input())
w = 0
i = 2

while((i <= num**0.5) and w==0):
    if(num%i != 0):
        i = i+1
    else:
        w = 1

if(w == 0):
    print(num,'是素数')
else:
    print(num,'不是素数')
        
