# Python模块 (module)



先给大家解释一下模块、包、库之间的概念：

在Python中，一个.py文件就构成一个模块module，用来封装一组功能；包package是将一类模块归集到一起，比模块的概念更大一些；库就是由其它程序员封装好的功能组，一般比包的概念更大一些。



## 引入模块

我们先写一个first.py文件，内容如下：

```
def laugh():
    print 'HaHaHaHa'
```

 

再写一个second.py，并引入first中的程序：

```
import first

for i in range(10):
    first.laugh()
```

在second.py中，我们使用了first.py中定义的laugh()函数。

 

引入模块后，可以通过模块.对象的方式来调用引入模块中的某个对象。上面例子中，first为引入的模块，laugh()是我们所引入的对象。

Python中还有其它的引入方式,

```

import a as b            # 引入模块a，并将模块a重命名为b

from a import function1  # 从模块a中引入function1对象。调用a中对象时，我们不用再说明模块，即直接使用function1，而不是a.function1。

from a import *          # 从模块a中引入所有对象。调用a中对象时，我们不用再说明模块，即直接使用对象，而不是a.对象。
```
这些引用方式，可以方便后面的程序书写。



## 作用域

在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过`_`前缀来实现的。

正常的函数和变量名是公开的（public），可以被直接引用，比如：`abc`，`x123`，`PI`等；

类似`__xxx__`这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的`__author__`，`__name__`就是特殊变量，`hello`模块定义的文档注释也可以用特殊变量`__doc__`访问，我们自己的变量一般不要用这种变量名；

类似`_xxx`和`__xxx`这样的函数或变量就是非公开的（private），不应该被直接引用，比如`_abc`，`__abc`等；

之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。

private函数或变量不应该被别人引用，那它们有什么用呢？请看例子：

```
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
```

我们在模块里公开`greeting()`函数，而把内部逻辑用private函数隐藏起来了，这样，调用`greeting()`函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：

外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。



## 安装第三方模块

在Python中，安装第三方模块，是通过包管理工具pip完成的。

注意：Mac或Linux上有可能并存Python 3.x和Python 2.x，因此对应的pip命令是`pip3`。

例如，我们要安装一个第三方库——Pillow，这是Python下非常强大的处理图像的工具库。安装Pillow的命令是：

```
pip install Pillow
```
macOS需要执行下面的命令：
```
pip3 install Pillow
```
耐心等待下载并安装后，就可以使用Pillow了。



### 使用Anaconda

如果开发中需要用到很多第三方库，例如，上面提到的Pillow，以及MySQL驱动程序，Web框架Flask，科学计算Numpy等。用pip一个一个安装费时费力，还需要考虑兼容性。可以直接使用[Anaconda](https://www.anaconda.com/)，这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库，我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用，缺点是占用磁盘空间大。

可以从[Anaconda官网](https://www.anaconda.com/download/)下载GUI安装包，安装包有500~600M，所以需要耐心等待下载。下载后直接安装，Anaconda会把系统Path中的python指向自己自带的Python，并且，Anaconda安装的第三方模块会安装在Anaconda自己的路径下，不影响系统已安装的Python目录。
