strs = input("请输入单词和中文翻译：")

dic = {}
while(strs != "end"):
    lists = strs.split()
    dic[lists[0]] = lists[1]
    strs = input()

strss = input("请输入单词以翻译英文：")

while(strss != "end"):    
    if strss in dic:
        print(dic[strss])
    else:
        print("您输入的单词不存在,重新输入或退出！")
    strss = input()

