

[TOC]



# 序列 -- list和tuple

sequence(序列)是一组有顺序的元素的集合。

序列有两种：tuple（元组） 和 list (列表)，tuple和list的主要区别在于，tuple的各个元素一旦建立便不可再变更，而list的各个元素可以随意变更。 

序列可以包含一个或多个元素，也可以没有任何元素。



# 1. 序列通用操作

## 1.1 index (索引)

序列中所有元素都有编号，这些编号是从 0 开始，依次递增，这个编号就是索引，索引用来访问序列中每一个位置的元素，索引是**从`0`开始**的：

```
>>> classmates = ['Michael', 'Bob', 'Tracy']

>>> classmates[0]
'Michael'
>>> classmates[1]
'Bob'
>>> classmates[2]
'Tracy'
>>> classmates[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

当索引超出了范围时，Python会报一个`IndexError`错误，所以，要确保索引不要越界。

如果要取最后一个元素，除了计算索引位置外，还可以用`-1`做索引，直接获取最后一个元素：

```
>>> classmates[-1]
'Tracy'
```

以此类推，可以获取倒数第2个、倒数第3个：

```
>>> classmates[-2]
'Bob'
>>> classmates[-3]
'Michael'
>>> classmates[-4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

当然，倒数第4个就越界了。



## 1.2 分片

分片是通过冒号操作来访问一定范围内的元素，例如：


```
>>> num=[1,2,3,4,5,6,7,8,9,10]

>>> num[3:10]    // 表示从第4（含）个到第10（不含）个元素
[4, 5, 6, 7, 8, 9, 10]

>>> num[0:3]    // 取前3个数据
[1, 2, 3]
```

由上所知，分片操作的的实现需要提供两个索引作为边界，是一个左闭右开的区间，也就是第 1 个索引包含在分片内，而第2个索引不包含在这个分片内。

 

## 1.3 序列相加

通过加号`+`可以将两个序列连接起来：

```
>>> 'hello'+' world !'
  'hello world !'

>>> [1,2,3]+['zhangsan','lisi','wangwu']
[1, 2, 3, 'zhangsan', 'lisi', 'wangwu']
```



## 1.4 in 运算符

`in`运算符用于检查一个元素是否在一个序列中，是则返回 true，否则返回 false，例如：

```
>>> str = 'believe'
>>> 'lie' in str
True

>>> 'x' in str
False
```



## 1.5 序列长度、最大值和最小值

内建函数 len、max、min 分别用于获取序列长度、最大值和最小值。

```
>>> len([11,34,23])
3
>>> max([11,34,23])
34
>>> min([11,34,23])
11
```



# 2. list (列表)

列表是最常用的 Python 数据类型，它是一种有序的集合，可以随时添加和删除其中的元素。list用方括号`[ ]`表示。

比如，列出班里所有同学的名字，就可以用一个list表示：

```
>>> classmates = ['Michael', 'Bob', 'Tracy']
>>> classmates
['Michael', 'Bob', 'Tracy']
```

变量`classmates`就是一个list。

要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：

```
>>> classmates[1] = 'Sarah'
>>> classmates
['Michael', 'Sarah', 'Tracy']
```



## 2.1 常用的列表方法

列表提供了几个详细的方法，这些方法用于检查或者修改列表中的内容

### 2.1.1 append

append 方法用于在列表的末尾追加新的元素

```
>>> l = [1,2,3,4]
>>> l.append(5)
>>> l
[1, 2, 3, 4, 5]

>>> classmates.append('Adam')
>>> classmates
['Michael', 'Bob', 'Tracy', 'Adam']
```

### 2.1.2 count

count 方法用于统计某个元素在列表中出现的次数

```
>>> numList = [1, 2, 3, 4, 5, 5, 5, 5, 6]
>>> num.count(5)    // 统计numList列表中5出现的次数
4

>>> name=['a','a','abf','ark','nhk']
>>> name.count('a')     // 统计name中字母a出现的次数
2
```

### 2.1.3 insert

insert 方法用于把元素插入到指定的位置，比如索引为`1`的位置：

```
>>> classmates.insert(1, 'Jack')
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
```

### 2.1.4 pop

要删除list末尾的元素，用`pop()`方法：

```
>>> classmates.pop()
'Adam'
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy']
```

要删除指定位置的元素，用`pop(i)`方法，其中`i`是索引位置：

```
>>> classmates.pop(1)
'Jack'
>>> classmates
['Michael', 'Bob', 'Tracy']
```

### 2.1.5 reverse

reverse 方法是将列表中的元素进行反转操作

```
>>> x = [1, 2, 3]
>>> x.reverse()    // 元素反向存储
x
[3, 2, 1]
```



# 3. tuple (元组)

tuple和list非常类似，但是tuple一旦初始化就不能修改，元组用`( )`表示。比如同样是列出同学的名字：

```
>>> classmates = ('Michael', 'Bob', 'Tracy')
```

现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。你可以正常地使用`classmates[0]`，`classmates[-1]`，但不能赋值成另外的元素。

不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。写代码时，能用tuple就尽量用tuple。



### 3.1 字符串是元组

字符串是一种特殊的元组，因此可以执行元组的相关操作。
```
>>> str = 'abcdef'

>>> print(str[2:4])
```


