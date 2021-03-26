# 测试数据解析
# BeautifulSoup4 将复杂的HTML文档转换成一个树形结构，每个节点都是 Python对象
# 所有对象可以归纳为4种 :
# Tag
# NavigableString
# BeautifulSoup
# Comment

from bs4 import BeautifulSoup
import re

file = open("./baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")

# 查找第一个标签
print(bs.title)  # <title>百度一下，你就知道</title>
print(bs.title.string)  # 百度一下，你就知道
print(bs.a)  # <a class="toindex" href="/">百度首页</a>
print(bs.head)

print(type(bs.a))  # <class 'bs4.element.Tag'>
print(type(bs.a.string))  # <class 'bs4.element.NavigableString'>

print(bs.a.comment)  # 找到的事注释内容

# --------------------应用--------------------


# 文档的遍历
print(bs.head.contents)

# 文档的搜索

t_list = bs.find_all("a")  # 查找所有a标签
print(t_list)

t_list2 = bs.find_all(re.compile("a"))  # 查找所有a标签
print(t_list2)


# find_all(func) 其实也可以穿入一个方法
def name_is_exists(tag):
    return tag.has_attr("name")


t_list3 = bs.find_all(name_is_exists)  # 查找
print(t_list3)

t_list4 = bs.find_all(id="head")  # 查找id="head"标签
print(t_list4)


t_list5 = bs.find_all(class_=True)  # 查找所有有class的标签
print(t_list4)


t_list6 = bs.find_all(text = ["123","456"])  # 查找所有
print(t_list6)

t_list7 = bs.find_all(text = re.compile("\d"))  # 查找所有
print(t_list7)

t_list8 = bs.find_all("a", limit=3)  # 查找3个a标签
print(t_list8)

t_list9 = bs.select('title')  # 选择器
print(t_list9)

t_list10 = bs.select(".mnav")  # 选择器
print(t_list10)