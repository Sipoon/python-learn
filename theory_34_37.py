"""理论讲解数据 - 阶段34~37 — v5.0 第六篇：架构与算法（设计模式/算法基础/算法进阶/综合实战）"""
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

THEORY_34_37 = {
    # ==================== 阶段34：设计模式 ====================
    34: (f"""{B}阶段34：设计模式 — 前人总结的代码套路{END}

{C_}生活类比：设计模式 = 菜谱模板{END}
    你不用每次发明新做法，照着菜谱做就好
    设计模式 = 编程界的经典菜谱

{BD}一、单例模式 — 全局只要一个{END}
    >>> class Database:
    ...     _instance = None
    ...
    ...     def __new__(cls):
    ...         if cls._instance is None:
    ...             cls._instance = super().__new__(cls)
    ...             cls._instance.connection = "connected"
    ...         return cls._instance
    ...
    >>> db1 = Database()
    >>> db2 = Database()
    >>> db1 is db2       # True — 永远是同一个实例
    True

{BD}二、工厂模式 — 用函数创建对象{END}
    >>> class Dog:
    ...     def speak(self): return "Woof!"

    >>> class Cat:
    ...     def speak(self): return "Meow!"

    >>> def animal_factory(animal_type):
    ...     if animal_type == "dog": return Dog()
    ...     elif animal_type == "cat": return Cat()
    ...     else: raise ValueError(f"Unknown: {{animal_type}}")

    >>> pet = animal_factory("dog")
    >>> pet.speak()
    'Woof!'

{BD}三、策略模式 — 算法可替换{END}
    >>> class BubbleSort:
    ...     def sort(self, data):
    ...         # 冒泡排序实现...
    ...         return sorted(data)  # 简化演示

    >>> class QuickSort:
    ...     def sort(self, data):
    ...         return sorted(data)  # 简化演示

    >>> class Sorter:
    ...     def __init__(self, strategy):
    ...         self.strategy = strategy
    ...     def sort(self, data):
    ...         return self.strategy.sort(data)

    >>> sorter = Sorter(QuickSort())
    >>> sorter.sort([3, 1, 2])
    [1, 2, 3]

{BD}四、观察者模式 — 一处变化，多处响应{END}
    >>> class EventEmitter:
    ...     def __init__(self):
    ...         self._listeners = []
    ...     def subscribe(self, listener):
    ...         self._listeners.append(listener)
    ...     def emit(self, event):
    ...         for listener in self._listeners:
    ...             listener(event)

    >>> emitter = EventEmitter()
    >>> emitter.subscribe(lambda e: print(f"Listener1: {{e}}"))
    >>> emitter.subscribe(lambda e: print(f"Listener2: {{e}}"))
    >>> emitter.emit("click")
    Listener1: click
    Listener2: click

{BD}五、装饰器模式 — 动态加功能{END}
    >>> # 不修改原函数，动态增加功能（你已经在阶段18学过装饰器了！）
    >>> def log_calls(func):
    ...     def wrapper(*args, **kwargs):
    ...         print(f"Calling {{func.__name__}}")
    ...         result = func(*args, **kwargs)
    ...         print(f"{{func.__name__}} returned {{result}}")
    ...         return result
    ...     return wrapper

    >>> @log_calls
    ... def add(a, b):
    ...     return a + b

    >>> add(1, 2)
    Calling add
    add returned 3
    3

{C_}设计模式不是死规则，是经验的总结，灵活运用才是关键{END}


{BD}三、工厂模式 — 灵活创建对象{END}

{C_}用函数/类决定实例化哪个类{END}
    >>> class Dog:
    ...     def speak(self): return "汪汪"

    >>> class Cat:
    ...     def speak(self): return "喵喵"

    >>> def pet_factory(pet_type):
    ...     pets = {{'dog': Dog, 'cat': Cat}}
    ...     return pets[pet_type]()

    >>> pet = pet_factory('dog')
    >>> print(pet.speak())
    汪汪

{C_}好处：创建逻辑集中，易于扩展新类型{END}

{DIM}>> 动手试试！{END}
    {C_}在代码实验室里实现一个单例模式或工厂模式{END}
""", ["pattern_singleton", "pattern_factory", "pattern_observer", "pattern_strategy"]),

    # ==================== 阶段35：算法基础 ====================
    35: (f"""{B}阶段35：算法基础 — 编程的内功心法{END}

{C_}生活类比：算法 = 做事的步骤{END}
    做饭：随便乱做 → 也能吃，但慢且不好吃
    按菜谱做 → 快、好吃、可复现
    算法 = 编程的菜谱

{BD}一、时间复杂度 Big O{END}
    衡量算法效率：数据量翻倍，时间变多少？

    >>> # O(1) — 常数时间，最快
    >>> def get_first(lst):
    ...     return lst[0]

    >>> # O(n) — 线性时间，扫描一遍
    >>> def find_item(lst, target):
    ...     for i, item in enumerate(lst):
    ...         if item == target:
    ...             return i
    ...     return -1

    >>> # O(n^2) — 平方时间，两重循环
    >>> def bubble_sort(lst):
    ...     n = len(lst)
    ...     for i in range(n):
    ...         for j in range(n - i - 1):
    ...             if lst[j] > lst[j + 1]:
    ...                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
    ...     return lst

    >>> # O(log n) — 对数时间，每次砍一半
    >>> def binary_search(lst, target):
    ...     lo, hi = 0, len(lst) - 1
    ...     while lo <= hi:
    ...         mid = (lo + hi) // 2
    ...         if lst[mid] == target:
    ...             return mid
    ...         elif lst[mid] < target:
    ...             lo = mid + 1
    ...         else:
    ...             hi = mid - 1
    ...     return -1

    >>> # 复杂度排序：O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n)

{BD}二、冒泡排序{END}
    >>> def bubble_sort(arr):
    ...     n = len(arr)
    ...     for i in range(n):
    ...         swapped = False
    ...         for j in range(n - i - 1):
    ...             if arr[j] > arr[j + 1]:
    ...                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
    ...                 swapped = True
    ...         if not swapped:  # 没有交换说明已排好
    ...             break
    ...     return arr

    >>> bubble_sort([5, 3, 8, 1, 9])
    [1, 3, 5, 8, 9]

{BD}三、选择排序{END}
    >>> def selection_sort(arr):
    ...     for i in range(len(arr)):
    ...         min_idx = i
    ...         for j in range(i + 1, len(arr)):
    ...             if arr[j] < arr[min_idx]:
    ...                 min_idx = j
    ...         arr[i], arr[min_idx] = arr[min_idx], arr[i]
    ...     return arr

{BD}四、插入排序{END}
    >>> def insertion_sort(arr):
    ...     for i in range(1, len(arr)):
    ...         key = arr[i]
    ...         j = i - 1
    ...         while j >= 0 and arr[j] > key:
    ...             arr[j + 1] = arr[j]
    ...             j -= 1
    ...         arr[j + 1] = key
    ...     return arr

{BD}五、归并排序{END}
    >>> def merge_sort(arr):
    ...     if len(arr) <= 1:
    ...         return arr
    ...     mid = len(arr) // 2
    ...     left = merge_sort(arr[:mid])
    ...     right = merge_sort(arr[mid:])
    ...     return merge(left, right)

    >>> def merge(left, right):
    ...     result = []
    ...     i = j = 0
    ...     while i < len(left) and j < len(right):
    ...         if left[i] <= right[j]:
    ...             result.append(left[i]); i += 1
    ...         else:
    ...             result.append(right[j]); j += 1
    ...     result.extend(left[i:])
    ...     result.extend(right[j:])
    ...     return result

    >>> merge_sort([5, 3, 8, 1, 9, 2])
    [1, 2, 3, 5, 8, 9]

{BD}六、快速排序{END}
    >>> def quick_sort(arr):
    ...     if len(arr) <= 1:
    ...         return arr
    ...     pivot = arr[len(arr) // 2]
    ...     left = [x for x in arr if x < pivot]
    ...     middle = [x for x in arr if x == pivot]
    ...     right = [x for x in arr if x > pivot]
    ...     return quick_sort(left) + middle + quick_sort(right)

    >>> quick_sort([5, 3, 8, 1, 9])
    [1, 3, 5, 8, 9]

{BD}七、二分查找{END}
    >>> # 前提：列表必须已排序！
    >>> def binary_search(arr, target):
    ...     lo, hi = 0, len(arr) - 1
    ...     while lo <= hi:
    ...         mid = (lo + hi) // 2
    ...         if arr[mid] == target:
    ...             return mid
    ...         elif arr[mid] < target:
    ...             lo = mid + 1
    ...         else:
    ...             hi = mid - 1
    ...     return -1

    >>> binary_search([1, 3, 5, 7, 9], 5)
    2

{BD}八、递归思想{END}
    >>> # 递归 = 函数调用自己 + 终止条件
    >>> def factorial(n):
    ...     if n <= 1:       # 终止条件
    ...         return 1
    ...     return n * factorial(n - 1)  # 递归调用

    >>> factorial(5)       # 5 * 4 * 3 * 2 * 1
    120

    >>> # 斐波那契数列
    >>> def fib(n):
    ...     if n <= 1: return n
    ...     return fib(n - 1) + fib(n - 2)

    >>> # 注意：纯递归 fib 效率极低(O(2^n))，需记忆化优化

{C_}排序算法对比：{END}
    | 算法     | 平均时间   | 最坏时间   | 稳定性 |
    |---------|-----------|-----------|-------|
    | 冒泡     | O(n^2)    | O(n^2)    | 稳定   |
    | 选择     | O(n^2)    | O(n^2)    | 不稳定  |
    | 插入     | O(n^2)    | O(n^2)    | 稳定   |
    | 归并     | O(n log n)| O(n log n)| 稳定   |
    | 快速     | O(n log n)| O(n^2)    | 不稳定  |

{DIM}>> 动手试试！{END}
    {C_}在代码实验室里实现冒泡排序，观察排序过程{END}
""", ["algo_search", "algo_sort", "algo_complexity", "algo_recursion"]),

    # ==================== 阶段36：算法进阶 ====================
    36: (f"""{B}阶段36：算法进阶 — 解决更复杂的问题{END}

{C_}生活类比：进阶算法 = 更聪明的策略{END}
    基础算法 = 暴力尝试所有可能
    进阶算法 = 用策略聪明地缩小搜索范围

{BD}一、动态规划（DP）— 记住中间结果{END}
    核心思想：把大问题拆成小问题，记住答案避免重复计算

    >>> # 斐波那契 — DP 版本（从底向上）
    >>> def fib_dp(n):
    ...     if n <= 1: return n
    ...     dp = [0] * (n + 1)
    ...     dp[1] = 1
    ...     for i in range(2, n + 1):
    ...         dp[i] = dp[i - 1] + dp[i - 2]
    ...     return dp[n]

    >>> fib_dp(50)      # 瞬间出结果，纯递归要算到天荒地老
    12586269025

    >>> # 背包问题 — 经典 DP
    >>> def knapsack(weights, values, capacity):
    ...     n = len(weights)
    ...     dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    ...     for i in range(1, n + 1):
    ...         for w in range(capacity + 1):
    ...             if weights[i-1] <= w:
    ...                 dp[i][w] = max(dp[i-1][w],
    ...                                dp[i-1][w-weights[i-1]] + values[i-1])
    ...             else:
    ...                 dp[i][w] = dp[i-1][w]
    ...     return dp[n][capacity]

    >>> knapsack([2, 3, 4, 5], [3, 4, 5, 6], 8)
    10

{BD}二、贪心算法 — 每步选最优{END}
    核心思想：局部最优 → 希望全局最优

    >>> # 零钱兑换（贪心版，不一定最优）
    >>> def coin_change_greedy(amount, coins):
    ...     coins.sort(reverse=True)
    ...     count = 0
    ...     for coin in coins:
    ...         while amount >= coin:
    ...             amount -= coin
    ...             count += 1
    ...     return count if amount == 0 else -1

    >>> coin_change_greedy(63, [25, 10, 5, 1])
    6

    >>> # 活动选择问题
    >>> def activity_select(activities):
    ...     # 按结束时间排序
    ...     activities.sort(key=lambda x: x[1])
    ...     selected = [activities[0]]
    ...     for act in activities[1:]:
    ...         if act[0] >= selected[-1][1]:  # 开始时间 >= 上一个结束时间
    ...             selected.append(act)
    ...     return selected

{BD}三、回溯法 — 试错+撤销{END}
    核心思想：走不通就退回来换条路

    >>> # N 皇后
    >>> def solve_n_queens(n):
    ...     def is_safe(board, row, col):
    ...         for i in range(row):
    ...             if board[i] == col or \\
    ...                abs(board[i] - col) == abs(i - row):
    ...                 return False
    ...         return True
    ...
    ...     def backtrack(board, row):
    ...         if row == n:
    ...             return [board[:]]
    ...         solutions = []
    ...         for col in range(n):
    ...             if is_safe(board, row, col):
    ...                 board[row] = col
    ...                 solutions.extend(backtrack(board, row + 1))
    ...                 board[row] = -1  # 撤销
    ...         return solutions
    ...
    ...     return backtrack([-1] * n, 0)

    >>> len(solve_n_queens(8))   # 8皇后有92个解
    92

{BD}四、BFS 广度优先搜索{END}
    >>> from collections import deque

    >>> def bfs(graph, start):
    ...     visited = {{start}}
    ...     queue = deque([start])
    ...     order = []
    ...     while queue:
    ...         node = queue.popleft()
    ...         order.append(node)
    ...         for neighbor in graph[node]:
    ...             if neighbor not in visited:
    ...                 visited.add(neighbor)
    ...                 queue.append(neighbor)
    ...     return order

    >>> graph = {{0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}}
    >>> bfs(graph, 0)
    [0, 1, 2, 3]

{BD}五、DFS 深度优先搜索{END}
    >>> def dfs(graph, start, visited=None):
    ...     if visited is None:
    ...         visited = set()
    ...     visited.add(start)
    ...     order = [start]
    ...     for neighbor in graph[start]:
    ...         if neighbor not in visited:
    ...             order.extend(dfs(graph, neighbor, visited))
    ...     return order

    >>> dfs(graph, 0)
    [0, 1, 3, 2]

{BD}六、栈与队列{END}
    >>> # 栈 — 后进先出（LIFO）
    >>> stack = []
    >>> stack.append(1)     # 入栈
    >>> stack.append(2)
    >>> stack.pop()         # 出栈 → 2

    >>> # 队列 — 先进先出（FIFO）
    >>> from collections import deque
    >>> queue = deque()
    >>> queue.append(1)     # 入队
    >>> queue.append(2)
    >>> queue.popleft()     # 出队 → 1

{C_}算法选择指南：{END}
    | 问题类型     | 推荐算法     |
    |------------|-------------|
    | 最优化问题   | 动态规划     |
    | 每步选最优   | 贪心        |
    | 全部方案     | 回溯/DFS    |
    | 最短路径     | BFS         |
    | 排序        | 快排/归并    |

{DIM}>> 动手试试！{END}
    {C_}在代码实验室里实现斐波那契的 DP 版本，对比递归版的速度{END}
""", ["algo_dp", "algo_greedy", "algo_backtrack", "algo_graph"]),

    # ==================== 阶段37：综合实战 — 架构与算法 ====================
    37: (f"""{B}阶段37：综合实战 — 架构与算法{END}

{C_}三个实战项目，融会贯通设计模式与算法！{END}

{BD}一、设计模式库 — 插件系统{END}
    用工厂+策略+观察者+单例模式组合实现一个可扩展的插件架构

    >>> # 1. 工厂模式 — 动态创建插件
    >>> class PluginFactory:
    ...     _plugins = {{}}
    ...
    ...     @classmethod
    ...     def register(cls, name, plugin_class):
    ...         cls._plugins[name] = plugin_class
    ...
    ...     @classmethod
    ...     def create(cls, name):
    ...         if name not in cls._plugins:
    ...             raise ValueError("Unknown plugin: " + name)
    ...         return cls._plugins[name]()

    >>> # 2. 观察者模式 — 事件通知
    >>> class EventBus:
    ...     def __init__(self):
    ...         self._listeners = {{}}
    ...     def subscribe(self, event, fn):
    ...         self._listeners.setdefault(event, []).append(fn)
    ...     def emit(self, event, data=None):
    ...         for fn in self._listeners.get(event, []):
    ...             fn(data)

    >>> # 3. 单例模式 — 全局配置
    >>> class Config:
    ...     _instance = None
    ...     def __new__(cls):
    ...         if cls._instance is None:
    ...             cls._instance = super().__new__(cls)
    ...             cls._instance.settings = {{}}
    ...         return cls._instance
    ...     def set(self, key, value):
    ...         self.settings[key] = value
    ...     def get(self, key, default=None):
    ...         return self.settings.get(key, default)

    >>> # 4. 策略模式 — 不同处理方式
    >>> class JsonFormatter:
    ...     def format(self, data):
    ...         return json.dumps(data, ensure_ascii=False)

    >>> class CsvFormatter:
    ...     def format(self, data):
    ...         if not data: return ""
    ...         keys = data[0].keys()
    ...         lines = [",".join(str(d[k]) for k in keys) for d in data]
    ...         return "\n".join(lines)

    >>> # 5. 组合使用
    >>> bus = EventBus()
    >>> bus.subscribe("data", lambda d: print("[Event]", d))
    >>> config = Config()
    >>> config.set("format", "json")
    >>> bus.emit("data", "Plugin system ready")
    [Event] Plugin system ready

{BD}二、算法工具箱 — 排序性能对比{END}
    实现多种排序算法并对比性能

    >>> import time, random
    >>> random.seed(42)
    >>> data = [random.randint(1, 10000) for _ in range(1000)]

    >>> def time_sort(sort_func, data):
    ...     arr = data[:]
    ...     start = time.time()
    ...     result = sort_func(arr)
    ...     elapsed = time.time() - start
    ...     return elapsed, result if result else arr

    >>> # 冒泡排序 O(n^2)
    >>> def bubble_sort(arr):
    ...     for i in range(len(arr)):
    ...         for j in range(len(arr)-i-1):
    ...             if arr[j] > arr[j+1]:
    ...                 arr[j], arr[j+1] = arr[j+1], arr[j]
    ...     return arr

    >>> # 快速排序 O(n log n) 平均
    >>> def quick_sort(arr):
    ...     if len(arr) <= 1: return arr
    ...     pivot = arr[len(arr)//2]
    ...     left = [x for x in arr if x < pivot]
    ...     mid = [x for x in arr if x == pivot]
    ...     right = [x for x in arr if x > pivot]
    ...     return quick_sort(left) + mid + quick_sort(right)

    >>> # 内置排序（Timsort）— 永远优先使用！
    >>> def builtin_sort(arr):
    ...     return sorted(arr)

    >>> # 性能对比结果（1000 个数）
    >>> # bubble_sort:  ~0.05s
    >>> # quick_sort:   ~0.002s
    >>> # sorted():     ~0.0002s  ← 内置排序最快

{BD}三、代码审查工具{END}
    扫描 Python 源码，检测常见问题

    >>> import ast, re
    >>>
    >>> def check_source(code):
    ...     issues = []
    ...
    ...     # 1. 行长检查
    ...     for i, line in enumerate(code.split('\n'), 1):
    ...         if len(line) > 120:
    ...             issues.append("Line " + str(i) + ": 过长 (" + str(len(line)) + " chars)")
    ...
    ...     # 2. 可变默认参数
    ...     if '=[]' in code or '=dict()' in code:
    ...         issues.append("可变默认参数：def f(x=[]) 或 def f(d=dict()) 有隐患")
    ...
    ...     # 3. 裸 except
    ...     if re.search(r'except\s*:', code):
    ...         issues.append("裸 except: 应指定异常类型如 except ValueError:")
    ...
    ...     # 4. 蛇形命名检查（类名应用 PascalCase）
    ...     for match in re.finditer(r'class\s+([a-z]\w*)', code):
    ...         issues.append("类名 '" + match.group(1) + "' 应使用 PascalCase")
    ...
    ...     return issues

    >>> sample = 'def f(x=[]):\n    try:\n        pass\n    except:\n        pass'
    >>> for issue in check_source(sample):
    ...     print(issue)
    可变默认参数：def f(x=[]) 或 def f(d={{}}) 有隐患
    裸 except: 应指定异常类型如 except ValueError:

{C_}恭喜！你已完成 Python 互动学习系统全部 37 个阶段！{END}

{C_}回顾你的学习旅程：{END}
    第一篇（1-13）：Python 基础 — 从变量到综合实战
    第二篇（14-18）：Python 进阶 — 正则/OOP/模块/装饰器
    第三篇（19-21）：工程基础 — 数据库/测试/API
    第四篇（22-29）：数据方向 — 爬虫/数据/异步/综合
    第五篇（30-33）：自动化与桌面 — 脚本/GUI/综合
    第六篇（34-37）：架构与算法 — 设计模式/算法/综合

{BD}你的下一步：{END}
    1. 参与开源项目 — GitHub 上找感兴趣的项目
    2. 做自己的项目 — 把想法变成代码
    3. 持续学习 — Python 生态太大，永远有新东西
    4. 教别人 — 最好的学习方式是教

{DIM}>> 动手试试！{END}
    {C_}选择一个综合项目，从设计到实现完整走一遍{END}
""", ["project_plugin", "project_algo_bench", "project_code_review", "project_deploy"]),
}
