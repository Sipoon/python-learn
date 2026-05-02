"""陷阱练习数据 - v5.0"""
from typing import Dict, List

PITFALL_EXERCISES: Dict = {
  2: [
    {
      "answer": "if x == 5:\n    print(\"x等于5\")",
      "buggy_code": "if x = 5:\n    print(\"x等于5\")",
      "explanation": "if x = 5 会报 SyntaxError。= 是赋值运算符，== 才是比较运算符。这是新手最常犯的错！",
      "hint": "= 是赋值，== 才是比较",
      "id": "assign_vs_compare",
      "kp": [
        "op_compare"
      ],
      "question": "这段代码能运行吗？为什么？请修正它（设 x 已定义）",
      "stage": 2,
      "title": "= 和 == 傻傻分不清"
    },
    {
      "answer": "a = [1, 2, 3]\nb = [1, 2, 3]\nprint(a == b)",
      "buggy_code": "a = [1, 2, 3]\nb = [1, 2, 3]\nprint(a is b)",
      "explanation": "is 比较两个变量是否指向同一个对象，== 比较值是否相等。一般判断值用 ==，判断 None 用 is。",
      "hint": "is 比较身份（是否同一对象），== 比较值",
      "id": "is_vs_eq",
      "kp": [
        "op_compare"
      ],
      "question": "a is b 会打印什么？如果判断两个列表内容一样该用什么？",
      "stage": 2,
      "title": "is 和 == 的区别"
    },
    {
      "answer": "print(7 / 2)   # 3.5\nprint(7 // 2)  # 3",
      "buggy_code": "print(7 / 2)\nprint(7 // 2)",
      "explanation": "/ 返回浮点数 3.5，// 返回整数 3（向下取整）。新手常混淆这两个运算符。",
      "hint": "/ 是真除（返回浮点），// 是整除（向下取整）",
      "id": "integer_division",
      "kp": [
        "op_arithmetic"
      ],
      "question": "两行分别打印什么？如果要得到3.5该用哪个？",
      "stage": 2,
      "title": "整除 vs 真除"
    }
  ],
  3: [
    {
      "answer": "if True:\n    print(\"hello\")\n    print(\"world\")",
      "buggy_code": "if True:\n    print(\"hello\")\n  print(\"world\")",
      "explanation": "IndentationError: 缩进不一致。Python 靠缩进判断代码块，统一用4个空格。",
      "hint": "同一代码块缩进必须一致（4个空格）",
      "id": "indentation",
      "kp": [
        "if_basic"
      ],
      "question": "这段代码会报什么错？请修正缩进",
      "stage": 3,
      "title": "缩进不一致"
    },
    {
      "answer": "score = 85\nif score >= 90:\n    print(\"A\")\nelif score >= 80:\n    print(\"B\")\nelif score >= 60:\n    print(\"C\")",
      "buggy_code": "score = 85\nif score >= 90:\n    print(\"A\")\nif score >= 80:\n    print(\"B\")\nif score >= 60:\n    print(\"C\")",
      "explanation": "多个独立 if 会逐个检查，85>=80 和 85>=60 都成立所以打印 B 和 C。elif 只在前面条件都不满足时才检查。",
      "hint": "用 elif 代替后续的 if",
      "id": "elif_chain",
      "kp": [
        "if_elif_else"
      ],
      "question": "score=85 时打印几个等级？如何只打印一个？",
      "stage": 3,
      "title": "多个 if vs elif"
    }
  ],
  4: [
    {
      "answer": "for i in range(1, 11):\n    print(i)",
      "buggy_code": "for i in range(1, 10):\n    print(i)",
      "explanation": "range(start, stop) 不包含 stop！range(1,10) 打印 1-9。要打印1-10 需要 range(1,11)。",
      "hint": "range(1, 10) 不包含 10",
      "id": "off_by_one",
      "kp": [
        "for_range"
      ],
      "question": "这段代码打印 1 到几？如果要打印 1 到 10 该怎么改？",
      "stage": 4,
      "title": "range 的 off-by-one"
    },
    {
      "answer": "i = 0\nwhile i < 5:\n    print(i)\n    i += 1",
      "buggy_code": "i = 0\nwhile i < 5:\n    print(i)",
      "explanation": "i 永远是 0，条件永远 True，死循环！while 循环必须手动更新变量，或者优先用 for 循环。",
      "hint": "while 循环需要手动更新变量",
      "id": "infinite_loop",
      "kp": [
        "while_basic"
      ],
      "question": "这段代码会怎样？请修正",
      "stage": 4,
      "title": "忘更新循环变量导致死循环"
    }
  ],
  5: [
    {
      "answer": "def add_item(item, lst=None):\n    if lst is None:\n        lst = []\n    lst.append(item)\n    return lst\n\nprint(add_item(\"a\"))\nprint(add_item(\"b\"))",
      "buggy_code": "def add_item(item, lst=[]):\n    lst.append(item)\n    return lst\n\nprint(add_item(\"a\"))\nprint(add_item(\"b\"))",
      "explanation": "默认参数 lst=[] 在定义时只创建一次，所有调用共享同一个列表。正确做法：用 None 做默认值，在函数内创建新列表。",
      "hint": "默认参数在函数定义时创建，不是每次调用时创建",
      "id": "mutable_default_arg",
      "kp": [
        "func_default"
      ],
      "question": "第二次调用会打印什么？为什么不是 [\"b\"]？请修正",
      "stage": 5,
      "title": "可变默认参数的坑"
    },
    {
      "answer": "def add(a, b):\n    result = a + b\n    return result\n\nprint(add(1, 2))",
      "buggy_code": "def add(a, b):\n    result = a + b\n\nprint(add(1, 2))",
      "explanation": "函数没有 return 语句时默认返回 None。计算结果要 return 出去才能被外部使用。",
      "hint": "没有 return 语句的函数返回 None",
      "id": "return_none",
      "kp": [
        "func_return"
      ],
      "question": "打印什么？为什么不是 3？请修正",
      "stage": 5,
      "title": "函数没有 return 就返回 None"
    }
  ],
  6: [
    {
      "answer": "nums = [1, 2, 3, 4, 5, 6]\nnums = [n for n in nums if n % 2 != 0]\nprint(nums)",
      "buggy_code": "nums = [1, 2, 3, 4, 5, 6]\nfor n in nums:\n    if n % 2 == 0:\n        nums.remove(n)\nprint(nums)",
      "explanation": "遍历时 remove 会导致索引错位，跳过元素。正确做法：用列表推导式创建新列表。",
      "hint": "遍历时删除元素会跳过，用列表推导式代替",
      "id": "modify_list_while_iter",
      "kp": [
        "list_methods",
        "list_comprehension"
      ],
      "question": "输出是什么？为什么不是 [1,3,5]？请修正",
      "stage": 6,
      "title": "遍历时删除列表元素"
    },
    {
      "answer": "nums = [3, 1, 4, 1, 5]\nnums.sort()\nprint(nums)",
      "buggy_code": "nums = [3, 1, 4, 1, 5]\nresult = nums.sort()\nprint(result)",
      "explanation": "list.sort() 是原地排序（修改原列表），返回 None。想赋值给变量用 sorted(nums)。",
      "hint": "sort() 原地排序，返回 None。要么直接 print(nums)，要么用 sorted()",
      "id": "sort_returns_none",
      "kp": [
        "list_methods"
      ],
      "question": "result 是什么？请修正代码，让排序后的列表被打印",
      "stage": 6,
      "title": "sort() 返回 None"
    }
  ],
  7: [
    {
      "answer": "t = (42,)\nprint(type(t))",
      "buggy_code": "t = (42)\nprint(type(t))",
      "explanation": "(42) 只是小括号包裹的整数，等价于 42。单元素元组必须加逗号：(42,)。",
      "hint": "(42) 是整数不是元组，(42,) 才是",
      "id": "single_element_tuple",
      "kp": [
        "tuple_create",
        {
          "id": "pit7_02",
          "stage": 7,
          "title": "单元素元组的陷阱",
          "question": "为什么 t = (5) 不是元组?",
          "buggy_code": "t = (5)\nprint(type(t))  # 期望 <class 'tuple'>, 实际 <class 'int'>",
          "hint": "单元素元组需要逗号",
          "explanation": "Python 中 (5) 只是带括号的表达式, 不是元组. 单元素元组必须写 (5,), 末尾的逗号才是关键!",
          "answer": "t = (5,)\nprint(type(t))  # <class 'tuple'>",
          "kp": [
            "tuple",
            "single_element"
          ]
        }
      ],
      "question": "type(t) 打印什么？为什么不是 tuple？请修正",
      "stage": 7,
      "title": "单元素元组忘加逗号"
    },
    {
      "id": "pit7_02",
      "stage": 7,
      "title": "单元素元组的陷阱",
      "question": "为什么 t = (5) 不是元组?",
      "buggy_code": "t = (5)\nprint(type(t))  # 期望 tuple, 实际 int",
      "hint": "单元素元组需要逗号",
      "explanation": "Python 中 (5) 只是带括号的表达式, 不是元组. 单元素元组必须写 (5,), 末尾的逗号才是关键!",
      "answer": "t = (5,)\nprint(type(t))  # <class 'tuple'>",
      "kp": [
        "tuple",
        "single_element"
      ]
    }
  ],
  8: [
    {
      "answer": "person = {\"name\": \"张三\", \"age\": 25}\nprint(person.get(\"phone\", \"未设置\"))",
      "buggy_code": "person = {\"name\": \"张三\", \"age\": 25}\nprint(person[\"phone\"])",
      "explanation": "KeyError: 键不存在时用 [] 访问会报错。安全做法：dict.get(key, default)。",
      "hint": "用 get() 方法代替 [] 访问",
      "id": "dict_key_error",
      "kp": [
        "dict_access",
        "dict_methods",
        {
          "id": "pit8_02",
          "stage": 8,
          "title": "字典迭代时修改",
          "question": "遍历字典时删除元素会报错吗?",
          "buggy_code": "d = {'a': 1, 'b': 2, 'c': 3}\nfor k in d:\n    if d[k] < 3:\n        del d[k]  # RuntimeError!",
          "hint": "不能在遍历时修改字典大小, 收集key后再删",
          "explanation": "遍历字典时不能添加/删除键, 否则触发 RuntimeError. 解决方案: 先收集要删除的 key 到列表, 遍历完后再删.",
          "answer": "d = {'a': 1, 'b': 2, 'c': 3}\nto_del = [k for k, v in d.items() if v < 3]\nfor k in to_del:\n    del d[k]",
          "kp": [
            "dict",
            "iteration",
            "runtime_error"
          ]
        }
      ],
      "question": "这段代码会报什么错？请用安全方式改写",
      "stage": 8,
      "title": "字典键不存在直接访问报错"
    },
    {
      "id": "pit8_02",
      "stage": 8,
      "title": "字典迭代时修改",
      "question": "遍历字典时删除元素会报错吗?",
      "buggy_code": "d = {'a': 1, 'b': 2, 'c': 3}\nfor k in d:\n    if d[k] < 3:\n        del d[k]  # RuntimeError!",
      "hint": "不能在遍历时修改字典大小, 收集key后再删",
      "explanation": "遍历字典时不能添加/删除键, 否则触发 RuntimeError. 解决方案: 先收集要删除的 key 到列表, 遍历完后再删.",
      "answer": "d = {'a': 1, 'b': 2, 'c': 3}\nto_del = [k for k, v in d.items() if v < 3]\nfor k in to_del:\n    del d[k]",
      "kp": [
        "dict",
        "iteration",
        "runtime_error"
      ]
    }
  ],
  9: [
    {
      "answer": "s = set()\nprint(type(s))",
      "buggy_code": "s = {}\nprint(type(s))",
      "explanation": "{} 创建空字典，不是空集合！空集合必须用 set()。有元素可以用 {1,2,3}。",
      "hint": "{} 创建的是空字典，空集合用 set()",
      "id": "empty_set",
      "kp": [
        "set_create",
        "dict_create",
        {
          "id": "pit9_02",
          "stage": 9,
          "title": "集合元素必须是可哈希的",
          "question": "为什么 s = {[1,2]} 会报错?",
          "buggy_code": "s = {[1, 2]}  # TypeError: unhashable type: 'list'",
          "hint": "集合元素需要可哈希, 列表不可哈希",
          "explanation": "集合基于哈希表实现, 元素必须是不可变类型. 列表/字典/集合本身不可哈希, 不能作为集合元素. 用元组代替: {(1,2)}",
          "answer": "s = {(1, 2)}  # 元组可哈希, 没问题",
          "kp": [
            "set",
            "hashable",
            "immutable"
          ]
        }
      ],
      "question": "type(s) 是什么？如果要创建空集合该怎么改？",
      "stage": 9,
      "title": "空集合不是 {}"
    },
    {
      "id": "pit9_02",
      "stage": 9,
      "title": "集合元素必须是可哈希的",
      "question": "为什么 s = {[1,2]} 会报错?",
      "buggy_code": "s = {[1, 2]}  # TypeError: unhashable type: 'list'",
      "hint": "集合元素需要可哈希, 列表不可哈希",
      "explanation": "集合基于哈希表实现, 元素必须是不可变类型. 列表/字典/集合本身不可哈希, 不能作为集合元素. 用元组代替: {(1,2)}",
      "answer": "s = {(1, 2)}  # 元组可哈希, 没问题",
      "kp": [
        "set",
        "hashable",
        "immutable"
      ]
    }
  ],
  10: [
    {
      "answer": "s = \"hello\"\ns = \"H\" + s[1:]\nprint(s)",
      "buggy_code": "s = \"hello\"\ns[0] = \"H\"\nprint(s)",
      "explanation": "TypeError: 字符串是不可变对象，不能通过索引修改。需要创建新字符串或用 .replace()。",
      "hint": "字符串是不可变的，需要创建新字符串",
      "id": "str_immutable",
      "kp": [
        "str_index",
        "str_slice",
        {
          "id": "pit10_02",
          "stage": 10,
          "title": "字符串是不可变的",
          "question": "为什么 s[0] = 'H' 会报错?",
          "buggy_code": "s = 'hello'\ns[0] = 'H'  # TypeError: 'str' object does not support item assignment",
          "hint": "字符串是不可变对象, 不能原地修改",
          "explanation": "Python 字符串是不可变类型, 不能通过索引修改单个字符. 需要创建新字符串: s = 'H' + s[1:]",
          "answer": "s = 'hello'\ns = 'H' + s[1:]  # 'Hello'",
          "kp": [
            "str",
            "immutable",
            "string_ops"
          ]
        }
      ],
      "question": "这段代码会报什么错？请修正",
      "stage": 10,
      "title": "字符串不能原地修改"
    },
    {
      "id": "pit10_02",
      "stage": 10,
      "title": "字符串是不可变的",
      "question": "为什么 s[0] = 'H' 会报错?",
      "buggy_code": "s = 'hello'\ns[0] = 'H'  # TypeError!",
      "hint": "字符串是不可变对象, 不能原地修改",
      "explanation": "Python 字符串是不可变类型, 不能通过索引修改单个字符. 需要创建新字符串: s = 'H' + s[1:]",
      "answer": "s = 'hello'\ns = 'H' + s[1:]  # 'Hello'",
      "kp": [
        "str",
        "immutable",
        "string_ops"
      ]
    }
  ],
  11: [
    {
      "answer": "with open(\"data.txt\", \"r\", encoding=\"utf-8\") as f:\n    content = f.read()",
      "buggy_code": "with open(\"data.txt\", \"r\") as f:\n    content = f.read()",
      "explanation": "Windows 默认用 GBK 编码，不指定 encoding 会乱码或报 UnicodeDecodeError。养成习惯：open() 永远加 encoding='utf-8'。",
      "hint": "Windows 默认编码是 GBK，中文文件需要指定 UTF-8",
      "id": "file_no_encoding",
      "kp": [
        "file_open",
        {
          "id": "pit11_02",
          "stage": 11,
          "title": "忘记关闭文件",
          "question": "open() 后忘记 close() 会怎样?",
          "buggy_code": "f = open('data.txt')\ndata = f.read()\n# 忘记 f.close(), 文件句柄泄漏!",
          "hint": "使用 with 语句自动关闭文件",
          "explanation": "忘记关闭文件会导致资源泄漏, 在大量操作时可能耗尽文件句柄. 始终用 with open() 语句, 它保证退出时自动关闭.",
          "answer": "with open('data.txt') as f:\n    data = f.read()\n# 自动关闭, 无需手动 close()",
          "kp": [
            "file",
            "with_statement",
            "resource_leak"
          ]
        }
      ],
      "question": "这段代码在 Windows 上读中文文件会出什么问题？请修正",
      "stage": 11,
      "title": "文件读写忘加 encoding"
    },
    {
      "id": "pit11_02",
      "stage": 11,
      "title": "忘记关闭文件",
      "question": "open() 后忘记 close() 会怎样?",
      "buggy_code": "f = open('data.txt')\ndata = f.read()\n# 忘记 f.close(), 文件句柄泄漏!",
      "hint": "使用 with 语句自动关闭文件",
      "explanation": "忘记关闭文件会导致资源泄漏, 在大量操作时可能耗尽文件句柄. 始终用 with open() 语句, 它保证退出时自动关闭.",
      "answer": "with open('data.txt') as f:\n    data = f.read()\n# 自动关闭, 无需手动 close()",
      "kp": [
        "file",
        "with_statement",
        "resource_leak"
      ]
    }
  ],
  14: [
    {
      "answer": "import re\npattern = r\"\\d+\"\nresult = re.findall(pattern, \"abc123\")\nprint(result)",
      "buggy_code": "import re\npattern = \"\\d+\"\nresult = re.findall(pattern, \"abc123\")\nprint(result)",
      "explanation": "没有 r 前缀时，\\d 被Python解释为转义字符，可能变成非法转义或丢失反斜杠。正则模式永远用 r\"\" 原始字符串。",
      "hint": "\\d 在普通字符串中被转义了，正则模式需要 r 前缀",
      "id": "regex_raw_string",
      "kp": [
        "regex_basic",
        {
          "id": "pit14_02",
          "stage": 14,
          "title": "正则的贪婪匹配",
          "question": "为什么 re.findall(r'<.*>', '<a>b<c>') 返回 ['<a>b<c>'] 而不是 ['<a>', '<c>']?",
          "buggy_code": "import re\nresult = re.findall(r'<.*>', '<a>b<c>')\nprint(result)  # ['<a>b<c>'] - 贪婪匹配!",
          "hint": "用 .*? 非贪婪模式代替 .*",
          "explanation": ".* 是贪婪模式, 会匹配尽可能多的字符. .*? 是非贪婪模式, 匹配尽可能少的字符. 结果: re.findall(r'<.*?>', '<a>b<c>') 返回 ['<a>', '<c>']",
          "answer": "import re\nresult = re.findall(r'<.*?>', '<a>b<c>')\nprint(result)  # ['<a>', '<c>']",
          "kp": [
            "regex",
            "greedy",
            "non_greedy"
          ]
        }
      ],
      "question": "这段代码能正确匹配吗？为什么？请修正",
      "stage": 14,
      "title": "正则忘写 r 前缀"
    },
    {
      "id": "pit14_02",
      "stage": 14,
      "title": "正则的贪婪匹配",
      "question": "为什么 re.findall(r'<.*>', '<a>b<c>') 返回 ['<a>b<c>']?",
      "buggy_code": "import re\nresult = re.findall(r'<.*>', '<a>b<c>')\nprint(result)  # 贪婪匹配!",
      "hint": "用 .*? 非贪婪模式代替 .*",
      "explanation": ".* 是贪婪模式, 会匹配尽可能多的字符. .*? 是非贪婪模式, 匹配尽可能少的字符.",
      "answer": "import re\nresult = re.findall(r'<.*?>', '<a>b<c>')\nprint(result)  # ['<a>', '<c>']",
      "kp": [
        "regex",
        "greedy",
        "non_greedy"
      ]
    }
  ],
  15: [
    {
      "answer": "class Dog:\n    def bark(self):\n        print(\"汪!\")\n\ndog = Dog()\ndog.bark()",
      "buggy_code": "class Dog:\n    def bark():\n        print(\"汪!\")\n\ndog = Dog()\ndog.bark()",
      "explanation": "TypeError: 实例方法第一个参数必须是 self，Python 自动传入实例对象。忘写 self 是 OOP 新手最常见的错。",
      "hint": "实例方法的第一个参数必须是 self",
      "id": "forgot_self",
      "kp": [
        "oop_init_self",
        "oop_class_object",
        {
          "id": "pit15_02",
          "stage": 15,
          "title": "可变默认参数",
          "question": "为什么 def f(x=[]) 的默认值会在调用间共享?",
          "buggy_code": "def add_item(item, lst=[]):\n    lst.append(item)\n    return lst\n\nprint(add_item(1))  # [1]\nprint(add_item(2))  # [1, 2] - 不是 [2]!",
          "hint": "默认参数在函数定义时创建一次, 不是每次调用时创建",
          "explanation": "可变对象作为默认参数时, 所有调用共享同一个对象. 正确做法: 用 None 作为默认值, 在函数体内创建新对象.",
          "answer": "def add_item(item, lst=None):\n    if lst is None:\n        lst = []\n    lst.append(item)\n    return lst",
          "kp": [
            "oop",
            "mutable_default",
            "gotcha"
          ]
        }
      ],
      "question": "调用 dog.bark() 会报什么错？请修正",
      "stage": 15,
      "title": "方法忘写 self"
    },
    {
      "id": "pit15_02",
      "stage": 15,
      "title": "可变默认参数",
      "question": "为什么 def f(x=[]) 的默认值会在调用间共享?",
      "buggy_code": "def add_item(item, lst=[]):\n    lst.append(item)\n    return lst\n\nprint(add_item(1))  # [1]\nprint(add_item(2))  # [1, 2] - 不是 [2]!",
      "hint": "默认参数在函数定义时创建一次",
      "explanation": "可变对象作为默认参数时, 所有调用共享同一个对象. 正确做法: 用 None 作为默认值, 在函数体内创建新对象.",
      "answer": "def add_item(item, lst=None):\n    if lst is None:\n        lst = []\n    lst.append(item)\n    return lst",
      "kp": [
        "oop",
        "mutable_default",
        "gotcha"
      ]
    }
  ],
  16: [
    {
      "answer": "class Animal:\n    def __init__(self, name):\n        self.name = name\n\nclass Dog(Animal):\n    def __init__(self, name, breed):\n        super().__init__(name)\n        self.breed = breed\n\ndog = Dog(\"旺财\", \"金毛\")\nprint(dog.name)",
      "buggy_code": "class Animal:\n    def __init__(self, name):\n        self.name = name\n\nclass Dog(Animal):\n    def __init__(self, breed):\n        self.breed = breed\n\ndog = Dog(\"金毛\")\nprint(dog.name)",
      "explanation": "子类定义了 __init__ 会覆盖父类的，导致 self.name 没有被设置。需要在子类 __init__ 中调用 super().__init__()。",
      "hint": "子类 __init__ 覆盖了父类，需要用 super() 调用父类初始化",
      "id": "override_init",
      "kp": [
        "oop_inherit",
        "oop_super",
        {
          "id": "pit16_02",
          "stage": 16,
          "title": "多重继承的 MRO 陷阱",
          "question": "钻石继承中, super() 到底调用谁?",
          "buggy_code": "class A:\n    def greet(self): print('A')\nclass B(A):\n    def greet(self): print('B'); super().greet()\nclass C(A):\n    def greet(self): print('C'); super().greet()\nclass D(B, C):\n    pass\nD().greet()  # B -> C -> A, 不是 B -> A!",
          "hint": "Python 用 C3 线性化确定 MRO, 不是简单的深度优先",
          "explanation": "多重继承时, Python 使用 C3 线性化算法计算方法解析顺序(MRO). D 的 MRO 是 D->B->C->A, super() 按此顺序查找. 用 ClassName.__mro__ 查看.",
          "answer": "print(D.__mro__)\n# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)",
          "kp": [
            "oop",
            "mro",
            "multiple_inheritance"
          ]
        }
      ],
      "question": "打印 dog.name 会报什么错？请修正",
      "stage": 16,
      "title": "子类忘调用 super().__init__()"
    },
    {
      "id": "pit16_02",
      "stage": 16,
      "title": "多重继承的 MRO 陷阱",
      "question": "钻石继承中, super() 到底调用谁?",
      "buggy_code": "class A:\n    def greet(self): print('A')\nclass B(A):\n    def greet(self): print('B'); super().greet()\nclass C(A):\n    def greet(self): print('C'); super().greet()\nclass D(B, C): pass\nD().greet()  # B -> C -> A!",
      "hint": "Python 用 C3 线性化确定 MRO",
      "explanation": "多重继承时, Python 使用 C3 线性化算法计算方法解析顺序(MRO). 用 ClassName.__mro__ 查看.",
      "answer": "print(D.__mro__)\n# (D, B, C, A, object)",
      "kp": [
        "oop",
        "mro",
        "multiple_inheritance"
      ]
    }
  ],
  17: [
    {
      "answer": "# 方案1：延迟导入\ndef func_a():\n    from b import func_b\n    func_b()\n\n# 方案2：提取公共部分到第三个模块",
      "buggy_code": "# a.py: from b import func_b\n# b.py: from a import func_a\n# 两个文件互相导入会报 ImportError",
      "explanation": "两个模块互相导入会形成循环依赖。解决：把导入移到函数内部（延迟导入），或提取公共部分到独立模块。",
      "hint": "把导入放到函数内部，或重构模块结构",
      "id": "circular_import",
      "kp": [
        "mod_import",
        {
          "id": "pit17_02",
          "stage": 17,
          "title": "循环导入",
          "question": "为什么 a.py 导入 b.py, b.py 又导入 a.py 会出错?",
          "buggy_code": "# a.py\nfrom b import func_b\ndef func_a(): return func_b()\n\n# b.py\nfrom a import func_a  # ImportError!",
          "hint": "避免循环导入: 延迟导入或重构模块结构",
          "explanation": "循环导入导致其中一个模块在初始化时还无法访问另一个模块的符号. 解决方案: 1) 将导入移到函数内部(延迟导入); 2) 合并模块; 3) 提取共享部分到第三个模块.",
          "answer": "# b.py\ndef func_b():\n    from a import func_a  # 延迟导入\n    return func_a()",
          "kp": [
            "module",
            "circular_import",
            "lazy_import"
          ]
        }
      ],
      "question": "循环导入怎么解决？（写解决方案代码）",
      "stage": 17,
      "title": "循环导入问题"
    },
    {
      "id": "pit17_02",
      "stage": 17,
      "title": "循环导入",
      "question": "为什么 a.py 导入 b.py, b.py 又导入 a.py 会出错?",
      "buggy_code": "# a.py\nfrom b import func_b\ndef func_a(): return func_b()\n\n# b.py\nfrom a import func_a  # ImportError!",
      "hint": "避免循环导入: 延迟导入或重构模块结构",
      "explanation": "循环导入导致其中一个模块在初始化时还无法访问另一个模块的符号. 解决方案: 延迟导入、合并模块、或提取共享部分.",
      "answer": "# b.py\ndef func_b():\n    from a import func_a  # 延迟导入\n    return func_a()",
      "kp": [
        "module",
        "circular_import",
        "lazy_import"
      ]
    }
  ],
  18: [
    {
      "answer": "from functools import wraps\n\ndef my_decorator(func):\n    @wraps(func)\n    def wrapper(*args, **kwargs):\n        return func(*args, **kwargs)\n    return wrapper\n\n@my_decorator\ndef my_function():\n    # 我的函数\n    pass\n\nprint(my_function.__name__)",
      "buggy_code": "def my_decorator(func):\n    def wrapper(*args, **kwargs):\n        return func(*args, **kwargs)\n    return wrapper\n\n@my_decorator\ndef my_function():\n    # 我的函数\n    pass\n\nprint(my_function.__name__)",
      "explanation": "不用 @wraps 时，装饰后函数的 __name__ 变成 'wrapper'，丢失了原函数名和文档。@wraps 保留原函数的元信息。",
      "hint": "用 @functools.wraps 保留原函数信息",
      "id": "decorator_no_wraps",
      "kp": [
        "dec_wraps",
        "dec_basic",
        {
          "id": "pit18_02",
          "stage": 18,
          "title": "装饰器丢失函数元信息",
          "question": "为什么被装饰的函数 __name__ 变成了 wrapper?",
          "buggy_code": "def my_decorator(func):\n    def wrapper(*args):\n        return func(*args)\n    return wrapper\n\n@my_decorator\ndef greet(): pass\n\nprint(greet.__name__)  # 'wrapper' 不是 'greet'!",
          "hint": "使用 functools.wraps 保留原函数信息",
          "explanation": "装饰器返回的 wrapper 函数会覆盖原函数的 __name__, __doc__ 等属性. 使用 @functools.wraps(func) 装饰 wrapper 即可保留原函数信息.",
          "answer": "import functools\ndef my_decorator(func):\n    @functools.wraps(func)\n    def wrapper(*args):\n        return func(*args)\n    return wrapper",
          "kp": [
            "decorator",
            "functools_wraps",
            "metadata"
          ]
        }
      ],
      "question": "my_function.__name__ 打印什么？为什么不是 'my_function'？请修正",
      "stage": 18,
      "title": "装饰器忘用 @wraps"
    },
    {
      "id": "pit18_02",
      "stage": 18,
      "title": "装饰器丢失函数元信息",
      "question": "为什么被装饰的函数 __name__ 变成了 wrapper?",
      "buggy_code": "def my_decorator(func):\n    def wrapper(*args):\n        return func(*args)\n    return wrapper\n\n@my_decorator\ndef greet(): pass\n\nprint(greet.__name__)  # 'wrapper'!",
      "hint": "使用 functools.wraps 保留原函数信息",
      "explanation": "装饰器返回的 wrapper 函数会覆盖原函数的 __name__, __doc__ 等属性. 使用 @functools.wraps(func) 即可保留.",
      "answer": "import functools\ndef my_decorator(func):\n    @functools.wraps(func)\n    def wrapper(*args):\n        return func(*args)\n    return wrapper",
      "kp": [
        "decorator",
        "functools_wraps",
        "metadata"
      ]
    }
  ],
  19: [
    {
      "answer": "import sqlite3\nconn = sqlite3.connect('test.db')\ncursor = conn.cursor()\ncursor.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))\nconn.commit()\nprint('数据已插入')",
      "buggy_code": "import sqlite3\nconn = sqlite3.connect('test.db')\ncursor = conn.cursor()\ncursor.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))\n# 程序结束了\nprint('数据已插入')",
      "explanation": "SQLite 默认在事务中执行，不 commit 的修改会在连接关闭时回滚。写操作后必须 commit()。",
      "hint": "INSERT/UPDATE/DELETE 后必须 conn.commit()",
      "id": "sqlite_no_commit",
      "kp": [
        "db_sqlite",
        "db_transaction",
        {
          "id": "pit19_02",
          "stage": 19,
          "title": "SQL 注入风险",
          "question": "为什么用 f-string 拼接 SQL 很危险?",
          "buggy_code": "name = input('Name: ')\ncursor.execute(f\"SELECT * FROM users WHERE name='{name}'\")\n# 输入: ' OR 1=1 -- 就能绕过验证!",
          "hint": "使用参数化查询, 永远不要拼接 SQL",
          "explanation": "字符串拼接 SQL 是注入攻击的入口. 用户输入 ' OR 1=1 -- 可以修改查询逻辑. 使用参数化查询: cursor.execute('SELECT * FROM users WHERE name=?', (name,))",
          "answer": "name = input('Name: ')\ncursor.execute('SELECT * FROM users WHERE name=?', (name,))",
          "kp": [
            "sql",
            "injection",
            "parameterized_query"
          ]
        }
      ],
      "question": "重启程序后为什么查不到 Alice？",
      "stage": 19,
      "title": "忘记 commit 导致数据丢失"
    },
    {
      "id": "pit19_02",
      "stage": 19,
      "title": "SQL 注入风险",
      "question": "为什么用 f-string 拼接 SQL 很危险?",
      "buggy_code": "name = input('Name: ')\ncursor.execute(f\"SELECT * FROM users WHERE name='{name}'\")",
      "hint": "使用参数化查询, 永远不要拼接 SQL",
      "explanation": "字符串拼接 SQL 是注入攻击的入口. 用户输入可以修改查询逻辑. 使用参数化查询.",
      "answer": "name = input('Name: ')\ncursor.execute('SELECT * FROM users WHERE name=?', (name,))",
      "kp": [
        "sql",
        "injection",
        "parameterized_query"
      ]
    }
  ],
  21: [
    {
      "answer": "from pydantic import BaseModel\n\nclass Item(BaseModel):\n    name: str\n    price: float\n\napp = FastAPI()\n\n@app.post('/items')\nasync def create(item: Item):\n    return {'name': item.name, 'price': item.price}",
      "buggy_code": "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.post('/items')\ndef create(item: dict):\n    return {'name': item['name'], 'price': item['price']}",
      "explanation": "dict 参数没有验证，缺字段或类型错误会导致 500。Pydantic BaseModel 自动验证+类型转换+友好错误信息。",
      "hint": "dict 类型没有验证，传错字段会 500 错误。用 Pydantic BaseModel",
      "id": "api_no_validation",
      "kp": [
        "api_pydantic",
        "api_fastapi"
      ],
      "question": "这个 API 有什么问题？",
      "stage": 21,
      "title": "API 不做输入验证"
    },
    {
      "id": "pit21_02",
      "stage": 21,
      "title": "API 返回数据未验证",
      "question": "为什么不能直接信任 API 返回的数据?",
      "buggy_code": "import requests\ndata = requests.get(url).json()\nname = data['name']  # KeyError!",
      "hint": "API 可能返回错误格式, 需要校验关键字段",
      "explanation": "外部 API 可能因版本更新、服务器错误等返回意外格式. 应检查响应状态码, 使用 .get() 安全访问字典.",
      "answer": "import requests\nresp = requests.get(url)\nresp.raise_for_status()\ndata = resp.json()\nname = data.get('name', 'Unknown')",
      "kp": [
        "api",
        "validation",
        "error_handling"
      ]
    }
  ],
  24: [
    {
      "answer": "import matplotlib\nmatplotlib.rcParams[\"font.sans-serif\"] = [\"SimHei\"]\nmatplotlib.rcParams[\"axes.unicode_minus\"] = False\nimport matplotlib.pyplot as plt\nplt.title(\"销售趋势\")\nplt.savefig(\"chart.png\")",
      "buggy_code": "import matplotlib.pyplot as plt\nplt.title(\"销售趋势\")\nplt.savefig(\"chart.png\")",
      "explanation": "matplotlib 默认用英文字体，中文会显示方块。设置 SimHei 字体可解决。Mac 用 Arial Unicode MS。",
      "hint": "matplotlib 默认字体不支持中文，需要设置",
      "id": "matplotlib_chinese",
      "kp": [
        "viz_line",
        {
          "id": "pit24_02",
          "stage": 24,
          "title": "matplotlib 中文乱码",
          "question": "为什么图表上的中文显示为方块?",
          "buggy_code": "import matplotlib.pyplot as plt\nplt.title('你好')  # 显示为方块!",
          "hint": "需要设置中文字体",
          "explanation": "matplotlib 默认字体不支持中文. 解决: plt.rcParams['font.sans-serif'] = ['SimHei'] 设置中文字体, plt.rcParams['axes.unicode_minus'] = False 修复负号显示.",
          "answer": "import matplotlib.pyplot as plt\nplt.rcParams['font.sans-serif'] = ['SimHei']\nplt.rcParams['axes.unicode_minus'] = False\nplt.title('你好')  # 正常显示",
          "kp": [
            "matplotlib",
            "chinese_font",
            "rcParams"
          ]
        }
      ],
      "question": "保存的图标题会显示什么？请修正中文显示问题",
      "stage": 24,
      "title": "matplotlib 中文显示乱码"
    },
    {
      "id": "pit24_02",
      "stage": 24,
      "title": "matplotlib 中文乱码",
      "question": "为什么图表上的中文显示为方块?",
      "buggy_code": "import matplotlib.pyplot as plt\nplt.title('你好')  # 显示为方块!",
      "hint": "需要设置中文字体",
      "explanation": "matplotlib 默认字体不支持中文. 解决: 设置 SimHei 字体和 unicode_minus 选项.",
      "answer": "import matplotlib.pyplot as plt\nplt.rcParams['font.sans-serif'] = ['SimHei']\nplt.rcParams['axes.unicode_minus'] = False\nplt.title('你好')",
      "kp": [
        "matplotlib",
        "chinese_font",
        "rcParams"
      ]
    }
  ],
  25: [
    {
      "answer": "from selenium import webdriver\nfrom selenium.webdriver.common.by import By\nfrom selenium.webdriver.support.ui import WebDriverWait\nfrom selenium.webdriver.support import expected_conditions as EC\n\ndriver = webdriver.Chrome()\ndriver.get(\"https://example.com\")\nwait = WebDriverWait(driver, 10)\nelement = wait.until(EC.presence_of_element_located((By.ID, 'content')))\nprint(element.text)",
      "buggy_code": "from selenium import webdriver\ndriver = webdriver.Chrome()\ndriver.get(\"https://example.com\")\nelement = driver.find_element('id', 'content')\nprint(element.text)",
      "explanation": "动态页面元素可能还没渲染出来，find_element 立即执行就会找不到。必须用 WebDriverWait 显式等待元素出现。",
      "hint": "页面可能还没加载完，需要显式等待",
      "id": "selenium_no_wait",
      "kp": [
        "crawl_selenium",
        "crawl_wait",
        {
          "id": "pit25_02",
          "stage": 25,
          "title": "Selenium 等待不足",
          "question": "为什么 element.click() 前经常报 NoSuchElementException?",
          "buggy_code": "from selenium import webdriver\ndriver = webdriver.Chrome()\ndriver.get(url)\ndriver.find_element('id', 'btn').click()  # 元素还没加载!",
          "hint": "使用显式等待 WebDriverWait 而非 time.sleep",
          "explanation": "页面加载是异步的, 直接查找元素可能还未渲染. time.sleep 固定等待浪费时间且不可靠. 用 WebDriverWait + expected_conditions 等元素就绪再操作.",
          "answer": "from selenium.webdriver.support.ui import WebDriverWait\nfrom selenium.webdriver.support import expected_conditions as EC\nwait = WebDriverWait(driver, 10)\nbtn = wait.until(EC.element_to_be_clickable(('id', 'btn')))\nbtn.click()",
          "kp": [
            "selenium",
            "webdriver_wait",
            "explicit_wait"
          ]
        }
      ],
      "question": "为什么这段代码经常报 NoSuchElementException？",
      "stage": 25,
      "title": "Selenium 不等元素加载就操作"
    },
    {
      "id": "pit25_02",
      "stage": 25,
      "title": "Selenium 等待不足",
      "question": "为什么 element.click() 前经常报 NoSuchElementException?",
      "buggy_code": "from selenium import webdriver\ndriver = webdriver.Chrome()\ndriver.get(url)\ndriver.find_element('id', 'btn').click()  # 元素还没加载!",
      "hint": "使用显式等待 WebDriverWait",
      "explanation": "页面加载是异步的, 直接查找元素可能还未渲染. 用 WebDriverWait + expected_conditions 等元素就绪再操作.",
      "answer": "from selenium.webdriver.support.ui import WebDriverWait\nfrom selenium.webdriver.support import expected_conditions as EC\nwait = WebDriverWait(driver, 10)\nbtn = wait.until(EC.element_to_be_clickable(('id', 'btn')))\nbtn.click()",
      "kp": [
        "selenium",
        "webdriver_wait",
        "explicit_wait"
      ]
    }
  ],
  26: [
    {
      "answer": "import asyncio\nasync def fetch_data():\n    await asyncio.sleep(0.1)\n    return 42\nasync def main():\n    result = await fetch_data()\n    print(result)\nasyncio.run(main())",
      "buggy_code": "import asyncio\nasync def fetch_data():\n    await asyncio.sleep(0.1)\n    return 42\nresult = fetch_data()\nprint(result)",
      "explanation": "直接调用 async 函数返回的是协程对象，不是结果。必须用 await 等待结果，或在 asyncio.run 中执行。",
      "hint": "调用 async 函数返回的是协程对象，必须 await",
      "id": "async_no_await",
      "kp": [
        "async_def",
        "async_await",
        {
          "id": "pit26_02",
          "stage": 26,
          "title": "asyncio 中调用阻塞函数",
          "question": "为什么在 async 函数里用 time.sleep 会卡住整个事件循环?",
          "buggy_code": "import asyncio, time\nasync def task():\n    time.sleep(5)  # 阻塞整个事件循环!\n    print('done')",
          "hint": "在 async 函数中使用 await asyncio.sleep() 代替 time.sleep()",
          "explanation": "time.sleep() 是同步阻塞调用, 会冻结整个事件循环. 在 async 函数中应使用 await asyncio.sleep(), 它会交出控制权让其他协程运行.",
          "answer": "import asyncio\nasync def task():\n    await asyncio.sleep(5)  # 非阻塞等待\n    print('done')",
          "kp": [
            "asyncio",
            "blocking",
            "event_loop"
          ]
        }
      ],
      "question": "为什么 result 不是 42？",
      "stage": 26,
      "title": "忘记 await 协程"
    },
    {
      "id": "pit26_02",
      "stage": 26,
      "title": "asyncio 中调用阻塞函数",
      "question": "为什么在 async 函数里用 time.sleep 会卡住整个事件循环?",
      "buggy_code": "import asyncio, time\nasync def task():\n    time.sleep(5)  # 阻塞事件循环!\n    print('done')",
      "hint": "在 async 函数中使用 await asyncio.sleep()",
      "explanation": "time.sleep() 是同步阻塞调用, 会冻结整个事件循环. 在 async 函数中应使用 await asyncio.sleep().",
      "answer": "import asyncio\nasync def task():\n    await asyncio.sleep(5)\n    print('done')",
      "kp": [
        "asyncio",
        "blocking",
        "event_loop"
      ]
    }
  ],
  27: [
    {
      "answer": "class MySpider(scrapy.Spider):\n    name = 'my'\n    start_urls = ['https://example.com/page/1']\n    def parse(self, response):\n        for item in response.css('.item'):\n            yield {'text': item.css('::text').get()}\n        next_page = response.css('.next a::attr(href)').get()\n        if next_page:\n            yield response.follow(next_page, callback=self.parse)",
      "buggy_code": "class MySpider(scrapy.Spider):\n    name = 'my'\n    start_urls = ['https://example.com/page/1']\n    def parse(self, response):\n        for item in response.css('.item'):\n            yield {'text': item.css('::text').get()}",
      "explanation": "Scrapy 不会自动翻页，必须在 parse 中手动提取下一页链接并 yield response.follow 请求。",
      "hint": "需要在 parse 中找到下一页链接并用 response.follow",
      "id": "scrapy_no_follow",
      "kp": [
        "crawl_scrapy",
        {
          "id": "pit27_02",
          "stage": 27,
          "title": "Scrapy 不遵守 robots.txt",
          "question": "为什么 Scrapy 爬不到数据?",
          "buggy_code": "# settings.py 中 ROBOTSTXT_OBEY = True (默认)\n# 目标网站 robots.txt 禁止爬取",
          "hint": "检查 ROBOTSTXT_OBEY 设置和目标网站的 robots.txt",
          "explanation": "Scrapy 默认遵守 robots.txt 协议. 如果目标网站禁止爬取, Scrapy 会跳过. 开发/学习时可设 ROBOTSTXT_OBEY = False, 但生产环境应遵守协议.",
          "answer": "# settings.py\nROBOTSTXT_OBEY = False  # 仅用于学习/开发",
          "kp": [
            "scrapy",
            "robots_txt",
            "crawling_rules"
          ]
        }
      ],
      "question": "这个爬虫为什么不会自动翻页？",
      "stage": 27,
      "title": "Scrapy 爬虫只爬第一页"
    },
    {
      "id": "pit27_02",
      "stage": 27,
      "title": "Scrapy 不遵守 robots.txt",
      "question": "为什么 Scrapy 爬不到数据?",
      "buggy_code": "# settings.py ROBOTSTXT_OBEY = True (默认)\n# 目标网站 robots.txt 禁止爬取",
      "hint": "检查 ROBOTSTXT_OBEY 设置",
      "explanation": "Scrapy 默认遵守 robots.txt 协议. 如果目标网站禁止爬取, Scrapy 会跳过. 开发时可设 ROBOTSTXT_OBEY = False.",
      "answer": "# settings.py\nROBOTSTXT_OBEY = False  # 仅用于学习",
      "kp": [
        "scrapy",
        "robots_txt",
        "crawling_rules"
      ]
    }
  ],
  28: [
    {
      "answer": "name = input('Name: ')\ncursor.execute('SELECT * FROM users WHERE name=?', (name,))",
      "buggy_code": "name = input('Name: ')\ncursor.execute(f\"SELECT * FROM users WHERE name='{name}'\")",
      "explanation": "f-string 拼 SQL 导致注入漏洞（输入 ' OR 1=1 -- 可绕过验证）。必须用参数化查询（? 占位符）。",
      "hint": "永远不要用 f-string/format 拼接 SQL，用参数化查询",
      "id": "sql_injection",
      "kp": [
        "crawl_mysql",
        {
          "id": "pit28_02",
          "stage": 28,
          "title": "爬虫数据未去重",
          "question": "为什么数据库里有大量重复数据?",
          "buggy_code": "# 爬虫重启后重新爬取, 未做去重检查\ncursor.execute('INSERT INTO items VALUES (?)', (item,))\n# 重复插入!",
          "hint": "插入前检查是否已存在, 或使用 UNIQUE 约束",
          "explanation": "爬虫重启或增量爬取时, 可能重复插入数据. 解决: 1) 数据库设置 UNIQUE 约束 + INSERT OR IGNORE; 2) 爬取前检查 URL 是否已处理; 3) 使用 Scrapy 的 dupefilter.",
          "answer": "cursor.execute(\n    'INSERT OR IGNORE INTO items VALUES (?, ?)',\n    (item_id, item_data)\n)",
          "kp": [
            "crawl",
            "deduplication",
            "unique_constraint"
          ]
        }
      ],
      "question": "这段代码有什么安全漏洞？如何修复？",
      "stage": 28,
      "title": "SQL 注入漏洞"
    },
    {
      "id": "pit28_02",
      "stage": 28,
      "title": "爬虫数据未去重",
      "question": "为什么数据库里有大量重复数据?",
      "buggy_code": "cursor.execute('INSERT INTO items VALUES (?)', (item,))\n# 重复插入!",
      "hint": "使用 UNIQUE 约束或 INSERT OR IGNORE",
      "explanation": "爬虫重启或增量爬取时, 可能重复插入数据. 解决: UNIQUE 约束 + INSERT OR IGNORE.",
      "answer": "cursor.execute('INSERT OR IGNORE INTO items VALUES (?, ?)', (item_id, item_data))",
      "kp": [
        "crawl",
        "deduplication",
        "unique_constraint"
      ]
    }
  ],
  30: [
    {
      "answer": "from pathlib import Path\npath = Path(\"data\") / \"files\" / \"report.csv\"\nprint(path)",
      "buggy_code": "path = \"data\\\\files\\\\report.csv\"\nprint(path)",
      "explanation": "Windows 用 \\ 分隔，Linux/Mac 用 /。硬编码反斜杠跨平台必出问题。pathlib 自动处理路径分隔符。",
      "hint": "用 os.path.join 或 pathlib",
      "id": "path_hardcode",
      "kp": [
        "auto_pathlib",
        "auto_os",
        {
          "id": "pit30_02",
          "stage": 30,
          "title": "os.system 的返回值不是输出",
          "question": "为什么 result = os.system('echo hello') 拿不到输出?",
          "buggy_code": "result = os.system('echo hello')\nprint(result)  # 0 (退出码), 不是 'hello'!",
          "hint": "用 subprocess.run + capture_output=True 获取输出",
          "explanation": "os.system() 只返回退出码(0=成功), 不捕获输出. 要获取命令输出, 使用 subprocess.run() + capture_output=True + text=True.",
          "answer": "import subprocess\nresult = subprocess.run(['echo', 'hello'], capture_output=True, text=True)\nprint(result.stdout)  # 'hello\\n'",
          "kp": [
            "subprocess",
            "os_system",
            "capture_output"
          ]
        }
      ],
      "question": "这段路径在 Windows 和 Linux 上都能用吗？请用跨平台方式改写",
      "stage": 30,
      "title": "硬编码路径跨平台出错"
    },
    {
      "id": "pit30_02",
      "stage": 30,
      "title": "os.system 的返回值不是输出",
      "question": "为什么 result = os.system('echo hello') 拿不到输出?",
      "buggy_code": "result = os.system('echo hello')\nprint(result)  # 0 (退出码), 不是 'hello'!",
      "hint": "用 subprocess.run + capture_output=True",
      "explanation": "os.system() 只返回退出码, 不捕获输出. 使用 subprocess.run() + capture_output=True.",
      "answer": "import subprocess\nresult = subprocess.run(['echo', 'hello'], capture_output=True, text=True)\nprint(result.stdout)",
      "kp": [
        "subprocess",
        "os_system",
        "capture_output"
      ]
    }
  ],
  31: [
    {
      "answer": "from selenium.webdriver.support.ui import WebDriverWait\nfrom selenium.webdriver.support import expected_conditions as EC\nfrom selenium.webdriver.common.by import By\n\ndriver.get(\"https://example.com\")\nelement = WebDriverWait(driver, 10).until(\n    EC.presence_of_element_located((By.ID, \"content\"))\n)",
      "buggy_code": "driver.get(\"https://example.com\")\nelement = driver.find_element(By.ID, \"content\")",
      "explanation": "页面加载需要时间，立即 find_element 可能找不到。显式等待（WebDriverWait）比 time.sleep 更可靠。",
      "hint": "页面可能还没加载完，元素不存在",
      "id": "selenium_no_wait",
      "kp": [
        "auto_wait",
        "auto_selenium",
        {
          "id": "pit31_02",
          "stage": 31,
          "title": "pyautogui 的安全开关",
          "question": "为什么 pyautogui 操作突然停了?",
          "buggy_code": "import pyautogui\nfor i in range(1000):\n    pyautogui.click()  # 鼠标失控!",
          "hint": "pyautogui 有安全机制: 鼠标移到屏幕角落会触发 FailSafeException",
          "explanation": "pyautogui 内置安全机制: 当鼠标快速移到屏幕左上角(0,0)时, 抛出 FailSafeException 中止所有操作. 这是为了防止脚本失控. 也可设 pyautogui.FAILSAFE = False 关闭(不推荐).",
          "answer": "import pyautogui\npyautogui.PAUSE = 1  # 每个操作后暂停1秒\n# 紧急时: 把鼠标快速甩到屏幕左上角",
          "kp": [
            "pyautogui",
            "failsafe",
            "automation_safety"
          ]
        }
      ],
      "question": "这段代码可能出什么问题？请用显式等待修正",
      "stage": 31,
      "title": "Selenium 不等页面加载就找元素"
    },
    {
      "id": "pit31_02",
      "stage": 31,
      "title": "pyautogui 的安全开关",
      "question": "为什么 pyautogui 操作突然停了?",
      "buggy_code": "import pyautogui\nfor i in range(1000):\n    pyautogui.click()  # 鼠标失控!",
      "hint": "鼠标移到屏幕角落会触发 FailSafeException",
      "explanation": "pyautogui 内置安全机制: 鼠标快速移到左上角时, 抛出 FailSafeException 中止操作.",
      "answer": "import pyautogui\npyautogui.PAUSE = 1  # 每个操作后暂停1秒",
      "kp": [
        "pyautogui",
        "failsafe",
        "automation_safety"
      ]
    }
  ],
  32: [
    {
      "answer": "import tkinter as tk\nroot = tk.Tk()\nlabel = tk.Label(root, text='Loading...')\nlabel.pack()\ndef load_data():\n    label.config(text='Done')\nroot.after(100, load_data)\nroot.mainloop()",
      "buggy_code": "import tkinter as tk\nimport time\nroot = tk.Tk()\ntime.sleep(5)  # 加载数据\nlabel = tk.Label(root, text='Done')\nlabel.pack()\nroot.mainloop()",
      "explanation": "time.sleep 阻塞主线程，mainloop 无法启动，GUI 冻结。耗时操作要用 after() 延迟执行或 threading 后台处理。",
      "hint": "time.sleep 会阻塞主线程，GUI 无法渲染。用 after 延迟执行",
      "id": "tkinter_mainloop_block",
      "kp": [
        "gui_tkinter",
        "gui_event",
        {
          "id": "pit32_02",
          "stage": 32,
          "title": "Tkinter 主循环阻塞",
          "question": "为什么在 Tkinter 里跑耗时操作界面会卡死?",
          "buggy_code": "import tkinter as tk\ndef heavy_task():\n    for i in range(10000000): pass  # 界面卡死!\n\nroot = tk.Tk()\nbtn = tk.Button(root, command=heavy_task)\nbtn.pack()\nroot.mainloop()",
          "hint": "耗时操作应在子线程运行, 或用 after() 分片处理",
          "explanation": "Tkinter 的 mainloop() 是单线程事件循环. 耗时操作会阻塞界面更新. 解决: 1) 使用 threading.Thread 运行耗时任务; 2) 用 root.after() 将任务分片; 3) 使用 queue 传递结果.",
          "answer": "import tkinter as tk, threading\ndef heavy_task():\n    for i in range(10000000): pass\n    root.after(0, lambda: label.config(text='Done'))\n\nthreading.Thread(target=heavy_task, daemon=True).start()",
          "kp": [
            "tkinter",
            "mainloop",
            "threading"
          ]
        }
      ],
      "question": "为什么窗口5秒后才出现？如何修复？",
      "stage": 32,
      "title": "mainloop 之前放耗时操作"
    },
    {
      "id": "pit32_02",
      "stage": 32,
      "title": "Tkinter 主循环阻塞",
      "question": "为什么在 Tkinter 里跑耗时操作界面会卡死?",
      "buggy_code": "def heavy_task():\n    for i in range(10000000): pass  # 界面卡死!",
      "hint": "耗时操作应在子线程运行",
      "explanation": "Tkinter 的 mainloop() 是单线程事件循环. 耗时操作会阻塞界面更新. 使用 threading.Thread.",
      "answer": "import threading\ndef heavy_task():\n    for i in range(10000000): pass\nthreading.Thread(target=heavy_task, daemon=True).start()",
      "kp": [
        "tkinter",
        "mainloop",
        "threading"
      ]
    }
  ],
  33: [
    {
      "answer": "import shutil\nfrom pathlib import Path\n\ntarget = Path(\"old_project\")\nif target.exists() and target.is_dir():\n    confirm = input(f\"确定要删除 {target} 吗？(y/n): \")\n    if confirm.lower() == \"y\":\n        try:\n            shutil.rmtree(target)\n            print(\"删除完成\")\n        except Exception as e:\n            print(f\"删除失败: {e}\")\n    else:\n        print(\"已取消\")\nelse:\n    print(f\"{target} 不存在或不是目录\")",
      "buggy_code": "import shutil\nshutil.rmtree(\"old_project\")\nprint(\"删除完成\")",
      "explanation": "rmtree 不可恢复，路径写错可能删错目录。自动化脚本必须有：1.路径确认 2.用户确认 3.异常捕获 4.失败回退。",
      "hint": "rmtree 不可恢复！至少要确认路径、加 try/except",
      "id": "no_failsafe",
      "kp": [
        "auto_shutil",
        "auto_best_practice",
        {
          "id": "pit33_02",
          "stage": 33,
          "title": "自动化脚本无日志",
          "question": "脚本出错后为什么找不到原因?",
          "buggy_code": "# 自动化脚本没有日志记录\nfor url in urls:\n    data = requests.get(url).json()  # 出错了也不知道是哪个URL",
          "hint": "用 logging 模块记录关键操作和错误",
          "explanation": "自动化脚本无人值守运行, 没有日志就无法排查问题. 应在关键步骤添加 logging.info/warning/error, 记录时间戳和操作上下文.",
          "answer": "import logging\nlogging.basicConfig(filename='auto.log', level=logging.INFO,\n    format='%(asctime)s %(levelname)s %(message)s')\nfor url in urls:\n    try:\n        data = requests.get(url, timeout=10).json()\n        logging.info(f'Fetched {url}')\n    except Exception as e:\n        logging.error(f'Failed {url}: {e}')",
          "kp": [
            "logging",
            "automation",
            "error_tracking"
          ]
        }
      ],
      "question": "这段代码有什么风险？请加上安全措施",
      "stage": 33,
      "title": "自动化脚本没有异常处理和回退"
    },
    {
      "id": "pit33_02",
      "stage": 33,
      "title": "自动化脚本无日志",
      "question": "脚本出错后为什么找不到原因?",
      "buggy_code": "for url in urls:\n    data = requests.get(url).json()  # 出错了也不知道是哪个URL",
      "hint": "用 logging 模块记录关键操作和错误",
      "explanation": "自动化脚本无人值守运行, 没有日志就无法排查问题. 应在关键步骤添加 logging.",
      "answer": "import logging\nlogging.basicConfig(filename='auto.log', level=logging.INFO)\nfor url in urls:\n    try:\n        data = requests.get(url, timeout=10).json()\n        logging.info(f'Fetched {url}')\n    except Exception as e:\n        logging.error(f'Failed {url}: {e}')",
      "kp": [
        "logging",
        "automation",
        "error_tracking"
      ]
    }
  ],
  34: [
    {
      "answer": "import threading\nclass Config:\n    _instance = None\n    _lock = threading.Lock()\n    def __new__(cls):\n        with cls._lock:\n            if cls._instance is None:\n                cls._instance = super().__new__(cls)\n        return cls._instance",
      "buggy_code": "class Config:\n    _instance = None\n    def __new__(cls):\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)\n        return cls._instance",
      "explanation": "两个线程可能同时通过 if None 检查，各创建一个实例。加 Lock 确保只有一个线程能进入创建逻辑。",
      "hint": "两个线程可能同时通过 None 检查，加 threading.Lock",
      "id": "singleton_thread_safety",
      "kp": [
        "pattern_singleton",
        {
          "id": "pit34_02",
          "stage": 34,
          "title": "单例模式的线程安全",
          "question": "为什么多线程下单例可能创建多个实例?",
          "buggy_code": "class Singleton:\n    _instance = None\n    def __new__(cls):\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)  # 线程不安全!\n        return cls._instance",
          "hint": "使用 threading.Lock 保护实例创建过程",
          "explanation": "多线程下, 两个线程可能同时通过 None 检查, 各创建一个实例. 解决: 使用锁保护, 或用模块级变量(天然线程安全), 或用 __new__ + 双重检查.",
          "answer": "import threading\nclass Singleton:\n    _instance = None\n    _lock = threading.Lock()\n    def __new__(cls):\n        if cls._instance is None:\n            with cls._lock:\n                if cls._instance is None:\n                    cls._instance = super().__new__(cls)\n        return cls._instance",
          "kp": [
            "singleton",
            "thread_safety",
            "design_pattern"
          ]
        }
      ],
      "question": "在多线程环境下，这个单例可能创建多个实例，为什么？",
      "stage": 34,
      "title": "单例模式在多线程下不安全"
    },
    {
      "id": "pit34_02",
      "stage": 34,
      "title": "单例模式的线程安全",
      "question": "为什么多线程下单例可能创建多个实例?",
      "buggy_code": "class Singleton:\n    _instance = None\n    def __new__(cls):\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)  # 线程不安全!\n        return cls._instance",
      "hint": "使用 threading.Lock 保护实例创建过程",
      "explanation": "多线程下, 两个线程可能同时通过 None 检查, 各创建一个实例. 解决: 使用锁保护或双重检查.",
      "answer": "import threading\nclass Singleton:\n    _instance = None\n    _lock = threading.Lock()\n    def __new__(cls):\n        if cls._instance is None:\n            with cls._lock:\n                if cls._instance is None:\n                    cls._instance = super().__new__(cls)\n        return cls._instance",
      "kp": [
        "singleton",
        "thread_safety",
        "design_pattern"
      ]
    }
  ],
  35: [
    {
      "answer": "def binary_search(arr, target):\n    lo, hi = 0, len(arr) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return -1",
      "buggy_code": "def binary_search(arr, target):\n    lo, hi = 0, len(arr)\n    while lo < hi:\n        mid = (lo + hi) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return -1",
      "explanation": "两个常见错误：1. hi=len(arr) 应为 len(arr)-1（越界）2. while lo<hi 应为 lo<=hi（漏查最后一个元素）。二分查找边界条件是最容易出错的。",
      "hint": "hi 应为 len(arr)-1，while 条件应为 lo <= hi",
      "id": "binary_search_boundary",
      "kp": [
        "algo_search"
      ],
      "question": "这个二分查找有什么边界错误？请修正",
      "stage": 35,
      "title": "二分查找边界条件错误"
    },
    {
      "answer": "def fibonacci(n):\n    if n <= 1:\n        return n\n    a, b = 0, 1\n    for _ in range(2, n + 1):\n        a, b = b, a + b\n    return b\n\nprint(fibonacci(50))",
      "buggy_code": "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n - 1) + fibonacci(n - 2)\n\nprint(fibonacci(50))",
      "explanation": "递归 fibonacci(50) 会做约 2^50 次调用，指数级爆炸。用迭代或记忆化可 O(n) 解决。",
      "hint": "递归树有大量重复计算，fib(50) 会永远跑不完",
      "id": "recursion_explosion",
      "kp": [
        "algo_recursion",
        "algo_complexity"
      ],
      "question": "为什么 fibonacci(50) 跑不完？请用迭代改写",
      "stage": 35,
      "title": "递归斐波那契的指数爆炸"
    }
  ],
  36: [
    {
      "answer": "def coin_change(coins, amount):\n    dp = [float(\"inf\")] * (amount + 1)\n    dp[0] = 0\n    for coin in coins:\n        for i in range(coin, amount + 1):\n            dp[i] = min(dp[i], dp[i - coin] + 1)\n    return dp[amount] if dp[amount] != float(\"inf\") else -1",
      "buggy_code": "def coin_change(coins, amount):\n    dp = [0] * (amount + 1)\n    for coin in coins:\n        for i in range(coin, amount + 1):\n            dp[i] = min(dp[i], dp[i - coin] + 1)\n    return dp[amount]",
      "explanation": "dp 初始化为 0 导致 min(dp[i], dp[i-coin]+1) 永远选 0。DP 求最小值应初始化为 inf，表示不可达状态。",
      "hint": "dp 初始化为 0 导致 min 总是选 0，应该用 inf 初始化",
      "id": "dp_init_zero",
      "kp": [
        "algo_dp"
      ],
      "question": "为什么这个 DP 总是返回 0？请修正初始化",
      "stage": 36,
      "title": "DP 数组初始化为 0 的陷阱"
    },
    {
      "answer": "def knapsack(weights, values, capacity):\n    n = len(weights)\n    dp = [[0] * (capacity + 1) for _ in range(n + 1)]\n    for i in range(1, n + 1):\n        for w in range(capacity + 1):\n            if weights[i-1] <= w:\n                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])\n            else:\n                dp[i][w] = dp[i-1][w]\n    return dp[n][capacity]",
      "buggy_code": "def knapsack(weights, values, capacity):\n    n = len(weights)\n    dp = [[0] * (capacity + 1)] * (n + 1)\n    for i in range(1, n + 1):\n        for w in range(capacity + 1):\n            if weights[i-1] <= w:\n                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])\n    return dp[n][capacity]",
      "explanation": "[[0]*m]*n 创建的 n 行引用同一个列表对象，修改一行会影响所有行！必须用列表推导式 [[0]*m for _ in range(n)] 创建独立行。",
      "hint": "列表乘法创建的是引用拷贝，修改一行所有行都变",
      "id": "dp_2d_list_ref",
      "kp": [
        "algo_dp",
        "list_create"
      ],
      "question": "为什么这个背包 DP 结果总是错的？请修正初始化",
      "stage": 36,
      "title": "2D DP 用列表乘法初始化导致引用共享"
    }
  ],
  12: [
    {
      "answer": "try:\n    x = int(input('请输入数字: '))\nexcept ValueError:\n    print('输入的不是数字')\nelse:\n    print(f'你输入了 {x}')",
      "buggy_code": "x = int(input('请输入数字: '))  # 输入 abc 就崩了",
      "explanation": "int() 遇到非数字字符串会抛 ValueError，没有 try-except 程序直接崩溃。应该捕获异常并友好提示。",
      "hint": "用 try-except 捕获 ValueError",
      "id": "no_error_handling",
      "kp": [
        "exception_try",
        "exception_value_error"
      ],
      "question": "这段代码有什么问题？",
      "stage": 12,
      "title": "不做异常处理"
    },
    {
      "id": "pit12_02",
      "stage": 12,
      "title": "裸 except 捕获所有异常",
      "question": "except: 和 except Exception: 有什么区别?",
      "buggy_code": "try:\n    x = 1 / 0\nexcept:  # 捕获一切, 包括 KeyboardInterrupt!\n    print('error')",
      "hint": "裸 except 会捕获 SystemExit 和 KeyboardInterrupt",
      "explanation": "裸 except: 会捕获所有异常包括 SystemExit/KeyboardInterrupt, 可能掩盖真正的错误. 应该用 except Exception: 或更具体的异常类型.",
      "answer": "try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')",
      "kp": [
        "exception",
        "bare_except",
        "best_practice"
      ]
    }
  ],
  20: [
    {
      "answer": "def add(a, b):\n    return a + b\n\ndef test_add():\n    assert add(1, 2) == 3\n    assert add(-1, 1) == 0\n    assert add(0, 0) == 0\n\ntest_add()",
      "buggy_code": "def add(a, b):\n    return a + b\n\nprint(add(1, 2))  # 只测了正常情况",
      "explanation": "只测试了正常输入（happy path），没有测试边界情况（0、负数、大数）。测试应该覆盖正常、边界和异常三种情况。",
      "hint": "测试要覆盖边界情况",
      "id": "only_happy_path",
      "kp": [
        "test_boundary",
        "test_coverage"
      ],
      "question": "这段测试有什么问题？",
      "stage": 20,
      "title": "只测试正常路径"
    },
    {
      "id": "pit20_02",
      "stage": 20,
      "title": "测试中的浮点数比较",
      "question": "为什么 assert 0.1 + 0.2 == 0.3 会失败?",
      "buggy_code": "assert 0.1 + 0.2 == 0.3  # AssertionError!",
      "hint": "浮点数有精度误差, 用 math.isclose",
      "explanation": "0.1 + 0.2 在二进制浮点数中等于 0.30000000000000004. 测试浮点数应使用 math.isclose().",
      "answer": "import math\nassert math.isclose(0.1 + 0.2, 0.3)",
      "kp": [
        "testing",
        "float_precision",
        "math_isclose"
      ]
    }
  ],
  22: [
    {
      "answer": "import requests\ntry:\n    resp = requests.get(url, timeout=10)\n    resp.raise_for_status()\nexcept requests.Timeout:\n    print('请求超时')\nexcept requests.RequestException as e:\n    print(f'请求失败: {e}')",
      "buggy_code": "import requests\nresp = requests.get(url)  # 没有 timeout!",
      "explanation": "没有设置 timeout，请求可能永远卡住。爬虫必须设置超时，并处理网络异常。",
      "hint": "requests 要设 timeout",
      "id": "requests_no_timeout",
      "kp": [
        "crawler_timeout",
        "crawler_exception"
      ],
      "question": "这个爬虫有什么问题？",
      "stage": 22,
      "title": "requests 没有 timeout"
    },
    {
      "id": "pit22_02",
      "stage": 22,
      "title": "爬虫被反封",
      "question": "为什么请求几次就被封 IP?",
      "buggy_code": "import requests\nfor url in urls:\n    requests.get(url)  # 没有 headers, 没有 delay!",
      "hint": "添加 User-Agent 和请求间隔",
      "explanation": "没有 User-Agent 的请求容易被识别为爬虫. 高频请求触发反爬. 解决: 添加浏览器 User-Agent, 随机延迟, 使用代理.",
      "answer": "import requests, time, random\nheaders = {'User-Agent': 'Mozilla/5.0'}\nfor url in urls:\n    requests.get(url, headers=headers)\n    time.sleep(random.uniform(1, 3))",
      "kp": [
        "crawler",
        "anti_scraping",
        "user_agent"
      ]
    }
  ],
  23: [
    {
      "answer": "import pandas as pd\ndf = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})\ndf.loc[df['A'] > 1, 'B'] = 10\nprint(df)",
      "buggy_code": "import pandas as pd\ndf = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})\ndf[df['A'] > 1]['B'] = 10\nprint(df)",
      "explanation": "df[...][...] 链式索引先筛选再赋值，可能不是修改原数据。应该用 .loc[row, col] 一步到位",
      "hint": "用 .loc 一步赋值",
      "id": "chain_indexing",
      "kp": [
        "pandas_loc",
        "pandas_chain"
      ],
      "question": "这段代码有什么问题？",
      "stage": 23,
      "title": "链式索引赋值"
    },
    {
      "id": "pit23_02",
      "stage": 23,
      "title": "pandas 的 SettingWithCopyWarning",
      "question": "为什么 df[df['age']>20]['name'] = 'x' 不生效?",
      "buggy_code": "df[df['age'] > 20]['name'] = 'x'  # Warning!",
      "hint": "链式索引可能操作的是副本, 用 .loc 一步到位",
      "explanation": "链式索引先筛选再赋值, 中间产生了副本, 赋值不回写原数据. 正确做法: df.loc[条件, 列] = 值",
      "answer": "df.loc[df['age'] > 20, 'name'] = 'x'",
      "kp": [
        "pandas",
        "loc",
        "chained_indexing"
      ]
    }
  ],
  29: [
    {
      "answer": "import pandas as pd\nimport numpy as np\n\ndf = pd.read_csv('data.csv')\n# 处理缺失值\ndf['age'] = df['age'].fillna(df['age'].median())\n# 类型转换\ndf['price'] = pd.to_numeric(df['price'], errors='coerce')\n# 保存\ndf.to_csv('clean.csv', index=False)",
      "buggy_code": "import pandas as pd\ndf = pd.read_csv('data.csv')\ndf.to_csv('clean.csv')  # 什么都没清洗!",
      "explanation": "直接读取后保存，没有做任何数据清洗：缺失值没处理、类型没转换、重复没去除。ETL 流程至少要处理这三项。",
      "hint": "ETL 至少要处理缺失值和类型",
      "id": "no_data_cleaning",
      "kp": [
        "etl_clean",
        "etl_pipeline"
      ],
      "question": "这段 ETL 代码有什么问题？",
      "stage": 29,
      "title": "不做数据清洗"
    },
    {
      "id": "pit29_02",
      "stage": 29,
      "title": "ETL 数据丢失",
      "question": "为什么清洗后的数据比原始数据少了很多?",
      "buggy_code": "df = df.dropna()  # 直接删除所有含空值的行!",
      "hint": "dropna() 会删除所有含空值的行, 可能丢失大量数据",
      "explanation": "直接 dropna() 不加参数会删除所有含空值的行, 可能丢失大量有效数据. 应该指定 subset 或用 fillna() 填充.",
      "answer": "df = df.dropna(subset=['important_col'])  # 只删关键列为空的行\n# 或: df = df.fillna({'col1': 0, 'col2': 'unknown'})",
      "kp": [
        "etl",
        "dropna",
        "data_quality"
      ]
    }
  ],
  37: [
    {
      "answer": "from abc import ABC, abstractmethod\n\nclass Animal(ABC):\n    @abstractmethod\n    def speak(self): pass\n\nclass Dog(Animal):\n    def speak(self): return \"Woof\"\n\nclass Cat(Animal):\n    def speak(self): return \"Meow\"\n\ndef animal_sound(animals):\n    for a in animals:\n        print(a.speak())",
      "buggy_code": "class Animal:\n    def speak(self):\n        if self.type == \"dog\": return \"Woof\"\n        elif self.type == \"cat\": return \"Meow\"\n        # 每加一种动物就要改这个函数!",
      "explanation": "用 if-elif 判断类型是违反开闭原则的典型做法。每增加一种动物都要修改已有代码。应该用多态。",
      "hint": "违反了开闭原则（对扩展开放，对修改关闭）",
      "id": "ocp_violation",
      "kp": [
        "design_ocp",
        "design_polymorphism"
      ],
      "question": "这段代码违反了什么设计原则？",
      "stage": 37,
      "title": "违反开闭原则"
    },
    {
      "id": "pit37_02",
      "stage": 37,
      "title": "过度设计",
      "question": "什么时候不应该用设计模式?",
      "buggy_code": "# 简单程序\nclass HelloWorldFactory:\n    def create(self):\n        return HelloWorldBuilder().set_message(\"Hello\").build()\n# 过度设计了!",
      "hint": "设计模式增加复杂度, 简单问题用简单解法",
      "explanation": "过度使用设计模式会让代码更复杂更难维护. 设计模式是解决特定问题的工具, 不是万能药. 原则: YAGNI.",
      "answer": "def hello():\n    print(\"Hello, World!\")\n\nhello()",
      "kp": [
        "design_anti_pattern",
        "yagni",
        "simplicity"
      ]
    }
  ],
  1: [
    {
      "answer": "age = 25\nprint(f\"我今年{age}岁\")",
      "buggy_code": "age = 25\nprint(\"我今年\" + age + \"岁\")",
      "explanation": "TypeError: 字符串不能和整数直接用 + 拼接。需要 str() 转换，或者用 f-string。",
      "hint": "用 str() 转换或 f-string",
      "id": "str_concat_int",
      "kp": [
        "var_type",
        "str_concat"
      ],
      "question": "这段代码有什么问题？",
      "stage": 1,
      "title": "字符串拼接整数"
    },
    {
      "id": "pit1_02",
      "stage": 1,
      "title": "变量名用关键字",
      "question": "为什么 class = 'A' 会报错?",
      "buggy_code": "class = 'A'  # SyntaxError!",
      "hint": "class 是 Python 关键字, 不能用作变量名",
      "explanation": "Python 关键字(class, def, if, for 等)不能用作变量名. 用 class_name 或 category 代替.",
      "answer": "class_name = 'A'",
      "kp": [
        "variable",
        "keyword",
        "naming"
      ]
    }
  ],
  13: [
    {
      "answer": "import sys\ntry:\n    with open(sys.argv[1]) as f:\n        data = f.read()\nexcept IndexError:\n    print('请提供文件名参数')\nexcept FileNotFoundError:\n    print('文件不存在')",
      "buggy_code": "f = open(sys.argv[1])  # 没参数就 IndexError，文件不存在就崩",
      "explanation": "访问 sys.argv[1] 没有参数时 IndexError，文件不存在 FileNotFoundError。综合项目要考虑各种边界情况。",
      "hint": "对用户输入做边界检查",
      "id": "no_arg_check",
      "kp": [
        "sys_argv",
        "boundary_check"
      ],
      "question": "这段代码有什么问题？",
      "stage": 13,
      "title": "不检查参数"
    },
    {
      "id": "pit13_02",
      "stage": 13,
      "title": "综合项目缺乏错误处理",
      "question": "为什么综合项目总是莫名崩溃?",
      "buggy_code": "# 主程序没有 try-except\nfor task in tasks:\n    task.run()  # 任何一个出错就全崩!",
      "hint": "在主循环中加 try-except 保护每个任务",
      "explanation": "综合项目应每个关键步骤都加错误处理, 确保一个任务失败不影响其他任务. 也要记录日志方便排查.",
      "answer": "for task in tasks:\n    try:\n        task.run()\n    except Exception as e:\n        logging.error(f'Task {task} failed: {e}')\n        continue",
      "kp": [
        "error_handling",
        "robustness",
        "logging"
      ]
    }
  ]
}
