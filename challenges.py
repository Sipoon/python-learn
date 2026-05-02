"""挑战练习数据 - v5.0"""
from typing import Dict, List

CHALLENGE_EXERCISES: Dict = {
  1: [
    {
      "answer": "print(2 ** 20)",
      "diff": "challenge",
      "hint": "print(2 ** 20)",
      "kp": [
        "op_arithmetic",
        "print_basic"
      ],
      "q": "不用任何变量，一行代码打印 2 的 20 次方"
    },
    {
      "answer": "a, b = 1, 2\na, b = b, a\nprint(a, b)",
      "diff": "challenge",
      "hint": "a, b = b, a",
      "kp": [
        "var_create",
        "tuple_unpack"
      ],
      "q": "用一行代码交换 a=1, b=2 的值（不使用第三个变量），然后打印"
    }
  ],
  2: [
    {
      "answer": "year = 2000\nprint((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))",
      "diff": "challenge",
      "hint": "and/or 组合逻辑表达式",
      "kp": [
        "op_logical",
        "op_arithmetic",
        "op_compare",
        {
          "q": "不使用 ** 运算符, 实现一个计算 x 的 n 次方的函数",
          "hint": "用循环累乘, 注意 n=0 时返回 1",
          "kp": [
            "operator",
            "loop",
            "power"
          ],
          "diff": "medium",
          "answer": "def power(x, n):\n    result = 1\n    for _ in range(n):\n        result *= x\n    return result\n\nprint(power(2, 10))"
        }
      ],
      "q": "不使用 if，用一行判断 year=2000 是否闰年，打印 True/False"
    },
    {
      "q": "用 while 循环实现一个猜数字游戏：程序随机生成1-100的数，用户输入猜测，提示大了/小了/猜对了，记录猜测次数",
      "hint": "import random; target = random.randint(1, 100); while 循环 + input()",
      "answer": "import random\ntarget = random.randint(1, 100)\ncount = 0\nwhile True:\n    guess = int(input('猜: '))\n    count += 1\n    if guess < target:\n        print('小了')\n    elif guess > target:\n        print('大了')\n    else:\n        print(f'猜对了! {count}次')\n        break",
      "diff": "challenge",
      "kp": [
        "while",
        "random",
        "input"
      ]
    }
  ],
  3: [
    {
      "answer": "a, b, op = 10, 3, \"+\"\nif op == \"+\":\n    print(a + b)\nelif op == \"-\":\n    print(a - b)\nelif op == \"*\":\n    print(a * b)\nelif op == \"/\":\n    print(a / b)",
      "diff": "challenge",
      "hint": "if-elif 四种运算",
      "kp": [
        "if_elif",
        "op_arithmetic",
        {
          "q": "输入一个数字, 判断它是正数、负数还是零, 并输出对应等级(优良中差)",
          "hint": "用 elif 链处理多条件",
          "kp": [
            "if_elif",
            "condition",
            "grade"
          ],
          "diff": "easy",
          "answer": "score = int(input())\nif score >= 90:\n    print('优')\nelif score >= 80:\n    print('良')\nelif score >= 60:\n    print('中')\nelse:\n    print('差')"
        }
      ],
      "q": "写一个简单的计算器：根据 op=\"+\"/\"-\"/\"*\"/\"/\" 对 a=10, b=3 做运算并打印结果"
    },
    {
      "q": "实现一个简单的通讯录：用字典存储姓名→电话，支持添加、查询、删除、列出所有联系人",
      "hint": "字典操作 + while True 菜单循环",
      "answer": "contacts = {}\nwhile True:\n    cmd = input('命令(add/find/del/list/quit): ')\n    if cmd == 'add':\n        name = input('姓名: ')\n        phone = input('电话: ')\n        contacts[name] = phone\n    elif cmd == 'find':\n        name = input('姓名: ')\n        print(contacts.get(name, '未找到'))\n    elif cmd == 'del':\n        name = input('姓名: ')\n        contacts.pop(name, None)\n    elif cmd == 'list':\n        for n, p in contacts.items():\n            print(f'{n}: {p}')\n    elif cmd == 'quit':\n        break",
      "diff": "challenge",
      "kp": [
        "dict",
        "while",
        "menu"
      ]
    }
  ],
  4: [
    {
      "answer": "result = [\"FizzBuzz\" if i%15==0 else \"Fizz\" if i%3==0 else \"Buzz\" if i%5==0 else str(i) for i in range(1, 31)]\nprint(result)",
      "diff": "challenge",
      "hint": "\"FizzBuzz\" if i%15==0 else \"Fizz\" if i%3==0 else \"Buzz\" if i%5==0 else str(i)",
      "kp": [
        "list_comprehension",
        "op_arithmetic"
      ],
      "q": "用一行列表推导式实现 FizzBuzz：1-30，3的倍数替换为\"Fizz\"，5的倍数替换为\"Buzz\"，15的倍数替换为\"FizzBuzz\"，其他保留数字，打印列表"
    },
    {
      "answer": "for i in range(5, 0, -1):\n    print(\" \" * (5 - i) + \"*\" * i)",
      "diff": "challenge",
      "hint": "外层循环5到1，内层：先打印空格再打印星号",
      "kp": [
        "for_loop",
        "nested_loop",
        "range_func"
      ],
      "q": "打印倒三角：\n*****\n ****\n  ***\n   **\n    *"
    }
  ],
  5: [
    {
      "answer": "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)\n\nprint(factorial(10))",
      "diff": "challenge",
      "hint": "if n <= 1: return 1 else: return n * factorial(n-1)",
      "kp": [
        "func_def",
        "func_return"
      ],
      "q": "写递归函数 factorial(n) 计算阶乘，打印 factorial(10)"
    },
    {
      "answer": "def flatten(nested):\n    return [x for sub in nested for x in sub]\n\nprint(flatten([[1, 2], [3, 4], [5]]))",
      "diff": "challenge",
      "hint": "列表推导式双重循环：[x for sub in nested for x in sub]",
      "kp": [
        "list_comprehension",
        "func_def"
      ],
      "q": "写函数 flatten(nested) 将嵌套列表 [[1,2],[3,4],[5]] 展平为 [1,2,3,4,5] 并打印"
    }
  ],
  6: [
    {
      "answer": "nums = [5, 3, 8, 1, 9, 2]\nfor i in range(len(nums)):\n    for j in range(len(nums) - 1 - i):\n        if nums[j] > nums[j + 1]:\n            nums[j], nums[j + 1] = nums[j + 1], nums[j]\nprint(nums)",
      "diff": "challenge",
      "hint": "嵌套循环，相邻比较交换",
      "kp": [
        "list_methods",
        "nested_loop",
        "op_compare"
      ],
      "q": "实现冒泡排序：对 [5, 3, 8, 1, 9, 2] 排序并打印"
    },
    {
      "answer": "for i in range(1, 10):\n    row = \"  \".join(f\"{j}x{i}={i*j}\" for j in range(1, i + 1))\n    print(row)",
      "diff": "challenge",
      "hint": "[f\"{j}x{i}={i*j}\" for j in range(1, i+1)]，外层 join",
      "kp": [
        "list_comprehension",
        "str_methods",
        "nested_loop"
      ],
      "q": "用列表推导式生成九九乘法表的每行字符串，打印整个表"
    }
  ],
  7: [
    {
      "answer": "p = (1, 2, 3)\nx, y, z = p\ndist = (x**2 + y**2 + z**2) ** 0.5\nprint(f\"{dist:.3f}\")",
      "diff": "challenge",
      "hint": "(x**2+y**2+z**2)**0.5",
      "kp": [
        "tuple_unpack",
        "op_arithmetic",
        {
          "q": "交换两个变量, 不使用第三个临时变量(用元组解包)",
          "hint": "a, b = b, a 就是元组解包",
          "kp": [
            "tuple",
            "swap",
            "unpacking"
          ],
          "diff": "easy",
          "answer": "a, b = 10, 20\na, b = b, a\nprint(a, b)  # 20 10"
        }
      ],
      "q": "用 namedtuple 或元组实现一个简单的3D点：p=(1,2,3)，计算到原点距离并打印（保留3位小数）"
    },
    {
      "q": "实现一个 Student 类，支持按成绩排序学生列表，并找出最高分和最低分学生",
      "hint": "class Student + __lt__ + sorted()",
      "answer": "class Student:\n    def __init__(self, name, score):\n        self.name = name\n        self.score = score\n    def __lt__(self, other):\n        return self.score < other.score\n    def __repr__(self):\n        return f'{self.name}({self.score})'\n\nstudents = [Student('Alice', 88), Student('Bob', 95), Student('Carol', 72)]\nsorted_stu = sorted(students)\nprint(f'最高: {sorted_stu[-1]}, 最低: {sorted_stu[0]}')",
      "diff": "challenge",
      "kp": [
        "class",
        "sorted",
        "__lt__"
      ]
    }
  ],
  8: [
    {
      "answer": "students = {\"Alice\": {\"math\": 90, \"eng\": 85}, \"Bob\": {\"math\": 78, \"eng\": 92}}\nfor name, scores in students.items():\n    avg = sum(scores.values()) / len(scores)\n    print(f\"{name}: {avg:.1f}\")",
      "diff": "challenge",
      "hint": "嵌套遍历 + sum/len",
      "kp": [
        "dict_access",
        "dict_methods",
        "for_loop",
        {
          "q": "统计一段文本中每个单词出现的次数, 按频率降序排列",
          "hint": "用 dict 或 Counter, sorted + key",
          "kp": [
            "dict",
            "counter",
            "sort"
          ],
          "diff": "medium",
          "answer": "from collections import Counter\ntext = 'hello world hello python world'\nwords = text.split()\ncounts = Counter(words)\nfor word, cnt in counts.most_common():\n    print(f'{word}: {cnt}')"
        }
      ],
      "q": "用嵌套字典表示学生成绩：{\"Alice\":{\"math\":90,\"eng\":85}, \"Bob\":{\"math\":78,\"eng\":92}}，打印每个学生的平均分"
    },
    {
      "q": "统计一段英文中每个单词出现的频率，按频率降序输出前10个",
      "hint": "str.split() + collections.Counter + most_common()",
      "answer": "from collections import Counter\ntext = 'the quick brown fox jumps over the lazy dog the fox is quick'\nwords = text.lower().split()\nfreq = Counter(words)\nfor word, count in freq.most_common(10):\n    print(f'{word}: {count}')",
      "diff": "challenge",
      "kp": [
        "dict",
        "Counter",
        "most_common"
      ]
    }
  ],
  9: [
    {
      "answer": "s1 = \"abcdef\"\ns2 = \"cdefgh\"\ncommon = sorted(set(s1) & set(s2))\nprint(common)",
      "diff": "challenge",
      "hint": "sorted(set(s1) & set(s2))",
      "kp": [
        "set_ops",
        "set_create",
        "str_methods",
        {
          "q": "用集合找出两个列表的交集、并集和差集",
          "hint": "set 支持 & | - 运算符",
          "kp": [
            "set",
            "intersection",
            "union"
          ],
          "diff": "easy",
          "answer": "a = {1, 2, 3, 4}\nb = {3, 4, 5, 6}\nprint(a & b)  # {3, 4} 交集\nprint(a | b)  # {1,2,3,4,5,6} 并集\nprint(a - b)  # {1, 2} 差集"
        }
      ],
      "q": "给定两个字符串 \"abcdef\" 和 \"cdefgh\"，找出它们共有的字符，按字母顺序打印"
    },
    {
      "q": "用集合操作找出两个列表的交集、并集、差集和对称差集",
      "hint": "set() 的 &, |, -, ^ 运算符",
      "answer": "a = {1, 2, 3, 4, 5}\nb = {4, 5, 6, 7, 8}\nprint(f'交集: {a & b}')\nprint(f'并集: {a | b}')\nprint(f'A-B: {a - b}')\nprint(f'对称差: {a ^ b}')",
      "diff": "challenge",
      "kp": [
        "set",
        "intersection",
        "union",
        "symmetric_difference"
      ]
    }
  ],
  10: [
    {
      "answer": "text = \"hello\"\nresult = \"\"\nfor c in text:\n    if c.isalpha():\n        shifted = chr((ord(c) - ord(\"a\") + 3) % 26 + ord(\"a\"))\n        result += shifted\n    else:\n        result += c\nprint(result)",
      "diff": "challenge",
      "hint": "chr((ord(c)-ord('a')+3)%26 + ord('a'))",
      "kp": [
        "str_methods",
        "for_loop",
        "op_arithmetic",
        {
          "q": "回文判断: 输入一个字符串, 判断是否是回文(忽略空格和大小写)",
          "hint": "先清洗字符串, 再与反转比较",
          "kp": [
            "string",
            "palindrome",
            "reverse"
          ],
          "diff": "easy",
          "answer": "s = 'A man a plan a canal Panama'\nclean = s.replace(' ', '').lower()\nprint(clean == clean[::-1])  # True"
        }
      ],
      "q": "实现 Caesar 密码：将 \"hello\" 每个字母后移3位（a->d, b->e...），打印密文"
    },
    {
      "q": "实现一个简单的字符串模板引擎：将 {{name}} 替换为变量值，支持循环 {{#items}}...{{/items}}",
      "hint": "正则 re.sub + 自定义替换函数",
      "answer": "import re\n\ndef render(template, data):\n    # 简单变量替换\n    def replace_var(m):\n        key = m.group(1)\n        return str(data.get(key, ''))\n    result = re.sub(r'\\{\\{(\\w+)\\}\\}', replace_var, template)\n    # 循环替换\n    def replace_loop(m):\n        key = m.group(1)\n        body = m.group(2)\n        items = data.get(key, [])\n        return ''.join(render(body, item) for item in items)\n    result = re.sub(r'\\{\\{#(\\w+)\\}\\}(.*?)\\{\\{/\\1\\}\\}', replace_loop, result, flags=re.DOTALL)\n    return result\n\ntmpl = 'Hello {{name}}! {{#items}}{{.}} {{/items}}'\nprint(render(tmpl, {'name': 'World', 'items': ['A', 'B', 'C']}))",
      "diff": "challenge",
      "kp": [
        "regex",
        "re_sub",
        "template"
      ]
    }
  ],
  11: [
    {
      "answer": "csv_data = \"name,age,city\\nAlice,25,Beijing\\nBob,30,Shanghai\"\nlines = csv_data.strip().split(\"\\n\")\nheaders = lines[0].split(\",\")\nresult = [dict(zip(headers, line.split(\",\"))) for line in lines[1:]]\nprint(result)",
      "diff": "challenge",
      "hint": "split('\\n') + split(',') + 第一行做key",
      "kp": [
        "str_methods",
        "list_comprehension",
        "dict_create",
        {
          "q": "读取一个 CSV 文件(不用 csv 模块), 按第二列排序后输出",
          "hint": "split(',') 拆分, sorted + key lambda",
          "kp": [
            "file",
            "csv",
            "sort"
          ],
          "diff": "medium",
          "answer": "with open('data.csv') as f:\n    lines = f.readlines()\nrows = [line.strip().split(',') for line in lines[1:]]\nfor row in sorted(rows, key=lambda r: r[1]):\n    print(row)"
        }
      ],
      "q": "实现简单的 CSV 解析：读取内容 \"name,age,city\\nAlice,25,Beijing\\nBob,30,Shanghai\"，解析为字典列表并打印"
    },
    {
      "q": "实现一个简单的日志文件分析器：读取日志文件，统计各IP的访问次数，找出访问量最大的前5个IP",
      "hint": "with open + re.findall + Counter",
      "answer": "from collections import Counter\nimport re\n\ndef analyze_log(filename):\n    ip_pattern = re.compile(r'^(\\d+\\.\\d+\\.\\d+\\.\\d+)')\n    ips = []\n    with open(filename) as f:\n        for line in f:\n            m = ip_pattern.match(line)\n            if m:\n                ips.append(m.group(1))\n    return Counter(ips).most_common(5)\n\n# Usage: top5 = analyze_log('access.log')",
      "diff": "challenge",
      "kp": [
        "file_read",
        "regex",
        "Counter"
      ]
    }
  ],
  12: [
    {
      "answer": "import random\n\ndef retry(func, max_attempts=3):\n    for attempt in range(max_attempts):\n        try:\n            result = func()\n            return result\n        except Exception as e:\n            if attempt == max_attempts - 1:\n                return f\"失败: {e}\"\n    return \"失败: 超过重试次数\"\n\nrandom.seed(42)\ncall_count = 0\ndef flaky():\n    global call_count\n    call_count += 1\n    if call_count < 3:\n        raise ValueError(\"临时错误\")\n    return \"成功\"\n\nprint(retry(flaky))",
      "diff": "challenge",
      "hint": "for _ in range(max_attempts): try: return func() except: continue",
      "kp": [
        "func_def",
        "try_except",
        "func_return",
        {
          "q": "写一个安全的除法函数, 处理除零和非数字输入",
          "hint": "多层 try/except 处理不同异常",
          "kp": [
            "exception",
            "zerodivision",
            "type_error"
          ],
          "diff": "easy",
          "answer": "def safe_divide(a, b):\n    try:\n        return float(a) / float(b)\n    except ZeroDivisionError:\n        return 'Cannot divide by zero'\n    except (ValueError, TypeError):\n        return 'Invalid input'\n\nprint(safe_divide(10, 3))"
        }
      ],
      "q": "写一个重试装饰器：写函数 retry(func, max_attempts=3)，对可能抛异常的函数自动重试。测试：对会随机失败的函数重试3次"
    },
    {
      "q": "实现一个带重试机制的函数装饰器：如果函数抛出指定异常，自动重试最多N次",
      "hint": "装饰器 + for 循环 + try-except",
      "answer": "import time\n\ndef retry(max_retries=3, delay=1, exceptions=(Exception,)):\n    def decorator(func):\n        def wrapper(*args, **kwargs):\n            for attempt in range(max_retries + 1):\n                try:\n                    return func(*args, **kwargs)\n                except exceptions as e:\n                    if attempt == max_retries:\n                        raise\n                    print(f'Retry {attempt+1}/{max_retries}: {e}')\n                    time.sleep(delay)\n        return wrapper\n    return decorator\n\n@retry(max_retries=3, delay=0.5, exceptions=(ValueError,))\ndef risky():\n    import random\n    if random.random() < 0.7:\n        raise ValueError('Random fail')\n    return 'Success!'",
      "diff": "challenge",
      "kp": [
        "decorator",
        "exception",
        "retry_pattern"
      ]
    }
  ],
  13: [
    {
      "answer": "import argparse\n\nparser = argparse.ArgumentParser()\nparser.add_argument(\"--name\", default=\"世界\")\nparser.add_argument(\"--age\", type=int, default=0)\nargs = parser.parse_args([])  # 空列表模拟无参数\nprint(f\"你好，{args.name}！你{args.age}岁了\")",
      "diff": "challenge",
      "hint": "import argparse; parser = argparse.ArgumentParser()",
      "kp": [
        "import_module",
        "func_def",
        {
          "q": "写一个通讯录程序: 添加/查找/删除联系人, 数据保存到文件",
          "hint": "用 dict 存储, json.dump/load 持久化",
          "kp": [
            "dict",
            "json",
            "file_io"
          ],
          "diff": "medium",
          "answer": "import json\ncontacts = {}\n\ndef add(name, phone):\n    contacts[name] = phone\n    with open('contacts.json', 'w') as f:\n        json.dump(contacts, f)\n\nadd('Alice', '123')"
        }
      ],
      "q": "用 argparse 写一个命令行工具骨架（不用真正运行），接收 --name 和 --age 参数，打印问候语"
    },
    {
      "q": "实现一个命令行待办事项应用，支持添加、完成、删除、列出任务，数据保存到JSON文件",
      "hint": "json.dump/load + while True 菜单 + 文件持久化",
      "answer": "import json, os\n\ndef load_tasks(path='tasks.json'):\n    if os.path.exists(path):\n        with open(path) as f:\n            return json.load(f)\n    return []\n\ndef save_tasks(tasks, path='tasks.json'):\n    with open(path, 'w') as f:\n        json.dump(tasks, f, ensure_ascii=False, indent=2)\n\ndef main():\n    tasks = load_tasks()\n    while True:\n        cmd = input('(add/done/del/list/quit) ')\n        if cmd == 'add':\n            tasks.append({'task': input('Task: '), 'done': False})\n        elif cmd == 'done':\n            i = int(input('Index: '))\n            tasks[i]['done'] = True\n        elif cmd == 'del':\n            tasks.pop(int(input('Index: ')))\n        elif cmd == 'list':\n            for i, t in enumerate(tasks):\n                mark = 'x' if t['done'] else ' '\n                print(f'[{mark}] {i}: {t[\"task\"]}')\n        elif cmd == 'quit':\n            save_tasks(tasks)\n            break\n\nmain()",
      "diff": "challenge",
      "kp": [
        "json",
        "file_persistence",
        "cli_app"
      ]
    }
  ],
  14: [
    {
      "answer": "import re\nipv4_pattern = re.compile(r\"^((25[0-5]|2[0-4]\\d|[01]?\\d\\d?)\\.){3}(25[0-5]|2[0-4]\\d|[01]?\\d\\d?)$\")\nprint(bool(ipv4_pattern.match(\"192.168.1.1\")))\nprint(bool(ipv4_pattern.match(\"256.1.1.1\")))",
      "diff": "challenge",
      "hint": "r'((25[0-5]|2[0-4]\\d|[01]?\\d\\d?)\\.) {3}(25[0-5]|2[0-4]\\d|[01]?\\d\\d?)'",
      "kp": [
        "regex_charset",
        "regex_quantifier",
        "regex_group",
        {
          "q": "用正则表达式验证邮箱地址格式是否合法",
          "hint": "模式: 字母数字+@+域名+.后缀",
          "kp": [
            "regex",
            "validation",
            "email"
          ],
          "diff": "medium",
          "answer": "import re\npattern = r'^[\\w.-]+@[\\w.-]+\\.\\w+$'\nemail = 'test@example.com'\nprint(bool(re.match(pattern, email)))"
        }
      ],
      "q": "写一个正则，匹配合法的 IPv4 地址（如 192.168.1.1），验证 '192.168.1.1' 匹配而 '256.1.1.1' 不匹配"
    },
    {
      "q": "用正则表达式解析CSV格式的字符串（处理引号内包含逗号的情况）",
      "hint": "re.findall 配合正确的CSV正则模式",
      "answer": "import re\n\ndef parse_csv_line(line):\n    pattern = r'(?:\"([^\"]*)\"|([^,]*))'\n    matches = re.findall(pattern, line)\n    return [m[0] if m[0] else m[1] for m in matches if m[0] or m[1]]\n\ncsv_line = 'Alice,\"Bob, Jr.\",Carol,\"Dave \\\"The Boss\\\"\"'\nprint(parse_csv_line(csv_line))",
      "diff": "challenge",
      "kp": [
        "regex",
        "csv",
        "parsing"
      ]
    }
  ],
  15: [
    {
      "answer": "class Node:\n    def __init__(self, value):\n        self.value = value\n        self.next = None\n\nn1 = Node(1)\nn2 = Node(2)\nn3 = Node(3)\nn1.next = n2\nn2.next = n3\n\ncurrent = n1\nwhile current:\n    print(current.value, end=\" \")\n    current = current.next",
      "diff": "challenge",
      "hint": "class Node: def __init__(self, val): self.value=val; self.next=None",
      "kp": [
        "oop_class_object",
        "oop_init_self",
        {
          "q": "实现一个 Stack 类, 包含 push/pop/peek/is_empty 方法",
          "hint": "内部用 list 存储, push=append, pop=pop",
          "kp": [
            "class",
            "stack",
            "data_structure"
          ],
          "diff": "easy",
          "answer": "class Stack:\n    def __init__(self): self._data = []\n    def push(self, item): self._data.append(item)\n    def pop(self): return self._data.pop()\n    def peek(self): return self._data[-1]\n    def is_empty(self): return len(self._data) == 0"
        }
      ],
      "q": "用 OOP 实现一个简单的链表节点 Node 类，有 value 和 next 属性，创建 1->2->3 并遍历打印"
    },
    {
      "q": "实现一个支持链式调用的QueryBuilder类：select().from_().where().limit() 生成SQL语句",
      "hint": "每个方法返回 self",
      "answer": "class QueryBuilder:\n    def __init__(self):\n        self._select = '*'\n        self._table = ''\n        self._where = ''\n        self._limit = ''\n\n    def select(self, *cols):\n        self._select = ', '.join(cols) if cols else '*'\n        return self\n\n    def from_(self, table):\n        self._table = table\n        return self\n\n    def where(self, condition):\n        self._where = f' WHERE {condition}'\n        return self\n\n    def limit(self, n):\n        self._limit = f' LIMIT {n}'\n        return self\n\n    def build(self):\n        return f'SELECT {self._select} FROM {self._table}{self._where}{self._limit}'\n\nq = QueryBuilder().select('name', 'age').from_('users').where('age > 18').limit(10)\nprint(q.build())",
      "diff": "challenge",
      "kp": [
        "oop",
        "method_chaining",
        "builder_pattern"
      ]
    }
  ],
  16: [
    {
      "answer": "class MyList:\n    def __init__(self, *items):\n        self._items = list(items)\n    def __getitem__(self, index):\n        return self._items[index]\n    def __len__(self):\n        return len(self._items)\n    def __iter__(self):\n        return iter(self._items)\n\nml = MyList(10, 20, 30)\nprint(ml[0])\nprint(len(ml))\nfor item in ml:\n    print(item)",
      "diff": "challenge",
      "hint": "__getitem__, __len__, __iter__",
      "kp": [
        "oop_magic_method",
        {
          "q": "实现一个支持上下文管理的 Timer 类(with 语句自动计时)",
          "hint": "实现 __enter__ 和 __exit__ 方法",
          "kp": [
            "context_manager",
            "magic_method",
            "timer"
          ],
          "diff": "medium",
          "answer": "import time\nclass Timer:\n    def __enter__(self):\n        self.start = time.time()\n        return self\n    def __exit__(self, *args):\n        print(f'Elapsed: {time.time() - self.start:.3f}s')\n\nwith Timer():\n    time.sleep(1)"
        }
      ],
      "q": "实现一个自定义容器类 MyList，支持 obj[i] 索引访问（__getitem__）、len(obj)（__len__）和 for 遍历（__iter__）"
    },
    {
      "q": "用多态实现一个简单的绘图程序：Shape基类，Circle/Rectangle/Triangle子类，各自实现area()和draw()",
      "hint": "抽象基类 + 子类多态 + __str__",
      "answer": "from abc import ABC, abstractmethod\nimport math\n\nclass Shape(ABC):\n    @abstractmethod\n    def area(self): pass\n\n    @abstractmethod\n    def draw(self): pass\n\nclass Circle(Shape):\n    def __init__(self, r): self.r = r\n    def area(self): return math.pi * self.r ** 2\n    def draw(self): return f'O (r={self.r})'\n\nclass Rectangle(Shape):\n    def __init__(self, w, h): self.w, self.h = w, h\n    def area(self): return self.w * self.h\n    def draw(self): return f'[ {self.w}x{self.h} ]'\n\nclass Triangle(Shape):\n    def __init__(self, b, h): self.b, self.h = b, h\n    def area(self): return 0.5 * self.b * self.h\n    def draw(self): return f'/\\\\  (b={self.b}, h={self.h})'\n\nshapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]\nfor s in shapes:\n    print(f'{s.draw()} area={s.area():.1f}')",
      "diff": "challenge",
      "kp": [
        "polymorphism",
        "abstract_class",
        "oop"
      ]
    }
  ],
  17: [
    {
      "answer": "module_code = \"\"\"\ndef add(a, b):\n    return a + b\n\ndef multiply(a, b):\n    return a * b\n\"\"\"\nnamespace = {}\nexec(module_code, namespace)\nprint(namespace[\"add\"](3, 5))\nprint(namespace[\"multiply\"](4, 6))",
      "diff": "challenge",
      "hint": "module_code = 'def add(a,b): return a+b'; exec(module_code); add(1,2)",
      "kp": [
        "mod_import",
        "func_def",
        {
          "q": "创建一个简单的插件系统: 自动发现并加载 plugins/ 目录下的模块",
          "hint": "importlib + os.listdir + import_module",
          "kp": [
            "module",
            "importlib",
            "plugin"
          ],
          "diff": "medium",
          "answer": "import importlib, os\nplugins = []\nfor f in os.listdir('plugins'):\n    if f.endswith('.py') and f != '__init__.py':\n        mod = importlib.import_module(f'plugins.{f[:-3]}')\n        plugins.append(mod)"
        }
      ],
      "q": "创建一个模块 mymath.py 的内容（写在字符串里），包含 add(a,b) 和 multiply(a,b)，然后用 exec 运行并测试"
    },
    {
      "q": "实现一个简单的插件系统：用importlib动态导入模块，扫描模块中@register装饰器注册的函数并执行",
      "hint": "importlib.import_module + 装饰器注册表",
      "answer": "PLUGINS = {}\n\ndef register(name):\n    def decorator(func):\n        PLUGINS[name] = func\n        return func\n    return decorator\n\n@register('greet')\ndef greet():\n    return 'Hello!'\n\n@register('farewell')\ndef farewell():\n    return 'Goodbye!'\n\nprint('Registered plugins:', list(PLUGINS.keys()))\nfor name, func in PLUGINS.items():\n    print(f'  {name}: {func()}')",
      "diff": "challenge",
      "kp": [
        "module",
        "importlib",
        "plugin_pattern"
      ]
    }
  ],
  18: [
    {
      "answer": "from functools import wraps\n\ndef memoize(func):\n    cache = {}\n    @wraps(func)\n    def wrapper(*args):\n        if args not in cache:\n            cache[args] = func(*args)\n        return cache[args]\n    return wrapper\n\n@memoize\ndef fib(n):\n    if n <= 1:\n        return n\n    return fib(n-1) + fib(n-2)\n\nprint(fib(30))",
      "diff": "challenge",
      "hint": "cache = {}; if args in cache: return cache[args]",
      "kp": [
        "dec_basic",
        "dec_args",
        {
          "q": "实现一个 @timeit 装饰器, 打印被装饰函数的执行时间",
          "hint": "在 wrapper 中用 time.time() 计时",
          "kp": [
            "decorator",
            "timing",
            "functools"
          ],
          "diff": "easy",
          "answer": "import time, functools\ndef timeit(func):\n    @functools.wraps(func)\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        print(f'{func.__name__}: {time.time()-start:.4f}s')\n        return result\n    return wrapper"
        }
      ],
      "q": "写一个 @memoize 装饰器，缓存函数返回值，对递归 fibonacci 加速"
    },
    {
      "q": "实现一个 @timed 装饰器，测量函数执行时间，并支持统计调用次数和平均时间",
      "hint": "functools.wraps + time.perf_counter + 闭包计数",
      "answer": "import time, functools\n\ndef timed(func):\n    stats = {'count': 0, 'total': 0.0}\n    @functools.wraps(func)\n    def wrapper(*args, **kwargs):\n        start = time.perf_counter()\n        result = func(*args, **kwargs)\n        elapsed = time.perf_counter() - start\n        stats['count'] += 1\n        stats['total'] += elapsed\n        print(f'{func.__name__} took {elapsed:.4f}s')\n        return result\n    wrapper.stats = stats\n    return wrapper\n\n@timed\ndef slow_add(a, b):\n    time.sleep(0.01)\n    return a + b\n\nslow_add(1, 2)\nslow_add(3, 4)\nprint(f'Stats: {slow_add.stats}')",
      "diff": "challenge",
      "kp": [
        "decorator",
        "timing",
        "closure"
      ]
    }
  ],
  19: [
    {
      "answer": "from sqlalchemy import Table, Column, Integer, String, ForeignKey\nfrom sqlalchemy.orm import declarative_base, Session, relationship\nfrom sqlalchemy import create_engine\n\nBase = declarative_base()\n\nenrollment = Table(\"enrollment\", Base.metadata,\n    Column(\"student_id\", Integer, ForeignKey(\"students.id\")),\n    Column(\"course_id\", Integer, ForeignKey(\"courses.id\")))\n\nclass Student(Base):\n    __tablename__ = \"students\"\n    id = Column(Integer, primary_key=True)\n    name = Column(String(50))\n    courses = relationship(\"Course\", secondary=enrollment, back_populates=\"students\")\n\nclass Course(Base):\n    __tablename__ = \"courses\"\n    id = Column(Integer, primary_key=True)\n    name = Column(String(50))\n    students = relationship(\"Student\", secondary=enrollment, back_populates=\"courses\")\n\nengine = create_engine(\"sqlite:///:memory:\")\nBase.metadata.create_all(engine)\nsession = Session(engine)\npython_course = Course(name=\"Python\")\ns1 = Student(name=\"Alice\")\ns2 = Student(name=\"Bob\")\npython_course.students = [s1, s2]\nsession.add_all([python_course, s1, s2])\nsession.commit()\n\nstudents = session.query(Student).filter(Student.courses.any(Course.name == \"Python\")).all()\nfor s in students:\n    print(s.name)",
      "diff": "challenge",
      "hint": "association table + relationship + query filter",
      "kp": [
        "db_sqlalchemy",
        {
          "q": "设计一个用户表(ORM 风格): 支持增删改查, 用参数化查询防注入",
          "hint": "CREATE TABLE + INSERT/SELECT/UPDATE/DELETE",
          "kp": [
            "sql",
            "crud",
            "orm"
          ],
          "diff": "medium",
          "answer": "import sqlite3\nconn = sqlite3.connect('users.db')\nc = conn.cursor()\nc.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')\nc.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))\nconn.commit()"
        }
      ],
      "q": "用 SQLAlchemy 实现多对多关系：Student ↔ Course，查询选了'Python'课的所有学生"
    },
    {
      "q": "用SQLite实现一个简易图书管理系统：建表、增删改查、按作者搜索",
      "hint": "sqlite3 + CREATE TABLE + CRUD操作",
      "answer": "import sqlite3\n\nconn = sqlite3.connect(':memory:')\nc = conn.cursor()\nc.execute('''CREATE TABLE books (\n    id INTEGER PRIMARY KEY,\n    title TEXT, author TEXT, year INT)''')\nconn.commit()\n\n# 增\nc.execute('INSERT INTO books VALUES (1, \"Python入门\", \"Alice\", 2023)')\nc.execute('INSERT INTO books VALUES (2, \"SQL实战\", \"Bob\", 2022)')\nconn.commit()\n\n# 查\nc.execute('SELECT * FROM books WHERE author = ?', ('Alice',))\nprint('Alice的书:', c.fetchall())\n\n# 改\nc.execute('UPDATE books SET year = 2024 WHERE id = 1')\n\n# 删\nc.execute('DELETE FROM books WHERE id = 2')\n\n# 列出\nc.execute('SELECT * FROM books')\nprint('所有书:', c.fetchall())",
      "diff": "challenge",
      "kp": [
        "sqlite",
        "crud",
        "database"
      ]
    }
  ],
  20: [
    {
      "answer": "import pytest\nimport sqlite3\n\n@pytest.fixture\ndef db_session():\n    conn = sqlite3.connect(\":memory:\")\n    conn.execute(\"CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT)\")\n    conn.commit()\n    yield conn\n    conn.close()\n\ndef test_insert(db_session):\n    db_session.execute(\"INSERT INTO items (name) VALUES (?)\", (\"Apple\",))\n    db_session.commit()\n    rows = db_session.execute(\"SELECT * FROM items\").fetchall()\n    assert len(rows) == 1\n\ndef test_empty(db_session):\n    rows = db_session.execute(\"SELECT * FROM items\").fetchall()\n    assert len(rows) == 0  # 新的连接，没有残留数据\n\nprint(\"conftest fixtures defined\")",
      "diff": "challenge",
      "hint": "yield fixture + rollback 或每个测试新建表",
      "kp": [
        "test_pytest",
        "test_fixture",
        {
          "q": "为 Stack 类写单元测试, 覆盖正常操作和边界情况",
          "hint": "用 unittest.TestCase, 测试 push/pop/empty",
          "kp": [
            "unittest",
            "test_case",
            "boundary"
          ],
          "diff": "medium",
          "answer": "import unittest\nclass TestStack(unittest.TestCase):\n    def test_push_pop(self):\n        s = Stack()\n        s.push(1)\n        self.assertEqual(s.pop(), 1)\n    def test_empty(self):\n        s = Stack()\n        self.assertTrue(s.is_empty())"
        }
      ],
      "q": "写一个 conftest.py，包含 db_session fixture（内存 SQLite），让多个测试共享数据库但不互相影响"
    },
    {
      "q": "用unittest框架为一个Calculator类编写完整测试：测试加减乘除、除零异常、边界情况",
      "hint": "unittest.TestCase + assertEqual + assertRaises",
      "answer": "import unittest\n\nclass Calculator:\n    def add(self, a, b): return a + b\n    def sub(self, a, b): return a - b\n    def mul(self, a, b): return a * b\n    def div(self, a, b):\n        if b == 0: raise ValueError('Division by zero')\n        return a / b\n\nclass TestCalc(unittest.TestCase):\n    def setUp(self):\n        self.calc = Calculator()\n\n    def test_add(self):\n        self.assertEqual(self.calc.add(2, 3), 5)\n        self.assertEqual(self.calc.add(-1, 1), 0)\n\n    def test_div_zero(self):\n        with self.assertRaises(ValueError):\n            self.calc.div(1, 0)\n\n    def test_mul_zero(self):\n        self.assertEqual(self.calc.mul(5, 0), 0)\n\nif __name__ == '__main__':\n    unittest.main()",
      "diff": "challenge",
      "kp": [
        "unittest",
        "assertEqual",
        "assertRaises"
      ]
    }
  ],
  21: [
    {
      "answer": "from fastapi import FastAPI, HTTPException, Query\nfrom pydantic import BaseModel\nfrom typing import List, Optional\n\napp = FastAPI()\n\nclass ItemCreate(BaseModel):\n    name: str\n    price: float\n\nclass ItemResponse(BaseModel):\n    id: int\n    name: str\n    price: float\n\nitems = {}\ncounter = 0\n\n@app.post(\"/items\", response_model=ItemResponse)\ndef create(item: ItemCreate):\n    global counter\n    counter += 1\n    items[counter] = {\"id\": counter, **item.dict()}\n    return items[counter]\n\n@app.get(\"/items\", response_model=List[ItemResponse])\ndef list_items(page: int = Query(1, ge=1), size: int = Query(5, ge=1, le=20)):\n    all_items = list(items.values())\n    start = (page - 1) * size\n    return all_items[start:start+size]\n\n@app.get(\"/items/{item_id}\")\ndef read(item_id: int):\n    if item_id not in items:\n        raise HTTPException(404)\n    return items[item_id]\n\nprint(\"CRUD with pagination created\")",
      "diff": "challenge",
      "hint": "slice 数据列表 + HTTPException + query 参数",
      "kp": [
        "api_crud",
        "api_fastapi",
        {
          "q": "用 Flask 写一个返回当前时间的 JSON API",
          "hint": "jsonify + datetime",
          "kp": [
            "flask",
            "api",
            "json"
          ],
          "diff": "easy",
          "answer": "from flask import Flask, jsonify\nfrom datetime import datetime\napp = Flask(__name__)\n@app.route('/time')\ndef get_time():\n    return jsonify({'time': datetime.now().isoformat()})"
        }
      ],
      "q": "给 FastAPI 项目加上完整的 CRUD + 错误处理 + 分页，实现 GET /items?page=1&size=5"
    },
    {
      "q": "用Flask实现一个TODO API：GET列表、POST新增、DELETE删除，数据存内存列表",
      "hint": "Flask + jsonify + request.get_json()",
      "answer": "from flask import Flask, jsonify, request\n\napp = Flask(__name__)\ntodos = []\n\n@app.route('/todos', methods=['GET'])\ndef get_todos():\n    return jsonify(todos)\n\n@app.route('/todos', methods=['POST'])\ndef add_todo():\n    todo = request.get_json()\n    todo['id'] = len(todos) + 1\n    todos.append(todo)\n    return jsonify(todo), 201\n\n@app.route('/todos/<int:tid>', methods=['DELETE'])\ndef del_todo(tid):\n    global todos\n    todos = [t for t in todos if t['id'] != tid]\n    return '', 204\n\n# app.run(debug=True)",
      "diff": "challenge",
      "kp": [
        "flask",
        "rest_api",
        "jsonify"
      ]
    }
  ],
  22: [
    {
      "answer": "import json\n\ndef fetch_json(json_str):\n    data = json.loads(json_str)\n    return data\n\nmock_response = '{\"name\": \"Python\", \"version\": 3.12, \"creator\": \"Guido\"}'\ndata = fetch_json(mock_response)\nfor key in data.keys():\n    print(key)",
      "diff": "challenge",
      "hint": "json.loads(); .keys()",
      "kp": [
        "crawl_requests",
        "json_advanced",
        {
          "q": "爬取一个网页, 提取所有链接并保存到文件",
          "hint": "requests.get + BeautifulSoup find_all('a')",
          "kp": [
            "crawler",
            "beautifulsoup",
            "links"
          ],
          "diff": "medium",
          "answer": "import requests\nfrom bs4 import BeautifulSoup\nresp = requests.get(url)\nsoup = BeautifulSoup(resp.text, 'html.parser')\nlinks = [a.get('href') for a in soup.find_all('a') if a.get('href')]\nwith open('links.txt', 'w') as f:\n    f.write('\\n'.join(links))"
        }
      ],
      "q": "写一个函数 fetch_json(url) 用 requests 获取 JSON API 数据（模拟，用 json.loads 解析给定字符串），打印所有 key"
    },
    {
      "q": "用BeautifulSoup抓取一个网页，提取所有链接的文本和URL，保存到CSV",
      "hint": "requests + BeautifulSoup + csv.writer",
      "answer": "import requests, csv\nfrom bs4 import BeautifulSoup\n\nurl = 'https://example.com'\nresp = requests.get(url, timeout=10)\nsoup = BeautifulSoup(resp.text, 'html.parser')\nlinks = [(a.text.strip(), a.get('href', '')) for a in soup.find_all('a')]\n\nwith open('links.csv', 'w', newline='', encoding='utf-8') as f:\n    writer = csv.writer(f)\n    writer.writerow(['Text', 'URL'])\n    writer.writerows(links)\n\nprint(f'Saved {len(links)} links')",
      "diff": "challenge",
      "kp": [
        "bs4",
        "requests",
        "csv"
      ]
    }
  ],
  23: [
    {
      "answer": "import pandas as pd\nimport io\ncsv_data = \"name,score\\n张三,85\\n李四,92\\n王五,78\"\ndf = pd.read_csv(io.StringIO(csv_data))\nprint(df.loc[df[\"score\"].idxmax(), \"name\"])",
      "diff": "challenge",
      "hint": "io.StringIO; df.loc[df['score'].idxmax()]",
      "kp": [
        "pandas_dataframe",
        "pandas_select",
        {
          "q": "读取 CSV 文件, 计算每列的平均值, 保存结果到新 CSV",
          "hint": "pandas read_csv + mean + to_csv",
          "kp": [
            "pandas",
            "csv",
            "mean"
          ],
          "diff": "easy",
          "answer": "import pandas as pd\ndf = pd.read_csv('data.csv')\nmeans = df.mean(numeric_only=True)\nmeans.to_csv('averages.csv')"
        }
      ],
      "q": "用 pandas 读取以下 CSV 数据（用 StringIO），找出成绩最高的学生姓名"
    },
    {
      "q": "用Selenium自动登录一个网站（模拟输入用户名密码并点击登录按钮），截图保存结果",
      "hint": "webdriver + find_element + send_keys + save_screenshot",
      "answer": "from selenium import webdriver\nfrom selenium.webdriver.common.by import By\nfrom selenium.webdriver.support.ui import WebDriverWait\nfrom selenium.webdriver.support import expected_conditions as EC\n\ndriver = webdriver.Chrome()\ndriver.get('https://example.com/login')\n\nwait = WebDriverWait(driver, 10)\nuser = wait.until(EC.presence_of_element_located((By.NAME, 'username')))\nuser.send_keys('myuser')\ndriver.find_element(By.NAME, 'password').send_keys('mypass')\ndriver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()\n\ndriver.save_screenshot('login_result.png')\n# driver.quit()",
      "diff": "challenge",
      "kp": [
        "selenium",
        "webdriver",
        "automation"
      ]
    }
  ],
  24: [
    {
      "answer": "import matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\n\ncities = [\"北京\", \"上海\", \"广州\"]\npop = [2171, 2487, 1868]\nplt.bar(cities, pop)\nplt.title(\"城市人口\")\nplt.savefig(\"chart.png\")\nprint(\"图表已保存为 chart.png\")",
      "diff": "challenge",
      "hint": "plt.bar(); plt.savefig()",
      "kp": [
        "viz_bar",
        {
          "q": "用 matplotlib 画一个柱状图, 展示各月份的销售数据并添加数据标签",
          "hint": "plt.bar + ax.text 添加标签",
          "kp": [
            "matplotlib",
            "bar_chart",
            "labels"
          ],
          "diff": "easy",
          "answer": "import matplotlib.pyplot as plt\nmonths = ['Jan','Feb','Mar','Apr']\nsales = [100, 150, 120, 180]\nbars = plt.bar(months, sales)\nfor bar, val in zip(bars, sales):\n    plt.text(bar.get_x()+0.3, val+2, str(val))\nplt.show()"
        }
      ],
      "q": "用 matplotlib 画一个简单的柱状图：三个城市 [\"北京\",\"上海\",\"广州\"] 人口 [2171,2487,1868]，保存为 chart.png 并打印完成提示"
    },
    {
      "q": "用matplotlib绘制一个子图布局：左侧折线图、右侧饼图，共享标题",
      "hint": "plt.subplots(1,2) + ax1.plot + ax2.pie",
      "answer": "import matplotlib.pyplot as plt\n\nfig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))\nfig.suptitle('Data Overview')\n\n# 折线图\nax1.plot([1,2,3,4], [10,20,25,30], 'b-o')\nax1.set_title('Trend')\nax1.set_xlabel('X')\nax1.set_ylabel('Y')\n\n# 饼图\nlabels = ['A', 'B', 'C']\nsizes = [40, 35, 25]\nax2.pie(sizes, labels=labels, autopct='%1.1f%%')\nax2.set_title('Distribution')\n\nplt.tight_layout()\nplt.savefig('subplot_demo.png')\nplt.show()",
      "diff": "challenge",
      "kp": [
        "matplotlib",
        "subplot",
        "visualization"
      ]
    }
  ],
  25: [
    {
      "answer": "import requests\nimport time\nimport random\n\ndef fetch_with_retry(url, retries=3):\n    headers = {\"User-Agent\": \"Mozilla/5.0\"}\n    for i in range(retries):\n        try:\n            time.sleep(random.uniform(0.5, 1.5))\n            resp = requests.get(url, headers=headers, timeout=10)\n            resp.raise_for_status()\n            return resp.text\n        except Exception as e:\n            if i == retries - 1:\n                raise\n            print(f\"Retry {i+1}: {e}\")\n    return None",
      "diff": "challenge",
      "hint": "requests + time.sleep(random) + try/except 循环",
      "kp": [
        "crawl_anti",
        "crawl_requests",
        {
          "q": "用 Selenium 自动登录一个网站(输入用户名密码, 点登录按钮)",
          "hint": "find_element + send_keys + click",
          "kp": [
            "selenium",
            "login",
            "automation"
          ],
          "diff": "medium",
          "answer": "from selenium import webdriver\ndriver = webdriver.Chrome()\ndriver.get('https://example.com/login')\ndriver.find_element('name', 'username').send_keys('user')\ndriver.find_element('name', 'password').send_keys('pass')\ndriver.find_element('id', 'login-btn').click()"
        }
      ],
      "q": "写一个函数 fetch_with_retry(url, retries=3)，实现带 UA 伪装、随机延时、自动重试的请求"
    },
    {
      "q": "用Selenium实现翻页抓取：自动点击下一页直到最后一页，收集所有页面的数据",
      "hint": "while True + try 点击下一页 + except StopIteration",
      "answer": "from selenium import webdriver\nfrom selenium.webdriver.common.by import By\nfrom selenium.common.exceptions import NoSuchElementException\n\ndriver = webdriver.Chrome()\ndriver.get('https://example.com/list')\nall_data = []\n\nwhile True:\n    items = driver.find_elements(By.CSS_SELECTOR, '.item')\n    all_data.extend([i.text for i in items])\n\n    try:\n        next_btn = driver.find_element(By.CSS_SELECTOR, '.next-page')\n        if 'disabled' in next_btn.get_attribute('class'):\n            break\n        next_btn.click()\n    except NoSuchElementException:\n        break\n\nprint(f'Collected {len(all_data)} items')\n# driver.quit()",
      "diff": "challenge",
      "kp": [
        "selenium",
        "pagination",
        "crawling"
      ]
    }
  ],
  26: [
    {
      "answer": "import asyncio\nimport time\n\nasync def task(name, seconds):\n    print(f\"{name} start\")\n    await asyncio.sleep(seconds)\n    print(f\"{name} done\")\n    return name\n\nasync def main():\n    start = time.time()\n    results = await asyncio.gather(\n        task(\"A\", 0.3),\n        task(\"B\", 0.3),\n        task(\"C\", 0.3),\n    )\n    elapsed = time.time() - start\n    print(f\"Total: {elapsed:.2f}s (concurrent: {elapsed < 0.5})\")\n\nasyncio.run(main())",
      "diff": "challenge",
      "hint": "asyncio.gather + time.time()，3个0.5秒任务并发应<1秒",
      "kp": [
        "async_gather",
        "async_def",
        {
          "q": "用 asyncio 并发请求 5 个 URL, 计算总耗时",
          "hint": "asyncio.gather + aiohttp",
          "kp": [
            "asyncio",
            "concurrent",
            "timing"
          ],
          "diff": "medium",
          "answer": "import asyncio, aiohttp, time\nasync def fetch(url):\n    async with aiohttp.ClientSession() as s:\n        async with s.get(url) as r: return await r.text()\nasync def main():\n    start = time.time()\n    await asyncio.gather(*[fetch(u) for u in urls])\n    print(f'Total: {time.time()-start:.2f}s')"
        }
      ],
      "q": "用 asyncio 写一个异步计时器：同时启动3个不同延时的任务，统计总耗时，验证是否并发执行"
    },
    {
      "q": "用asyncio实现并发下载多个URL，用aiohttp + asyncio.gather，并显示每个URL的下载耗时",
      "hint": "async with aiohttp.ClientSession() + asyncio.gather()",
      "answer": "import asyncio, time, aiohttp\n\nasync def fetch(url):\n    start = time.time()\n    async with aiohttp.ClientSession() as session:\n        async with session.get(url) as resp:\n            text = await resp.text()\n            elapsed = time.time() - start\n            return f'{url}: {len(text)} chars, {elapsed:.2f}s'\n\nasync def main():\n    urls = ['https://httpbin.org/get'] * 3\n    results = await asyncio.gather(*[fetch(u) for u in urls])\n    for r in results:\n        print(r)\n\n# asyncio.run(main())",
      "diff": "challenge",
      "kp": [
        "asyncio",
        "aiohttp",
        "concurrent"
      ]
    }
  ],
  27: [
    {
      "answer": "from concurrent.futures import ThreadPoolExecutor, as_completed\nimport requests\nimport time\n\ndef fetch(url):\n    start = time.time()\n    resp = requests.get(url, timeout=10)\n    elapsed = time.time() - start\n    return url, resp.status_code, elapsed\n\nurls = [\"https://httpbin.org/get\"] * 5\nwith ThreadPoolExecutor(max_workers=5) as pool:\n    futures = {pool.submit(fetch, url): url for url in urls}\n    for f in as_completed(futures):\n        url, status, elapsed = f.result()\n        print(f\"{status} ({elapsed:.2f}s)\")",
      "diff": "challenge",
      "hint": "concurrent.futures + time.time()",
      "kp": [
        "crawl_concurrent",
        {
          "q": "用 Scrapy 写一个爬虫, 爬取新闻标题并保存到 JSON",
          "hint": "scrapy.Spider + yield + FeedExport",
          "kp": [
            "scrapy",
            "spider",
            "json_export"
          ],
          "diff": "medium",
          "answer": "import scrapy\nclass NewsSpider(scrapy.Spider):\n    name = 'news'\n    start_urls = ['https://news.example.com']\n    def parse(self, response):\n        for h2 in response.css('h2'):\n            yield {'title': h2.css('::text').get()}"
        }
      ],
      "q": "用 ThreadPoolExecutor 并发爬取 5 个 URL，打印每个的状态码和耗时"
    },
    {
      "q": "用Scrapy写一个爬虫，抓取quotes.toscrape.com的名言、作者和标签，保存为JSON",
      "hint": "scrapy.Spider + response.css + yield",
      "answer": "import scrapy\nimport json\n\nclass QuotesSpider(scrapy.Spider):\n    name = 'quotes'\n    start_urls = ['https://quotes.toscrape.com/']\n\n    def parse(self, response):\n        for quote in response.css('div.quote'):\n            yield {\n                'text': quote.css('span.text::text').get(),\n                'author': quote.css('small.author::text').get(),\n                'tags': quote.css('div.tags a.tag::text').getall(),\n            }\n        next_page = response.css('li.next a::attr(href)').get()\n        if next_page:\n            yield response.follow(next_page, self.parse)\n\n# Run: scrapy runspider spider.py -o quotes.json",
      "diff": "challenge",
      "kp": [
        "scrapy",
        "spider",
        "json_export"
      ]
    }
  ],
  28: [
    {
      "answer": "import sqlite3\n\nclass URLDedup:\n    def __init__(self):\n        self.conn = sqlite3.connect(\":memory:\")\n        self.conn.execute(\"CREATE TABLE urls (url TEXT PRIMARY KEY)\")\n\n    def mark(self, url):\n        self.conn.execute(\"INSERT OR IGNORE INTO urls VALUES (?)\", (url,))\n        self.conn.commit()\n\n    def is_seen(self, url):\n        return self.conn.execute(\"SELECT 1 FROM urls WHERE url=?\", (url,)).fetchone() is not None\n\n    def stats(self):\n        total = self.conn.execute(\"SELECT COUNT(*) FROM urls\").fetchone()[0]\n        return {\"seen\": total}\n\nd = URLDedup()\nd.mark(\"https://example.com\")\nprint(d.is_seen(\"https://example.com\"))\nprint(d.stats())",
      "diff": "challenge",
      "hint": "CREATE TABLE + INSERT OR IGNORE + SELECT",
      "kp": [
        "crawl_mysql",
        "db_sqlite",
        {
          "q": "给爬虫添加断点续爬功能: 记录已爬 URL, 重启后跳过",
          "hint": "文件/set 存储已爬 URL, 每次启动时加载",
          "kp": [
            "crawl",
            "checkpoint",
            "resume"
          ],
          "diff": "medium",
          "answer": "import json\ntry:\n    with open('visited.json') as f:\n        visited = set(json.load(f))\nexcept FileNotFoundError:\n    visited = set()\n# ... 爬取逻辑, 跳过 visited 中的 URL\nwith open('visited.json', 'w') as f:\n    json.dump(list(visited), f)"
        }
      ],
      "q": "用 SQLite 实现一个 URL 去重器，支持 mark(url) 和 is_seen(url)，以及 stats() 返回已爬/未爬数量"
    },
    {
      "q": "实现一个爬虫中间件：自动重试失败的请求（最多3次），并记录每次请求的状态码",
      "hint": "自定义 middleware + retry + logging",
      "answer": "import logging, requests, time\nlogging.basicConfig(level=logging.INFO)\n\ndef fetch_with_retry(url, max_retries=3):\n    for attempt in range(1, max_retries + 1):\n        try:\n            resp = requests.get(url, timeout=10)\n            logging.info(f'[{attempt}] {url} -> {resp.status_code}')\n            if resp.status_code == 200:\n                return resp.text\n            elif resp.status_code >= 500:\n                time.sleep(2 ** attempt)\n            else:\n                return None\n        except requests.RequestException as e:\n            logging.warning(f'[{attempt}] {url} failed: {e}')\n            time.sleep(1)\n    return None",
      "diff": "challenge",
      "kp": [
        "middleware",
        "retry",
        "http"
      ]
    }
  ],
  29: [
    {
      "answer": "from bs4 import BeautifulSoup\nimport json\nimport pandas as pd\n\nhtml = \"\"\"<div class=\"book\"><b class=\"t\">Python</b><b class=\"p\">89</b></div><div class=\"book\"><b class=\"t\">Java</b><b class=\"p\">79</b></div>\"\"\"\n\nsoup = BeautifulSoup(html, \"html.parser\")\nbooks = []\nfor b in soup.select(\".book\"):\n    books.append({\"title\": b.select_one(\".t\").text, \"price\": int(b.select_one(\".p\").text)})\n\ndf = pd.DataFrame(books)\nprint(df.loc[df[\"price\"].idxmax(), \"title\"])",
      "diff": "challenge",
      "hint": "BeautifulSoup + json + pandas",
      "kp": [
        "crawl_beautifulsoup",
        "json_advanced",
        "pandas_select",
        {
          "q": "整合爬虫+清洗+分析: 爬取数据后自动生成分析报告",
          "hint": "crawl -> pandas clean -> matplotlib plot -> save",
          "kp": [
            "integration",
            "pipeline",
            "report"
          ],
          "diff": "hard",
          "answer": "# 1. 爬取\nimport requests, pandas as pd, matplotlib.pyplot as plt\ndata = requests.get(api_url).json()\ndf = pd.DataFrame(data)\n# 2. 清洗\ndf = df.dropna().drop_duplicates()\n# 3. 分析+可视化\ndf.plot(x='date', y='value')\nplt.savefig('report.png')"
        }
      ],
      "q": "综合：用 BeautifulSoup 解析 HTML 书籍数据，转为 JSON，再构造 DataFrame 找最贵的书"
    },
    {
      "q": "用pandas实现数据清洗管道：读取CSV→处理缺失值→类型转换→去重→标准化列名→保存",
      "hint": "pd.read_csv + fillna + astype + drop_duplicates + rename",
      "answer": "import pandas as pd\n\ndef clean_pipeline(input_path, output_path):\n    df = pd.read_csv(input_path)\n    # 填充缺失值\n    df['age'] = df['age'].fillna(df['age'].median())\n    df['name'] = df['name'].fillna('Unknown')\n    # 类型转换\n    df['age'] = df['age'].astype(int)\n    # 去重\n    df = df.drop_duplicates(subset=['email'])\n    # 标准化列名\n    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]\n    # 保存\n    df.to_csv(output_path, index=False)\n    return df.shape\n\n# shape = clean_pipeline('raw.csv', 'clean.csv')",
      "diff": "challenge",
      "kp": [
        "pandas",
        "etl",
        "data_cleaning"
      ]
    }
  ],
  30: [
    {
      "answer": "from pathlib import Path\n\ndef tree(directory, level=0):\n    p = Path(directory)\n    indent = \"  \" * level\n    print(f\"{indent}{p.name}/\")\n    for child in sorted(p.iterdir()):\n        if child.is_dir():\n            tree(child, level + 1)\n        else:\n            print(f\"{indent}  {child.name}\")\n\nprint(\"目录树:\")\ntree(\".\")",
      "diff": "challenge",
      "hint": "Path(dir).iterdir(); 递归调用 is_dir()",
      "kp": [
        "auto_pathlib",
        "func_recursive",
        {
          "q": "写一个定时备份脚本: 每天将指定目录打包为带日期的 zip 文件",
          "hint": "shutil.make_archive + datetime + schedule",
          "kp": [
            "backup",
            "zip",
            "schedule"
          ],
          "diff": "medium",
          "answer": "import shutil, datetime, schedule, time\ndef backup():\n    today = datetime.date.today().strftime('%Y%m%d')\n    shutil.make_archive(f'backup_{today}', 'zip', 'my_folder')\nschedule.every().day.at('02:00').do(backup)\nwhile True:\n    schedule.run_pending()\n    time.sleep(60)"
        }
      ],
      "q": "写一个函数 tree(directory, level=0)，递归打印目录树（用缩进表示层级）"
    },
    {
      "q": "写一个自动备份脚本：将指定目录下的.py文件复制到备份目录，文件名加日期后缀，只备份修改时间在24小时内的文件",
      "hint": "shutil.copy2 + os.path.getmtime + datetime",
      "answer": "import os, shutil, datetime\n\ndef backup_recent(src_dir, backup_dir, hours=24):\n    os.makedirs(backup_dir, exist_ok=True)\n    cutoff = datetime.datetime.now() - datetime.timedelta(hours=hours)\n    count = 0\n    for f in os.listdir(src_dir):\n        if not f.endswith('.py'): continue\n        src = os.path.join(src_dir, f)\n        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(src))\n        if mtime > cutoff:\n            name, ext = os.path.splitext(f)\n            dst = os.path.join(backup_dir, f'{name}_{mtime:%Y%m%d}{ext}')\n            shutil.copy2(src, dst)\n            count += 1\n    return count\n\n# n = backup_recent('src/', 'backup/')",
      "diff": "challenge",
      "kp": [
        "shutil",
        "os_path",
        "datetime"
      ]
    }
  ],
  31: [
    {
      "answer": "steps = [\n    \"1. driver = webdriver.Chrome()\",\n    \"2. driver.get(url)\",\n    \"3. page_source = driver.page_source\",\n    \"4. soup = BeautifulSoup(page_source, html.parser)\",\n    \"5. links = soup.find_all(a)\",\n    \"6. driver.quit()\",\n]\nfor s in steps:\n    print(s)",
      "diff": "challenge",
      "hint": "driver.page_source; BeautifulSoup(page_source)",
      "kp": [
        "auto_selenium",
        "crawl_beautifulsoup",
        {
          "q": "用 pyautogui 自动截图并识别屏幕上的文字(OCR)",
          "hint": "pyautogui.screenshot + pytesseract",
          "kp": [
            "pyautogui",
            "ocr",
            "tesseract"
          ],
          "diff": "medium",
          "answer": "import pyautogui, pytesseract\nfrom PIL import Image\nimg = pyautogui.screenshot()\ntext = pytesseract.image_to_string(img, lang='chi_sim+eng')\nprint(text)"
        }
      ],
      "q": "用 Selenium + BeautifulSoup 组合：模拟用 Selenium 获取网页源码，再用 BeautifulSoup 解析（打印步骤说明即可）"
    },
    {
      "q": "用pyautogui实现自动填表：读取Excel数据，自动在网页表单中逐行填入并提交",
      "hint": "openpyxl + pyautogui.typewrite + pyautogui.click + time.sleep",
      "answer": "import pyautogui, time, openpyxl\n\ndef auto_fill_form(excel_path, form_positions):\n    wb = openpyxl.load_workbook(excel_path)\n    ws = wb.active\n    for row in ws.iter_rows(min_row=2, values_only=True):\n        for col_idx, (x, y) in enumerate(form_positions):\n            pyautogui.click(x, y)\n            time.sleep(0.3)\n            pyautogui.hotkey('ctrl', 'a')\n            pyautogui.typewrite(str(row[col_idx] or ''), interval=0.05)\n        # 按Tab到提交按钮并回车\n        pyautogui.press('enter')\n        time.sleep(2)\n        print(f'Submitted: {row}')\n\n# form_positions = [(100, 200), (100, 250), (100, 300)]\n# auto_fill_form('data.xlsx', form_positions)",
      "diff": "challenge",
      "kp": [
        "pyautogui",
        "openpyxl",
        "automation"
      ]
    }
  ],
  32: [
    {
      "answer": "import tkinter as tk\n\nroot = tk.Tk()\nroot.title(\"BMI Calculator\")\nroot.geometry(\"300x200\")\n\ntk.Label(root, text=\"Height (m):\").grid(row=0, column=0, padx=5, pady=5)\nheight_entry = tk.Entry(root)\nheight_entry.grid(row=0, column=1, padx=5, pady=5)\n\ntk.Label(root, text=\"Weight (kg):\").grid(row=1, column=0, padx=5, pady=5)\nweight_entry = tk.Entry(root)\nweight_entry.grid(row=1, column=1, padx=5, pady=5)\n\nresult = tk.Label(root, text=\"\", font=(\"Arial\", 12))\nresult.grid(row=3, column=0, columnspan=2, pady=10)\n\ndef calc_bmi():\n    h = float(height_entry.get())\n    w = float(weight_entry.get())\n    bmi = w / (h ** 2)\n    if bmi < 18.5: cat = \"Underweight\"\n    elif bmi < 24: cat = \"Normal\"\n    elif bmi < 28: cat = \"Overweight\"\n    else: cat = \"Obese\"\n    result.config(text=f\"BMI: {bmi:.1f} ({cat})\")\n\ntk.Button(root, text=\"Calculate\", command=calc_bmi).grid(row=2, column=0, columnspan=2, pady=5)\nprint(\"BMI Calculator created\")",
      "diff": "challenge",
      "hint": "Entry + Button + Label.config + BMI分类判断",
      "kp": [
        "gui_tkinter",
        "gui_widget",
        "gui_event",
        {
          "q": "用 Tkinter 做一个简单的计算器界面(支持加减乘除)",
          "hint": "grid 布局 + Button + Entry + eval",
          "kp": [
            "tkinter",
            "calculator",
            "grid_layout"
          ],
          "diff": "medium",
          "answer": "import tkinter as tk\ndef calc():\n    try: result.set(eval(entry.get()))\n    except: result.set('Error')\nroot = tk.Tk()\nentry = tk.Entry(root)\nentry.grid(row=0, column=0, columnspan=4)\nresult = tk.StringVar()\ntk.Label(root, textvariable=result).grid(row=1, column=0, columnspan=4)\ntk.Button(root, text='=', command=calc).grid(row=2, column=0)\nroot.mainloop()"
        }
      ],
      "q": "用 tkinter 实现一个 BMI 计算器：输入身高体重，点击按钮显示 BMI 值和分类（偏瘦/正常/偏胖/肥胖）"
    },
    {
      "q": "用Tkinter实现一个简单的计算器GUI：数字按钮+运算符+等于+清除",
      "hint": "tkinter.Button grid + eval() + StringVar",
      "answer": "import tkinter as tk\n\nclass Calculator:\n    def __init__(self, root):\n        self.expr = tk.StringVar()\n        tk.Entry(root, textvariable=self.expr, font=('Arial', 20), justify='right').grid(row=0, column=0, columnspan=4)\n        buttons = ['7','8','9','/','4','5','6','*','1','2','3','-','C','0','=','+']\n        for i, b in enumerate(buttons):\n            cmd = lambda x=b: self.click(x)\n            tk.Button(root, text=b, command=cmd, width=5, height=2).grid(row=1+i//4, column=i%4)\n\n    def click(self, key):\n        if key == 'C':\n            self.expr.set('')\n        elif key == '=':\n            try: self.expr.set(str(eval(self.expr.get())))\n            except: self.expr.set('Error')\n        else:\n            self.expr.set(self.expr.get() + key)\n\nroot = tk.Tk()\nroot.title('Calculator')\nCalculator(root)\nroot.mainloop()",
      "diff": "challenge",
      "kp": [
        "tkinter",
        "gui",
        "event_handling"
      ]
    }
  ],
  33: [
    {
      "answer": "from pathlib import Path\nfrom collections import Counter\n\nclass DirStats:\n    def __init__(self, directory):\n        self.directory = Path(directory)\n        self._files = list(self.directory.iterdir()) if self.directory.exists() else []\n\n    def scan(self):\n        exts = [f.suffix for f in self._files if f.is_file()]\n        return dict(Counter(exts))\n\n    def largest(self):\n        files = [f for f in self._files if f.is_file()]\n        if not files:\n            return None\n        return max(files, key=lambda f: f.stat().st_size)\n\n    def report(self):\n        print(f\"# 目录报告：{self.directory}\")\n        print(f\"\n文件类型分布：\")\n        for ext, count in self.scan().items():\n            print(f\"- {ext or \"(无后缀)\"}: {count}个\")\n        biggest = self.largest()\n        if biggest:\n            print(f\"\n最大文件：{biggest.name} ({biggest.stat().st_size}字节)\")\n\nds = DirStats(\".\")\nds.report()",
      "diff": "challenge",
      "hint": "pathlib + Counter + f-string",
      "kp": [
        "auto_pathlib",
        "oop_class_object",
        "print_basic",
        {
          "q": "实现一个文件监控工具: 检测指定目录的文件变化(新建/修改/删除)",
          "hint": "os.listdir 或 watchdog 库",
          "kp": [
            "watchdog",
            "file_monitor",
            "automation"
          ],
          "diff": "medium",
          "answer": "import os, time\ndef snapshot(directory):\n    return {f: os.path.getmtime(os.path.join(directory, f))\n            for f in os.listdir(directory)}\nold = snapshot('.')\nwhile True:\n    time.sleep(5)\n    new = snapshot('.')\n    for f in set(new) - set(old): print(f'New: {f}')\n    for f in set(old) - set(new): print(f'Deleted: {f}')\n    old = new"
        }
      ],
      "q": "写一个完整的小工具：DirStats 类，scan() 统计目录文件类型分布，largest() 返回最大的文件，report() 打印 Markdown 格式报告"
    },
    {
      "q": "实现一个定时任务调度器：支持每N秒/每N分钟/每天固定时间执行指定函数，用logging记录执行结果",
      "hint": "threading.Timer + schedule库 + logging",
      "answer": "import threading, time, logging\nlogging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')\n\nclass TaskScheduler:\n    def __init__(self):\n        self.tasks = []\n\n    def every(self, interval, func, *args):\n        def wrapper():\n            while True:\n                func(*args)\n                time.sleep(interval)\n        t = threading.Thread(target=wrapper, daemon=True)\n        t.start()\n        self.tasks.append(t)\n\n    def at_time(self, hour, minute, func, *args):\n        def wrapper():\n            import datetime\n            while True:\n                now = datetime.datetime.now()\n                target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)\n                if now > target:\n                    target += datetime.timedelta(days=1)\n                time.sleep((target - now).total_seconds())\n                func(*args)\n        threading.Thread(target=wrapper, daemon=True).start()\n\nsched = TaskScheduler()\n# sched.every(60, lambda: logging.info('Heartbeat'))",
      "diff": "challenge",
      "kp": [
        "threading",
        "scheduler",
        "logging"
      ]
    }
  ],
  34: [
    {
      "answer": "class EventBus:\n    def __init__(self):\n        self._listeners = {}\n        self._history = {}\n\n    def subscribe(self, event, handler):\n        self._listeners.setdefault(event, []).append(handler)\n\n    def emit(self, event, data=None):\n        self._history.setdefault(event, []).append(data)\n        for handler in self._listeners.get(event, []):\n            handler(data)\n\n    def history(self, event):\n        return self._history.get(event, [])\n\nbus = EventBus()\nbus.subscribe(\"login\", lambda d: print(f\"User {d} logged in\"))\nbus.emit(\"login\", \"alice\")\nbus.emit(\"login\", \"bob\")\nprint(bus.history(\"login\"))",
      "diff": "challenge",
      "hint": "EventBus + history dict",
      "kp": [
        "pattern_observer",
        {
          "q": "用工厂模式实现一个形状创建器: 输入 'circle'/'rect'/'triangle' 返回对应对象",
          "hint": "工厂函数或工厂类 + if/elif 或 dict 映射",
          "kp": [
            "factory_pattern",
            "oop",
            "polymorphism"
          ],
          "diff": "easy",
          "answer": "class Circle:\n    def draw(self): return 'Circle'\nclass Rect:\n    def draw(self): return 'Rectangle'\ndef create_shape(name):\n    return {'circle': Circle, 'rect': Rect}[name]()\nshape = create_shape('circle')\nprint(shape.draw())"
        }
      ],
      "q": "用观察者模式实现一个简单的事件日志系统，支持 subscribe(event, handler)、emit(event, data)、history(event) 查看事件历史"
    },
    {
      "q": "实现观察者模式：Subject类维护观察者列表，notify时自动调用所有观察者的update方法",
      "hint": "Subject.attach/detach/notify + Observer.update",
      "answer": "class Subject:\n    def __init__(self):\n        self._observers = []\n        self._state = None\n\n    def attach(self, observer):\n        self._observers.append(observer)\n\n    def detach(self, observer):\n        self._observers.remove(observer)\n\n    def notify(self):\n        for obs in self._observers:\n            obs.update(self._state)\n\n    @property\n    def state(self):\n        return self._state\n\n    @state.setter\n    def state(self, value):\n        self._state = value\n        self.notify()\n\nclass Observer:\n    def __init__(self, name):\n        self.name = name\n    def update(self, state):\n        print(f'{self.name} received: {state}')\n\ns = Subject()\ns.attach(Observer('A'))\ns.attach(Observer('B'))\ns.state = 'Hello'",
      "diff": "challenge",
      "kp": [
        "observer_pattern",
        "design_pattern",
        "oop"
      ]
    }
  ],
  35: [
    {
      "answer": "def binary_search(arr, target):\n    lo, hi = 0, len(arr) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return -1\n\nprint(binary_search([1, 3, 5, 7, 9, 11, 13], 7))\nprint(binary_search([1, 3, 5, 7, 9, 11, 13], 6))",
      "diff": "challenge",
      "hint": "lo, hi = 0, len(arr)-1; while lo <= hi; mid = (lo+hi)//2",
      "kp": [
        "algo_search"
      ],
      "q": "实现二分查找：在 [1,3,5,7,9,11,13] 中查找 7 返回索引3，查找 6 返回 -1"
    },
    {
      "answer": "def merge_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    mid = len(arr) // 2\n    left = merge_sort(arr[:mid])\n    right = merge_sort(arr[mid:])\n    result = []\n    i = j = 0\n    while i < len(left) and j < len(right):\n        if left[i] <= right[j]:\n            result.append(left[i]); i += 1\n        else:\n            result.append(right[j]); j += 1\n    result.extend(left[i:])\n    result.extend(right[j:])\n    return result\n\nprint(merge_sort([5, 3, 8, 1, 9, 2, 7, 4]))",
      "diff": "challenge",
      "hint": "分治：递归拆半 + 双指针合并",
      "kp": [
        "algo_sort"
      ],
      "q": "实现归并排序：对 [5,3,8,1,9,2,7,4] 排序并打印 [1,2,3,4,5,7,8,9]"
    }
  ],
  36: [
    {
      "answer": "def lcs(s1, s2):\n    m, n = len(s1), len(s2)\n    dp = [[0] * (n + 1) for _ in range(m + 1)]\n    for i in range(1, m + 1):\n        for j in range(1, n + 1):\n            if s1[i-1] == s2[j-1]:\n                dp[i][j] = dp[i-1][j-1] + 1\n            else:\n                dp[i][j] = max(dp[i-1][j], dp[i][j-1])\n    return dp[m][n]\n\nprint(lcs(\"abcde\", \"ace\"))",
      "diff": "challenge",
      "hint": "dp[i][j] = dp[i-1][j-1]+1 if s1[i-1]==s2[j-1] else max(dp[i-1][j], dp[i][j-1])",
      "kp": [
        "algo_dp"
      ],
      "q": "实现最长公共子序列(LCS)：lcs(\"abcde\", \"ace\") 返回 3"
    },
    {
      "answer": "from collections import deque\n\ndef bfs_shortest(graph, start, end):\n    visited = {start}\n    queue = deque([(start, 0)])\n    while queue:\n        node, dist = queue.popleft()\n        if node == end:\n            return dist\n        for neighbor in graph[node]:\n            if neighbor not in visited:\n                visited.add(neighbor)\n                queue.append((neighbor, dist + 1))\n    return -1\n\ng = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2, 4], 4: [3]}\nprint(bfs_shortest(g, 0, 4))",
      "diff": "challenge",
      "hint": "deque + (node, dist) 元组 + visited set",
      "kp": [
        "algo_graph"
      ],
      "q": "用 BFS 求最短路径：图中 0 到 4 的最短距离是几？图: {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2,4], 4:[3]}"
    }
  ],
  37: [
    {
      "answer": "class PluginManager:\n    _plugins = {}\n    _bus = None\n\n    @classmethod\n    def init(cls, bus):\n        cls._bus = bus\n\n    @classmethod\n    def register(cls, name, plugin_cls):\n        cls._plugins[name] = plugin_cls\n        if cls._bus:\n            cls._bus.emit(\"plugin_registered\", name)\n\n    @classmethod\n    def create(cls, name):\n        return cls._plugins[name]()\n\nclass EventBus:\n    def __init__(self):\n        self._listeners = {}\n    def subscribe(self, event, fn):\n        self._listeners.setdefault(event, []).append(fn)\n    def emit(self, event, data=None):\n        for fn in self._listeners.get(event, []):\n            fn(data)\n\nbus = EventBus()\nbus.subscribe(\"plugin_registered\", lambda n: print(f\"Plugin {{n}} registered\"))\nPluginManager.init(bus)\nPluginManager.register(\"logger\", type(\"LoggerPlugin\", (), {\"run\": lambda self: \"logging\"}))\np = PluginManager.create(\"logger\")\nprint(p.run())",
      "diff": "challenge",
      "hint": "工厂 + 观察者 + 单例 组合",
      "kp": [
        "pattern_factory",
        "pattern_observer",
        {
          "q": "用观察者模式实现一个简单的事件系统: 发布者通知所有订阅者",
          "hint": "维护订阅者列表, 通知时遍历调用",
          "kp": [
            "observer_pattern",
            "event_system",
            "pub_sub"
          ],
          "diff": "medium",
          "answer": "class EventEmitter:\n    def __init__(self): self._listeners = []\n    def subscribe(self, fn): self._listeners.append(fn)\n    def emit(self, data):\n        for fn in self._listeners: fn(data)\nemitter = EventEmitter()\nemitter.subscribe(lambda d: print(f'Got: {d}'))\nemitter.emit('hello')"
        }
      ],
      "q": "综合：用工厂+观察者+单例模式组合实现 PluginManager，注册插件时通过 EventBus 发出通知，创建插件时用工厂"
    },
    {
      "q": "实现一个简易依赖注入容器：用装饰器@register注册类，用container.get(Name)获取实例（自动解析构造函数依赖）",
      "hint": "inspect.signature + 递归构造 + 单例缓存",
      "answer": "import inspect\n\nclass Container:\n    def __init__(self):\n        self._registry = {}\n        self._instances = {}\n\n    def register(self, name=None):\n        def decorator(cls):\n            key = name or cls.__name__\n            self._registry[key] = cls\n            return cls\n        return decorator\n\n    def get(self, name):\n        if name in self._instances:\n            return self._instances[name]\n        cls = self._registry[name]\n        sig = inspect.signature(cls.__init__)\n        deps = {}\n        for pname, param in sig.parameters.items():\n            if pname == 'self': continue\n            if param.annotation != inspect.Parameter.empty:\n                deps[pname] = self.get(param.annotation.__name__)\n        instance = cls(**deps)\n        self._instances[name] = instance\n        return instance\n\ncontainer = Container()\n\n@container.register()\nclass Database: pass\n\n@container.register()\nclass Service:\n    def __init__(self, db: Database): self.db = db\n\nsvc = container.get('Service')\nprint(f'Service.db is Database: {isinstance(svc.db, Database)}')",
      "diff": "challenge",
      "kp": [
        "dependency_injection",
        "design_pattern",
        "reflection"
      ]
    }
  ]
}
