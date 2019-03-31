# python 中staticmethod和classmethod
@staticmethod和@classmethod是python中的两个装饰器（装饰器理解请见：[python装饰器](https://github.com/BraveheartHui/NLP-Algorithm-Notes/blob/master/python/python%E8%A3%85%E9%A5%B0%E5%99%A8.md)）。

`@staticmethod`将函数转换成为一个静态方法，`@classmethod`将函数转换成为一个类方法。

## 使用方法
```python
# coding=utf-8
class Function(object):

    # Instance method
    def add(self, n1, n2):
        print("add : {} + {} = {}".format(n1, n2, n1 + n2))

    @classmethod
    def minus(cls, n1, n2):
        print("minus : {} - {} = {}".format(n1, n2, n1 - n2))

    @staticmethod
    def multiply(n1, n2):
        print("multiply : {} - {} = {}".format(n1, n2, n1 * n2))


if __name__ == '__main__':
    f = Function()
    f.add(3, 2)  # 输出：add : 3 + 2 = 5
    f.minus(3, 2)  # 输出：minus : 3 - 2 = 1
    Function().minus(3, 2)  # 输出：minus : 3 - 2 = 1
    Function().multiply(3, 2)  # 输出：multiply : 3 - 2 = 6
    f.multiply(3, 2)  # 输出 : multiply : 3 - 2 = 6
```

## 区别
|  | 实例方法 | 类方法（classmethod） | 静态方法（staticmethod） |
| ------ | ------ | ------ | ------ |
| **定义方式** | self作为第一个参数 | cls作为第一个参数 | 无强制参数 |
| **绑定对象** | 类的实例 | 类 | 无 |
| **调用方式** | 只能通过类的实例调用 | 类对象或类的实例均可调用 | 类对象或类的实例均可调用 |

## 特点

### `@staticmethod`
	
- 用法与类外函数很像，函数属于类，但是使用的时候不需要访问它所属的类。
- 可以被用来组织类之间有逻辑关系的函数。在很多情况下，一些函数与类相关，但不需要任何类或实例变量就可以实现一些功能。比如设置环境变量，修改另一个类的属性等等。假如我们想仅实现类之间的交互而不是通过实例，我们可以在类之外建立一个简单的函数来实现这个功能，但是这会使代码扩散到类之外，可能对未来代码维护产生问题。

### `@classmethod`
	
- 实例属性由实例更改，不会影响类属性。而类属性则可以由类方法 (classmethod) 来更改。
- 持有cls参数，可以调用类的属性，类的方法等，避免了使用类名硬编码。
## 参考博客

- [(译文)Python中的staticmethod与classmethod](https://www.cnblogs.com/agnewee/p/5653936.html)
- [python中@classmethod @staticmethod区别](https://www.cnblogs.com/elie/p/5876210.html)
- [python学习系列---staticmethod和classmethod](python学习系列---staticmethod和classmethod)
