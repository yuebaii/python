s = input('输入字符串：')

english_num = 0
space_num = 0
number_num =0
others_num = 0

for char in s:
    if char.isalpha():
        english_num = english_num+1
    elif char.isspace():
        space_num = space_num+1
    elif char.isdigit():
        number_num = number_num+1
    else:
        others_num = others_num+1

print(english_num, space_num, number_num, others_num)
