"""实战项目数据 - v5.0"""
from typing import Dict

PROJECTS: Dict = {1: {'answer': '# 温度转换器\ncelsius = 25\nfahrenheit = celsius * 9 / 5 + 32\nprint(f"{celsius}C = {fahrenheit}F")',
     'desc': '将摄氏度转换为华氏度',
     'expected': '25C = 77.0F',
     'kp': ['var_create', 'type_float', 'op_arithmetic', 'print_basic'],
     'name': '温度转换器',
     'requirements': ['创建变量 celsius = 25', '用公式 F = C * 9/5 + 32 计算', '用 f-string 打印："25C = 77.0F"']},
 2: {'answer': '# 个人财务计算器\n'
               'salary = 15000\n'
               'rent = 4500\n'
               'food = 2000\n'
               'transport = 500\n'
               'total_expense = rent + food + transport\n'
               'savings = salary - total_expense\n'
               'rate = savings / salary * 100\n'
               'print(f"月薪：{salary} 元")\n'
               'print(f"总支出：{total_expense} 元")\n'
               'print(f"储蓄：{savings} 元")\n'
               'print(f"储蓄率：{rate:.1f}%")',
     'desc': '计算月收支和储蓄率',
     'expected': '月薪：15000 元\n总支出：7000 元\n储蓄：8000 元\n储蓄率：53.3%',
     'kp': ['var_create', 'op_arithmetic', 'op_assign', 'print_basic'],
     'name': '个人财务计算器',
     'requirements': ['月薪 salary = 15000', '支出：房租 4500，餐饮 2000，交通 500', '计算总支出、储蓄、储蓄率']},
 3: {'answer': '# 猜数游戏\n'
               'secret = 7\n'
               'guess = int(input("猜一个数字："))\n'
               'if guess == secret:\n'
               '    print("恭喜你猜对了！")\n'
               'elif guess > secret:\n'
               '    print("太大了")\n'
               'else:\n'
               '    print("太小了")',
     'desc': '让用户猜一个数字，给出提示',
     'expected': '太小了',
     'kp': ['var_create', 'if_elif', 'op_compare'],
     'name': '猜数游戏（单次版）',
     'requirements': ['秘密数字 secret = 7', '获取用户猜测（模拟输入 5）', '猜对/大了/小了分别打印不同提示'],
     'test_input': '5\n'},
 4: {'answer': '# 乘法表生成器\n'
               'for i in range(1, 10):\n'
               '    for j in range(1, i + 1):\n'
               '        print(f"{j}x{i}={i*j}", end="  ")\n'
               '    print()',
     'desc': '打印 9x9 乘法表',
     'kp': ['for_loop', 'range_func', 'nested_loop'],
     'name': '乘法表生成器',
     'requirements': ['用嵌套循环打印乘法表', '格式：1x1=1  1x2=2 ...']},
 5: {'answer': '# BMI 计算器\n'
               'def calculate_bmi(weight, height):\n'
               '    return weight / (height ** 2)\n'
               '\n'
               'def bmi_category(bmi):\n'
               '    if bmi < 18.5:\n'
               '        return "偏瘦"\n'
               '    elif bmi < 25:\n'
               '        return "正常"\n'
               '    elif bmi < 30:\n'
               '        return "偏胖"\n'
               '    else:\n'
               '        return "肥胖"\n'
               '\n'
               'weight = float(input("体重(kg)："))\n'
               'height = float(input("身高(m)："))\n'
               'bmi = calculate_bmi(weight, height)\n'
               'category = bmi_category(bmi)\n'
               'print(f"BMI: {bmi:.1f}")\n'
               'print(f"分类: {category}")',
     'desc': '计算 BMI 并给出分类',
     'expected': 'BMI: 22.9\n分类: 正常',
     'kp': ['func_def', 'func_return', 'if_elif'],
     'name': 'BMI 计算器',
     'requirements': ['定义函数 calculate_bmi(weight, height)', '定义函数 bmi_category(bmi) 返回分类', '输入体重70kg，身高1.75m'],
     'test_input': '70\n1.75\n'},
 6: {'answer': '# 待办事项管理器\n'
               'tasks = []\n'
               'print("命令：add 任务 | list | done 编号 | quit")\n'
               'while True:\n'
               '    cmd = input("> ").strip()\n'
               '    if cmd == "quit":\n'
               '        break\n'
               '    parts = cmd.split()\n'
               '    action = parts[0]\n'
               '    if action == "add":\n'
               '        task = " ".join(parts[1:])\n'
               '        tasks.append(task)\n'
               '        print(f"已添加：{task}")\n'
               '    elif action == "list":\n'
               '        for i, task in enumerate(tasks, 1):\n'
               '            print(f"{i}. {task}")\n'
               '    elif action == "done":\n'
               '        idx = int(parts[1]) - 1\n'
               '        task = tasks.pop(idx)\n'
               '        print(f"已完成：{task}")',
     'desc': '添加、列出、完成待办事项',
     'kp': ['list_create', 'list_methods', 'list_iter', 'while_loop'],
     'name': '待办事项管理器',
     'requirements': ['用列表 tasks 存储', '命令：add/list/done 编号/quit'],
     'test_input': 'add 吃饭\nadd 睡觉\nlist\ndone 1\nlist\nquit\n'},
 7: {'answer': '# 坐标处理\n'
               'import math\n'
               'points = [(0, 0), (3, 4), (1, 1)]\n'
               'max_dist = 0\n'
               'for x, y in points:\n'
               '    dist = math.sqrt(x**2 + y**2)\n'
               '    if dist > max_dist:\n'
               '        max_dist = dist\n'
               'print(f"离原点最远距离：{max_dist:.2f}")',
     'desc': '用元组处理坐标数据',
     'expected': '离原点最远距离：5.00',
     'kp': ['tuple_create', 'tuple_unpack', 'list_iter'],
     'name': '坐标处理',
     'requirements': ['存储3个坐标点', '计算每两点间距离并打印最远的']},
 8: {'answer': '# 通讯录\n'
               'contacts = {}\n'
               'print("命令：add 姓名 电话 | find 姓名 | list | quit")\n'
               'while True:\n'
               '    cmd = input("> ").strip()\n'
               '    if cmd == "quit":\n'
               '        break\n'
               '    parts = cmd.split()\n'
               '    action = parts[0]\n'
               '    if action == "add":\n'
               '        name = parts[1]\n'
               '        phone = parts[2]\n'
               '        contacts[name] = phone\n'
               '        print(f"已添加：{name}")\n'
               '    elif action == "find":\n'
               '        name = parts[1]\n'
               '        print(f"{name}: {contacts.get(name, \'未找到\')}")\n'
               '    elif action == "list":\n'
               '        for name, phone in contacts.items():\n'
               '            print(f"{name}: {phone}")',
     'desc': '管理联系人信息',
     'kp': ['dict_create', 'dict_access', 'dict_methods', 'while_loop'],
     'name': '通讯录',
     'requirements': ['字典存储（姓名->电话）', '命令：add/find/list/quit'],
     'test_input': 'add 张三 138\nadd 李四 139\nfind 张三\nquit\n'},
 9: {'answer': '# 文本去重器\n'
               'text = "hello world hello python world"\n'
               'words = text.split()\n'
               'unique = sorted(set(words))\n'
               'print(unique)',
     'desc': '用集合去除重复单词',
     'expected': "['hello', 'python', 'world']",
     'kp': ['set_create', 'str_methods', 'list_iter'],
     'name': '文本去重器',
     'requirements': ['文本 "hello world hello python world"', '去重后按字母排序打印']},
 10: {'answer': '# 文本分析器\n'
                'text = "Hello World 123 Python 456"\n'
                'total = len(text)\n'
                'alpha = sum(1 for ch in text if ch.isalpha())\n'
                'digit = sum(1 for ch in text if ch.isdigit())\n'
                'words = len(text.split())\n'
                'print(f"总字符数：{total}")\n'
                'print(f"字母数：{alpha}")\n'
                'print(f"数字数：{digit}")\n'
                'print(f"单词数：{words}")',
      'desc': '统计文本信息',
      'expected': '总字符数：26\n字母数：15\n数字数：6\n单词数：5',
      'kp': ['str_methods', 'str_check', 'for_loop'],
      'name': '文本分析器',
      'requirements': ['分析 "Hello World 123 Python 456"', '统计：总字符数、字母数、数字数、单词数']},
 11: {'answer': '# 个人日记本\n'
                'import datetime\n'
                '\n'
                'def write_diary(text):\n'
                '    date = datetime.date.today()\n'
                '    with open("diary.txt", "a", encoding="utf-8") as f:\n'
                '        f.write(f"[{date}] {text}\\n")\n'
                '    print(f"已写入：[{date}] {text}")\n'
                '\n'
                'def read_diary():\n'
                '    try:\n'
                '        with open("diary.txt", "r", encoding="utf-8") as f:\n'
                '            print(f.read())\n'
                '    except FileNotFoundError:\n'
                '        print("还没有日记")\n'
                '\n'
                'while True:\n'
                '    cmd = input("> ").strip()\n'
                '    if cmd.startswith("write "):\n'
                '        write_diary(cmd[6:])\n'
                '    elif cmd == "read":\n'
                '        read_diary()\n'
                '    elif cmd == "quit":\n'
                '        break',
      'desc': '记录和查看日记',
      'kp': ['file_open', 'file_write', 'file_read', 'datetime_mod'],
      'name': '个人日记本',
      'requirements': ['日记存 diary.txt', '命令：write 内容 / read / quit'],
      'test_input': 'write 今天天气很好\nread\nquit\n'},
 12: {'answer': '# 数据校验器\n'
                'def validate_age(age_str):\n'
                '    try:\n'
                '        age = int(age_str)\n'
                '    except ValueError:\n'
                '        raise ValueError("年龄必须是数字")\n'
                '    if age < 0 or age > 150:\n'
                '        raise ValueError("年龄必须在0-150之间")\n'
                '    return age\n'
                '\n'
                'while True:\n'
                '    user_input = input("年龄（q退出）：")\n'
                '    if user_input == "q":\n'
                '        break\n'
                '    try:\n'
                '        age = validate_age(user_input)\n'
                '        print(f"有效年龄：{age}")\n'
                '    except ValueError as e:\n'
                '        print(f"错误：{e}")',
      'desc': '验证用户输入',
      'kp': ['func_def', 'try_except', 'raise_error', 'while_loop'],
      'name': '数据校验器',
      'requirements': ['函数 validate_age(age_str) 验证 0-150', '主程序循环输入，捕获异常'],
      'test_input': 'abc\n-5\n200\n25\nq\n'},
 13: {'answer': '# 命令行记账本\n'
                'import json\n'
                'import datetime\n'
                '\n'
                'FILENAME = "accounts.json"\n'
                '\n'
                'def load_data():\n'
                '    try:\n'
                '        with open(FILENAME, "r", encoding="utf-8") as f:\n'
                '            return json.load(f)\n'
                '    except FileNotFoundError:\n'
                '        return []\n'
                '\n'
                'def save_data(data):\n'
                '    with open(FILENAME, "w", encoding="utf-8") as f:\n'
                '        json.dump(data, f, ensure_ascii=False, indent=2)\n'
                '\n'
                'def add_record(data):\n'
                '    t = input("类型(收入/支出)：")\n'
                '    category = input("分类：")\n'
                '    try:\n'
                '        amount = float(input("金额："))\n'
                '    except ValueError:\n'
                '        print("金额无效")\n'
                '        return\n'
                '    note = input("备注：")\n'
                '    record = {\n'
                '        "date": str(datetime.date.today()),\n'
                '        "type": t,\n'
                '        "category": category,\n'
                '        "amount": amount,\n'
                '        "note": note\n'
                '    }\n'
                '    data.append(record)\n'
                '    print(f"已添加：{t} {category} {amount}")\n'
                '\n'
                'def list_records(data):\n'
                '    for r in data:\n'
                '        print(f"{r[\'date\']} {r[\'type\']} {r[\'category\']} {r[\'amount\']}")\n'
                '\n'
                'def summary(data):\n'
                "    income = sum(r['amount'] for r in data if r['type'] == '收入')\n"
                "    expense = sum(r['amount'] for r in data if r['type'] == '支出')\n"
                '    print(f"总收入：{income:,.2f}")\n'
                '    print(f"总支出：{expense:,.2f}")\n'
                '    print(f"余额：{income-expense:,.2f}")\n'
                '\n'
                'data = load_data()\n'
                'print("命令：add | list | summary | quit")\n'
                'while True:\n'
                '    cmd = input("> ").strip()\n'
                '    if cmd == "add":\n'
                '        add_record(data)\n'
                '    elif cmd == "list":\n'
                '        list_records(data)\n'
                '    elif cmd == "summary":\n'
                '        summary(data)\n'
                '    elif cmd == "quit":\n'
                '        save_data(data)\n'
                '        print("再见！")\n'
                '        break',
      'desc': '完整的记账应用（综合实战）',
      'kp': ['import_module', 'json_io', 'datetime_mod', 'func_def', 'dict_create', 'try_except'],
      'name': '命令行记账本',
      'requirements': ['数据结构：{date, type, category, amount, note}', '功能：add/list/summary/quit', '数据持久化到 accounts.json'],
      'test_input': 'add\nquit\n'},
 14: {'answer': 'import re\n'
                'text = "联系：13812345678，021-87654321"\n'
                'phones = re.findall(r"1\\d{10}", text)\n'
                'print(f"手机号：{phones}")\n'
                'landline = re.search(r"(\\d{3})-(\\d{8})", text)\n'
                'if landline:\n'
                '    print(f"区号：{landline.group(1)}")\n'
                '    print(f"座机号：{landline.group(2)}")',
      'desc': '用正则验证手机号和提取信息',
      'expected': "手机号：['13812345678']\n区号：021\n座机号：87654321",
      'kp': ['regex_basic', 'regex_quantifier', 'regex_group', 'print_basic'],
      'name': '手机号验证器',
      'requirements': ['定义字符串 text = "联系：13812345678，021-87654321"', '用正则提取手机号（1开头11位）', '用正则提取区号和座机号', '打印提取结果']},
 15: {'answer': 'class Student:\n'
                '    def __init__(self, name, scores):\n'
                '        self.name = name\n'
                '        self._scores = scores\n'
                '\n'
                '    def average(self):\n'
                '        return sum(self._scores) / len(self._scores)\n'
                '\n'
                '    @property\n'
                '    def grade(self):\n'
                '        avg = self.average()\n'
                '        if avg >= 90: return "A"\n'
                '        elif avg >= 80: return "B"\n'
                '        elif avg >= 60: return "C"\n'
                '        else: return "D"\n'
                '\n'
                'students = [\n'
                '    Student("张三", [90, 85, 92]),\n'
                '    Student("李四", [70, 75, 68]),\n'
                '    Student("王五", [95, 98, 97]),\n'
                ']\n'
                'for s in students:\n'
                '    print(f"{s.name}: 均分{s.average():.1f} 等级{s.grade}")',
      'desc': '用类设计学生和班级管理',
      'expected': '张三: 均分89.0 等级B\n李四: 均分71.0 等级C\n王五: 均分96.7 等级A',
      'kp': ['oop_class_object', 'oop_init_self', 'oop_encapsulation', 'oop_property', 'print_basic'],
      'name': '学生管理系统（OOP版）',
      'requirements': ['创建 Student 类，有 name/scores 属性',
                       '实现 average() 方法计算平均分',
                       '用 @property 提供 grade 属性（A/B/C/D）',
                       '创建3个学生并打印成绩单']},
 16: {'answer': 'class Vector:\n'
                '    def __init__(self, x, y):\n'
                '        self.x = x\n'
                '        self.y = y\n'
                '\n'
                '    def __add__(self, other):\n'
                '        return Vector(self.x + other.x, self.y + other.y)\n'
                '\n'
                '    def __mul__(self, scalar):\n'
                '        return Vector(self.x * scalar, self.y * scalar)\n'
                '\n'
                '    def __str__(self):\n'
                '        return f"Vector({self.x}, {self.y})"\n'
                '\n'
                '    @classmethod\n'
                '    def from_list(cls, lst):\n'
                '        return cls(lst[0], lst[1])\n'
                '\n'
                'v1 = Vector.from_list([3, 4])\n'
                'v2 = Vector(1, 2)\n'
                'print(v1 + v2)\n'
                'print(v1 * 3)',
      'desc': '用魔术方法实现向量运算',
      'expected': 'Vector(4, 6)\nVector(9, 12)',
      'kp': ['oop_magic_method', 'oop_classmethod', 'print_basic'],
      'name': '向量计算器',
      'requirements': ['创建 Vector 类，有 x/y 属性',
                       '实现 __add__(向量加)、__mul__(标量乘)、__str__',
                       '用 @classmethod from_list([3,4]) 工厂方法创建',
                       '测试 v1+v2 和 v1*3']},
 17: {'answer': '# 模拟 my_str_tools.py\n'
                'def capitalize_words(s):\n'
                '    return " ".join(w.capitalize() for w in s.split())\n'
                '\n'
                'if __name__ == "__main__":\n'
                '    print(capitalize_words("hello world python"))\n'
                '\n'
                '# 使用\n'
                'result = capitalize_words("hello world python")\n'
                'print(f"调用结果：{result}")',
      'desc': '创建模块并导入使用',
      'expected': '调用结果：Hello World Python',
      'kp': ['mod_import', 'mod_name_main', 'mod_stdlib', 'print_basic'],
      'name': '自己的工具包',
      'requirements': ['写一个字符串工具模块代码：capitalize_words(s) 把每个单词首字母大写',
                       "写 if __name__ == '__main__' 测试代码",
                       '模拟导入并使用（直接打印模块代码+调用结果）']},
 18: {'answer': 'import time\n'
                'from functools import wraps\n'
                '\n'
                'def timer(func):\n'
                '    @wraps(func)\n'
                '    def wrapper(*args, **kwargs):\n'
                '        start = time.time()\n'
                '        result = func(*args, **kwargs)\n'
                '        elapsed = time.time() - start\n'
                '        print(f"{func.__name__}耗时{elapsed:.6f}秒")\n'
                '        return result\n'
                '    return wrapper\n'
                '\n'
                '@timer\n'
                'def fibonacci(n):\n'
                '    """计算第n个斐波那契数"""\n'
                '    if n <= 1:\n'
                '        return n\n'
                '    a, b = 0, 1\n'
                '    for _ in range(2, n + 1):\n'
                '        a, b = b, a + b\n'
                '    return b\n'
                '\n'
                'result = fibonacci(30)\n'
                'print(f"fib(30) = {result}")\n'
                'print(f"函数名：{fibonacci.__name__}")',
      'desc': '用装饰器实现函数计时和统计',
      'expected': None,
      'kp': ['dec_basic', 'dec_args', 'dec_wraps', 'print_basic'],
      'name': '函数性能分析器',
      'requirements': ['写 @timer 装饰器，打印函数执行时间', '用 @wraps 保留原函数信息', '装饰一个 fibonacci 函数并测试']},
 19: {'answer': '# 学生成绩数据库\n'
                'from sqlalchemy import create_engine, Column, Integer, String\n'
                'from sqlalchemy.orm import declarative_base, Session\n'
                '\n'
                'Base = declarative_base()\n'
                '\n'
                'class Student(Base):\n'
                '    __tablename__ = "students"\n'
                '    id = Column(Integer, primary_key=True)\n'
                '    name = Column(String(50))\n'
                '    math = Column(Integer)\n'
                '    english = Column(Integer)\n'
                '    science = Column(Integer)\n'
                '\n'
                '    def total(self):\n'
                '        return self.math + self.english + self.science\n'
                '\n'
                'engine = create_engine("sqlite:///:memory:")\n'
                'Base.metadata.create_all(engine)\n'
                '\n'
                'session = Session(engine)\n'
                'session.add_all([\n'
                '    Student(name="Alice", math=90, english=85, science=88),\n'
                '    Student(name="Bob", math=78, english=92, science=80),\n'
                '    Student(name="Carol", math=95, english=90, science=93),\n'
                '])\n'
                'session.commit()\n'
                '\n'
                'top = max(session.query(Student).all(), key=lambda s: s.total())\n'
                'print(f"Top: {top.name} ({top.total()}分)")\n'
                'session.close()',
      'desc': '用 SQLAlchemy 创建学生成绩管理系统',
      'expected': None,
      'kp': ['db_sqlalchemy', 'db_sqlite', 'db_transaction'],
      'name': '学生成绩数据库',
      'requirements': ['定义 Student 模型（name, math, english, science）', '创建表并插入3条数据', '查询总成绩最高的学生', '打印结果']},
 20: {'answer': '# 测试套件\n'
                'class StringUtils:\n'
                '    @staticmethod\n'
                '    def capitalize(s):\n'
                '        return s.title()\n'
                '\n'
                '    @staticmethod\n'
                '    def reverse(s):\n'
                '        return s[::-1]\n'
                '\n'
                '    @staticmethod\n'
                '    def is_palindrome(s):\n'
                '        s = s.lower().replace(" ", "")\n'
                '        return s == s[::-1]\n'
                '\n'
                '# 测试（pytest 格式）\n'
                'import pytest\n'
                '\n'
                '@pytest.fixture\n'
                'def su():\n'
                '    return StringUtils()\n'
                '\n'
                'def test_capitalize(su):\n'
                '    assert su.capitalize("hello") == "Hello"\n'
                '\n'
                'def test_reverse(su):\n'
                '    assert su.reverse("abc") == "cba"\n'
                '\n'
                '@pytest.mark.parametrize("input,expected", [\n'
                '    ("radar", True),\n'
                '    ("hello", False),\n'
                '    ("A man a plan a canal Panama", True),\n'
                '])\n'
                'def test_palindrome(su, input, expected):\n'
                '    assert su.is_palindrome(input) == expected\n'
                '\n'
                'print("Tests defined")',
      'desc': '为一个工具类编写完整测试',
      'expected': None,
      'kp': ['test_unittest', 'test_pytest', 'test_fixture', 'test_parametrize'],
      'name': '测试套件',
      'requirements': ['实现 StringUtils 类（capitalize, reverse, is_palindrome）',
                       '用 pytest 写3个测试函数',
                       '参数化测试 is_palindrome',
                       '测试异常情况']},
 21: {'answer': '# 图书管理 API\n'
                'from fastapi import FastAPI, HTTPException\n'
                'from pydantic import BaseModel\n'
                'from typing import List, Optional\n'
                '\n'
                'app = FastAPI()\n'
                '\n'
                'class BookCreate(BaseModel):\n'
                '    title: str\n'
                '    author: str\n'
                '    price: float\n'
                '\n'
                'class BookResponse(BaseModel):\n'
                '    id: int\n'
                '    title: str\n'
                '    author: str\n'
                '    price: float\n'
                '\n'
                'books = {}\n'
                'counter = 0\n'
                '\n'
                '@app.post("/books", response_model=BookResponse)\n'
                'def create(book: BookCreate):\n'
                '    global counter\n'
                '    counter += 1\n'
                '    books[counter] = {"id": counter, **book.dict()}\n'
                '    return books[counter]\n'
                '\n'
                '@app.get("/books", response_model=List[BookResponse])\n'
                'def list_books():\n'
                '    return list(books.values())\n'
                '\n'
                '@app.delete("/books/{book_id}")\n'
                'def delete(book_id: int):\n'
                '    if book_id not in books:\n'
                '        raise HTTPException(404, "Not found")\n'
                '    del books[book_id]\n'
                '    return {"deleted": True}\n'
                '\n'
                '# 启动: uvicorn main:app --reload',
      'desc': '用 FastAPI 实现图书 CRUD 接口',
      'expected': None,
      'kp': ['api_fastapi', 'api_route', 'api_pydantic', 'api_crud'],
      'name': '图书管理 API',
      'requirements': ['定义 BookCreate 模型（title, author, price）',
                       '实现 POST /books 创建',
                       '实现 GET /books 列表',
                       '实现 DELETE /books/{id} 删除']},
 22: {'answer': 'from bs4 import BeautifulSoup\n'
                'import json\n'
                '\n'
                'html = """\n'
                '<div class="quote">\n'
                '    <span class="text">学而不思则罔</span>\n'
                '    <span class="author">孔子</span>\n'
                '</div>\n'
                '<div class="quote">\n'
                '    <span class="text">知之为知之</span>\n'
                '    <span class="author">孔子</span>\n'
                '</div>\n'
                '"""\n'
                '\n'
                'soup = BeautifulSoup(html, "html.parser")\n'
                'quotes = []\n'
                'for q in soup.select(".quote"):\n'
                '    quotes.append({\n'
                '        "text": q.select_one(".text").text,\n'
                '        "author": q.select_one(".author").text\n'
                '    })\n'
                '\n'
                'print(json.dumps(quotes, ensure_ascii=False, indent=2))',
      'desc': '爬取网页名言并保存',
      'expected': '[\n'
                  '  {\n'
                  '    "text": "学而不思则罔",\n'
                  '    "author": "孔子"\n'
                  '  },\n'
                  '  {\n'
                  '    "text": "知之为知之",\n'
                  '    "author": "孔子"\n'
                  '  }\n'
                  ']',
      'kp': ['crawl_requests', 'crawl_beautifulsoup', 'crawl_save', 'print_basic'],
      'name': '名言爬虫',
      'requirements': ['用 BeautifulSoup 解析以下 HTML', '提取所有 quote 的 text 和 author', '保存为 JSON 格式（用 json.dumps 打印）']},
 23: {'answer': 'import pandas as pd\n'
                'data = {\n'
                '    "班级": ["A", "A", "B", "B", "A"],\n'
                '    "姓名": ["张三", "李四", "王五", "赵六", "钱七"],\n'
                '    "成绩": [90, 78, 88, 65, 95]\n'
                '}\n'
                'df = pd.DataFrame(data)\n'
                'print("=== 成绩大于85 ===")\n'
                'print(df[df["成绩"] > 85])\n'
                'print("\n'
                '=== 各班平均 ===")\n'
                'print(df.groupby("班级")["成绩"].mean())',
      'desc': '用 pandas 分析学生成绩',
      'expected': None,
      'kp': ['pandas_dataframe', 'pandas_select', 'pandas_process', 'print_basic'],
      'name': '成绩分析器',
      'requirements': ['创建含班级/姓名/成绩的 DataFrame', '筛选成绩大于85的学生', '计算各班平均成绩']},
 24: {'answer': 'import matplotlib\n'
                'matplotlib.use("Agg")\n'
                'import matplotlib.pyplot as plt\n'
                'import random\n'
                '\n'
                'fig, axes = plt.subplots(2, 2, figsize=(12, 10))\n'
                '\n'
                'months = ["1月", "2月", "3月", "4月", "5月", "6月"]\n'
                'sales = [120, 150, 180, 200, 250, 300]\n'
                'axes[0, 0].plot(months, sales, marker="o", color="steelblue")\n'
                'axes[0, 0].set_title("月度销售")\n'
                '\n'
                'cities = ["北京", "上海", "广州"]\n'
                'pop = [2171, 2487, 1868]\n'
                'axes[0, 1].bar(cities, pop, color=["#FF6B6B", "#4ECDC4", "#45B7D1"])\n'
                'axes[0, 1].set_title("城市人口")\n'
                '\n'
                'axes[1, 0].pie([40, 30, 20, 10], labels=["A", "B", "C", "D"], autopct="%1.0f%%")\n'
                'axes[1, 0].set_title("分类占比")\n'
                '\n'
                'random.seed(42)\n'
                'hours = [random.uniform(1, 10) for _ in range(30)]\n'
                'scores = [min(100, h*9+random.gauss(0,8)) for h in hours]\n'
                'axes[1, 1].scatter(hours, scores, alpha=0.6)\n'
                'axes[1, 1].set_title("时间vs成绩")\n'
                '\n'
                'plt.tight_layout()\n'
                'plt.savefig("dashboard.png", dpi=100, bbox_inches="tight")\n'
                'print("仪表盘已保存为 dashboard.png")',
      'desc': '用 matplotlib 画综合图表面板',
      'expected': '仪表盘已保存为 dashboard.png',
      'kp': ['viz_line', 'viz_bar', 'viz_subplots', 'print_basic'],
      'name': '数据仪表盘',
      'requirements': ['用 subplots(2,2) 创建4个子图',
                       '左上：折线图（月度趋势）',
                       '右上：柱状图（各类别比较）',
                       '左下：饼图（占比分布）',
                       '右下：散点图（相关性）',
                       '保存为 dashboard.png']},
 25: {'answer': '# 动态新闻爬虫\n'
                'from selenium import webdriver\n'
                'from selenium.webdriver.common.by import By\n'
                'from selenium.webdriver.support.ui import WebDriverWait\n'
                'from selenium.webdriver.support import expected_conditions as EC\n'
                '\n'
                'driver = webdriver.Chrome()\n'
                'driver.get("https://quotes.toscrape.com/js/")\n'
                '\n'
                'wait = WebDriverWait(driver, 10)\n'
                'wait.until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))\n'
                '\n'
                'quotes = driver.find_elements(By.CLASS_NAME, "quote")\n'
                'for q in quotes:\n'
                '    text = q.find_element(By.CLASS_NAME, "text").text\n'
                '    author = q.find_element(By.CLASS_NAME, "author").text\n'
                '    print(f"{author}: {text}")\n'
                '\n'
                'driver.quit()',
      'desc': '用 Selenium 爬取动态加载的新闻页面',
      'expected': None,
      'kp': ['crawl_selenium', 'crawl_wait', 'crawl_session'],
      'name': '动态新闻爬虫',
      'requirements': ['启动 Selenium 访问 quotes.toscrape.com/js/', '显式等待 quote 元素加载', '提取所有名言和作者', '打印结果']},
 26: {'answer': '# 异步并发下载器\n'
                'import asyncio\n'
                'import aiohttp\n'
                '\n'
                'async def fetch(session, url, sem):\n'
                '    async with sem:\n'
                '        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as resp:\n'
                '            return resp.status\n'
                '\n'
                'async def main():\n'
                '    urls = ["https://httpbin.org/get"] * 5\n'
                '    sem = asyncio.Semaphore(3)\n'
                '    async with aiohttp.ClientSession() as session:\n'
                '        tasks = [fetch(session, url, sem) for url in urls]\n'
                '        results = await asyncio.gather(*tasks)\n'
                '    for i, status in enumerate(results):\n'
                '        print(f"Page {i+1}: {status}")\n'
                '\n'
                'asyncio.run(main())',
      'desc': '用 asyncio+aiohttp 并发下载多个页面',
      'expected': None,
      'kp': ['async_def', 'async_gather', 'async_aiohttp', 'async_semaphore'],
      'name': '异步并发下载器',
      'requirements': ['定义异步下载函数', '用 Semaphore 限制并发为3', '用 gather 并发执行', '打印每个页面的状态码']},
 27: {'answer': '# Scrapy 名言爬虫\n'
                'import scrapy\n'
                'import json\n'
                '\n'
                'class QuoteItem(scrapy.Item):\n'
                '    text = scrapy.Field()\n'
                '    author = scrapy.Field()\n'
                '    tags = scrapy.Field()\n'
                '\n'
                'class QuotesSpider(scrapy.Spider):\n'
                '    name = "quotes"\n'
                '    start_urls = ["https://quotes.toscrape.com/"]\n'
                '\n'
                '    def parse(self, response):\n'
                '        for quote in response.css("div.quote"):\n'
                '            yield {"text": quote.css("span.text::text").get(),\n'
                '                   "author": quote.css("small.author::text").get(),\n'
                '                   "tags": quote.css("div.tags a.tag::text").getall()}\n'
                '        next_page = response.css("li.next a::attr(href)").get()\n'
                '        if next_page:\n'
                '            yield response.follow(next_page, callback=self.parse)\n'
                '\n'
                '# 运行: scrapy crawl quotes -o quotes.jsonl',
      'desc': '用 Scrapy 爬取名言网站并保存为 JSON',
      'expected': None,
      'kp': ['crawl_scrapy', 'crawl_concurrent'],
      'name': 'Scrapy 名言爬虫',
      'requirements': ['定义 QuoteItem 数据结构', '编写 Spider 爬取 text/author/tags', '实现自动翻页', '保存为 JSON Lines 格式']},
 28: {'answer': '# 爬虫监控面板\n'
                'import logging\n'
                'import sqlite3\n'
                '\n'
                'logging.basicConfig(\n'
                '    level=logging.INFO,\n'
                '    format="%(asctime)s [%(levelname)s] %(message)s",\n'
                '    handlers=[\n'
                '        logging.FileHandler("spider.log", encoding="utf-8"),\n'
                '        logging.StreamHandler(),\n'
                '    ]\n'
                ')\n'
                'logger = logging.getLogger("spider")\n'
                '\n'
                'conn = sqlite3.connect(":memory:")\n'
                'conn.execute("CREATE TABLE IF NOT EXISTS urls (url TEXT PRIMARY KEY)")\n'
                '\n'
                'class SpiderStats:\n'
                '    def __init__(self):\n'
                '        self.success = 0\n'
                '        self.fail = 0\n'
                '\n'
                '    def report(self):\n'
                '        total = self.success + self.fail\n'
                '        rate = self.success / total * 100 if total else 0\n'
                '        print(f"\\n{\'=\'*40}")\n'
                '        print(f"爬取报告: {self.success}/{total} 成功 ({rate:.1f}%)")\n'
                '        print(f"{\'=\'*40}")\n'
                '\n'
                'stats = SpiderStats()\n'
                'logger.info("爬虫启动")\n'
                'stats.success = 10\n'
                'stats.fail = 2\n'
                'stats.report()',
      'desc': '创建带日志和统计的爬虫框架',
      'expected': None,
      'kp': ['crawl_mysql', 'crawl_redis', 'crawl_logging'],
      'name': '爬虫监控面板',
      'requirements': ['配置双输出日志（文件+终端）', '实现 SQLite URL 去重', '统计成功/失败次数', '打印爬取报告']},
 29: {'answer': 'from bs4 import BeautifulSoup\n'
                'import json\n'
                'import pandas as pd\n'
                '\n'
                'html = """\n'
                '<div class="item"><span class="city">北京</span><span class="temp">25</span></div>\n'
                '<div class="item"><span class="city">上海</span><span class="temp">28</span></div>\n'
                '<div class="item"><span class="city">广州</span><span class="temp">32</span></div>\n'
                '<div class="item"><span class="city">深圳</span><span class="temp">30</span></div>\n'
                '"""\n'
                '\n'
                'soup = BeautifulSoup(html, "html.parser")\n'
                'records = []\n'
                'for item in soup.select(".item"):\n'
                '    city = item.select_one(".city").text\n'
                '    temp = int(item.select_one(".temp").text)\n'
                '    records.append({"city": city, "temp": temp})\n'
                '\n'
                'json_str = json.dumps(records, ensure_ascii=False)\n'
                'print(f"JSON: {json_str}")\n'
                '\n'
                'df = pd.DataFrame(records)\n'
                'print(f"\n'
                '最高温：{df.loc[df[\'temp\'].idxmax(), \'city\']} {df[\'temp\'].max()}度")\n'
                'print(f"最低温：{df.loc[df[\'temp\'].idxmin(), \'city\']} {df[\'temp\'].min()}度")\n'
                'print(f"平均温度：{df[\'temp\'].mean():.1f}度")',
      'desc': '爬取→清洗→分析→可视化的完整流程',
      'expected': 'JSON: [{"city": "北京", "temp": 25}, {"city": "上海", "temp": 28}, {"city": "广州", "temp": 32}, {"city": '
                  '"深圳", "temp": 30}]\n'
                  '最高温：广州 32度\n'
                  '最低温：北京 25度\n'
                  '平均温度：28.8度',
      'kp': ['crawl_beautifulsoup', 'json_advanced', 'pandas_process', 'viz_bar', 'print_basic'],
      'name': '全栈数据分析项目',
      'requirements': ['用 BeautifulSoup 解析 HTML 提取数据', '转为 JSON 再加载为 pandas DataFrame', '分组统计并排序', '保存结果']},
 30: {'answer': 'import re\n'
                '\n'
                'files = ["IMG_001.jpg", "IMG_002.jpg", "photo.jpg"]\n'
                'for f in files:\n'
                '    new_name = re.sub(r"IMG_(\\d+)", r"vacation_\\1", f)\n'
                '    if new_name != f:\n'
                '        print(f"{f} -> {new_name}")\n'
                '    else:\n'
                '        print(f"{f} (不变)")',
      'desc': '用 pathlib+正则实现文件批量重命名',
      'expected': 'IMG_001.jpg -> vacation_001.jpg\nIMG_002.jpg -> vacation_002.jpg\nphoto.jpg (不变)',
      'kp': ['auto_pathlib', 'regex_sub', 'auto_batch_rename', 'print_basic'],
      'name': '批量文件重命名器',
      'requirements': ["定义文件列表 ['IMG_001.jpg', 'IMG_002.jpg', 'photo.jpg']",
                       '用正则匹配 IMG_ 开头的文件名',
                       '替换为 vacation_001.jpg 格式',
                       '打印重命名映射']},
 31: {'answer': 'from bs4 import BeautifulSoup\n'
                '\n'
                'html = """\n'
                '<html><body>\n'
                '<a href="https://python.org">Python</a>\n'
                '<a href="https://docs.python.org">Docs</a>\n'
                '<a href="https://pypi.org">PyPI</a>\n'
                '</body></html>\n'
                '"""\n'
                '\n'
                'soup = BeautifulSoup(html, "html.parser")\n'
                'links = {}\n'
                'for a in soup.find_all("a"):\n'
                '    links[a.text] = a["href"]\n'
                '\n'
                'for title, href in links.items():\n'
                '    print(f"{title}: {href}")',
      'desc': '用 BeautifulSoup+requests 提取网页信息',
      'expected': 'Python: https://python.org\nDocs: https://docs.python.org\nPyPI: https://pypi.org',
      'kp': ['auto_selenium', 'crawl_beautifulsoup', 'print_basic'],
      'name': '网页内容提取器',
      'requirements': ['解析 HTML 获取所有链接和标题', '用字典存储 {title: href}', '打印结果']},
 32: {'answer': '# 简易记事本\n'
                'import tkinter as tk\n'
                'from tkinter import filedialog, messagebox\n'
                '\n'
                'root = tk.Tk()\n'
                'root.title("Notepad")\n'
                'root.geometry("600x400")\n'
                '\n'
                'text = tk.Text(root, wrap=tk.WORD, font=("Consolas", 12))\n'
                'text.pack(fill=tk.BOTH, expand=True)\n'
                '\n'
                'status = tk.Label(root, text="Chars: 0", anchor=tk.W)\n'
                'status.pack(fill=tk.X)\n'
                '\n'
                'def update_status(event=None):\n'
                '    content = text.get("1.0", tk.END)\n'
                '    status.config(text=f"Chars: {len(content)-1}")\n'
                '\n'
                'text.bind("<KeyRelease>", update_status)\n'
                '\n'
                'def new_file():\n'
                '    text.delete("1.0", tk.END)\n'
                '\n'
                'def open_file():\n'
                '    path = filedialog.askopenfilename()\n'
                '    if path:\n'
                '        with open(path, "r", encoding="utf-8") as f:\n'
                '            text.delete("1.0", tk.END)\n'
                '            text.insert("1.0", f.read())\n'
                '\n'
                'def save_file():\n'
                '    path = filedialog.asksaveasfilename(defaultextension=".txt")\n'
                '    if path:\n'
                '        with open(path, "w", encoding="utf-8") as f:\n'
                '            f.write(text.get("1.0", tk.END))\n'
                '\n'
                'menubar = tk.Menu(root)\n'
                'file_menu = tk.Menu(menubar, tearoff=0)\n'
                'file_menu.add_command(label="New", command=new_file)\n'
                'file_menu.add_command(label="Open", command=open_file)\n'
                'file_menu.add_command(label="Save", command=save_file)\n'
                'file_menu.add_separator()\n'
                'file_menu.add_command(label="Exit", command=root.quit)\n'
                'menubar.add_cascade(label="File", menu=file_menu)\n'
                'root.config(menu=menubar)\n'
                '\n'
                'root.mainloop()',
      'desc': '用 tkinter 实现带菜单的记事本应用',
      'expected': None,
      'kp': ['gui_tkinter', 'gui_widget', 'gui_layout', 'gui_event', 'gui_menu'],
      'name': '简易记事本',
      'requirements': ['创建窗口和文本框', '添加菜单栏（文件：新建/打开/保存）', '实现文件打开和保存功能', '添加状态栏显示字符数']},
 33: {'answer': 'from pathlib import Path\n'
                'from collections import Counter\n'
                '\n'
                'class FileManager:\n'
                '    def __init__(self, directory):\n'
                '        self.directory = Path(directory)\n'
                '\n'
                '    def scan(self):\n'
                '        exts = [f.suffix for f in self.directory.iterdir() if f.is_file()]\n'
                '        return dict(Counter(exts))\n'
                '\n'
                '    def find_duplicates(self):\n'
                '        size_map = {}\n'
                '        for f in self.directory.iterdir():\n'
                '            if f.is_file():\n'
                '                size = f.stat().st_size\n'
                '                if size in size_map:\n'
                '                    print(f"可能重复: {size_map[size]} 和 {f.name} ({size}字节)")\n'
                '                else:\n'
                '                    size_map[size] = f.name\n'
                '\n'
                '    def summary(self):\n'
                '        ext_count = self.scan()\n'
                '        total = sum(ext_count.values())\n'
                '        print(f"目录: {self.directory}")\n'
                '        print(f"文件总数: {total}")\n'
                '        for ext, count in sorted(ext_count.items()):\n'
                '            print(f"  {ext or \'(无后缀)\'}: {count}个")\n'
                '\n'
                '# 用当前目录测试\n'
                'fm = FileManager(".")\n'
                'fm.summary()',
      'desc': '综合项目：文件扫描+分类+重命名',
      'expected': None,
      'kp': ['auto_pathlib', 'auto_shutil', 'auto_backup', 'oop_class_object', 'print_basic'],
      'name': '智能文件管理器',
      'requirements': ['创建 FileManager 类', 'scan() 方法扫描目录统计文件类型', 'find_duplicates() 方法找重复（按大小初步判断）', '创建几个模拟文件信息并测试']},
 34: {'answer': '# 插件系统\n'
                'class PluginFactory:\n'
                '    _plugins = {}\n'
                '\n'
                '    @classmethod\n'
                '    def register(cls, name, plugin_class):\n'
                '        cls._plugins[name] = plugin_class\n'
                '\n'
                '    @classmethod\n'
                '    def create(cls, name):\n'
                '        return cls._plugins[name]()\n'
                '\n'
                'class EventBus:\n'
                '    def __init__(self):\n'
                '        self._listeners = {}\n'
                '\n'
                '    def subscribe(self, event, fn):\n'
                '        self._listeners.setdefault(event, []).append(fn)\n'
                '\n'
                '    def emit(self, event, data=None):\n'
                '        for fn in self._listeners.get(event, []):\n'
                '            fn(data)\n'
                '\n'
                'class LoggerPlugin:\n'
                '    def on_data(self, data):\n'
                '        print(f"[LOG] {data}")\n'
                '\n'
                'class EmailPlugin:\n'
                '    def on_data(self, data):\n'
                '        print(f"[EMAIL] Sending: {data}")\n'
                '\n'
                'bus = EventBus()\n'
                'bus.subscribe("data", LoggerPlugin().on_data)\n'
                'bus.subscribe("data", EmailPlugin().on_data)\n'
                'bus.emit("data", "New order #42")',
      'desc': '用设计模式实现可扩展的插件架构',
      'expected': None,
      'kp': ['pattern_factory', 'pattern_observer', 'pattern_strategy'],
      'name': '插件系统',
      'requirements': ['用工厂模式创建不同插件', '用观察者模式通知插件事件', '用策略模式切换处理方式', '演示完整流程']},
 35: {'answer': '# 排序算法性能对比\n'
                'import time\n'
                'import random\n'
                '\n'
                'random.seed(42)\n'
                'data = [random.randint(1, 10000) for _ in range(1000)]\n'
                '\n'
                'def bubble_sort(arr):\n'
                '    arr = arr[:]\n'
                '    for i in range(len(arr)):\n'
                '        for j in range(len(arr)-i-1):\n'
                '            if arr[j] > arr[j+1]:\n'
                '                arr[j], arr[j+1] = arr[j+1], arr[j]\n'
                '    return arr\n'
                '\n'
                'def quick_sort(arr):\n'
                '    if len(arr) <= 1:\n'
                '        return arr\n'
                '    pivot = arr[len(arr)//2]\n'
                '    left = [x for x in arr if x < pivot]\n'
                '    mid = [x for x in arr if x == pivot]\n'
                '    right = [x for x in arr if x > pivot]\n'
                '    return quick_sort(left) + mid + quick_sort(right)\n'
                '\n'
                'def time_it(func, arr):\n'
                '    start = time.time()\n'
                '    func(arr[:])\n'
                '    return time.time() - start\n'
                '\n'
                'print(f"冒泡排序: {time_it(bubble_sort, data):.4f}s")\n'
                'print(f"快速排序: {time_it(quick_sort, data):.4f}s")\n'
                'print(f"内置排序: {time_it(sorted, data):.4f}s")',
      'desc': '对比冒泡/快排/内置排序的性能',
      'expected': None,
      'kp': ['algo_sort', 'algo_complexity'],
      'name': '排序算法性能对比',
      'requirements': ['生成 1000 个随机数', '实现冒泡排序和快速排序', '用 time.time() 计时对比', '与内置 sorted() 比较']},
 36: {'answer': '# 动态规划：爬楼梯变体\n'
                'def climb_stairs(n, steps):\n'
                '    dp = [0] * (n + 1)\n'
                '    dp[0] = 1\n'
                '    for i in range(1, n + 1):\n'
                '        for s in steps:\n'
                '            if i >= s:\n'
                '                dp[i] += dp[i - s]\n'
                '    return dp[n]\n'
                '\n'
                'print(f"5级楼梯(1-2步): {climb_stairs(5, [1, 2])}")\n'
                'print(f"5级楼梯(1-3步): {climb_stairs(5, [1, 2, 3])}")\n'
                '\n'
                '# 背包问题\n'
                'def knapsack(weights, values, capacity):\n'
                '    n = len(weights)\n'
                '    dp = [[0] * (capacity + 1) for _ in range(n + 1)]\n'
                '    for i in range(1, n + 1):\n'
                '        for w in range(capacity + 1):\n'
                '            if weights[i-1] <= w:\n'
                '                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])\n'
                '            else:\n'
                '                dp[i][w] = dp[i-1][w]\n'
                '    return dp[n][capacity]\n'
                '\n'
                'print(f"背包最大价值: {knapsack([2,3,4,5], [3,4,5,6], 8)}")',
      'desc': '实现爬楼梯DP和背包问题',
      'expected': None,
      'kp': ['algo_dp', 'algo_greedy'],
      'name': '动态规划实战',
      'requirements': ['爬楼梯问题：n级台阶，每次走steps中步数', '背包问题：给定重量和价值，求最大价值', '打印两种问题的结果']},
 37: {'answer': '# 代码审查工具\n'
                'import re\n'
                'import ast\n'
                '\n'
                'def lint(code):\n'
                '    issues = []\n'
                '    for i, line in enumerate(code.split(chr(10)), 1):\n'
                '        if len(line) > 120:\n'
                '            issues.append(f"Line {i}: 行过长 ({len(line)} chars)")\n'
                '    if "=[]" in code or "={}" in code:\n'
                '        issues.append("可变默认参数隐患")\n'
                '    if re.search(r"except\\s*:", code):\n'
                '        issues.append("裸 except: 应指定异常类型")\n'
                '    for m in re.finditer(r"class\\s+([a-z]\\w*)", code):\n'
                '        issues.append(f"类名 {m.group(1)} 应使用 PascalCase")\n'
                '    return issues\n'
                '\n'
                'bad_code = "def f(x=[]):\\n    try:\\n        pass\\n    except:\\n        pass\\nclass my_class:\\n    pass"\n'
                'for issue in lint(bad_code):\n'
                '    print(issue)',
      'desc': '扫描Python源码检测常见问题',
      'expected': None,
      'kp': ['project_code_review', 'regex_basic', 'ast_module'],
      'name': '代码审查工具',
      'requirements': ['检查行长超过120', '检测可变默认参数', '检测裸 except', '检测类名命名风格', '返回问题列表']}}
