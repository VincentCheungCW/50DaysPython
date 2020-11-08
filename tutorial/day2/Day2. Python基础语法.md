

[TOC]



# 基础 #

------



## Python书写规范



### 大小写敏感

首先要注意的是 Python 语言是大小写敏感的，如果写错了大小写，程序会报错。



### 每行一个语句

Python 鼓励每一行使用一句独立语句从而使得代码更加可读。

不同于C、Java等其他语言使用分号（；）区分多条语句，Python中利用换行区分多条语句。

举个例子：

```python
i = 5
print(i)
```

上面的两条语句必须写在两行里，若写成下面这样，程序是无法识别的：

```python
i = 5  print(i)
```

当然写在一行里用分号分隔也可以，但Python中一般不建议出现分号。实际上，我*从未*在 Python 程序中见过一个分号。



### 缩进

放置在一起的语句*必须*拥有相同的缩进。每一组这样的语句被称为 *块（block）*。我们将会在后文章节的案例中了解块这一概念是多么重要。

现在只需要记住一件事：错误的缩进可能会导致错误。下面是一个例子：

```python
i = 5
# 下面行首有一个空格，运行的话会报错
 print('Value is', i)
print('I repeat, the value is', i)
```

当你运行这一程序时，你将得到如下错误：

```
  File "whitespace.py", line 3
    print('Value is', i)
    ^
IndentationError: unexpected indent
# 缩进错误：意外缩进
```

> **如何缩进**
>
> 使用四个空格来缩进，这是来自 Python 语言官方的建议。好的编辑器会**自动为你完成这一工作**。请确保你在缩进中使用数量一致的空格，否则你的程序将不会运行，或引发不期望的行为。



### Python 标识符

标识符是语言中允许作为名字的有效字符串集合。

合法的 Python 标识符，需要遵守如下规定：

- 第一个字符必须是字母或下划线（_）
- 剩下的字符可以是字母和数字或下划线
- 大小写敏感
- 不能是 Python 的关键字，例如 def、class 就不能作为标识符

以下划线开头的标识符是有特殊意义的。以单下划线开头 `_foo` 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 `from xxx import *` 而导入。

以双下划线开头的 `__foo` 代表类的私有成员，以双下划线开头和结尾的 `__foo__` 代表 Python 里特殊方法专用的标识，如 `__init__()` 代表类的构造函数。



### 多行语句

Python 语句中一般以新行作为为语句的结束符。但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：

```
total = item_one + \
        item_two + \
        item_three
```

等价于：
```
total = item_one + item_two + item_three
```


语句中包含[], {} 或 () 括号就不需要使用多行连接符。如下实例：

```
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
```



### 注释（comment）

*注释* 是一行以 `#` 号开头的文字，其主要用作写给程序读者看的说明性文字。

举个例子：

```python
print('hello world')  # 使用 print 函数输出字符串
```

或者：

```python
# 使用 print 函数输出字符串
print('hello world')
```

你应该在你的程序中尽可能多地写注释，这样做对你的程序的读者来说非常有用，他们可以很容易地理解你的每条语句的用意。这个人可以是六个月后的你！



## 如何编写和运行 Python 程序

从今以后，保存和运行 Python 程序的标准步骤如下：

1. 打开你的编辑器（sublime text）。
2. 输入案例中给出的代码。
3. 以给定的文件名将其保存成文件。
4. 在命令行中通过命令 `python xxx.py` 来运行程序。（macOS使用命令`python3 xxx.py`）



------



## 变量（Variable）

变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。

变量在程序中用一个变量名表示，在 Python 中 变量命名规定，必须是大小写英文，数字和 下划线`(_)`的组合，并且不能用数字开头。比如：

```
a = 1
```

变量`a`是一个整数。

```
t_007 = 'T007'
```

变量`t_007`是一个字符串。

```
Answer = True
```

变量`Answer`是一个布尔值`True`。

在 Python 中，变量就是变量，它没有类型（或者称为动态类型），我们所说的”类型”是变量所指的内存中对象的类型。



### **变量赋值**

在 Python 中，**等号 = 是赋值语句**，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的值。

```
name = "neo"
```

