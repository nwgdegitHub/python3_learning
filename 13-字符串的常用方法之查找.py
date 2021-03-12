# str.find(subStr,startIndex,endIndex)

mystr = "My name is Liu Wei,My age is 30"

print("find()")
print(mystr.find("apple"))  # -1
print(mystr.find("name"))  # 3
print(mystr.find("Wei"))  # 15

# str.index(subStr,startIndex,endIndex)

print("index()")
print(mystr.index("name"))
# print(mystr.index("name",5,10)) #ValueError: substring not found

print("rfind()从右侧开始查")
print(mystr.rfind("name"))  # 3

print("rindex()从右侧开始查")
print(mystr.rindex("name"))  # 3

print("count()字串出现的次数")
print(mystr.count("is"))  # 2
