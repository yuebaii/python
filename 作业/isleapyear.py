years = int(input())

if((years%4==0 and years%100!=0) or (years%400==0)):
    print(years, '是闰年')
else:
    print(years, '不是闰年')
