[TOC]



# 变量（Variable）

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



## 变量赋值

在 Python 中，**等号 = 是赋值语句**，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的值。

```
name = "neo"
```

上述代码声明了一个变量，变量名为：name, 变量 name 的值为”neo”。



## 多个变量赋值

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



# 数据类型



## 数字（Number）

数字主要分为两种类型——整数（Integer）与浮点数（Float）。

浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，`1.23e9`和`12.3e8`是完全相等的。



## 布尔型（Bool）

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



## 字符串（String）

简单来说，字符串就是一串词汇。

严谨一点，字符串是以单引号''或双引号""括起来的任意文本，请注意，`''`或`""`本身只是一种表示方式，不是字符串的一部分。单引号和双引号是等价的。

几乎所有 Python 程序都会使用到字符串，所以，take care。



### r-string

Python用`r''`表示`''`内部的字符串为raw string，可以自己试试看有何不同：

```
print(r'Hamilton said: "In New York you can be a new man."')

print('''Hamilton said: "In New York you can be a new man."''')

print("Hamilton said: "In New York you can be a new man."")
```

上面前两种写法都是正确的，第三种不符合语法规范，会报错。



### format方法

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



### % 操作符

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