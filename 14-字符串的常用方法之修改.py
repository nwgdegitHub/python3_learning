# str.replace(oldStr,newStr,count)

mystr = " my name is Liu Wei,My age is 30, My name is LW "
print(mystr.replace("name","name2",3))

print("split()分割 返回一个列表")
print(mystr.split("is",2)) #前2个生效

print("join()合并列表里面的元素为一个大字符串")
mylist = ["aa","bb","cc","dd"]
print("...".join(mylist))

print("title()将字符串每个单词的首字母转成大写")
print(mystr.title())

print("capitalize()将字符串首个单词的首字母转成大写")
print(mystr.capitalize())

print("lower()将字符串中大写转小写")
print(mystr.lower())

print("upper()将字符串中小写转大写")
print(mystr.upper())

print("lstrip()删除左侧空白字符")
print(mystr.lstrip())

print("rstrip()删除右侧空白字符")
print(mystr.rstrip())

print("strip()删除开头结尾空白字符")
print(mystr.strip())

print("str.ljust(length,char) 使左对齐 不够补齐")
print(mystr.ljust(60,"."))

print("str.rjust(length,char) 使右对齐 不够补齐")
print(mystr.rjust(60,"*"))

print("str.rjust(length,char) 使右对齐 不够补齐")
print(mystr.rjust(60,"*"))

print("str.center(length,char) 居中对齐 不够补齐 默认补齐空格")
print(mystr.center(60,"*"))

print(mystr.startswith(" my",0,100)) #在0～100范围内 是否以 my开头
print(mystr.endswith("my",0,100))

str2 = "123"
print(str2.isalpha())
print(str2.isdigit())
print(str2.isalnum())




