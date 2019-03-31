# python装饰器
@[toc]
装饰器本质上是一个python函数，其返回值也是一个函数对象。
**作用：** 在不修改原函数的情况下，为已有的函数添加新的功能。如插入日志、性能测试、事务处理、缓存、权限校验等场景。

## 预备知识：闭包函数
### 概念
在函数内部定义一个内嵌函数，内嵌函数引用了外部函数的变量，此时内嵌函数称为**闭包函数**。闭包函数所引用的外部定义的变量被叫做**自由变量**。闭包可以将其自己的代码和作用域以及外部函数的作用结合在一起。

### 示例

```python
# coding=utf-8
def printer(number):
    def number_printer():
        print(number)
    return number_printer

if __name__ == '__main__':
    printer(4)
```

### 作用
- 闭包和面向接口编程的概念很像，可以把闭包理解成轻量级的接口封装。

```python
# coding=utf-8
def tag(content):
    def add_tag(tag_name):
        return "<{0}>{1}</{0}>".format(tag_name, content)
    return add_tag


if __name__ == '__main__':
    add_tag = tag('Hello')
    print(add_tag('a'))  # 输出：<a>Hello</a>
    print(add_tag('b'))  # 输出：<b>Hello</b>
```
这个示例可以理解为给定内容`content`，为其添加标签，`add_tag`类似于一个接口，根据传入的参数添加不同的标签。


## 装饰器的使用
### 函数装饰器

为一个函数添加debug信息输出。

```python
# coding=utf-8
def debug(func):
    def wrapper(*args, **kwargs):
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

@debug
def say_hi(name):
    print("Hi {}!".format(name))

if __name__ == '__main__':
    say_hi('Lucy')
    # 输出：
    # [DEBUG]: enter say_hi()
    # Hi Lucy!
```

在上面的代码中，`debug`函数是一个装饰器，`wrapper`是装饰函数，`say_hi`是被装饰的函数。如果被装饰的函数需要传参，则给装饰函数定义参数即可。

为了适应不同的被装饰函数需要不同的参数，可以直接将装饰函数的参数定义为可变参数`wrapper(*args, **kwargs)`。

### 类方法的装饰器
与函数装饰器类似。
```python
# coding=utf-8
def debug(func):
    def wrapper(*args, **kwargs):
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper


class Say(object):
    @debug
    def say_hi(self, name):
        print("Hi {}!".format(name))


if __name__ == '__main__':
    say = Say()
    say.say_hi('Lucy')
    # 输出：
    # [DEBUG]: enter say_hi()
    # Hi Lucy!
```

### 类装饰器
即定义一个类作为装饰器。具体做法是重载类中的`__call__`函数，使其返回一个函数。

```python
# coding=utf-8
class Decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[DEBUG]: enter {}()".format(self.func.__name__))
        return self.func(*args, **kwargs)


@Decorator
def say_hi(name):
    print("Hi {}!".format(name))


if __name__ == '__main__':
    say_hi('Lucy')
    # 输出：
    # [DEBUG]: enter say_hi()
    # Hi Lucy!
```

如果需要给类装饰器传参数，则需要在构造函数中传入并保存参数，重载`__call__`方法，接收一个函数作为参数，定义装饰函数，并返回装饰函数。

```python
# coding=utf-8
class Decorator(object):
    def __init__(self, level):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[DEBUG:{}]: enter {}()".format(
                self.level,
                func.__name__)
            )
            return func(*args, **kwargs)
        return wrapper


@Decorator('INFO')
def say_hi(name):
    print("Hi {}!".format(name))


if __name__ == '__main__':
    say_hi('Lucy')
    # 输出：
    # [DEBUG:INFO]: enter say_hi()
    # Hi Lucy!
```



## 参考博客

- [详解Python的装饰器](https://www.cnblogs.com/cicaday/p/python-decorator.html)
- [python 装饰器](https://www.cnblogs.com/lianyingteng/p/7743876.html)
- [说说Python中的闭包 - Closure](https://betacat.online/posts/2016-10-23/python-closure/)