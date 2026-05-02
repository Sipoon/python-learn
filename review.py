"""复习关卡 - v5.0 六大篇章"""
from typing import Dict, List

REVIEW_STAGES: Dict[int, Dict] = {
    # 第一篇复习
    3: {
        "name": "阶段1-3 复习：基础关",
        "desc": "变量、运算符、条件语句 — 这些是最基础的工具",
        "exercises": [
            {
                "q": "创建变量 name='Python' 和 version=3，用 f-string 打印 'Python3'",
                "hint": "f'{name}{version}'",
                "kp": ["var_create", "str_format"],
                "diff": "basic",
                "answer": 'name = "Python"\nversion = 3\nprint(f"{name}{version}")',
                "expected": "Python3",
            },
            {
                "q": "输入一个数字 score，如果>=90打印'A'，>=60打印'B'，否则打印'C'",
                "hint": "if-elif-else",
                "kp": ["if_elif", "var_create"],
                "diff": "intermediate",
                "answer": 'score = 85\nif score >= 90:\n    print("A")\nelif score >= 60:\n    print("B")\nelse:\n    print("C")',
                "expected": "B",
            },
            {
                "q": "计算 1+2+...+100 的和，用循环实现",
                "hint": "total = 0; for i in range(1, 101): total += i",
                "kp": ["for_loop", "op_arithmetic"],
                "diff": "intermediate",
                "answer": 'total = 0\nfor i in range(1, 101):\n    total += i\nprint(total)',
                "expected": "5050",
            },
            {
                "q": "判断一个数是奇数还是偶数，打印 'odd' 或 'even'",
                "hint": "x % 2 == 0 就是偶数",
                "kp": ["op_arithmetic", "if_else"],
                "diff": "basic",
                "answer": 'x = 7\nif x % 2 == 0:\n    print("even")\nelse:\n    print("odd")',
                "expected": "odd",
            },
        ],
    },
    6: {
        "name": "阶段4-6 复习：循环与函数关",
        "desc": "循环、函数、列表 — 编程的核心武器",
        "exercises": [
            {
                "q": "写函数 is_prime(n) 判断素数，测试 is_prime(17) 和 is_prime(18)",
                "hint": "2到sqrt(n)检查能否整除",
                "kp": ["func_def", "for_loop", "op_arithmetic"],
                "diff": "intermediate",
                "answer": 'def is_prime(n):\n    if n < 2:\n        return False\n    for i in range(2, int(n**0.5)+1):\n        if n % i == 0:\n            return False\n    return True\n\nprint(is_prime(17))\nprint(is_prime(18))',
                "expected": "True\nFalse",
            },
            {
                "q": "用列表推导式生成1-20中所有3的倍数",
                "hint": "[x for x in range(1,21) if x%3==0]",
                "kp": ["list_comprehension", "op_arithmetic"],
                "diff": "basic",
                "answer": 'result = [x for x in range(1, 21) if x % 3 == 0]\nprint(result)',
                "expected": "[3, 6, 9, 12, 15, 18]",
            },
            {
                "q": "写函数 remove_duplicates(lst) 去除列表中的重复元素，保持原序",
                "hint": "用 set 记录见过的元素",
                "kp": ["func_def", "list_methods"],
                "diff": "challenge",
                "answer": 'def remove_duplicates(lst):\n    seen = set()\n    result = []\n    for item in lst:\n        if item not in seen:\n            seen.add(item)\n            result.append(item)\n    return result\n\nprint(remove_duplicates([1, 3, 2, 3, 1, 4]))',
                "expected": "[1, 3, 2, 4]",
            },
            {
                "q": "用 while 循环实现猜数字：从1猜到目标数7，每次打印猜测值",
                "hint": "guess=1; while guess!=target: guess+=1",
                "kp": ["while_loop", "if_else"],
                "diff": "basic",
                "answer": 'target = 7\nguess = 1\nwhile guess != target:\n    print(f"guessing {guess}")\n    guess += 1\nprint(f"found {guess}")',
                "expected": "",
            },
        ],
    },
    9: {
        "name": "阶段7-9 复习：数据结构关",
        "desc": "元组、字典、集合 — 数据的组织方式",
        "exercises": [
            {
                "q": "用字典统计字符串 'hello world' 中每个字符出现的次数",
                "hint": "遍历字符，dict.get(char, 0)+1",
                "kp": ["dict_methods", "for_loop"],
                "diff": "intermediate",
                "answer": 's = "hello world"\ncounts = {}\nfor ch in s:\n    counts[ch] = counts.get(ch, 0) + 1\nprint(counts["l"])',
                "expected": "3",
            },
            {
                "q": "用集合找出两个列表 [1,2,3,4,5] 和 [3,4,5,6,7] 的交集和并集",
                "hint": "set(a) & set(b), set(a) | set(b)",
                "kp": ["set_ops", "set_create"],
                "diff": "basic",
                "answer": 'a = [1, 2, 3, 4, 5]\nb = [3, 4, 5, 6, 7]\nprint(sorted(set(a) & set(b)))\nprint(sorted(set(a) | set(b)))',
                "expected": "[3, 4, 5]\n[1, 2, 3, 4, 5, 6, 7]",
            },
            {
                "q": "元组解包：points = [(1,2), (3,4), (5,6)]，打印所有x坐标之和",
                "hint": "sum(x for x, y in points)",
                "kp": ["tuple_unpack", "for_loop"],
                "diff": "intermediate",
                "answer": 'points = [(1, 2), (3, 4), (5, 6)]\ntotal_x = sum(x for x, y in points)\nprint(total_x)',
                "expected": "9",
            },
        ],
    },
    12: {
        "name": "阶段10-12 复习：字符串与异常关",
        "desc": "字符串方法、文件、异常 — 处理真实数据",
        "exercises": [
            {
                "q": "写函数 count_words(text) 统计文本中单词数量",
                "hint": "text.split() 按空格分词，len() 计数",
                "kp": ["str_methods", "func_def"],
                "diff": "basic",
                "answer": 'def count_words(text):\n    return len(text.split())\n\nprint(count_words("hello world python"))',
                "expected": "3",
            },
            {
                "q": "写安全除法函数 safe_divide(a,b)，除零时返回 None 而不报错",
                "hint": "try-except ZeroDivisionError",
                "kp": ["try_except", "func_def"],
                "diff": "intermediate",
                "answer": 'def safe_divide(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return None\n\nprint(safe_divide(10, 3))\nprint(safe_divide(10, 0))',
                "expected": "3.3333333333333335\nNone",
            },
            {
                "q": "将列表 [3, 1, 4, 1, 5] 转为字符串 '3-1-4-1-5'",
                "hint": "'-'.join(str(x) for x in lst)",
                "kp": ["str_methods", "list_iter"],
                "diff": "basic",
                "answer": 'lst = [3, 1, 4, 1, 5]\nresult = "-".join(str(x) for x in lst)\nprint(result)',
                "expected": "3-1-4-1-5",
            },
        ],
    },
    13: {
        "name": "阶段13 复习：正则表达式关",
        "desc": "正则表达式 — 文本处理的瑞士军刀",
        "exercises": [
            {
                "q": "用正则提取字符串 '联系方式：010-12345678' 中的电话号码",
                "hint": "re.search(r'\\d{3}-\\d{8}', s)",
                "kp": ["regex_search", "regex_charset"],
                "diff": "basic",
                "answer": 'import re\ns = "联系方式：010-12345678"\nresult = re.search(r"\\d{3}-\\d{8}", s)\nprint(result.group())',
                "expected": "010-12345678",
            },
            {
                "q": "用正则将 'hello   world   python' 中的多个空格替换为单个",
                "hint": "re.sub(r'\\s+', ' ', s)",
                "kp": ["regex_sub", "regex_quantifier"],
                "diff": "intermediate",
                "answer": 'import re\ns = "hello   world   python"\nresult = re.sub(r"\\s+", " ", s)\nprint(result)',
                "expected": "hello world python",
            },
            {
                "q": "用正则验证邮箱格式：判断 'test@example.com' 和 'not-email' 是否合法",
                "hint": "re.match(r'[\\w.]+@[\\w.]+\\.\\w+', s)",
                "kp": ["regex_match", "regex_charset"],
                "diff": "challenge",
                "answer": 'import re\ndef is_valid_email(s):\n    return bool(re.match(r"[\\w.]+@[\\w.]+\\.\\w+", s))\n\nprint(is_valid_email("test@example.com"))\nprint(is_valid_email("not-email"))',
                "expected": "True\nFalse",
            },
        ],
    },

    # 第二篇复习
    16: {
        "name": "阶段14-16 复习：正则与OOP关",
        "desc": "正则表达式、面向对象基础与进阶",
        "exercises": [
            {
                "q": "用正则提取字符串 'abc123def456' 中的所有数字",
                "hint": "re.findall(r'\\d+', s)",
                "kp": ["regex_basic", "regex_charset"],
                "diff": "basic",
                "answer": 'import re\ns = "abc123def456"\nnumbers = re.findall(r"\\d+", s)\nprint(numbers)',
                "expected": "['123', '456']",
            },
            {
                "q": "定义 Circle 类，有 radius 属性和 area() 方法，计算面积",
                "hint": "area = 3.14159 * r * r",
                "kp": ["oop_class_object", "oop_init_self"],
                "diff": "intermediate",
                "answer": 'class Circle:\n    def __init__(self, radius):\n        self.radius = radius\n    def area(self):\n        return 3.14159 * self.radius ** 2\n\nc = Circle(5)\nprint(f"{c.area():.2f}")',
                "expected": "78.54",
            },
            {
                "q": "实现 Dog 继承 Animal，Animal 有 speak() 返回 '...'，Dog 覆盖返回 'Woof!'",
                "hint": "class Dog(Animal): def speak(self): return 'Woof!'",
                "kp": ["oop_inheritance", "oop_polymorphism"],
                "diff": "challenge",
                "answer": 'class Animal:\n    def speak(self):\n        return "..."\n\nclass Dog(Animal):\n    def speak(self):\n        return "Woof!"\n\nd = Dog()\nprint(d.speak())',
                "expected": "Woof!",
            },
        ],
    },
    18: {
        "name": "阶段17-18 复习：模块与装饰器关",
        "desc": "模块、包、生成器、装饰器",
        "exercises": [
            {
                "q": "写装饰器 timer，在函数执行前后打印 'start' 和 'end'",
                "hint": "def timer(func): def wrapper(*a,**k): print('start'); result=func(*a,**k); print('end'); return result; return wrapper",
                "kp": ["dec_basic", "func_def"],
                "diff": "intermediate",
                "answer": 'def timer(func):\n    def wrapper(*args, **kwargs):\n        print("start")\n        result = func(*args, **kwargs)\n        print("end")\n        return result\n    return wrapper\n\n@timer\ndef greet():\n    print("hello")\n\ngreet()',
                "expected": "",
            },
            {
                "q": "写生成器函数 countdown(n)，从 n 倒数到 1，每次 yield 一个数",
                "hint": "while n > 0: yield n; n -= 1",
                "kp": ["gen_yield", "while_loop"],
                "diff": "basic",
                "answer": 'def countdown(n):\n    while n > 0:\n        yield n\n        n -= 1\n\nprint(list(countdown(5)))',
                "expected": "[5, 4, 3, 2, 1]",
            },
            {
                "q": "实现一个上下文管理器 Timer，用 with 语句测量代码块执行时间",
                "hint": "定义 __enter__ 和 __exit__",
                "kp": ["ctx_manager", "oop_class_object"],
                "diff": "challenge",
                "answer": 'import time\n\nclass Timer:\n    def __enter__(self):\n        self.start = time.time()\n        return self\n    def __exit__(self, *args):\n        self.elapsed = time.time() - self.start\n        print(f"Elapsed: {self.elapsed:.4f}s")\n\nwith Timer():\n    sum(range(100000))',
                "expected": "",
            },
        ],
    },

    # 第三篇复习
    21: {
        "name": "阶段19-21 复习：工程基础关",
        "desc": "数据库、测试、API — 工程化基础",
        "exercises": [
            {
                "q": "用 sqlite3 创建内存数据库，建表并插入一条数据，查询打印",
                "hint": "sqlite3.connect(':memory:')",
                "kp": ["db_sqlite", "file_context"],
                "diff": "basic",
                "answer": 'import sqlite3\nconn = sqlite3.connect(":memory:")\nc = conn.cursor()\nc.execute("CREATE TABLE t (name TEXT, age INTEGER)")\nc.execute("INSERT INTO t VALUES (?, ?)", ("Alice", 20))\nconn.commit()\nprint(c.execute("SELECT * FROM t").fetchone())',
                "expected": "('Alice', 20)",
            },
            {
                "q": "写 pytest 风格的测试函数 test_upper()，测试 'hello'.upper() == 'HELLO'",
                "hint": "def test_upper(): assert 'hello'.upper() == 'HELLO'",
                "kp": ["test_pytest", "str_methods"],
                "diff": "basic",
                "answer": 'def test_upper():\n    assert "hello".upper() == "HELLO"\n\ntest_upper()\nprint("pass")',
                "expected": "pass",
            },
            {
                "q": "定义 Pydantic 模型 User（name:str, age:int=0），创建实例并打印",
                "hint": "from pydantic import BaseModel; class User(BaseModel): ...",
                "kp": ["api_pydantic", "oop_class_object"],
                "diff": "intermediate",
                "answer": 'class User:\n    def __init__(self, name, age=0):\n        self.name = name\n        self.age = age\n    def __repr__(self):\n        return f"User({self.name}, {self.age})"\n\nu = User("Alice", 20)\nprint(u)',
                "expected": "User(Alice, 20)",
            },
        ],
    },

    # 第四篇复习
    25: {
        "name": "阶段22-25 复习：数据方向关",
        "desc": "爬虫、pandas、可视化、浏览器自动化",
        "exercises": [
            {
                "q": "用 BeautifulSoup 解析 '<ul><li>A</li><li>B</li></ul>'，提取所有 li 文本",
                "hint": "soup.find_all('li')",
                "kp": ["crawl_beautifulsoup", "list_iter"],
                "diff": "basic",
                "answer": 'from bs4 import BeautifulSoup\nhtml = "<ul><li>A</li><li>B</li></ul>"\nsoup = BeautifulSoup(html, "html.parser")\nitems = [li.text for li in soup.find_all("li")]\nprint(items)',
                "expected": "['A', 'B']",
            },
            {
                "q": "创建 DataFrame 并筛选 score>80 的行",
                "hint": "df[df['score'] > 80]",
                "kp": ["pandas_dataframe", "pandas_select"],
                "diff": "intermediate",
                "answer": 'import pandas as pd\ndf = pd.DataFrame({"name": ["A", "B", "C"], "score": [90, 75, 85]})\nresult = df[df["score"] > 80]\nprint(list(result["name"]))',
                "expected": "['A', 'C']",
            },
            {
                "q": "用 asyncio.gather 并发执行两个 async 函数（各 sleep 0.1秒），验证总耗时<0.3秒",
                "hint": "async def task(): await asyncio.sleep(0.1); return 'done'",
                "kp": ["async_gather", "async_def"],
                "diff": "challenge",
                "answer": 'import asyncio\nimport time\n\nasync def task(name):\n    await asyncio.sleep(0.01)\n    return f"{name}_done"\n\nasync def main():\n    results = await asyncio.gather(task("A"), task("B"))\n    print(sorted(results))\n\nasyncio.run(main())',
                "expected": "['A_done', 'B_done']",
            },
        ],
    },
    29: {
        "name": "阶段26-29 复习：数据方向综合关",
        "desc": "异步、爬虫高级、工程化、综合实战",
        "exercises": [
            {
                "q": "用 aiohttp 异步获取一个URL的状态码（模拟即可）",
                "hint": "async with session.get(url) as resp: resp.status",
                "kp": ["async_aiohttp", "async_def"],
                "diff": "basic",
                "answer": 'import asyncio\n\nasync def mock_fetch(url):\n    await asyncio.sleep(0.01)\n    return 200\n\nasync def main():\n    status = await mock_fetch("https://example.com")\n    print(status)\n\nasyncio.run(main())',
                "expected": "200",
            },
            {
                "q": "用 hashlib 计算 'hello' 的 MD5 哈希值",
                "hint": "hashlib.md5(s.encode()).hexdigest()",
                "kp": ["crawl_redis", "import_module"],
                "diff": "intermediate",
                "answer": 'import hashlib\nresult = hashlib.md5("hello".encode()).hexdigest()\nprint(result)',
                "expected": "5d41402abc4b2a76b9719d911017c592",
            },
            {
                "q": "写数据清洗函数：去除列表中的 None 和空字符串",
                "hint": "[x for x in lst if x is not None and x != '']",
                "kp": ["data_cleaning", "list_comprehension"],
                "diff": "basic",
                "answer": 'def clean_data(lst):\n    return [x for x in lst if x is not None and x != ""]\n\nprint(clean_data([1, None, "", "hello", 0]))',
                "expected": "[1, 'hello', 0]",
            },
        ],
    },

    # 第五篇复习
    33: {
        "name": "阶段30-33 复习：自动化与桌面关",
        "desc": "脚本自动化、桌面自动化、GUI、综合实战",
        "exercises": [
            {
                "q": "用 pathlib 列出当前目录下所有 .py 文件的文件名",
                "hint": "Path('.').glob('*.py')",
                "kp": ["auto_pathlib", "for_loop"],
                "diff": "basic",
                "answer": 'from pathlib import Path\nnames = [p.name for p in Path(".").glob("*.py")]\nprint(type(names).__name__)',
                "expected": "list",
            },
            {
                "q": "用 tkinter 创建窗口，标题为 'Test'，打印窗口标题",
                "hint": "root = tk.Tk(); root.title('Test'); print(root.title())",
                "kp": ["gui_tkinter", "import_module"],
                "diff": "intermediate",
                "answer": 'import tkinter as tk\nroot = tk.Tk()\nroot.title("Test")\nprint(root.title())\nroot.destroy()',
                "expected": "Test",
            },
            {
                "q": "写一个函数批量重命名：给文件名列表加前缀 'new_'",
                "hint": "[f'new_{name}' for name in names]",
                "kp": ["auto_batch_rename", "list_comprehension"],
                "diff": "basic",
                "answer": 'def batch_rename(names, prefix="new_"):\n    return [f"{prefix}{name}" for name in names]\n\nprint(batch_rename(["a.txt", "b.txt"]))',
                "expected": "['new_a.txt', 'new_b.txt']",
            },
        ],
    },

    # 第六篇复习
    37: {
        "name": "阶段34-37 复习：架构与算法关",
        "desc": "设计模式、算法基础、算法进阶、综合实战",
        "exercises": [
            {
                "q": "用二分查找在 [2,4,6,8,10,12,14] 中找 8，返回索引",
                "hint": "lo=0, hi=len-1, mid比较",
                "kp": ["algo_search", "while_loop"],
                "diff": "basic",
                "answer": 'def binary_search(arr, target):\n    lo, hi = 0, len(arr)-1\n    while lo <= hi:\n        mid = (lo+hi)//2\n        if arr[mid] == target: return mid\n        elif arr[mid] < target: lo = mid+1\n        else: hi = mid-1\n    return -1\n\nprint(binary_search([2,4,6,8,10,12,14], 8))',
                "expected": "3",
            },
            {
                "q": "用 DP 计算 [1,2,3,1] 房屋偷窃问题（不能偷相邻房屋）的最大金额",
                "hint": "dp[i] = max(dp[i-1], dp[i-2]+nums[i])",
                "kp": ["algo_dp", "list_index"],
                "diff": "intermediate",
                "answer": 'def rob(nums):\n    if not nums: return 0\n    if len(nums) <= 2: return max(nums)\n    dp = [0]*len(nums)\n    dp[0] = nums[0]\n    dp[1] = max(nums[0], nums[1])\n    for i in range(2, len(nums)):\n        dp[i] = max(dp[i-1], dp[i-2]+nums[i])\n    return dp[-1]\n\nprint(rob([1,2,3,1]))',
                "expected": "4",
            },
            {
                "q": "实现工厂模式：ShapeFactory 根据 type 创建 Circle(radius) 或 Rectangle(w,h)，计算面积",
                "hint": "工厂函数返回对象，对象有 area() 方法",
                "kp": ["pattern_factory", "oop_class_object"],
                "diff": "challenge",
                "answer": 'class Circle:\n    def __init__(self, r): self.r = r\n    def area(self): return 3.14159 * self.r ** 2\n\nclass Rectangle:\n    def __init__(self, w, h): self.w = w; self.h = h\n    def area(self): return self.w * self.h\n\ndef shape_factory(shape_type, **kwargs):\n    if shape_type == "circle": return Circle(kwargs["r"])\n    elif shape_type == "rect": return Rectangle(kwargs["w"], kwargs["h"])\n\nc = shape_factory("circle", r=2)\nprint(f"{c.area():.2f}")',
                "expected": "12.57",
            },
        ],
    },
}
