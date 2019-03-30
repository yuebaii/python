hour,minute,second = input('please input time（h:m:s):').split(':')
hour = int(hour)
minute = int(minute)
second = int(second)

second += 30
if(second >= 60):
    second -= 60
    minute += 1
minute += 5
if(minute > 60):
    minute -= 60
    hour += 1
if(hour == 24):
    hour = 0

print('time is',hour,':',minute,':',second)


