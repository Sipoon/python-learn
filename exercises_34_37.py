"""Exercises for stages 34-37"""

EXERCISES_34_37 = {
        34: [
            {
                "id": "s34_01",
                "title": "实现一个单例模式的 Database 类，创建两次应得到同一个实例",
                "desc": "实现一个单例模式的 Database 类，创建两次应得到同一个实例",
                "diff": "basic",
                "kp": [
                    "pattern_singleton",
                    "oop_class_object"
                ],
                "hint": "在 __new__ 中检查 _instance 是否为 None",
                "answer": "class Database:\n    _instance = None\n    def __new__(cls):\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)\n        return cls._instance\n\ndb1 = Database()\ndb2 = Database()\nprint(db1 is db2)",
                "expected": "True",
                "explain": "单例模式：__new__ 控制实例创建，类变量 _instance 保存唯一实例。两次创建返回同一对象。",
                "template": "class Database:\n    pass  # TODO\n    _instance = ...  # TODO\n    def __new__(cls):\n        pass  # TODO\n            cls._instance = ...  # TODO\ndb1 = ...  # TODO\ndb2 = ...  # TODO"
            },
            {
                "id": "s34_02",
                "title": "实现工厂函数 animal_factory(type)，dog 返回 'Woof!'，cat 返回 'Meow!'",
                "desc": "实现工厂函数 animal_factory(type)，dog 返回 'Woof!'，cat 返回 'Meow!'",
                "diff": "basic",
                "kp": [
                    "pattern_factory",
                    "oop_class_object"
                ],
                "hint": "定义两个类，用 if-elif 选择返回哪个",
                "answer": "class Dog:\n    def speak(self):\n        return \"Woof!\"\n\nclass Cat:\n    def speak(self):\n        return \"Meow!\"\n\ndef animal_factory(animal_type):\n    if animal_type == \"dog\":\n        return Dog()\n    elif animal_type == \"cat\":\n        return Cat()\n\npet = animal_factory(\"dog\")\nprint(pet.speak())",
                "expected": "Woof!",
                "explain": "工厂模式：函数根据类型参数返回不同对象，调用方无需知道具体类。解耦创建和使用。",
                "template": "class Dog:\n    pass  # TODO\n    def speak(self):\n        pass  # TODO\nclass Cat:\n    pass  # TODO\n    def speak(self):\n        pass  # TODO\ndef animal_factory(animal_type):\n    pass  # TODO\npet = ...  # TODO"
            },
            {
                "id": "s34_03",
                "title": "用策略模式实现 Sorter 类，可以切换排序策略（bubble 或 python内置 sorted）",
                "desc": "用策略模式实现 Sorter 类，可以切换排序策略（bubble 或 python内置 sorted）",
                "diff": "intermediate",
                "kp": [
                    "pattern_strategy",
                    "oop_class_object"
                ],
                "hint": "Sorter.__init__ 接受 strategy 参数，strategy 有 sort 方法",
                "answer": "class BubbleSort:\n    def sort(self, data):\n        arr = data[:]\n        n = len(arr)\n        for i in range(n):\n            for j in range(n-i-1):\n                if arr[j] > arr[j+1]:\n                    arr[j], arr[j+1] = arr[j+1], arr[j]\n        return arr\n\nclass PythonSort:\n    def sort(self, data):\n        return sorted(data)\n\nclass Sorter:\n    def __init__(self, strategy):\n        self.strategy = strategy\n    def sort(self, data):\n        return self.strategy.sort(data)\n\ns = Sorter(BubbleSort())\nprint(s.sort([3, 1, 2]))",
                "expected": "[1, 2, 3]",
                "explain": "策略模式：将算法封装为对象，运行时可切换。Sorter 持有策略引用，sort() 委托给策略执行。",
                "template": "class BubbleSort:\n    pass  # TODO\n    def sort(self, data):\n        pass  # TODO\n        arr = ...  # TODO\n        n = ...  # TODO\n                    arr[j], arr[j+1] = ...  # TODO\nclass PythonSort:\n    pass  # TODO\n    def sort(self, data):\n        pass  # TODO\nclass Sorter:\n    pass  # TODO\n    def __init__(self, strategy):\n        pass  # TODO\n        self.strategy = ...  # TODO\n    def sort(self, data):\n        pass  # TODO\ns = ...  # TODO"
            },
            {
                "id": "s34_04",
                "title": "实现一个简单的 EventEmitter，支持 subscribe 和 emit",
                "desc": "实现一个简单的 EventEmitter，支持 subscribe 和 emit",
                "diff": "challenge",
                "kp": [
                    "pattern_observer",
                    "func_def"
                ],
                "hint": "维护一个 _listeners 列表，emit 时遍历调用",
                "answer": "class EventEmitter:\n    def __init__(self):\n        self._listeners = []\n    def subscribe(self, listener):\n        self._listeners.append(listener)\n    def emit(self, event):\n        for listener in self._listeners:\n            listener(event)\n\ncalled = []\nee = EventEmitter()\nee.subscribe(lambda e: called.append(f\"A:{e}\"))\nee.subscribe(lambda e: called.append(f\"B:{e}\"))\nee.emit(\"click\")\nprint(called)",
                "expected": "['A:click', 'B:click']",
                "explain": "观察者模式：subscribe 注册回调，emit 触发通知所有订阅者。事件驱动架构的基础。",
                "template": "class EventEmitter:\n    pass  # TODO\n    def __init__(self):\n        pass  # TODO\n        self._listeners = ...  # TODO\n    def subscribe(self, listener):\n        pass  # TODO\n    def emit(self, event):\n        pass  # TODO\ncalled = ...  # TODO\nee = ...  # TODO"
            }
        ],
        35: [
            {
                "id": "s35_01",
                "title": "实现冒泡排序，对列表 [5, 3, 8, 1, 9] 排序并打印结果",
                "desc": "实现冒泡排序，对列表 [5, 3, 8, 1, 9] 排序并打印结果",
                "diff": "basic",
                "kp": [
                    "algo_sort_basic",
                    "nested_loop"
                ],
                "hint": "两重循环，相邻元素比较交换",
                "answer": "def bubble_sort(arr):\n    arr = arr[:]\n    n = len(arr)\n    for i in range(n):\n        for j in range(n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n\nprint(bubble_sort([5, 3, 8, 1, 9]))",
                "expected": "[1, 3, 5, 8, 9]",
                "explain": "冒泡排序：相邻元素两两比较，大的往后冒。外层n轮，内层n-i-1次比较。时间O(n²)，空间O(1)。",
                "template": "def bubble_sort(arr):\n    pass  # TODO\n    arr = ...  # TODO\n    n = ...  # TODO\n                arr[j], arr[j+1] = ...  # TODO"
            },
            {
                "id": "s35_02",
                "title": "实现二分查找，在有序列表 [1, 3, 5, 7, 9, 11, 13] 中查找 7 的索引",
                "desc": "实现二分查找，在有序列表 [1, 3, 5, 7, 9, 11, 13] 中查找 7 的索引",
                "diff": "basic",
                "kp": [
                    "algo_search",
                    "while_loop"
                ],
                "hint": "用 lo/hi 双指针，mid = (lo+hi)//2",
                "answer": "def binary_search(arr, target):\n    lo, hi = 0, len(arr) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return -1\n\nprint(binary_search([1, 3, 5, 7, 9, 11, 13], 7))",
                "expected": "3",
                "explain": "二分查找：有序数组中折半搜索。left/right 指针夹逼，mid=(l+r)//2。时间O(log n)。",
                "template": "def binary_search(arr, target):\n    pass  # TODO\n    lo, hi = ...  # TODO\n        mid = ...  # TODO\n            lo = ...  # TODO\n            hi = ...  # TODO"
            },
            {
                "id": "s35_03",
                "title": "实现快速排序，对 [5, 3, 8, 1, 9, 2, 7] 排序",
                "desc": "实现快速排序，对 [5, 3, 8, 1, 9, 2, 7] 排序",
                "diff": "intermediate",
                "kp": [
                    "algo_sort_adv",
                    "func_def"
                ],
                "hint": "选 pivot，分 left/middle/right 三部分递归",
                "answer": "def quick_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr)//2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quick_sort(left) + middle + quick_sort(right)\n\nprint(quick_sort([5, 3, 8, 1, 9, 2, 7]))",
                "expected": "[1, 2, 3, 5, 7, 8, 9]",
                "explain": "快速排序：选基准分区，小于基准放左，大于放右，递归处理两侧。平均O(n log n)。",
                "template": "def quick_sort(arr):\n    pass  # TODO\n    pivot = ...  # TODO"
            },
            {
                "id": "s35_04",
                "title": "用递归实现阶乘函数，计算 10! 并打印",
                "desc": "用递归实现阶乘函数，计算 10! 并打印",
                "diff": "intermediate",
                "kp": [
                    "algo_recursive",
                    "func_def"
                ],
                "hint": "终止条件 n<=1，递归 n*factorial(n-1)",
                "answer": "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)\n\nprint(factorial(10))",
                "expected": "3628800",
                "explain": "递归阶乘：n!=n*(n-1)!，基线条件0!=1。递归必须有终止条件否则栈溢出。",
                "template": "def factorial(n):\n    pass  # TODO"
            },
            {
                "id": "s35_05",
                "title": "用动态规划（DP）计算第 20 个斐波那契数",
                "desc": "用动态规划（DP）计算第 20 个斐波那契数",
                "diff": "challenge",
                "kp": [
                    "algo_sort_adv",
                    "list_index"
                ],
                "hint": "dp 数组从底向上，dp[i] = dp[i-1] + dp[i-2]",
                "answer": "def fib_dp(n):\n    if n <= 1:\n        return n\n    dp = [0] * (n + 1)\n    dp[1] = 1\n    for i in range(2, n + 1):\n        dp[i] = dp[i-1] + dp[i-2]\n    return dp[n]\n\nprint(fib_dp(20))",
                "expected": "6765",
                "explain": "DP斐波那契：用数组存已计算值避免重复递归。dp[i]=dp[i-1]+dp[i-2]，时间O(n)，空间O(n)。",
                "template": "def fib_dp(n):\n    pass  # TODO\n    dp = ...  # TODO\n    dp[1] = ...  # TODO\n        dp[i] = ...  # TODO"
            },
            {
                "id": "s35_06",
                "title": "实现插入排序，对 [4, 2, 7, 1, 3] 排序",
                "desc": "实现插入排序，对 [4, 2, 7, 1, 3] 排序",
                "diff": "basic",
                "kp": [
                    "algo_sort_basic",
                    "for_loop"
                ],
                "hint": "从第2个元素开始，向前找到合适位置插入",
                "answer": "def insertion_sort(arr):\n    arr = arr[:]\n    for i in range(1, len(arr)):\n        key = arr[i]\n        j = i - 1\n        while j >= 0 and arr[j] > key:\n            arr[j+1] = arr[j]\n            j -= 1\n        arr[j+1] = key\n    return arr\n\nprint(insertion_sort([4, 2, 7, 1, 3]))",
                "expected": "[1, 2, 3, 4, 7]",
                "explain": "插入排序：将未排序元素插入已排序部分的正确位置。类似整理扑克牌。时间O(n²)，最佳O(n)。",
                "template": "def insertion_sort(arr):\n    pass  # TODO\n    arr = ...  # TODO\n        key = ...  # TODO\n        j = ...  # TODO\n            arr[j+1] = ...  # TODO\n            j - = ...  # TODO\n        arr[j+1] = ...  # TODO"
            }
        ],
        36: [
            {
                "id": "s36_01",
                "title": "用 DP 解决背包问题：物品重量[2,3,4,5]价值[3,4,5,6]，容量8，求最大价值",
                "desc": "用 DP 解决背包问题：物品重量[2,3,4,5]价值[3,4,5,6]，容量8，求最大价值",
                "diff": "basic",
                "kp": [
                    "algo_dp",
                    "nested_loop"
                ],
                "hint": "dp[i][w] = max(dp[i-1][w], dp[i-1][w-wi]+vi)",
                "answer": "def knapsack(weights, values, capacity):\n    n = len(weights)\n    dp = [[0]*(capacity+1) for _ in range(n+1)]\n    for i in range(1, n+1):\n        for w in range(capacity+1):\n            if weights[i-1] <= w:\n                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]]+values[i-1])\n            else:\n                dp[i][w] = dp[i-1][w]\n    return dp[n][capacity]\n\nprint(knapsack([2,3,4,5], [3,4,5,6], 8))",
                "expected": "10",
                "explain": "01背包DP：dp[i][w]=max(不选i,选i+剩余容量)。dp表二维，倒序遍历重量防重复选取。",
                "template": "def knapsack(weights, values, capacity):\n    pass  # TODO\n    n = ...  # TODO\n                dp[i][w] = ...  # TODO\n                dp[i][w] = ...  # TODO"
            },
            {
                "id": "s36_02",
                "title": "实现贪心算法的零钱兑换：硬币[25,10,5,1]，金额63，求最少硬币数",
                "desc": "实现贪心算法的零钱兑换：硬币[25,10,5,1]，金额63，求最少硬币数",
                "diff": "basic",
                "kp": [
                    "algo_greedy",
                    "while_loop"
                ],
                "hint": "从大到小贪心选择",
                "answer": "def coin_change_greedy(amount, coins):\n    coins = sorted(coins, reverse=True)\n    count = 0\n    for coin in coins:\n        while amount >= coin:\n            amount -= coin\n            count += 1\n    return count\n\nprint(coin_change_greedy(63, [25, 10, 5, 1]))",
                "expected": "6",
                "explain": "贪心找零：优先用大面额硬币。63=25*2+10*1+1*3=6枚。贪心不一定最优但对美元面额有效。",
                "template": "def coin_change_greedy(amount, coins):\n    pass  # TODO\n    coins = ...  # TODO\n    count = ...  # TODO\n            amount - = ...  # TODO\n            count + = ...  # TODO"
            },
            {
                "id": "s36_03",
                "title": "用 BFS 找出图从节点0开始的遍历顺序，图：{0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2]}",
                "desc": "用 BFS 找出图从节点0开始的遍历顺序，图：{0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2]}",
                "diff": "intermediate",
                "kp": [
                    "algo_graph_bfs",
                    "dict_access"
                ],
                "hint": "用 collections.deque，维护 visited 集合",
                "answer": "from collections import deque\n\ndef bfs(graph, start):\n    visited = {start}\n    queue = deque([start])\n    order = []\n    while queue:\n        node = queue.popleft()\n        order.append(node)\n        for neighbor in graph[node]:\n            if neighbor not in visited:\n                visited.add(neighbor)\n                queue.append(neighbor)\n    return order\n\ngraph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}\nprint(bfs(graph, 0))",
                "expected": "[0, 1, 2, 3]",
                "explain": "BFS广度优先：队列逐层遍历。visited集合防重复访问。保证最短路径（无权图）。",
                "template": "from collections import deque\ndef bfs(graph, start):\n    pass  # TODO\n    visited = ...  # TODO\n    queue = ...  # TODO\n    order = ...  # TODO\n        node = ...  # TODO\ngraph = ...  # TODO"
            },
            {
                "id": "s36_04",
                "title": "用 DFS 找出图从节点0开始的遍历顺序（邻接小的先），图同上",
                "desc": "用 DFS 找出图从节点0开始的遍历顺序（邻接小的先），图同上",
                "diff": "intermediate",
                "kp": [
                    "algo_graph_dfs",
                    "algo_recursive"
                ],
                "hint": "递归实现，visited 集合防止重复",
                "answer": "def dfs(graph, start, visited=None):\n    if visited is None:\n        visited = set()\n    visited.add(start)\n    order = [start]\n    for neighbor in sorted(graph[start]):\n        if neighbor not in visited:\n            order.extend(dfs(graph, neighbor, visited))\n    return order\n\ngraph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}\nprint(dfs(graph, 0))",
                "expected": "[0, 1, 3, 2]",
                "explain": "DFS深度优先：栈/递归一条路走到底再回溯。邻接小的先访问保证确定性输出。",
                "template": "def dfs(graph, start, visited=None):\n    pass  # TODO\n        visited = ...  # TODO\n    order = ...  # TODO\ngraph = ...  # TODO"
            },
            {
                "id": "s36_05",
                "title": "用回溯法求4皇后问题的解的数量",
                "desc": "用回溯法求4皇后问题的解的数量",
                "diff": "challenge",
                "kp": [
                    "algo_backtrack",
                    "algo_recursive"
                ],
                "hint": "递归尝试每列，检查是否和已放置皇后冲突",
                "answer": "def solve_n_queens(n):\n    def is_safe(board, row, col):\n        for i in range(row):\n            if board[i] == col or abs(board[i]-col) == abs(i-row):\n                return False\n        return True\n\n    def backtrack(board, row):\n        if row == n:\n            return 1\n        count = 0\n        for col in range(n):\n            if is_safe(board, row, col):\n                board[row] = col\n                count += backtrack(board, row+1)\n                board[row] = -1\n        return count\n\n    return backtrack([-1]*n, 0)\n\nprint(solve_n_queens(4))",
                "expected": "2",
                "explain": "回溯法解N皇后：逐行放置皇后，检查列和对角线冲突，冲突则回退。剪枝减少搜索空间。",
                "template": "def solve_n_queens(n):\n    pass  # TODO\n    def is_safe(board, row, col):\n        pass  # TODO\n    def backtrack(board, row):\n        pass  # TODO\n        count = ...  # TODO\n                board[row] = ...  # TODO\n                count + = ...  # TODO\n                board[row] = ...  # TODO"
            },
            {
                "id": "s36_06",
                "title": "实现归并排序，对 [38, 27, 43, 3, 9, 82, 10] 排序",
                "desc": "实现归并排序，对 [38, 27, 43, 3, 9, 82, 10] 排序",
                "diff": "challenge",
                "kp": [
                    "algo_sort_adv",
                    "algo_recursive"
                ],
                "hint": "递归分半，merge 合并两个有序列表",
                "answer": "def merge_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    mid = len(arr) // 2\n    left = merge_sort(arr[:mid])\n    right = merge_sort(arr[mid:])\n    return merge(left, right)\n\ndef merge(left, right):\n    result = []\n    i = j = 0\n    while i < len(left) and j < len(right):\n        if left[i] <= right[j]:\n            result.append(left[i]); i += 1\n        else:\n            result.append(right[j]); j += 1\n    result.extend(left[i:])\n    result.extend(right[j:])\n    return result\n\nprint(merge_sort([38, 27, 43, 3, 9, 82, 10]))",
                "expected": "[3, 9, 10, 27, 38, 43, 82]",
                "explain": "归并排序：分治法，递归拆半→排序→合并。稳定排序，时间O(n log n)，空间O(n)。",
                "template": "def merge_sort(arr):\n    pass  # TODO\n    mid = ...  # TODO\n    left = ...  # TODO\n    right = ...  # TODO\ndef merge(left, right):\n    pass  # TODO\n    result = ...  # TODO\n    i = ...  # TODO\n            result.append(left[i]); i + = ...  # TODO\n            result.append(right[j]); j + = ...  # TODO"
            }
        ],
        37: [
            {
                "id": "s37_01",
                "title": "实现一个简单的插件系统：PluginManager 注册和执行插件",
                "desc": "实现一个简单的插件系统：PluginManager 注册和执行插件",
                "diff": "basic",
                "kp": [
                    "pattern_factory",
                    "pattern_strategy",
                    "dict_methods"
                ],
                "hint": "用字典存储插件，register(name, func) + execute(name, *args)",
                "answer": "class PluginManager:\n    def __init__(self):\n        self._plugins = {}\n    def register(self, name, func):\n        self._plugins[name] = func\n    def execute(self, name, *args):\n        if name in self._plugins:\n            return self._plugins[name](*args)\n        return None\n\npm = PluginManager()\npm.register(\"add\", lambda a, b: a + b)\npm.register(\"mul\", lambda a, b: a * b)\nprint(pm.execute(\"add\", 3, 4))\nprint(pm.execute(\"mul\", 3, 4))",
                "expected": "",
                "explain": "插件系统：register() 注册函数/类到字典，execute() 按名调用。解耦核心与扩展，符合开闭原则。",
                "template": "class PluginManager:\n    pass  # TODO\n    def __init__(self):\n        pass  # TODO\n        self._plugins = ...  # TODO\n    def register(self, name, func):\n        pass  # TODO\n        self._plugins[name] = ...  # TODO\n    def execute(self, name, *args):\n        pass  # TODO\npm = ...  # TODO"
            },
            {
                "id": "s37_02",
                "title": "实现算法计时器：分别计时冒泡排序和快速排序对1000个随机数的排序",
                "desc": "实现算法计时器：分别计时冒泡排序和快速排序对1000个随机数的排序",
                "diff": "intermediate",
                "kp": [
                    "algo_bigo",
                    "algo_sort_basic",
                    "algo_sort_adv"
                ],
                "hint": "import time; start=time.time(); ...; elapsed=time.time()-start",
                "answer": "import time, random\n\ndef bubble_sort(arr):\n    arr = arr[:]\n    n = len(arr)\n    for i in range(n):\n        for j in range(n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n\ndef quick_sort(arr):\n    if len(arr) <= 1: return arr\n    pivot = arr[len(arr)//2]\n    left = [x for x in arr if x < pivot]\n    mid = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quick_sort(left) + mid + quick_sort(right)\n\ndata = [random.randint(1, 1000) for _ in range(100)]\n\nt1 = time.time()\nbubble_sort(data)\nt_bubble = time.time() - t1\n\nt2 = time.time()\nquick_sort(data)\nt_quick = time.time() - t2\n\nprint(f\"Bubble: {t_bubble:.4f}s\")\nprint(f\"Quick:  {t_quick:.4f}s\")\nprint(f\"Quick is faster: {t_quick < t_bubble}\")",
                "expected": "",
                "explain": "time.perf_counter() 高精度计时。冒泡O(n²) vs 快排O(n log n)，数据量大时差异显著。",
                "template": "import time, random\ndef bubble_sort(arr):\n    pass  # TODO\n    arr = ...  # TODO\n    n = ...  # TODO\n                arr[j], arr[j+1] = ...  # TODO\ndef quick_sort(arr):\n    pass  # TODO\n    pivot = ...  # TODO\nt1 = ...  # TODO\nt_bubble = ...  # TODO\nt2 = ...  # TODO\nt_quick = ...  # TODO"
            },
            {
                "id": "s37_03",
                "title": "实现一个简单的代码复杂度检查器：统计函数的圈复杂度（if/elif/else/for/while/and/or 的数量）",
                "desc": "实现一个简单的代码复杂度检查器：统计函数的圈复杂度（if/elif/else/for/while/and/or 的数量）",
                "diff": "intermediate",
                "kp": [
                    "pattern_strategy",
                    "oop_class_object"
                ],
                "hint": "用 ast 模块解析代码，遍历节点统计",
                "answer": "import ast\n\ndef cyclomatic_complexity(code):\n    tree = ast.parse(code)\n    complexity = 1\n    for node in ast.walk(tree):\n        if isinstance(node, (ast.If, ast.For, ast.While)):\n            complexity += 1\n        elif isinstance(node, ast.BoolOp):\n            complexity += len(node.values) - 1\n    return complexity\n\ncode = \"\"\"\ndef check(x):\n    if x > 0:\n        if x > 10:\n            return \"high\"\n        else:\n            return \"low\"\n    elif x < 0:\n        return \"negative\"\n    else:\n        return \"zero\"\n\"\"\"\nprint(cyclomatic_complexity(code))",
                "expected": "4",
                "explain": "圈复杂度：统计if/elif/for/while/and/or等分支点数量，值越高代码越复杂难维护。",
                "template": "import ast\ndef cyclomatic_complexity(code):\n    pass  # TODO\n    tree = ...  # TODO\n    complexity = ...  # TODO\n            complexity + = ...  # TODO\n            complexity + = ...  # TODO\ncode = ...  # TODO\ndef check(x):\n    pass  # TODO"
            },
            {
                "id": "s37_04",
                "title": "实现一个用观察者模式的日志系统：Logger 支持 add_handler 和 log，handler 收到消息后打印前缀+消息",
                "desc": "实现一个用观察者模式的日志系统：Logger 支持 add_handler 和 log，handler 收到消息后打印前缀+消息",
                "diff": "challenge",
                "kp": [
                    "pattern_observer",
                    "func_def"
                ],
                "hint": "handlers 列表，每个 handler 是 callable",
                "answer": "class Logger:\n    def __init__(self):\n        self._handlers = []\n    def add_handler(self, handler):\n        self._handlers.append(handler)\n    def log(self, message):\n        for handler in self._handlers:\n            handler(message)\n\noutput = []\nlogger = Logger()\nlogger.add_handler(lambda msg: output.append(f\"[FILE] {msg}\"))\nlogger.add_handler(lambda msg: output.append(f\"[CONSOLE] {msg}\"))\nlogger.log(\"System started\")\nlogger.log(\"Task done\")\nprint(len(output))\nprint(output[0])",
                "expected": "",
                "explain": "观察者模式日志：add_handler() 注册处理器，log() 遍历处理器分发消息。解耦日志产生和消费。",
                "template": "class Logger:\n    pass  # TODO\n    def __init__(self):\n        pass  # TODO\n        self._handlers = ...  # TODO\n    def add_handler(self, handler):\n        pass  # TODO\n    def log(self, message):\n        pass  # TODO\noutput = ...  # TODO\nlogger = ...  # TODO"
            },
            {
                "id": "s37_05",
                "title": "用栈实现括号匹配检查：输入 '((()))' 返回 True，输入 '(()' 返回 False",
                "desc": "用栈实现括号匹配检查：输入 '((()))' 返回 True，输入 '(()' 返回 False",
                "diff": "challenge",
                "kp": [
                    "algo_stack_queue",
                    "list_methods"
                ],
                "hint": "遇左括号入栈，遇右括号出栈比对，最后栈空则匹配",
                "answer": "def is_balanced(s):\n    stack = []\n    pairs = {\")\": \"(\", \"]\": \"[\", \"}\": \"{\"}\n    for ch in s:\n        if ch in \"([{\":\n            stack.append(ch)\n        elif ch in \")]}\":\n            if not stack or stack.pop() != pairs[ch]:\n                return False\n    return len(stack) == 0\n\nprint(is_balanced(\"((()))\"))\nprint(is_balanced(\"(()\"))",
                "expected": "True\nFalse",
                "explain": "栈实现括号匹配：左括号入栈，右括号弹栈匹配。栈空且字符串遍历完则匹配成功。",
                "template": "def is_balanced(s):\n    pass  # TODO\n    stack = ...  # TODO\n    pairs = ...  # TODO\n    return len(stack) = ...  # TODO"
            }
        ]
    }
