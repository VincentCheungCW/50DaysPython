# Day 1   Python 的安装 #

因为Python是跨平台的，也就是说它可以运行在Windows、Mac和各种Linux/Unix系统上。在Windows上写的Python程序，放到Linux上也是能够运行的。要开始学习Python编程，首先就得把Python安装到你的电脑里。安装后，你会得到Python解释器（就是负责运行Python程序的），一个命令行交互环境，还有一个简单的集成开发环境。这里我们安装的是 3.9.0 版本的Python。

建议大家直接去官网下载最新版本的安装包，官网地址：[https://www.python.org/](https://www.python.org/)。也可以用我提供给大家的安装包，安装包的位置：tools/necessary。

## 1、windows 系统下安装配置 ##

windows 系统对应的安装包名字为python-3.9.0.exe，下载完后，双击进入下图安装页面，记得勾上Add Python 3.9 to PATH，然后点 「Install Now」 即可完成安装。

![Python安装.png](http://upload-images.jianshu.io/upload_images/2136918-2bf6591f0a12e80b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 验证是否安装成功

安装完成后，打开命令提示符（即cmd.exe），敲入 python ，出现Python版本信息，证明 Python 安装成功了。

![运行python.png](http://upload-images.jianshu.io/upload_images/2136918-817c22f802e8cfce.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

命令提示符最后一行 `>>>` 表示我们已经在 Python 交互环境中了，可以输入任何 Python 代码，回车后会立刻得到执行结果，试着输入下面代码，然后按回车看看吧。

```

print (100 / 3.1415926)

```




## 2、Mac 系统下安装配置 ##

Mac系统安装Python就更简单了，安装包名字为python-3.9.0-macosx10.9.pkg，双击安装即可。

这里还有另外一种方法，如果你安装了Homebrew，直接通过命令`brew install python3`安装即可。（如果你没有读懂这句话，说明你不需要它）

### 验证是否安装成功

安装完成后，打开终端.app（或者iTerm），敲入 `python3` ，出现Python版本信息，证明 Python 安装成功了。

![运行python.png](http://ww1.sinaimg.cn/large/007uCb0fgy1gkb7b3m7r9j31js0k2gpt.jpg)

注意：终端里输入`python`得到的是macOS系统预装的Python 2.7.16 版本，输入`python3`才会进入我们安装的版本。

Python2已经是过时的版本，而macOS之所以预装了这个版本，是为了兼容一些历史软件。我们一般使用Python3。



这样我们输入`python3`后就进入 Python 交互环境中了，可以输入任何 Python 代码，回车后会立刻得到执行结果，试着输入下面代码，然后按回车看看吧。

```

print ("玉在椟中求善价，钗于奁内待时飞。")

```



这样我们的Python环境就搭建完成了，第一个 Python 程序也成功运行了，是不是很简单。


