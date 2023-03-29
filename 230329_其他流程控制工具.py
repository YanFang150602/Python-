# if语句
print('if语句:')
x = int(input('请输入一个整数：'))
if x < 0:
  x = 0
  print('整数被赋值为0')
elif x == 0:
  print('什么也没有')
elif x == 1:
  print('Single')
else:
  print('More')

# for语句
print('\nfor语句：')
words = ['cat', 'table', 'window']
print('words =', words)
for w in words:
  print(w, len(w))

# 内置函数 range() 常用于遍历数字序列，该函数可以生成算术级数：
print('\n内置函数 range() 常用于遍历数字序列，该函数可以生成算术级数：')
for i in range(5):
  print(i)
  
print('list(range(5, 10)) =', list(range(5, 10))) # list(range(5, 10)) = [5, 6, 7, 8, 9]
print('list(range(0, 10, 3)) =', list(range(0, 10, 3))) # list(range(0, 10, 3)) = [0, 3, 6, 9]

# range() 和 len() 组合在一起，可以按索引迭代序列：
print('\nrange() 和 len() 组合在一起，可以按索引迭代序列：')
a = ['Mary', 'had', 'a', 'little', 'lamb']
print('a =', a)
for i in range(len(a)):
  print(f'a[{i}] = {a[i]}')

# break 语句和 C 中的类似，用于跳出最近的 for 或 while 循环。
# 循环语句支持 else 子句
for n in range(2, 10):
  print('n =', n)
  
  # for 循环中，可迭代对象中的元素全部循环完毕，或 while 循环的条件为假时，执行 else 子句:
  # 下面的 for 循环执行完毕后，又继续执行 else 子句
  for x in range(2, n):
    print('x =', x)
    if n % x == 0:
      print(n, 'equals', x, '*', n//x)
      # break 语句终止循环时，不执行 else 子句
      print('break 语句终止循环时，不执行 else 子句\n')
      break
  else:
    print('执行 else 子句。', n, '是个素数。\n')
    
# continue 语句也借鉴自 C 语言，表示继续执行循环的下一次迭代：
for num in range(2, 10):
  if num % 2 == 0:
    print(f'{num}是个偶数。')
    continue
  print(f'{num}是个奇数。')
  
# pass 语句
# pass 语句不执行任何操作。语法上需要一个语句，但程序不实际执行任何动作时，可以使用该语句。
# while True:
#  pass # Busy-wait for keyboard interrupt (Ctrl+C)
  
def test():
  # pass 还可以用作函数或条件子句的占位符，让开发者聚焦更抽象的层次。此时，程序直接忽略 pass：
  pass
  
test()

# match 语句
def http_error(status):
  match status:
    case 400:
      return 'Bad Request'
    case 404:
      return 'Not Found'
    case 401 | 403:
      print('使用 | （“ or ”）在一个模式中可以组合多个字面值：')
      return 'Not Allowed'
    case _:
      print('“变量名” _ 被作为 通配符 并必定会匹配成功。')
      return 'Something\'s wrong with the internet.'
print(http_error(405))


point = (0, 1)
match point:
  case (0, 0):
    print("Origin")
  case (0, y):
    print(f"point={point};Y={y}")
  case (x, 0):
    print(f"X={x}")
  case (x, y):
    print(f"X={x}, Y={y}")
  case _:
    raise ValueError("Not a point")

class Point:
  x: int
  y: int
def where_is(point):
  match point:
    case Point(x=0, y=0):
      print("Origin")
    case Point(x=0, y=y):
      print(f"Y={y}")
    case Point(x=x, y=0):
      print(f"X={x}")
    case Point():
      print("Somewhere else")
    case _:
      print("Not a point")
point = Point()
point.x = 1
point.y = 0
where_is(point)
