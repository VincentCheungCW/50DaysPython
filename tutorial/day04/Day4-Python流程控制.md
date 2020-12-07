



[TOC]



# Python 流程控制

在编程的世界中，流程控制决定了程序中语句执行的先后顺序，是程序员编程的基础，本节给大家介绍 Python 流程控制相关语法。

## if 语句

if 语句用来进行条件判断。计算机之所以能做很多自动化任务，因为它可以自己做条件判断。

语法：

```
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
```

关键字 `'elif'` 是 `'else if'` 的缩写，上述结构中可以有0到多个 elif 部分，可以有0或1个else。

示例：BMI计算器
```
    
    height = input("请输入你的身高（米）：")
    weight = input("请输入你的体重（千克）：")

    bmi = float(weight) / (float(height) * float(height))
    print("你的BMI指数：" + str(bmi))

    if bmi < 18.5:
        print("过轻")
    elif 18.5 <= bmi < 25:
        print("正常")
    elif 25 <= bmi < 28:
        print("过重")
    elif 28 <= bmi < 32:
        print("肥胖")
    elif 32 <= bmi:
        print("严重肥胖")
```




## for 循环

试想，要计算1+2+3+...+10000，怎么样让计算机去完成这样的工作呢？

答案是，循环语句。

Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：

```
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
```

执行这段代码，会依次打印`names`的每一个元素：

```
Michael
Bob
Tracy
```

所以`for x in ...`循环就是把每个元素代入变量`x`，然后执行缩进块的语句。

回到计算1+2+3+...+10000的问题，以下代码即可实现：

```
sum = 0
for x in range(0, 10001):
    sum = sum + x
print(sum)
```

Python3 `range() `函数返回的是一个可迭代对象（类型是对象），` list()` 函数可以把`range()`返回的可迭代对象转为一个列表。

```
>>> list(range(0, 5))
[0, 1, 2, 3, 4]
```



## while 循环

第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。其基本形式为：

语法：

```
while 判断条件：
    执行语句……
```

示例：

```
count = 0
while (count < 9):
   print( 'The count is:', count)
   count = count + 1
 
print("Good bye!")
```



## break 用法

break 语句可以跳出 for 和 while 循环。

示例：

```
for letter in 'Alexander Hamilton':     
   if letter == 'i':        # 字母为 i 时结束循环
      break
   print ('当前字母 :', letter)
```



## continue 用法

continue 语句被用来结束当前一轮循环，进行下一轮循环。

示例：

```
for letter in 'Alexander Hamilton':     
   if letter == 'i':        # 字母为 i 时直接进入下一轮循环
      continue
   print ('当前字母 :', letter)
```



## pass 语句

Python pass 是空语句，是为了保持程序结构的完整性。它用于那些语法上必须要有什么语句，但程序什么也不做的场合。

示例：

```

# 这通常用于创建最小结构的类:

class MyEmptyClass:
  pass
```



## 总结

本节给大家介绍了 Python 语法中的流程控制相关语法，方便后期在代码逻辑中进行条件控制。