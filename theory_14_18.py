"""理论讲解数据 - 阶段14~18 — v3.2 正则/OOP/模块/生成器装饰器"""
from .ui import C

BD = C.BD
G = C.G
Y = C.Y
R = C.R
B = C.B
END = C.END
C_ = C.C
DIM = C.DIM
M = C.M

THEORY_14_18 = {
    14: (f"""{B}阶段14：正则表达式 — 文本处理的瑞士军刀{END}

{C_}生活类比：正则就像高级搜索{END}
    普通搜索：在文章里找"张三" → 只能精确匹配
    正则搜索：找"姓张的两个人名" → pattern = "张\\w{{2}}"
    正则就是"搜索模式"的语法，比 Ctrl+F 强大一百倍

{BD}一、re 模块基础{END}
    >>> import re

    >>> # re.search — 在字符串中搜索模式（找到第一个）
    >>> result = re.search(r"\\d{{3}}", "电话：021-12345678")
    >>> result.group()
    '021'

    >>> # re.findall — 找出所有匹配
    >>> re.findall(r"\\d{{3}}", "电话：021-12345678，手机：13812345678")
    ['021', '123', '456', '138', '123', '456']

    >>> # re.match — 只匹配字符串开头
    >>> re.match(r"Hello", "Hello World")
    <re.Match object>
    >>> re.match(r"World", "Hello World")    # 不在开头，匹配失败
    >>>

{BD}二、元字符 — 正则的魔法符号{END}
    {Y}通配符和量词：{END}
    >>> # . 匹配任意字符（除换行）
    >>> re.findall(r"a.c", "abc adc aec axc")
    ['abc', 'adc', 'aec', 'axc']

    >>> # * 前面的字符出现0次或多次
    >>> re.findall(r"ab*c", "ac abc abbc abbbc")
    ['ac', 'abc', 'abbc', 'abbbc']

    >>> # + 前面的字符出现1次或多次
    >>> re.findall(r"ab+c", "ac abc abbc")
    ['abc', 'abbc']          # ac 不匹配，+要求至少1个b

    >>> # ? 前面的字符出现0次或1次
    >>> re.findall(r"colou?r", "color colour")
    ['color', 'colour']

    >>> # {{n,m}} 指定次数范围
    >>> re.findall(r"\\d{{2,4}}", "1 12 123 12345")
    ['12', '123', '1234']    # 12345 取前4位

    {Y}字符类：{END}
    >>> # \\d 数字, \\w 字母数字下划线, \\s 空白
    >>> # \\D 非数字, \\W 非字母数字, \\S 非空白
    >>> re.findall(r"\\d+", "年龄25，身高175cm")
    ['25', '175']

    >>> # [abc] 匹配a或b或c, [a-z] 匹配范围
    >>> re.findall(r"[aeiou]", "hello world")
    ['e', 'o', 'o']

    >>> # [^abc] 匹配除了abc以外的
    >>> re.findall(r"[^0-9]", "abc123")
    ['a', 'b', 'c']

    {Y}锚点：{END}
    >>> # ^ 开头, $ 结尾
    >>> re.search(r"^Hello", "Hello World")    # 匹配
    >>> re.search(r"World$", "Hello World")    # 匹配

    {Y}分组和或：{END}
    >>> # ( ) 分组, | 或
    >>> m = re.search(r"(\\d{{4}})-(\\d{{2}})-(\\d{{2}})", "日期：2025-01-15")
    >>> m.group()       # 整个匹配
    '2025-01-15'
    >>> m.group(1)      # 第1个分组
    '2025'
    >>> m.group(2)      # 第2个分组
    '01'

    >>> # | 或运算
    >>> re.findall(r"cat|dog", "I have a cat and a dog")
    ['cat', 'dog']

{BD}三、re.sub — 替换{END}
    >>> # 把所有数字替换为 #
    >>> re.sub(r"\\d", "#", "手机13812345678")
    '手机###########'

    >>> # 去除多余空格
    >>> re.sub(r"\\s+", " ", "  hello   world  ").strip()
    'hello world'

{BD}四、实战案例{END}
    {Y}1. 验证手机号：{END}
    >>> phone = "13812345678"
    >>> bool(re.match(r"^1[3-9]\\d{{9}}$", phone))
    True

    {Y}2. 提取邮箱：{END}
    >>> text = "联系 admin@test.com 或 info@example.org"
    >>> re.findall(r"[\\w.+-]+@[\\w-]+\\.[\\w.]+", text)
    ['admin@test.com', 'info@example.org']

    {Y}3. 验证密码强度（至少8位，含大小写和数字）：{END}
    >>> pwd = "Abc12345"
    >>> bool(re.search(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).{{8,}}", pwd))
    True

{BD}五、编译正则（性能优化）{END}
    >>> # 如果同一个模式要多次使用，先编译
    >>> phone_pattern = re.compile(r"^1[3-9]\\d{{9}}$")
    >>> phone_pattern.match("13812345678")    # 速度更快

{C_}>> 动手试试！{END}
    打开代码实验室(l)，试这些：
    - re.findall(r"\\d+", "今天25度，明天18度") → 看看提取了什么
    - 试试写一个匹配你手机号的正则
    - 用 re.sub 把一段文字里的英文单词替换为 "[EN]"
""",
    ["regex_basic", "regex_meta", "regex_quantifier", "regex_charset", "regex_group",
     "regex_sub", "regex_compile", "regex_practice"]),

    15: (f"""{B}阶段15：面向对象基础 — 做自己的模具{END}

{C_}生活类比：类 = 模具，对象 = 用模具做出来的产品{END}
    ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
    │   饼干模具   │ →   │  星星饼干    │     │  星星饼干    │
    │  (类 Class)  │     │  (对象 obj1) │     │  (对象 obj2) │
    └─────────────┘     └─────────────┘     └─────────────┘
    同一个模具 → 可以做无数个饼干，每个独立互不影响

{BD}一、定义类和创建对象{END}
    >>> class Dog:
    ...     # 一个简单的狗类
    ...     def __init__(self, name, age):
    ...         self.name = name       # 属性：名字
    ...         self.age = age         # 属性：年龄
    ...
    ...     def bark(self):            # 方法：叫
    ...         return f"{{self.name}}：汪汪！"
    ...
    ...     def info(self):            # 方法：信息
    ...         return f"{{self.name}}，{{self.age}}岁"

    >>> dog1 = Dog("旺财", 3)
    >>> dog2 = Dog("来福", 5)
    >>> dog1.bark()
    '旺财：汪汪！'
    >>> dog2.info()
    '来福，5岁'

    {Y}关键概念：{END}
    - class  → 定义类的关键字
    - __init__ → 构造方法，创建对象时自动调用
    - self → 对象自身的引用（类似"我"）
    - self.xxx → 实例属性（每个对象各自拥有）
    - def xxx(self) → 实例方法

{BD}二、self 到底是什么？{END}
    >>> class Person:
    ...     def __init__(self, name):
    ...         self.name = name
    ...
    ...     def say_hi(self):
    ...         print(f"我是{{self.name}}")

    >>> p = Person("张三")
    >>> p.say_hi()              # Python 自动把 p 传给 self
    我是张三
    >>> # 等价于：
    >>> Person.say_hi(p)        # 手动传 self
    我是张三

{BD}三、继承 — 子承父业{END}
    {C_}类比：动物→狗→导盲犬，每层更具体{END}

    >>> class Animal:
    ...     def __init__(self, name):
    ...         self.name = name
    ...
    ...     def speak(self):
    ...         return "..."
    ...
    ...     def __str__(self):
    ...         return f"Animal({{self.name}})"

    >>> class Cat(Animal):              # Cat 继承 Animal
    ...     def speak(self):             # 重写方法
    ...         return f"{{self.name}}：喵～"
    ...
    ...     def purr(self):              # Cat 独有方法
    ...         return f"{{self.name}}：呼噜噜..."

    >>> class Dog(Animal):
    ...     def speak(self):
    ...         return f"{{self.name}}：汪汪！"
    ...
    ...     def fetch(self):
    ...         return f"{{self.name}}捡回了球"

    >>> cat = Cat("小花")
    >>> dog = Dog("旺财")
    >>> cat.speak()
    '小花：喵～'
    >>> dog.fetch()
    '旺财捡回了球'
    >>> str(cat)                         # 继承了 __str__
    'Animal(小花)'

    {Y}super() — 调用父类方法：{END}
    >>> class GuideDog(Dog):
    ...     def __init__(self, name, owner):
    ...         super().__init__(name)    # 调用父类 __init__
    ...         self.owner = owner
    ...
    ...     def guide(self):
    ...         return f"{{self.name}}正在引导{{self.owner}}"

    >>> gd = GuideDog("路路", "王先生")
    >>> gd.speak()       # 继承自 Dog
    '路路：汪汪！'
    >>> gd.guide()
    '路路正在引导王先生'

{BD}四、多态 — 同一个接口，不同表现{END}
    >>> def animal_concert(animals):
    ...     for a in animals:
    ...         print(a.speak())     # 同一个方法，不同表现

    >>> animals = [Cat("小花"), Dog("旺财"), Cat("咪咪")]
    >>> animal_concert(animals)
    小花：喵～
    旺财：汪汪！
    咪咪：喵～

    {Y}多态的好处：{END}
    不用管具体是什么类型，只要都有 speak() 方法就能用
    新增动物类不需要改 animal_concert 的代码

{BD}五、封装 — 保护内部数据{END}
    >>> class BankAccount:
    ...     def __init__(self, owner, balance=0):
    ...         self.owner = owner
    ...         self._balance = balance        # _ 开头表示"私有"（约定）
    ...
    ...     def deposit(self, amount):
    ...         if amount > 0:
    ...             self._balance += amount
    ...             return f"存入{{amount}}，余额{{self._balance}}"
    ...         return "金额必须大于0"
    ...
    ...     def withdraw(self, amount):
    ...         if 0 < amount <= self._balance:
    ...             self._balance -= amount
    ...             return f"取出{{amount}}，余额{{self._balance}}"
    ...         return "余额不足或金额无效"
    ...
    ...     @property                          # 用 property 控制读取
    ...     def balance(self):
    ...         return self._balance

    >>> acc = BankAccount("张三", 1000)
    >>> acc.deposit(500)
    '存入500，余额1500'
    >>> acc.withdraw(200)
    '取出200，余额1300'
    >>> acc.balance              # 用 property，像属性一样访问
    1300

    {Y}_name vs __name：{END}
    - `_balance` → 约定私有，外部仍可访问（但不推荐）
    - `__balance` → 名称修饰，外部难以意外访问
    - `@property` → Pythonic 方式，提供受控的访问接口

{C_}>> 动手试试！{END}
    打开代码实验室(l)，试这些：
    - 创建一个 Student 类，有 name/scores 属性和 average() 方法
    - 创建 Teacher 类继承 Person，增加 subject 属性
    - 试着用 _ 保护一个属性，用 @property 提供读取
""",
    ["oop_class_object", "oop_init_self", "oop_inheritance", "oop_polymorphism",
     "oop_encapsulation", "oop_super", "oop_property"]),

    16: (f"""{B}阶段16：面向对象进阶 — 深入类的内核{END}

{C_}生活类比：魔术方法 = 遥控器上的隐藏按钮{END}
    你按"+"音量增大，按"-"音量减小
    但你不知道遥控器内部怎么实现的
    Python 的魔术方法就是这些"隐藏按钮"：
    len(obj) → 实际调用 obj.__len__()
    str(obj) → 实际调用 obj.__str__()
    obj + obj2 → 实际调用 obj.__add__(obj2)

{BD}一、常用魔术方法{END}
    >>> class Vector:
    ...     def __init__(self, x, y):
    ...         self.x = x
    ...         self.y = y
    ...
    ...     def __str__(self):              # str() 调用
    ...         return f"Vector({{self.x}}, {{self.y}})"
    ...
    ...     def __repr__(self):             # 调试时显示
    ...         return f"Vector({{self.x}}, {{self.y}})"
    ...
    ...     def __add__(self, other):       # + 运算符
    ...         return Vector(self.x + other.x, self.y + other.y)
    ...
    ...     def __mul__(self, scalar):      # * 运算符
    ...         return Vector(self.x * scalar, self.y * scalar)
    ...
    ...     def __len__(self):              # len() 调用
    ...         return int((self.x**2 + self.y**2) ** 0.5)
    ...
    ...     def __eq__(self, other):        # == 比较运算
    ...         return self.x == other.x and self.y == other.y
    ...
    ...     def __lt__(self, other):        # < 比较运算
    ...         return len(self) < len(other)

    >>> v1 = Vector(3, 4)
    >>> v2 = Vector(1, 2)
    >>> str(v1)
    'Vector(3, 4)'
    >>> v1 + v2                     # 调用 __add__
    Vector(4, 6)
    >>> v1 * 3                      # 调用 __mul__
    Vector(9, 12)
    >>> len(v1)                     # 调用 __len__
    5
    >>> v1 == Vector(3, 4)          # 调用 __eq__
    True

    {Y}魔术方法速查表：{END}
    ┌──────────────┬──────────────┬────────────────┐
    │  语法        │  魔术方法     │  说明           │
    ├──────────────┼──────────────┼────────────────┤
    │  str(obj)    │  __str__     │  可读字符串      │
    │  repr(obj)   │  __repr__    │  调试字符串      │
    │  len(obj)    │  __len__     │  长度           │
    │  obj + other │  __add__     │  加法           │
    │  obj - other │  __sub__     │  减法           │
    │  obj * n     │  __mul__     │  乘法           │
    │  obj == other│  __eq__      │  等于           │
    │  obj < other │  __lt__      │  小于           │
    │  obj[key]    │  __getitem__ │  索引访问        │
    │  obj[key]=v  │  __setitem__ │  索引赋值        │
    │  obj in container │ __contains__ │ in 运算    │
    │  for x in obj│  __iter__   │  迭代           │
    │  bool(obj)   │  __bool__    │  布尔值         │
    └──────────────┴──────────────┴────────────────┘

{BD}二、类方法 @classmethod 和静态方法 @staticmethod{END}
    >>> class Date:
    ...     def __init__(self, year, month, day):
    ...         self.year = year
    ...         self.month = month
    ...         self.day = day
    ...
    ...     @classmethod
    ...     def from_string(cls, date_str):
    ...         # 用字符串创建 Date（工厂方法）
    ...         y, m, d = date_str.split("-")
    ...         return cls(int(y), int(m), int(d))    # cls 就是当前类
    ...
    ...     @staticmethod
    ...     def is_valid(date_str):
    ...         # 检查日期字符串格式（不需要 self 或 cls）
    ...         parts = date_str.split("-")
    ...         return len(parts) == 3 and all(p.isdigit() for p in parts)
    ...
    ...     def __str__(self):
    ...         return f"{{self.year}}-{{self.month:02d}}-{{self.day:02d}}"

    >>> d = Date.from_string("2025-01-15")    # 用类方法创建
    >>> str(d)
    '2025-01-15'
    >>> Date.is_valid("2025-01-15")            # 用静态方法检查
    True

    {Y}三者的区别：{END}
    ┌──────────────┬───────────┬────────────────────────┐
    │  类型        │  第一个参数 │  用途                   │
    ├──────────────┼───────────┼────────────────────────┤
    │  实例方法     │  self     │  操作实例数据            │
    │  类方法       │  cls      │  工厂方法/替代构造器      │
    │  静态方法     │  无       │  工具函数，逻辑上属于类    │
    └──────────────┴───────────┴────────────────────────┘

{BD}三、抽象类 — 制定规则{END}
    >>> from abc import ABC, abstractmethod
    ...
    ... class Shape(ABC):
    ...     @abstractmethod
    ...     def area(self):
    ...         # 子类必须实现 area 方法
    ...         pass
    ...
    ...     @abstractmethod
    ...     def perimeter(self):
    ...         # 子类必须实现 perimeter 方法
    ...         pass
    ...
    ...     def describe(self):
    ...         return f"面积={{self.area():.2f}}，周长={{self.perimeter():.2f}}"

    >>> # Shape()  → 报错！抽象类不能直接创建对象
    >>> # 必须子类实现所有抽象方法才行

    >>> class Rectangle(Shape):
    ...     def __init__(self, w, h):
    ...         self.w = w
    ...         self.h = h
    ...     def area(self):
    ...         return self.w * self.h
    ...     def perimeter(self):
    ...         return 2 * (self.w + self.h)

    >>> class Circle(Shape):
    ...     def __init__(self, r):
    ...         self.r = r
    ...     def area(self):
    ...         import math
    ...         return math.pi * self.r ** 2
    ...     def perimeter(self):
    ...         import math
    ...         return 2 * math.pi * self.r

    >>> r = Rectangle(3, 4)
    >>> c = Circle(5)
    >>> r.describe()
    '面积=12.00，周长=14.00'
    >>> c.describe()
    '面积=78.54，周长=31.42'

{BD}四、组合 vs 继承{END}
    {Y}继承：is-a 关系（狗是动物）{END}
    {Y}组合：has-a 关系（汽车有引擎）{END}

    >>> class Engine:
    ...     def __init__(self, hp):
    ...         self.hp = hp
    ...     def start(self):
    ...         return f"{{self.hp}}马力引擎启动！"
    ...
    ... class Car:
    ...     def __init__(self, brand, hp):
    ...         self.brand = brand
    ...         self.engine = Engine(hp)    # 组合：Car 有 Engine
    ...     def start(self):
    ...         return f"{{self.brand}}：{{self.engine.start()}}"

    >>> car = Car("特斯拉", 300)
    >>> car.start()
    '特斯拉：300马力引擎启动！'

    {Y}原则：优先用组合，只在明确 is-a 时用继承{END}

{C_}>> 动手试试！{END}
    打开代码实验室(l)，试这些：
    - 给 Vector 添加 __sub__ 和 __abs__ 魔术方法
    - 用 @classmethod 写一个 Student.from_dict() 工厂方法
    - 定义抽象类 Animal，让 Cat/Dog 继承并实现 speak()
""",
    ["oop_magic_method", "oop_classmethod", "oop_staticmethod",
     "oop_abstract", "oop_composition"]),

    17: (f"""{B}阶段17：模块与包 — 造自己的工具箱{END}

{C_}生活类比：{END}
    模块 = 一个工具箱（一个 .py 文件）
    包 = 工具柜（一个文件夹，装多个工具箱）
    pip = 网上五金店（下载别人造的工具箱）

{BD}一、导入模块的5种方式{END}
    >>> # 1. import 模块名
    >>> import math
    >>> math.sqrt(16)
    4.0

    >>> # 2. from 模块 import 名字
    >>> from math import pi, sqrt
    >>> pi
    3.141592653589793

    >>> # 3. from 模块 import * （不推荐！命名冲突）
    >>> from math import *       # 导入所有名字

    >>> # 4. 别名导入
    >>> import numpy as np       # 约定别名
    >>> import datetime as dt

    >>> # 5. 条件导入
    >>> try:
    ...     import orjson as json
    ... except ImportError:
    ...     import json

{BD}二、自己造模块{END}
    {Y}文件 my_tools.py：{END}
        def add(a, b):
            return a + b

        def greet(name):
            return f"你好，{{name}}！"

        if __name__ == "__main__":
            # 只在直接运行时执行，被导入时不执行
            print(greet("测试"))

    {Y}使用：{END}
    >>> from my_tools import add, greet
    >>> add(3, 5)
    8
    >>> greet("张三")
    '你好，张三！'

    {Y}__name__ 的作用：{END}
    - 直接运行 python my_tools.py → __name__ == "__main__"
    - 被 import → __name__ == "my_tools"
    - 这是 Python 最常见的"可导入+可运行"模式

{BD}三、包 — 组织多个模块{END}
    {Y}目录结构：{END}
        my_package/
        ├── __init__.py        # 包的标识（可以为空）
        ├── math_tools.py
        ├── str_tools.py
        └── data/
            ├── __init__.py
            └── csv_tools.py

    >>> # 导入包中的模块
    >>> from my_package import math_tools
    >>> from my_package.data.csv_tools import read_csv

    {Y}__init__.py 的妙用：{END}
        # my_package/__init__.py
        from .math_tools import add, subtract     # 方便直接导入
        from .str_tools import greet

    >>> # 这样就可以直接从包导入
    >>> from my_package import add, greet

{BD}四、pip — 包管理器{END}
    {Y}常用命令：{END}
    pip install requests          # 安装包
    pip install requests==2.31.0  # 指定版本
    pip install -U requests       # 升级包
    pip uninstall requests        # 卸载包
    pip list                      # 查看已安装的包
    pip show requests             # 查看包信息
    pip freeze > requirements.txt # 导出依赖清单
    pip install -r requirements.txt  # 从清单安装

{BD}五、虚拟环境 — 项目隔离{END}
    {C_}类比：每个项目一个独立厨房，调料互不干扰{END}

    {Y}创建和激活：{END}
    # Windows
    python -m venv myenv
    myenv\\Scripts\\activate

    # Linux/Mac
    python3 -m venv myenv
    source myenv/bin/activate

    {Y}退出虚拟环境：{END}
    deactivate

    {Y}为什么要用虚拟环境？{END}
    - 项目A需要 Django 3.x，项目B需要 Django 4.x
    - 没有虚拟环境 → 版本冲突
    - 有了虚拟环境 → 各自独立，互不影响

{BD}六、常用标准库速查{END}
    ┌──────────────┬────────────────────────────┐
    │  模块         │  用途                      │
    ├──────────────┼────────────────────────────┤
    │  os           │  操作系统接口               │
    │  sys          │  系统相关                   │
    │  pathlib      │  路径操作（推荐替代os.path） │
    │  datetime     │  日期时间                   │
    │  json         │  JSON 读写                  │
    │  re           │  正则表达式                  │
    │  collections  │  特殊容器(defaultdict等)     │
    │  itertools    │  迭代工具                   │
    │  logging      │  日志                       │
    │  unittest     │  单元测试                   │
    │  argparse     │  命令行参数                  │
    │  hashlib      │  哈希加密                   │
    │  csv          │  CSV 文件                   │
    │  random       │  随机数                     │
    │  math         │  数学函数                   │
    └──────────────┴────────────────────────────┘

{C_}>> 动手试试！{END}
    打开代码实验室(l)，试这些：
    - import this → 看看 Python 之禅
    - 创建一个 my_tools.py，写几个工具函数，然后在另一个文件导入
    - 试试 python -m venv test_env 创建虚拟环境
""",
    ["mod_import", "mod_name_main", "mod_package", "mod_pip", "mod_venv",
     "mod_stdlib"]),

    18: (f"""{B}阶段18：生成器与装饰器 — Python 的独门绝技{END}

{C_}生活类比：{END}
    生成器 = 自助餐传送带（要用一盘才上一盘，不会一次摆满）
    装饰器 = 手机壳（不改动手机本身，但增加功能：防摔/美观）

{BD}一、生成器 — 惰性求值{END}
    {Y}普通函数：一次性返回所有结果{END}
    >>> def get_squares(n):
    ...     result = []
    ...     for i in range(n):
    ...         result.append(i ** 2)
    ...     return result
    >>> get_squares(5)
    [0, 1, 4, 9, 16]

    {Y}生成器函数：用 yield 一个一个吐出结果{END}
    >>> def gen_squares(n):
    ...     for i in range(n):
    ...         yield i ** 2          # yield 暂停函数，返回一个值

    >>> g = gen_squares(5)
    >>> next(g)         # 一次取一个
    0
    >>> next(g)
    1
    >>> next(g)
    4
    >>> list(g)         # 取剩下的
    [9, 16]

    {Y}为什么用生成器？{END}
    - 节省内存：不需要一次性生成所有数据
    - 处理大数据：读取10GB文件，每次只放一行在内存

    >>> def read_large_file(path):
    ...     with open(path, "r", encoding="utf-8") as f:
    ...         for line in f:
    ...             yield line.strip()    # 每次只读一行

    {Y}生成器表达式：{END}
    >>> squares = (x**2 for x in range(10))    # 注意是 () 不是 []
    >>> list(squares)
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    >>> # 列表推导式 vs 生成器表达式
    >>> [x**2 for x in range(10)]     # 一次生成全部，占内存
    >>> (x**2 for x in range(10))     # 惰性生成，省内存

{BD}二、装饰器 — 函数的"外挂"{END}
    {Y}第一步：理解函数是对象{END}
    >>> def hello():
    ...     return "Hello"
    >>> hi = hello               # 函数可以赋值给变量
    >>> hi()
    'Hello'

    {Y}第二步：函数可以作为参数{END}
    >>> def loud(func):
    ...     def wrapper():
    ...         result = func()
    ...         return result.upper()
    ...     return wrapper

    >>> @loud                     # 等价于 shout = loud(shout)
    ... def shout():
    ...     return "hello"

    >>> shout()
    'HELLO'

    {Y}第三步：带参数的装饰器{END}
    >>> def repeat(n):
    ...     def decorator(func):
    ...         def wrapper(*args, **kwargs):
    ...             results = []
    ...             for _ in range(n):
    ...                 results.append(func(*args, **kwargs))
    ...             return results
    ...         return wrapper
    ...     return decorator

    >>> @repeat(3)
    ... def greet(name):
    ...     return f"Hi {{name}}"

    >>> greet("张三")
    ['Hi 张三', 'Hi 张三', 'Hi 张三']

    {Y}第四步：实用装饰器示例{END}
    >>> import time
    ...
    ... def timer(func):
    ...     # 计算函数执行时间
    ...     def wrapper(*args, **kwargs):
    ...         start = time.time()
    ...         result = func(*args, **kwargs)
    ...         elapsed = time.time() - start
    ...         print(f"{{func.__name__}} 耗时 {{elapsed:.4f}}秒")
    ...         return result
    ...     return wrapper

    >>> @timer
    ... def slow_add(a, b):
    ...     time.sleep(0.1)
    ...     return a + b

    >>> slow_add(3, 5)
    slow_add 耗时 0.1005秒
    8

    {Y}functools.wraps — 保留原函数信息{END}
    >>> from functools import wraps
    ...
    ... def timer(func):
    ...     @wraps(func)                   # 保留 __name__, __doc__
    ...     def wrapper(*args, **kwargs):
    ...         start = time.time()
    ...         result = func(*args, **kwargs)
    ...         print(f"{{func.__name__}}: {{time.time()-start:.4f}}s")
    ...         return result
    ...     return wrapper

    >>> @timer
    ... def my_func():
    ...     # 这是我的函数
    ...     pass

    >>> my_func.__name__       # 没有 @wraps 会变成 'wrapper'
    'my_func'
    >>> my_func.__doc__
    '这是我的函数'

{BD}三、上下文管理器 — with 的原理{END}
    >>> class Timer:
    ...     def __enter__(self):
    ...         self.start = time.time()
    ...         return self
    ...
    ...     def __exit__(self, *args):
    ...         self.elapsed = time.time() - self.start
    ...         print(f"耗时 {{self.elapsed:.4f}}秒")

    >>> with Timer() as t:
    ...     time.sleep(0.1)
    耗时 0.1005秒

    {Y}也可以用 @contextmanager 生成器写：{END}
    >>> from contextlib import contextmanager
    ...
    ... @contextmanager
    ... def timer():
    ...     start = time.time()
    ...     yield                   # yield 前是 __enter__，后是 __exit__
    ...     print(f"耗时 {{time.time()-start:.4f}}秒")

    >>> with timer():
    ...     time.sleep(0.1)
    耗时 0.1005秒

{C_}>> 动手试试！{END}
    打开代码实验室(l)，试这些：
    - 写一个生成斐波那契数列的生成器
    - 写一个 @debug 装饰器，打印函数的参数和返回值
    - 试试 (x**2 for x in range(1000000)) 和 [x**2 for x in range(1000000)] 的内存区别
""",
    ["gen_yield", "gen_expression", "dec_basic", "dec_args", "dec_wraps",
     "ctx_manager"]),
}
