"""理论讲解数据 - 阶段8~13 — v3.2 大幅扩充示例与类比"""
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

THEORY_8_13 = {
    8: (f"""{B}阶段8：字典 — 用名字找东西{END}

{C_}生活类比：字典就像通讯录{END}
    ┌────────┬──────────────┐
    │  名字  │    电话      │    ← 键(key): 值(value)
    ├────────┼──────────────┤
    │ "张三" │ "138-0000"   │
    │ "李四" │ "139-1111"   │
    │ "王五" │ "137-2222"   │
    └────────┴──────────────┘
    查"张三"就能找到电话 → dict["张三"]

{BD}一、创建{END}
    >>> person = {{"name": "张三", "age": 25}}
    >>> person["name"]
    '张三'

    >>> scores = dict(语文=90, 数学=85)    # 用关键字参数创建
    >>> scores
    {{"语文": 90, "数学": 85}}

    >>> # 从列表对创建
    >>> dict([("a", 1), ("b", 2)])
    {{'a': 1, 'b': 2}}

{BD}二、访问{END}
    >>> person = {{"name": "张三", "age": 25, "city": "上海"}}

    >>> person["name"]                # 直接访问
    '张三'

    >>> person.get("phone")           # 不存在返回 None
    >>> person.get("phone", "无号码")  # 不存在返回默认值
    '无号码'

    >>> "name" in person              # 检查键是否存在
    True

{C_}d[k] vs d.get(k) 的区别：{END}
    >>> person["phone"]               # 键不存在 → KeyError！
    KeyError: 'phone'
    >>> person.get("phone")           # 键不存在 → 安全返回 None
    >>>

{BD}三、修改{END}
    >>> person = {{"name": "张三", "age": 25}}

    >>> person["age"] = 26            # 修改已有键
    >>> person["city"] = "上海"       # 添加新键
    >>> person
    {{'name': '张三', 'age': 26, 'city': '上海'}}

    >>> del person["city"]            # 删除
    >>> person.pop("age")             # 删除并返回值
    26
    >>> person
    {{'name': '张三'}}

    >>> # 批量更新
    >>> person.update({{"age": 30, "job": "工程师"}})
    >>> person
    {{'name': '张三', 'age': 30, 'job': '工程师'}}

{BD}四、遍历{END}
    >>> scores = {{"语文": 90, "数学": 85, "英语": 92}}

    >>> for key in scores:            # 遍历键
    ...     print(key, scores[key])
    ...
    语文 90
    数学 85
    英语 92

    >>> for key, value in scores.items():  # 同时遍历键和值（推荐！）
    ...     print(f"{{key}}：{{value}}分")
    ...
    语文：90分
    数学：85分
    英语：92分

    >>> for value in scores.values():      # 只遍历值
    ...     print(value)
    ...
    90
    85
    92

{BD}五、字典推导式 — 一行创建字典{END}
    >>> words = ["hello", "world", "python"]
    >>> word_lengths = {{w: len(w) for w in words}}
    >>> word_lengths
    {{'hello': 5, 'world': 5, 'python': 6}}

{C_}反转字典：{END}
    >>> scores = {{"张三": 90, "李四": 85}}
    >>> reversed_d = {{v: k for k, v in scores.items()}}
    >>> reversed_d
    {{90: '张三', 85: '李四'}}

{BD}六、嵌套字典{END}
    >>> students = {{
    ...     "张三": {{"age": 20, "score": 90}},
    ...     "李四": {{"age": 21, "score": 85}}
    ... }}
    >>> students["张三"]["score"]
    90

{BD}[!] 常见陷阱{END}
• 键不存在时 d[k] 报 KeyError，用 d.get(k) 更安全
• 遍历时修改字典大小会报 RuntimeError
• 键必须是不可变类型（字符串、数字、元组），列表不能做键
• 字典从 Python 3.7+ 是有序的（按插入顺序）


{BD}三、字典推导式{END}

{C_}快速创建字典{END}
    >>> # 列表转字典：元素做键，索引做值
    >>> fruits = ['apple', 'banana', 'orange']
    >>> d = {{f: i for i, f in enumerate(fruits)}}
    >>> print(d)
    {{'apple': 0, 'banana': 1, 'orange': 2}}

    >>> # 过滤并转换
    >>> scores = {{'a': 90, 'b': 60, 'c': 85}}
    >>> passed = {{k: v for k, v in scores.items() if v >= 80}}
    >>> print(passed)
    {{'a': 90, 'c': 85}}

{M}>> 动手试试！{END}
    # 统计字符出现次数
    text = "hello world"
    char_count = {{}}
    for ch in text:
        char_count[ch] = char_count.get(ch, 0) + 1
    print(char_count)
""", ["dict_create", "dict_access", "dict_methods", "dict_update"]),

    9: (f"""{B}阶段9：集合 — 去重和数学运算{END}

{C_}生活类比：集合就像一袋弹珠{END}
    • 每种弹珠只有一个（不重复）
    • 没有顺序（倒在桌上随便滚）
    • 可以找"两种弹珠的共有种类"（交集）

{BD}一、创建{END}
    >>> s = {{1, 2, 3}}
    >>> s
    {{1, 2, 3}}

    >>> # 从列表去重
    >>> s = set([1, 2, 2, 3, 3, 3])
    >>> s
    {{1, 2, 3}}

    >>> empty = set()          # 空集合
    >>> # 不能用 {{}}！那是空字典！
    >>> type({{}})
    <class 'dict'>
    >>> type(set())
    <class 'set'>

{BD}二、集合运算 — 数学课上的东西{END}

{C_}文氏图理解：{END}
        a = {{1, 2, 3}}    b = {{2, 3, 4}}
             ┌───┐              ┌───┐
           ╱ 1 ╲ 2,3 ╱ 4 ╲
           ╲    ╱    ╲    ╱
             └───┘              └───┘

    >>> a = {{1, 2, 3}}
    >>> b = {{2, 3, 4}}

    >>> a & b              # 交集：两者都有
    {{2, 3}}

    >>> a | b              # 并集：合在一起
    {{1, 2, 3, 4}}

    >>> a - b              # 差集：a有b没有
    {{1}}

    >>> a ^ b              # 对称差：只有一边有
    {{1, 4}}

{C_}子集和超集：{END}
    >>> {{1, 2}} <= {{1, 2, 3}}    # 子集
    True
    >>> {{1, 2, 3}} >= {{1, 2}}    # 超集
    True

{BD}三、常用方法{END}
    >>> s = {{1, 2, 3}}

    >>> s.add(5)             # 添加（已有则忽略）
    >>> s
    {{1, 2, 3, 5}}

    >>> s.remove(3)          # 删除（不存在会报错！）
    >>> s.discard(99)        # 删除（不存在不报错，更安全）

    >>> s.clear()            # 清空
    >>> len({{1, 2, 3}})     # 元素个数
    3

{BD}四、集合的实际用途{END}

{C_}1. 去重（最常见）{END}
    >>> names = ["张三", "李四", "张三", "王五", "李四"]
    >>> unique = list(set(names))
    >>> unique
    ['张三', '李四', '王五']    # 顺序可能不同

    # 保持原顺序去重
    >>> from collections import OrderedDict
    >>> unique_ordered = list(dict.fromkeys(names))
    >>> unique_ordered
    ['张三', '李四', '王五']

{C_}2. 成员检测（比列表快得多！）{END}
    >>> # 列表：逐个比较 → 慢
    >>> big_list = list(range(100000))
    >>> 99999 in big_list     # 要比较10万次

    >>> # 集合：哈希查找 → 快
    >>> big_set = set(range(100000))
    >>> 99999 in big_set      # 一次就找到！

{C_}3. 找两个列表的公共元素{END}
    >>> class_a = {{80, 85, 90, 95}}
    >>> class_b = {{85, 90, 100}}
    >>> class_a & class_b     # 两个班都有的分数
    {{85, 90}}

{BD}[!] 常见陷阱{END}
• 集合无序，不能索引访问：s[0] 会报 TypeError
• 空集合用 set()，不是 {{}}
• 集合元素必须是不可变类型（不能放列表）
• set() 去重后顺序不确定

{M}>> 动手试试！{END}
    # 找出两个字符串的公共字符
    s1 = set("python")
    s2 = set("typescript")
    common = s1 & s2
    print(f"公共字符：{{common}}")
    print(f"只在python中：{{s1 - s2}}")


{BD}五、集合运算方法（等价写法）{END}

{C_}运算符和方法两种写法都能用：{END}
    >>> a = {{1, 2, 3}}
    >>> b = {{2, 3, 4}}

    >>> a.intersection(b)        # 等价于 a & b（交集）
    {{2, 3}}
    >>> a.union(b)               # 等价于 a | b（并集）
    {{1, 2, 3, 4}}
    >>> a.difference(b)          # 等价于 a - b（差集）
    {{1}}
    >>> a.symmetric_difference(b) # 等价于 a ^ b（对称差集）
    {{1, 4}}

{C_}什么时候用方法？{END}
    当操作对象不是集合类型时，方法更灵活：
    >>> a.intersection([2, 3, 4, 5])   # 方法可以接受任意可迭代对象
    {{2, 3}}
    >>> a & set([2, 3, 4, 5])         # 运算符两边必须都是集合
    {{2, 3}}

{C_}原地修改运算（update 系列）：{END}
    >>> a = {{1, 2, 3}}
    >>> a.update({{3, 4, 5}})          # 等价于 a |= b
    >>> a
    {{1, 2, 3, 4, 5}}

    >>> a.intersection_update({{2, 3, 4}})  # 等价于 a &= b
    >>> a
    {{2, 3, 4}}

    >>> a.difference_update({{4}})     # 等价于 a -= b
    >>> a
    {{2, 3}}

{BD}六、frozenset — 不可变集合{END}

{C_}frozenset = 集合的"只读版本"{END}
    创建后不能添加、删除元素，但可以安全地：
    • 用作字典的键
    • 放入另一个集合中
    • 作为函数默认参数

    >>> fs = frozenset([1, 2, 3, 2, 1])
    >>> fs
    frozenset({{1, 2, 3}})

    >>> fs.add(4)            # AttributeError！不能修改
    >>> fs.remove(1)         # AttributeError！不能修改

    >>> # 可以做运算（返回新的 frozenset）
    >>> fs2 = frozenset([2, 3, 4])
    >>> fs & fs2             # 交集，返回 frozenset
    frozenset({{2, 3}})

    >>> # 当字典的键
    >>> d = {{frozenset([1, 2]): "值"}}
    >>> d[frozenset([1, 2])]
    '值'

{BD}七、集合推导式{END}

{C_}和列表推导式语法一样，换成花括号：{END}
    >>> # 列表推导式
    >>> [x**2 for x in range(5)]
    [0, 1, 4, 9, 16]

    >>> # 集合推导式 — 自动去重
    >>> {{x**2 for x in range(-3, 4)}}
    {{0, 1, 4, 9}}

    >>> # 实际场景：提取文本中的所有不同单词长度
    >>> words = ["hello", "world", "python", "hi", "code"]
    >>> {{len(w) for w in words}}
    {{2, 5, 6}}

    >>> # 带条件的集合推导式
    >>> {{x for x in range(20) if x % 3 == 0}}
    {{0, 3, 6, 9, 12, 15, 18}}

{BD}八、集合应用场景总结{END}

{C_}1. 数据去重{END}
    >>> raw = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    >>> unique = sorted(set(raw))    # 去重+排序
    >>> unique
    [1, 2, 3, 4, 5, 6, 9]

{C_}2. 权限判断{END}
    >>> admin_perms = {{'read', 'write', 'delete', 'create'}}
    >>> user_perms = {{'read', 'write'}}
    >>> user_perms.issubset(admin_perms)    # 用户权限是否在管理员范围内
    True
    >>> admin_perms.issuperset(user_perms)
    True

{C_}3. 找差异{END}
    >>> yesterday = {{'apple', 'banana', 'orange'}}
    >>> today = {{'apple', 'orange', 'grape'}}
    >>> added = today - yesterday      # 新增的
    >>> removed = yesterday - today    # 删除的
    >>> print(f"新增：{{added}}，删除：{{removed}}")
    新增：{{'grape'}}，删除：{{'banana'}}""", ["set_create", "set_ops", "set_methods"]),

    10: (f"""{B}阶段10：字符串 — 文本处理利器{END}

{C_}生活类比：字符串就像一条珠串{END}
    P - y - t - h - o - n
    0   1   2   3   4   5
   -6  -5  -4  -3  -2  -1
    每个字符是一颗珠子，可以单独取、切片取

{BD}一、基础操作{END}
    >>> s = "Hello, World!"
    >>> s[0]          # 第一个字符
    'H'
    >>> s[0:5]        # 前5个字符
    'Hello'
    >>> s[-1]         # 最后一个字符
    '!'
    >>> s[::-1]       # 反转
    '!dlroW ,olleH'
    >>> len(s)        # 长度
    13

{C_}字符串不可变！{END}
    >>> s = "hello"
    >>> s[0] = "H"    # TypeError！不能直接改
    >>> s = "H" + s[1:]   # 要创建新字符串
    >>> s
    'Hello'

{BD}二、常用方法{END}
    >>> s = "  Hello, World!  "

    >>> s.strip()              # 去首尾空白
    'Hello, World!'
    >>> s.lstrip()             # 只去左边
    'Hello, World!  '
    >>> s.rstrip()             # 只去右边
    '  Hello, World!'

    >>> "hello".upper()        # 转大写
    'HELLO'
    >>> "HELLO".lower()        # 转小写
    'hello'
    >>> "hello world".title()  # 首字母大写
    'Hello World'
    >>> "hello world".capitalize()  # 句首大写
    'Hello world'

{C_}分割和连接（一对好搭档）：{END}
    >>> "a,b,c,d".split(",")           # 分割 → 列表
    ['a', 'b', 'c', 'd']

    >>> "-".join(["a", "b", "c"])      # 连接列表 → 字符串
    'a-b-c'

    >>> "Hello World".split()          # 默认按空白分割
    ['Hello', 'World']

{C_}查找和替换：{END}
    >>> "hello world".find("world")    # 找位置（-1=不存在）
    6
    >>> "hello world".find("python")
    -1
    >>> "hello world".count("l")       # 计数
    3
    >>> "hello world".replace("world", "python")
    'hello python'

{BD}三、判断方法 — 返回 True/False{END}
    >>> "123".isdigit()        # 全是数字
    True
    >>> "abc".isalpha()        # 全是字母
    True
    >>> "abc123".isalnum()     # 字母或数字
    True
    >>> "hello".startswith("he")  # 以...开头
    True
    >>> "hello".endswith("lo")    # 以...结尾
    True
    >>> "   ".isspace()        # 全是空白
    True

{C_}实际场景：验证用户输入{END}
    >>> user_input = "13812345678"
    >>> if user_input.isdigit() and len(user_input) == 11:
    ...     print("有效的手机号")
    ...
    有效的手机号

{BD}四、格式化 — 三种方式{END}

{Y}1. f-string（推荐！Python 3.6+）{END}
    >>> name = "张三"
    >>> age = 25
    >>> f"我叫{{name}}，今年{{age}}岁"
    '我叫张三，今年25岁'

    >>> pi = 3.14159
    >>> f"{{pi:.2f}}"          # 保留2位小数
    '3.14'
    >>> f"{{10000:,}}"         # 千分位
    '10,000'
    >>> f"{{42:05d}}"          # 补零到5位
    '00042'
    >>> f"{{'hello':>10}}"     # 右对齐，宽度10
    '     hello'
    >>> f"{{'hello':<10}}"     # 左对齐
    'hello     '
    >>> f"{{'hello':^10}}"     # 居中
    '  hello   '

{Y}2. format() 方法{END}
    >>> "{{}}今年{{}}岁".format("张三", 25)
    '张三今年25岁'

{Y}3. % 格式化（老写法，了解即可）{END}
    >>> "我叫%s，今年%d岁" % ("张三", 25)
    '我叫张三，今年25岁'

{BD}五、正则表达式简介（re 模块）{END}

{C_}正则表达式是"超级搜索工具"，适合复杂文本匹配：{END}
    >>> import re
    >>> # 找出所有数字
    >>> re.findall(r'\\d+', "我有3个苹果和15个橙子")
    ['3', '15']

    >>> # 验证邮箱格式（简化版）
    >>> pattern = r'[\\w.]+@[\\w.]+\\.\\w+'
    >>> bool(re.match(pattern, "test@example.com"))
    True

    >>> # 替换所有数字为 #
    >>> re.sub(r'\\d', '#', "手机号13812345678")
    '手机号###########'

{C_}常用模式：{END}
    \\d    数字
    \\w    字母数字下划线
    \\s    空白字符
    .     任意字符
    *     前面0次或多次
    +     前面1次或多次
    {{m,n}}  前面m到n次

{BD}[!] 常见陷阱{END}
• 字符串不可变，方法返回新字符串（原字符串不变）
• split/join 是一对：split拆开，join连上
• 忘记 encoding="utf-8" 导致中文乱码
• strip() 只去首尾，不去中间

{M}>> 动手试试！{END}
    # 密码强度检查
    password = "MyPass123!"
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)
    score = sum([has_upper, has_lower, has_digit, has_symbol])
    print(f"强度：{{score}}/4")
""", ["str_methods", "str_format", "str_find", "str_check", "str_regex"]),

    11: (f"""{B}阶段11：文件读写 — 数据持久化{END}

{C_}生活类比：文件就像笔记本{END}
    内存 = 草稿纸（断电就没）
    文件 = 笔记本（写下来就能保存）

    你写程序时变量在内存里，关了程序就没了。
    文件读写就是把数据从草稿纸抄到笔记本上（或反过来）。

{BD}一、打开文件 — with 语句（推荐）{END}
    >>> # with 自动关闭文件，即使出错也不会忘关
    >>> with open("hello.txt", "w", encoding="utf-8") as f:
    ...     f.write("Hello World!\\n")
    ...
    >>> with open("hello.txt", "r", encoding="utf-8") as f:
    ...     content = f.read()
    ...
    >>> content
    'Hello World!\\n'

{C_}为什么用 with？{END}
    # 不用 with — 忘记 close 会出问题
    f = open("file.txt", "r")
    content = f.read()
    f.close()    # 如果上面出错，这行就不执行了！

    # 用 with — 自动 close，不用操心
    with open("file.txt", "r") as f:
        content = f.read()
    # 出了 with 块，文件自动关闭

{BD}二、模式{END}
    "r"   只读（默认）         文件不存在 → FileNotFoundError
    "w"   写入（覆盖）         文件不存在 → 创建新文件
    "a"   追加                 文件不存在 → 创建新文件
    "r+"  读写                 文件不存在 → FileNotFoundError
    "rb"  二进制读（图片等）
    "wb"  二进制写

{BD}三、读取{END}
    >>> # 1. read() — 一次读全部
    >>> with open("data.txt", "r", encoding="utf-8") as f:
    ...     content = f.read()      # 小文件用这个
    ...
    >>> # 2. readlines() — 每行一个元素
    >>> with open("data.txt", "r", encoding="utf-8") as f:
    ...     lines = f.readlines()   # 返回列表
    ...
    >>> # 3. 逐行读取（推荐！大文件省内存）
    >>> with open("data.txt", "r", encoding="utf-8") as f:
    ...     for line in f:
    ...         print(line.strip())  # strip() 去掉末尾换行
    ...

{C_}实际场景：统计文件行数{END}
    >>> with open("data.txt", "r", encoding="utf-8") as f:
    ...     count = sum(1 for line in f)
    ...
    >>> print(f"共{{count}}行")

{BD}四、写入{END}
    >>> # write() 不会自动加换行！
    >>> with open("output.txt", "w", encoding="utf-8") as f:
    ...     f.write("第一行\\n")     # 手动加 \\n
    ...     f.write("第二行\\n")
    ...

    >>> # writelines() 写入列表（也不自动加换行）
    >>> lines = ["行1\\n", "行2\\n", "行3\\n"]
    >>> with open("output.txt", "w", encoding="utf-8") as f:
    ...     f.writelines(lines)
    ...

{BD}五、文件检查{END}
    >>> import os
    >>> os.path.exists("data.txt")      # 文件/目录是否存在
    True
    >>> os.path.isfile("data.txt")      # 是否是文件
    True
    >>> os.path.isdir("my_folder")      # 是否是目录
    False
    >>> os.path.getsize("data.txt")     # 文件大小（字节）
    1024

{C_}实际场景：安全读取文件{END}
    >>> import os
    >>> filename = "data.txt"
    >>> if os.path.exists(filename):
    ...     with open(filename, "r", encoding="utf-8") as f:
    ...         content = f.read()
    ... else:
    ...     print("文件不存在！")

{BD}六、CSV 文件处理{END}

{C_}CSV = 逗号分隔值，表格数据最常用格式{END}
    >>> import csv
    >>> # 写入 CSV
    >>> with open("grades.csv", "w", encoding="utf-8", newline="") as f:
    ...     writer = csv.writer(f)
    ...     writer.writerow(["姓名", "成绩"])
    ...     writer.writerow(["张三", 90])
    ...     writer.writerow(["李四", 85])
    ...

    >>> # 读取 CSV
    >>> with open("grades.csv", "r", encoding="utf-8") as f:
    ...     reader = csv.reader(f)
    ...     for row in reader:
    ...         print(row)
    ...
    ['姓名', '成绩']
    ['张三', '90']
    ['李四', '85']

{BD}七、JSON 文件处理{END}

{C_}JSON = 最流行的数据交换格式，Python 字典的"亲戚"{END}
    >>> import json
    >>> # 写入 JSON
    >>> data = {{"name": "张三", "age": 25, "scores": [90, 85, 92]}}
    >>> with open("data.json", "w", encoding="utf-8") as f:
    ...     json.dump(data, f, ensure_ascii=False, indent=2)
    ...

    >>> # 读取 JSON
    >>> with open("data.json", "r", encoding="utf-8") as f:
    ...     loaded = json.load(f)
    ...
    >>> loaded["name"]
    '张三'
    >>> loaded["scores"]
    [90, 85, 92]

{C_}json.dumps() 和 json.loads() — 字符串版{END}
    >>> json_str = json.dumps({{"a": 1, "b": 2}}, ensure_ascii=False)
    >>> json_str
    '{{"a": 1, "b": 2}}'
    >>> json.loads(json_str)
    {{'a': 1, 'b': 2}}

{BD}[!] 常见陷阱{END}
• 忘记 encoding="utf-8" 会乱码（Windows 默认 GBK）
• "w" 模式会覆盖原文件！追加用 "a"
• write() 不会自动换行
• 大文件不要一次 read()，用逐行读取
• CSV 写入要加 newline="" 防止多空行

{M}>> 动手试试！{END}
    import json
    # 保存数据到文件再读回来
    data = {{"language": "Python", "version": 3.12, "features": ["简单", "强大"]}}
    with open("test.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with open("test.json", "r", encoding="utf-8") as f:
        loaded = json.load(f)
    print(loaded["features"])
""", ["file_open", "file_read", "file_write", "file_context", "file_csv", "file_json"]),

    12: (f"""{B}阶段12：异常处理 — 让程序更健壮{END}

{C_}生活类比：异常处理就像开车系安全带{END}
    没有安全带：出事故就完蛋（程序崩溃）
    有安全带：出事故能保护（程序继续运行）

    不写 try-except = 不系安全带 = 一个错误整崩程序
    写 try-except = 系安全带 = 出错了也能妥善处理

{BD}一、try-except — 基本用法{END}
    >>> try:
    ...     result = 10 / 0
    ... except:
    ...     print("出错了！")
    ...
    出错了！

{BD}二、捕获特定异常 — 精确处理{END}
    >>> try:
    ...     result = 10 / 0
    ... except ZeroDivisionError:
    ...     print("不能除以零！")
    ... except Exception as e:
    ...     print(f"其他错误：{{e}}")
    ...
    不能除以零！

{C_}为什么要捕获特定异常？{END}
    # 空 except — 什么错都吞掉，连想看到的错误也看不到！
    try:
        important_function()
    except:           # 不好！所有错误都被隐藏
        pass

    # 捕获特定异常 — 只处理预想的错误
    try:
        num = int(input("输入数字："))
    except ValueError:      # 只处理"输入不是数字"的情况
        print("请输入有效数字！")

{BD}三、常见异常类型{END}
    ValueError         值错误      int("abc")
    TypeError          类型错误    "3" + 1
    ZeroDivisionError  除以零      10 / 0
    IndexError         索引越界    [1,2][5]
    KeyError           键不存在    {{"a":1}}["b"]
    FileNotFoundError  文件不存在  open("不存在.txt")
    AttributeError     属性不存在  "hello".append()
    NameError          名字未定义  print(undefined_var)

{C_}实际场景：安全读取文件{END}
    >>> try:
    ...     with open("config.txt", "r", encoding="utf-8") as f:
    ...         config = f.read()
    ... except FileNotFoundError:
    ...     print("配置文件不存在，使用默认配置")
    ...     config = "default"
    ...

{C_}实际场景：安全类型转换{END}
    >>> def safe_int(value, default=0):
    ...     try:
    ...         return int(value)
    ...     except (ValueError, TypeError):
    ...         return default
    ...
    >>> safe_int("123")
    123
    >>> safe_int("abc")
    0
    >>> safe_int(None)
    0

{BD}四、else 和 finally{END}
    >>> try:
    ...     f = open("data.txt", "r", encoding="utf-8")
    ... except FileNotFoundError:
    ...     print("文件不存在")
    ... else:
    ...     # 没有异常时执行
    ...     content = f.read()
    ...     f.close()
    ... finally:
    ...     # 无论如何都执行（清理工作）
    ...     print("操作完成")
    ...

{C_}finally 的典型用途：{END}
    try:
        f = open("data.txt", "r")
        # 操作文件...
    finally:
        f.close()    # 无论是否出错，都要关闭文件
        # （不过用 with 更好！）

{BD}五、raise — 主动抛出异常{END}
    >>> def set_age(age):
    ...     if age < 0:
    ...         raise ValueError("年龄不能为负数")
    ...     if age > 150:
    ...         raise ValueError("年龄不合理")
    ...     return age
    ...
    >>> set_age(-5)
    Traceback (most recent call last):
      ...
    ValueError: 年龄不能为负数

{BD}六、自定义异常 — 为你的项目定制{END}
    >>> class InvalidScoreError(Exception):
    ...     \"\"\"成绩无效时抛出\"\"\"
    ...     def __init__(self, score, message="成绩无效"):
    ...         self.score = score
    ...         self.message = f"{{message}}：{{score}}"
    ...         super().__init__(self.message)
    ...
    >>> def check_score(score):
    ...     if not 0 <= score <= 100:
    ...         raise InvalidScoreError(score, "成绩必须在0-100之间")
    ...     return score
    ...
    >>> try:
    ...     check_score(150)
    ... except InvalidScoreError as e:
    ...     print(e)
    ...
    成绩必须在0-100之间：150

{C_}自定义异常的继承体系（进阶了解）：{END}
    class AppError(Exception):
        \"\"\"应用基础异常\"\"\"
        pass

    class NetworkError(AppError):
        \"\"\"网络相关异常\"\"\"
        pass

    class DatabaseError(AppError):
        \"\"\"数据库相关异常\"\"\"
        pass

    # 可以统一捕获：except AppError:
    # 也可以分别捕获：except NetworkError:

{BD}[!] 常见陷阱{END}
• 不要用空 except:，至少 except Exception:
• 捕获特定异常比捕获所有异常好
• 有些情况 if 判断比 try-except 更合适（EAFP vs LBYL）
• raise 不是 return，函数不会继续执行
• 自定义异常继承 Exception，不是 BaseException

{M}>> 动手试试！{END}
    # 安全的计算器
    def safe_calculate(expr):
        try:
            result = eval(expr)   # 注意：实际项目别用 eval！
            return result
        except ZeroDivisionError:
            return "错误：除以零"
        except SyntaxError:
            return "错误：表达式无效"
        except Exception as e:
            return f"未知错误：{{e}}"

    print(safe_calculate("10 / 2"))
    print(safe_calculate("10 / 0"))
    print(safe_calculate("abc"))
""", ["try_except", "exception_types", "raise_error", "custom_exception"]),

    13: (f"""{B}阶段13：综合实战 — 模块、JSON、datetime{END}

{C_}本阶段学习项目所需的关键模块，然后综合运用完成实战项目{END}

{BD}一、模块 — 使用别人的代码{END}

{C_}生活类比：模块就像工具箱{END}
    你不需要自己造锤子，import 一个工具箱就行

    >>> import math
    >>> math.sqrt(16)       # 平方根
    4.0
    >>> math.pi             # 圆周率
    3.141592653589793
    >>> math.ceil(3.2)      # 向上取整
    4
    >>> math.floor(3.8)     # 向下取整
    3

    >>> import random
    >>> random.randint(1, 10)       # 1到10的随机整数
    7
    >>> random.choice(["苹果","香蕉","橙子"])  # 随机选一个
    '香蕉'
    >>> random.shuffle([1,2,3,4,5]) # 打乱顺序

{C_}from ... import ... — 只拿需要的工具{END}
    >>> from math import sqrt, pi
    >>> sqrt(9)        # 不用写 math.sqrt 了
    3.0

    >>> from datetime import datetime
    >>> datetime.now()
    datetime(2026, 5, 2, 12, 0, 0)

{BD}二、JSON — 数据存储的最佳搭档{END}

{C_}JSON 就像 Python 字典的"通用语言版"{END}
    Python 字典和 JSON 长得几乎一样，但有几个小区别：

    Python                    JSON
    True/False        →       true/false
    None              →       null
    单引号 'str'      →       双引号 "str"

    >>> import json
    >>> # Python 对象 → JSON 字符串
    >>> data = {{"name": "张三", "scores": [90, 85]}}
    >>> json_str = json.dumps(data, ensure_ascii=False, indent=2)
    >>> print(json_str)
    {{
      "name": "张三",
      "scores": [90, 85]
    }}

    >>> # JSON 字符串 → Python 对象
    >>> loaded = json.loads(json_str)
    >>> loaded["name"]
    '张三'

{C_}JSON 文件读写（持久化！）：{END}
    >>> # 保存到文件
    >>> with open("save.json", "w", encoding="utf-8") as f:
    ...     json.dump(data, f, ensure_ascii=False, indent=2)
    ...

    >>> # 从文件读取
    >>> with open("save.json", "r", encoding="utf-8") as f:
    ...     loaded = json.load(f)
    ...

{C_}ensure_ascii=False 很重要！{END}
    没有它，中文会变成 \\uXXXX 转义序列
    >>> json.dumps({{"名字": "张三"}})              # 有中文
    '{{"\\u540d\\u5b57": "\\u5f20\\u4e09"}}'        # 不可读！
    >>> json.dumps({{"名字": "张三"}}, ensure_ascii=False)
    '{{"名字": "张三"}}'                            # 可读！

{BD}三、datetime — 时间日期处理{END}
    >>> from datetime import datetime, date, timedelta

    >>> # 当前时间
    >>> now = datetime.now()
    >>> now
    datetime(2026, 5, 2, 12, 0, 0)
    >>> now.year, now.month, now.day
    (2026, 5, 2)

    >>> # 格式化输出
    >>> now.strftime("%Y年%m月%d日 %H:%M")
    '2026年05月02日 12:00'

    >>> # 解析字符串为日期
    >>> dt = datetime.strptime("2026-01-15", "%Y-%m-%d")
    >>> dt
    datetime(2026, 1, 15, 0, 0)

    >>> # 日期计算
    >>> today = date.today()
    >>> tomorrow = today + timedelta(days=1)
    >>> week_later = today + timedelta(weeks=1)
    >>> diff = date(2026, 12, 31) - date(2026, 5, 2)
    >>> diff.days
    243

{C_}常用格式符号：{END}
    %Y  四位年份   2026
    %m  月份       01-12
    %d  日期       01-31
    %H  小时(24)   00-23
    %M  分钟       00-59
    %S  秒         00-59

{BD}四、os 模块 — 操作系统交互{END}
    >>> import os
    >>> os.getcwd()              # 当前工作目录
    'C:\\\\Users\\\\demo'
    >>> os.listdir(".")          # 列出当前目录文件
    ['data.txt', 'script.py']
    >>> os.makedirs("output", exist_ok=True)   # 创建目录
    >>> os.path.join("folder", "file.txt")     # 拼接路径
    'folder\\\\file.txt'

{BD}五、综合项目：命令行记账本{END}

{C_}设计思路：{END}
    数据结构：{{"date": "2026-05-02", "type": "支出", "category": "餐饮",
              "amount": 35.5, "note": "午餐"}}

    功能划分：
    ┌──────────────────────────────┐
    │ 1. 添加账目                   │
    │ 2. 查看所有账目               │
    │ 3. 统计收支                   │
    │ 4. 按分类统计                 │
    │ 5. 保存到JSON / 从JSON加载    │
    └──────────────────────────────┘

{C_}核心代码结构：{END}
    import json
    from datetime import datetime

    DATA_FILE = "records.json"

    def load_data():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_data(records):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)

    def add_record(records):
        record = {{
            "date": datetime.now().strftime("%Y-%m-%d"),
            "type": input("收入/支出："),
            "category": input("分类："),
            "amount": float(input("金额：")),
            "note": input("备注：")
        }}
        records.append(record)
        save_data(records)    # 每次添加都保存！

{BD}[!] 常见陷阱{END}
• 退出程序时忘记保存数据
• 用户输入没有做校验（金额输入abc会崩溃）
• 金额用浮点数有精度问题（0.1 + 0.2 != 0.3），精确计算用 Decimal
• 忘记 ensure_ascii=False，中文变乱码

{M}>> 动手试试！{END}
    import json
    from datetime import datetime, timedelta

    # 试试日期计算
    today = datetime.now()
    birthday = datetime(2026, 12, 25)
    days_left = (birthday - today).days
    print(f"距离生日还有{{days_left}}天")

    # 试试 JSON 序列化
    record = {{"date": today.strftime("%Y-%m-%d"), "event": "学Python"}}
    print(json.dumps(record, ensure_ascii=False, indent=2))
""", ["import_module", "json_io", "datetime_mod", "os_module", "custom_exception"]),
}
