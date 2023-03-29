"""
  字符串有多种表现形式，用单引号（'……'）或双引号（"……"）标注的结果相同 2。反斜杠 \ 用于转义
"""

print("\"Yes,\" they said.")

# 如果不希望前置 \ 的字符转义成特殊字符，可以使用 原始字符串，在引号前添加 r 即可：
print('C:\some\name') # 出现换行
print(r'C:\some\name') # C:\some\name

# 字符串字面值可以包含多行。 一种实现方式是使用三重引号："""...""" 或 '''...'''。
print('ttt\naaa\nerror'); # 出现换行
print('字符串字面值可以包含多行。 一种实现方式是使用三重引号："""...""" 或 \'\'\'...\'\'\'。');
print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""") # 出现换行
# 字符串中将自动包括行结束符，但也可以在换行的地方添加一个 \ 来避免此情况：
print("""\
Usage: thingy [OPTIONS]\
     -h                        Display this usage message\
     -H hostname               Hostname to connect to\
""") # Usage: thingy [OPTIONS]     -h                        Display this usage message     -H hostname               Hostname to connect to

# 字符串可以用 + 合并（粘到一起），也可以用 * 重复：
print('I ' + 'am ' + 't' * 3) # I am ttt

# 相邻的两个或多个 字符串字面值 （引号标注的字符）会自动合并：
print('相邻的两个或多个 字符串字面值 （引号标注的字符）会自动合并：');
print('I am ''a developor') # I am a developor
# 拼接分隔开的长字符串时，这个功能特别实用：
text = ('Put several strings within parentheses '
  'to have them joined together.')
print(text) # Put several strings within parentheses to have them joined together.
# 这项功能只能用于两个字面值，不能用于变量或表达式：
p = 'py'
# p 'thon' # SyntaxError: invalid syntax
t = 'thon'
# p t # SyntaxError: invalid syntax
# 合并多个变量，或合并变量与字面值，要用 +：
print(p + 'thon') # python
print(p + t) # python

# 字符串支持 索引 （下标访问），第一个字符的索引是 0。单字符没有专用的类型，就是长度为一的字符串：
s = 'abcdefg'
c = 'a'
print(s[0]) # a
print(c[0]) # a
# 索引还支持负数，用负数索引时，从右边开始计数：
print(s[-1]) # g
print(c[-1]) # a
# 注意，-0 和 0 一样，因此，负数索引从 -1 开始。

# 字符串还支持 切片。索引可以提取单个字符，切片 则提取子字符串：
print('字符串还支持 切片。索引可以提取单个字符，切片 则提取子字符串：')
w = 'Python'
print(w[0:2]) # Py
print(w[0:5:2]) # Pto
print(w[:2]) # Py
print(w[2:]) # thon
print(w[-1]) # n
print(w[-2]) # o
print(w[-2:]) # on
# 索引越界会报错：
# print(w[42]) # IndexError: string index out of range
# 切片会自动处理越界索引：
print('切片会自动处理越界索引：')
print(w[:42]) # Python
print(w[42:]) # 空

#Python 字符串不能修改，是不可变对象（immutable）的。因此，为字符串中某个索引位置赋值会报错：
# w[2] = 'O' # TypeError: 'str' object does not support item assignment
# 要生成不同的字符串，应新建一个字符串：
w2 = w[0:2] + 'O' + w[3:]
print(w2)

# str.swapcase()返回原字符串的副本，其中大写字符转换为小写，小写字符则转换为大写。
print('str.swapcase()返回原字符串的副本，其中大写字符转换为小写，小写字符则转换为大写。');
s = 'I am HelloWorld!'
print(s.swapcase()); # i AM hELLOwORLD!

# str.title()返回原字符串的标题版本，其中每个单词第一个字母为大写，其余字母为小写。
print('str.title()返回原字符串的标题版本，其中每个单词第一个字母为大写，其余字母为小写。')
print(s.title())
