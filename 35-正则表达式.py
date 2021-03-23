import re

str = "imooc python imooc"

# ----------------------------一些实例----------------------------
# []     匹配需要的字符集合
# .      表示匹配除\n外的任意字符
# [.\n]    要匹配包括 '\n' 在内的任何字符
# *      0个，1个，多个
# [0-9]+ 多个(至少1个)
# [0-9]  1个

# ^abc      开头 [^] 写在方括号里面表示匹配相反的 例如[^0-9]表示匹配任意非数字
# abc$      结束
#
# ^[a-z0-9_-]{3,15}$  这里{3,15}表示3-15个字符

# a{2}      表示匹配a出现2次
# a{3,}     表示匹配a至少出现2次


# ----------------------------re使用步骤----------------------------
# r表示原字符串 re.I表示匹配模式忽略大小写
# re.M 多行模式
# ...
pattern = re.compile(r'imooc\n')  # r表示原字符串
ret = pattern.match(str)
print(ret)  # None

# ----------------------------re.match函数 和 pattern.match函数----------------------------
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# re.match(pattern, string, flags=0)
# 如果是pattern.match(string, 开始位置, 结束位置)


pattern1 = re.compile(r'(imooc)', re.I)
ret1 = pattern1.match(str)
print(ret1.groups())  # ('imooc',)

# ----------------------------匹配手机号码？----------------------------
# 1.都是数字 2.长度为11 3.第一位是1 4.第二位是35678中的一位

phone_pattern = re.compile(r'1[3456789]\d{9}')
# \d 表示匹配任意数字，等价于[0-9] 所以\d{9}此处表示9个任意数字
# \D 表示匹配任意非数字，等价于[^0-9]
# \\d 表示匹配\d本身
phone_ret = phone_pattern.match("18856425363")
print(phone_ret.group())  # 18856425363

# ----------------------------re.match与re.search的区别----------------------------
# re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，而 re.search 匹配整个字符串，直到找到一个匹配。
line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")


# ----------------------------检索和替换----------------------------
# re.sub用于替换字符串中的匹配项
# re.sub(r'',替换的字符串，也可为一个函数,要被查找替换的原始字符串)
phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)


# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))