上述代码声明了一个变量，变量名为：name, 变量 name 的值为”neo”。



### **多个变量赋值**

Python 允许你同时为多个变量赋值。例如：

```
a = b = c = 1
```

以上实例，创建一个整型对象，值为 1，三个变量被赋予相同的数值。

您也可以为多个对象指定多个变量。例如：

```
a, b, c = 1, 2, "neo"
```

以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 “neo” 分配给变量 c。



------



## 数据类型



### 数字（Number）

数字主要分为两种类型——整数（Integer）与浮点数（Float）。

浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，`1.23e9`和`12.3e8`是完全相等的。



### 布尔型（Bool）

一个布尔值只有`True`、`False`两种状态，要么是`True`，要么是`False`。试试下面的例子：

```
>>> True
True
>>> False
False
>>> 3 > 2
True
>>> 1 + 2 == 5
False
```



### 字符串（String）

简单来说，字符串就是一串词汇。

严谨一点，字符串是以单引号''或双引号""括起来的任意文本，请注意，`''`或`""`本身只是一种表示方式，不是字符串的一部分。单引号和双引号是等价的。

几乎所有 Python 程序都会使用到字符串，所以，take care。



#### r-string

Python用`r''`表示`''`内部的字符串为raw string，可以自己试试看有何不同：

```
print(r'Hamilton said: "In New York you can be a new man."')

print('''Hamilton said: "In New York you can be a new man."''')

print("Hamilton said: "In New York you can be a new man."")
```

上面前两种写法都是正确的，第三种不符合语法规范，会报错。



#### format方法

格式化字符串。

运行下面的语句看看结果吧 ：

```python

output = '亲爱的{}你好！你{}月的话费是{}元，余额是{}元。'

ella = 'Ella'
month = '11'
bill = 120
remain = 300
print(output.format(ella, month, bill, remain))

mike = 'Mike'
bill = 150
remain = 900
print(output.format(mike, month, bill, remain))

```

输出：

```
$ python str_format.py
Swaroop was 20 years old when he wrote this book
Why is Swaroop playing with that python?
```

**它是如何工作的**

一个字符串可以使用某些特定的格式（Specification），随后，`format` 方法将被调用，使用这一方法中与之相应的参数替换这些格式。

Python 中 `format` 方法所做的事情便是将每个参数值替换至格式所在的位置。



#### % 操作符

Python中内置的%操作符可用于格式化字符串，控制字符串的呈现格式。

格式化字符串时，Python使用一个字符串作为模板。模板中有格式符，这些格式符为真实值预留位置，并说明真实数值应该呈现的格式。Python用一个`tuple`将多个值传递给模板，每个值对应一个格式符。

比如下面的例子：

```
print("I'm %s. I'm %d year old" % ('Jaden', 20))
```

上面的例子中，

`"I'm %s. I'm %d year old"` 为我们的模板。%s为第一个格式符，表示一个字符串。%d为第二个格式符，表示一个整数。`('Jaden', 20)`的两个元素'Jaden'和20为替换%s和%d的真实值。在模板和tuple之间，有一个%号分隔，它代表了格式化操作。

整个`"I'm %s. I'm %d year old" % ('Jaden', 20)`实际上构成一个字符串表达式。我们可以像一个正常的字符串那样，将它赋值给某个变量。比如:

```
a = "I'm %s. I'm %d year old" % ('Jaden', 20)
print(a)
```

 **格式符**

格式符为真实值预留位置，并控制显示的格式。格式符可以包含有一个类型码，用以控制显示的类型，如下:
```

%s  字符串

%d  十进制整数

%f  浮点数
```


可以用如下的方式，对格式进行进一步的控制：
```

%[(name)][flags][width].[precision]typecode

```
(name)为命名

flags可以有+,-,' '或0。+表示右对齐。-表示左对齐。' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。

width表示显示宽度

precision表示小数点后精度

比如：

```
print("%04d" % 5)
print("%6.3f" % 2.3)
```

 



除上面列举的几种数据类型外，Python还提供了List（列表）、Tuple（元组）、Sets（集合）、Dictionary（字典）等多种数据类型，并且允许用户创建自定义数据类型，我们后面会继续讲到。

