# -*- coding: utf-8 -*-

import re

# str( )是python自带函数，是python保留的关键字，定义变量时应该避免使用str作为变量名
# 如果在使用str( )函数之前已经定义过str变量，则会出现TypeError: ‘str’ object is not callable这个报错
strTest = "imooc python imooc"

# ----------------------------一些实例----------------------------
# []     匹配需要的字符集合
# [^abc] 表示非a或非b或非c
# .      表示匹配除\n外的任意字符 ,当匹配模式为re.S时，.表示匹配包括\n的任意字符
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

# abc*  表示*号前面一个字符的0次或无限次扩展 比如这里表示ab,abc,abcc,abccc
# abc+ 表示+号前面一个字符的1次或无限次扩展 比如这里表示abc,abcc,abccc
# abc? 表示?号前面一个字符的0次或1次扩展 比如这里表示ab,abc
# abc|def 表示左右任意一个

# (abc | def) 分组标记 表示abc,def ()里面只能用|
# \w 单词字符 等价于[A-Za-z0-9_]


# 更多示例可以参考一个博客：史上最全正则表达式


# ----------------------------re使用步骤----------------------------
# r表示原字符串 re.I表示匹配模式忽略大小写
# re.M 多行模式
# ...
pattern = re.compile(r'imooc\n')  # r表示原字符串 不存在转义
ret = pattern.match(strTest)
print(ret)  # None

# ----------------------------re常用函数----------------------------
# re.search()  在一个字符串中搜索匹配正则表达式的第一个位置 返回match对象
# re.match() 从一个字符串的开始位置起匹配正则表达式 返回match对象
# re.findall() 搜索字符串 以列表类型返回全部能匹配的字串
# re.split()  将一个字符串按照正则表达式匹配结果进行分割 返回列表
# re.finditer() 搜素字符串 返回一个匹配结果的迭代类型 每个迭代元素是match对象
# re.sub() 在一个字符串中替换所有匹配正则表达式的字串 返回替换后的字符串


# ----------------------------re.match函数 和 pattern.match函数----------------------------
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# re.match(pattern, string, flags=0)
# 如果是pattern.match(string, 开始位置, 结束位置)


pattern1 = re.compile(r'(imooc)', re.I)
ret1 = pattern1.match(strTest)
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
s = "A23G4HFD567"


def double(matched):
    print(matched)  # <re.Match object; span=(1, 3), match='23'>
    print(matched.group()) #23
    print(matched.groups()) #('23',)
    value = int(matched.group('value'))
    print(value)
    return str(value * 2)


print(re.sub('(?P<value>\d+)', double, s))

# 更多re.sub相关：https://blog.csdn.net/mrzhoug/article/details/51585615

print(re.findall(r'[0-9]', s))
# ?P<type>, type是匹配的组名，方便用matched.group(type)获取
# 找出所有的大写字母
print(re.findall("[A-Z]", "AHDISHABCasjdkasjdHHHHJC"))
