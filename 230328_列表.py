"""
  Python 支持多种 复合 数据类型，可将不同值组合在一起。最常用的 列表 ，是用方括号标注，逗号分隔的一组值。
  列表 可以包含不同类型的元素。
  但一般情况下，各个元素的类型相同。
"""

squares = [1, 4, 9, 16, 25]
print('squares =', squares)

# 和字符串（及其他内置 序列sequence 类型）一样，列表也支持索引和切片：
print('\n和字符串（及其他内置 sequence 类型）一样，列表也支持索引和切片：')
print('squares[0] =', squares[0]) # 1
print('squares[-1] =', squares[-1]) # 25
print('squares[1:] =', squares[1:]) # [4, 9, 16, 25]
print('squares[-3:] =', squares[-3:]) # [9, 16, 25]

# 切片操作返回包含请求元素的 新列表。以下切片操作会返回列表的 浅拷贝：
print('\n切片操作返回包含请求元素的“新列表”。以下切片操作会返回列表的 浅拷贝：')
print('squares[:] =', squares[:])

# 列表还支持合并操作：
print('\n列表还支持合并操作：')
print('squares + [36, 49, 64, 81] =', squares + [36, 49, 64, 81])

# 与 不可变对象immutable 字符串不同, 列表是 可变对象mutable 类型，其内容可以改变：
print('\n与 不可变对象immutable 字符串不同, 列表是 可变对象mutable 类型，其内容可以改变：')
cubes = [1, 8, 27, 65, 125]
print('cubes =', cubes) # cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print('cubes =', cubes) # cubes = [1, 8, 27, 64, 125]

# append() 方法 可以在列表结尾添加新元素：
print('\nappend() 方法 可以在列表结尾添加新元素:')
cubes.append(216)
cubes.append(7 ** 3)
print('cubes =', cubes) # cubes = [1, 8, 27, 64, 125, 216, 343]

# 为切片赋值可以改变列表大小，甚至清空整个列表：
print('\n为切片赋值可以改变列表大小，甚至清空整个列表：')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print('letters =', letters) # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
print("letters[2:5] = ['C', 'D', 'E']:\n  letters =", letters) # letters = ['a', 'b', 'C', 'D', 'E', 'f', 'g']
letters[2:5] = []
print('letters[2:5] = []:\n  letters =', letters) # letters = ['a', 'b', 'f', 'g']
letters[:] = []
print('letters[:] = []:\n  letters =', letters) # letters = []

a, b = 0, 1
print(a, b) # 0 1
