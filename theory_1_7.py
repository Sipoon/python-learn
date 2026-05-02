"""理论讲解数据 - 阶段1~7 — v3.2 大幅扩充示例与类比"""
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

# 每个阶段: (理论文本, 知识点列表)
THEORY_1_7 = {
    1: (f"""{B}阶段1：变量与数据类型{END}

{BD}一、变量 — 给数据起个名字{END}

{C_}生活类比：变量就像贴了标签的盒子{END}
    ┌──────────┐
    │ name     │ ← 标签（变量名）
    │ "张三"   │ ← 盒子里的东西（值）
    └──────────┘

    >>> name = "张三"
    >>> age = 25
    >>> height = 1.75
    >>> print(name)
    张三
    >>> print(age)
    25

{C_}命名规则：{END}
• 只能用字母、数字、下划线
• 不能以数字开头（1st → 错！first → 对）
• 区分大小写（Name 和 name 是两个不同的变量）
• 不能用 Python 关键字（if, for, class 等）
• 要有意义：user_age > x（别人看得懂！）

{BD}二、数据类型 — 盒子里装什么{END}

{C_}生活类比：不同类型的盒子装不同的东西{END}
    整数盒 → 装完整苹果（1, 2, 3）
    浮点盒 → 装切开的水果（3.14, 0.5）
    字符盒 → 装标签纸（"hello", '世界'）
    布尔盒 → 装开关（开/关）

{Y}1. 整数 int — 没有小数点的数{END}
    >>> 42
    42
    >>> -7
    -7
    >>> 0
    0
    >>> type(42)
    <class 'int'>

{Y}2. 浮点数 float — 有小数点的数{END}
    >>> 3.14
    3.14
    >>> -0.5
    -0.5
    >>> type(3.14)
    <class 'float'>
    >>> 1.0 + 2.0
    3.0    # 注意：结果是浮点数 3.0，不是整数 3

{Y}3. 字符串 str — 用引号包裹的文字{END}
    >>> "hello"
    'hello'
    >>> '世界'
    '世界'
    >>> "123"       # 这是字符串，不是数字！
    '123'
    >>> type("123")
    <class 'str'>
    >>> "你好" + "世界"    # 字符串拼接
    '你好世界'
    >>> "哈" * 3           # 字符串重复
    '哈哈哈'

{Y}4. 布尔值 bool — 只有 True 和 False{END}
    >>> True
    True
    >>> False
    False
    >>> type(True)
    <class 'bool'>
    >>> 5 > 3
    True
    >>> 5 < 3
    False

{Y}5. 空值 None — "什么都没有"{END}
    >>> x = None
    >>> print(x)
    None
    >>> type(None)
    <class 'NoneType'>

{BD}三、类型操作{END}

{C_}查看类型 type(){END}
    >>> x = 42
    >>> type(x)
    <class 'int'>
    >>> type("hello")
    <class 'str'>

{C_}类型转换 — 换个盒子装{END}
    >>> int("123")        # 字符串 → 整数
    123
    >>> float("3.14")     # 字符串 → 浮点数
    3.14
    >>> str(42)           # 整数 → 字符串
    '42'
    >>> int(3.9)          # 浮点数 → 整数（截断，不是四舍五入！）
    3
    >>> int(-3.9)         # 负数也截断
    -3

{C_}实际场景：用户输入的都是字符串，需要转换{END}
    >>> age = input("年龄：")   # 用户输入 25
    >>> type(age)
    <class 'str'>              # input() 永远返回字符串！
    >>> age = int(age)         # 转成整数才能做数学运算
    >>> age + 1
    26

{BD}四、print() 输出{END}
    >>> print("Hello")
    Hello
    >>> print(42)
    42
    >>> print("年龄:", 25)
    年龄: 25
    >>> print("不换行", end="")
    不换行>>>                    # 光标紧跟在后面

{C_}多个值一起输出{END}
    >>> name = "张三"
    >>> age = 25
    >>> print("我叫" + name + "，今年" + str(age) + "岁")  # 麻烦！
    我叫张三，今年25岁
    >>> print(f"我叫{{name}}，今年{{age}}岁")              # f-string 更方便！
    我叫张三，今年25岁

{BD}[!] 常见陷阱{END}
• = 是赋值，== 才是比较（后面会学）
• 变量名要有意义：user_age > x
• 字符串不能做数学运算："3" + 1 会报 TypeError！
• input() 返回的一定是字符串，要手动转换


{BD}三、多变量赋值技巧{END}

{C_}Python 特色：一行给多个变量赋值{END}
    >>> # 同时赋值
    >>> a, b, c = 1, 2, 3
    >>> print(a, b, c)
    1 2 3

    >>> # 交换两个变量的值（不需要临时变量！）
    >>> x, y = 10, 20
    >>> x, y = y, x
    >>> print(x, y)
    20 10

    >>> # 从列表/元组解包
    >>> first, second, third = [1, 2, 3]
    >>> print(first)
    1

    >>> # 用 * 收集剩余元素
    >>> head, *tail = [1, 2, 3, 4, 5]
    >>> print(head, tail)
    1 [2, 3, 4, 5]

{M}>> 动手试试！在代码实验室输入以下代码看结果：{END}
    x = 10
    y = 3.14
    name = "Python"
    print(type(x), type(y), type(name))
    print(int(y))
    print(str(x) + name)
""", ["var_create", "var_naming", "type_int", "type_float", "type_str", "type_bool", "type_none", "type_check", "type_convert", "print_basic"]),

    2: (f"""{B}阶段2：运算符与表达式{END}

{BD}一、算术运算符 — 数学计算{END}

{C_}生活类比：运算符就是计算器上的按钮{END}
    >>> 5 + 3
    8
    >>> 5 - 3
    2
    >>> 5 * 3
    15
    >>> 7 / 2
    3.5         # / 永远返回浮点数
    >>> 7 // 2
    3           # 整除：只要整数部分
    >>> 7 % 2
    1           # 取余：7 = 2*3 + 1
    >>> 2 ** 3
    8           # 幂运算：2的3次方

{C_}实际场景：{END}
    >>> # 判断偶数
    >>> 6 % 2 == 0
    True
    >>> 7 % 2 == 0
    False

    >>> # 计算分钟和秒
    >>> total_seconds = 135
    >>> minutes = total_seconds // 60
    >>> seconds = total_seconds % 60
    >>> print(f"{{minutes}}分{{seconds}}秒")
    2分15秒

{C_}注意：{END}
• / 永远返回浮点数：10 / 5 = 2.0
• // 向下取整：-7 // 2 = -4（不是 -3！）
• % 可判断整除：n % 2 == 0 判断偶数
• ** 右结合：2 ** 3 ** 2 = 2 ** 9 = 512

{BD}二、比较运算符 — 问"是不是"{END}
    >>> 5 == 5
    True        # 等于
    >>> 5 != 3
    True        # 不等于
    >>> 5 > 3
    True
    >>> 5 < 3
    False
    >>> 5 >= 5
    True
    >>> 5 <= 3
    False

{C_}字符串也能比较（按字典序）：{END}
    >>> "apple" < "banana"
    True
    >>> "abc" == "abc"
    True

{C_}注意：{END} == 是比较，= 是赋值，不要混淆！

{BD}三、逻辑运算符 — 组合条件{END}

{C_}生活类比：{END}
    and = "而且"（两个都要满足）
    or  = "或者"（满足一个就行）
    not = "反过来"（取反）

    >>> True and False
    False
    >>> True or False
    True
    >>> not True
    False

{C_}实际场景：{END}
    >>> age = 20
    >>> has_ticket = True
    >>> age >= 18 and has_ticket      # 两个条件都满足
    True
    >>> age < 12 or age > 65          # 满足一个
    False
    >>> not has_ticket                 # 取反
    False

{C_}短路求值（了解即可）：{END}
    >>> 0 and print("不会执行")        # 0 为假，and 直接返回，不执行后面
    0
    >>> 1 or print("不会执行")         # 1 为真，or 直接返回，不执行后面
    1

{BD}四、赋值运算符 — 快捷写法{END}
    >>> x = 10
    >>> x += 3     # x = x + 3
    >>> x
    13
    >>> x -= 5     # x = x - 5
    >>> x
    8
    >>> x *= 2     # x = x * 2
    >>> x
    16
    >>> x //= 3    # x = x // 3
    >>> x
    5

{BD}五、运算符优先级 — 谁先算？{END}
    1. **（幂）
    2. * / // %（乘除）
    3. + -（加减）
    4. == != > < >= <=（比较）
    5. not and or（逻辑）

{C_}不确定就加括号！括号永远最优先：{END}
    >>> 2 + 3 * 4      # 先乘后加
    14
    >>> (2 + 3) * 4    # 括号优先
    20

{BD}[!] 常见陷阱{END}
• = 和 == 混淆：if x = 5 会报 SyntaxError！
• 忘记括号：a > 0 and b > 0，建议写 (a > 0) and (b > 0)
• // 对负数向下取整：-7 // 2 = -4 不是 -3

{M}>> 动手试试！{END}
    seconds = 3725
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    print(f"{{hours}}小时{{minutes}}分{{secs}}秒")


{BD}六、位运算符 — 直接操作二进制{END}

{C_}生活类比：位运算就像开关灯泡{END}
    每个灯泡是一个二进制位（0=灭，1=亮）
    
    数字 5 = 二进制 101 = ○●○（三个灯泡）
    数字 3 = 二进制 011 = ●●○

{Y}1. 按位与 & — 两个都是1才是1{END}
    >>> 5 & 3          # 101 & 011
    1                  # 001（只有最低位都是1）

{Y}2. 按位或 | — 有一个1就是1{END}
    >>> 5 | 3          # 101 | 011
    7                  # 111（有三个位是1）

{Y}3. 按位异或 ^ — 相同为0，不同为1{END}
    >>> 5 ^ 3          # 101 ^ 011
    6                  # 110

{Y}4. 按位取反 ~ — 0变1，1变0{END}
    >>> ~5
    -6    # 公式：~x = -(x+1)

{Y}5. 左移 << — 乘以2的n次方{END}
    >>> 5 << 1         # 101 左移1位
    10                 # 1010 = 5*2
    >>> 5 << 2
    20                 # 10100 = 5*4

{Y}6. 右移 >> — 除以2的n次方（向下取整）{END}
    >>> 20 >> 1
    10                 # 1010 >> 1 = 101 = 10
    >>> 20 >> 2
    5                  # 10100 >> 2 = 101 = 5

{C_}实际场景：快速判断奇偶{END}
    >>> n = 7
    >>> n & 1          # 最低位是1就是奇数
    1                   # 奇数
    >>> n = 8
    >>> n & 1
    0                   # 偶数

{BD}七、运算符优先级完整表{END}

{C_}从高到低排列（同行优先级相同）：{END}
    优先级  运算符                    说明
    ─────────────────────────────────────────
    1       **                        幂运算（最高）
    2       +x, -x, ~x                正负号、按位取反
    3       *, /, //, %               乘除、整除、取余
    4       +, -                      加减
    5       <<, >>                    左移、右移
    6       &                         按位与
    7       ^                         按位异或
    8       |                         按位或
    9       ==, !=, >, <, >=, <=      比较运算
    10      not                       逻辑非
    11      and                       逻辑与
    12      or                        逻辑或（最低）

{C_}记忆口诀：{END}
    幂正负 → 乘除 → 加减 → 位移 → 位运算 → 比较 → 逻辑

{C_}不确定就加括号！{END}
    >>> 2 + 3 * 4 ** 2          # 先算 4**2，再乘3，最后加2
    50
    >>> ((2 + 3) * 4) ** 2      # 括号最优先
    400

{BD}八、链式比较 — Python 特色写法{END}

{C_}其他语言写法：{END}
    >>> x = 5
    >>> x > 0 and x < 10       # 正确但啰嗦
    True

{C_}Python 链式比较：{END}
    >>> x = 5
    >>> 0 < x < 10              # 更直观！
    True
    >>> 1 <= x <= 10            # 包含边界
    True
    >>> 0 < x < 5 < 10          # 可以连续链式
    False                       # 5 < 5 是 False

{C_}实际场景：检查年龄范围{END}
    >>> age = 25
    >>> 18 <= age <= 65         # 工作年龄
    True

{BD}九、is 和 == 的区别{END}

{C_}== 比较值，is 比较身份（内存地址）{END}
    >>> a = [1, 2, 3]
    >>> b = [1, 2, 3]
    >>> a == b          # 值相同
    True
    >>> a is b          # 不是同一个对象
    False
    >>> a is a          # 同一个对象
    True

{C_}小整数缓存（Python 优化）：{END}
    >>> x = 256
    >>> y = 256
    >>> x is y
    True              # -5 到 256 被缓存，同一对象
    >>> x = 257
    >>> y = 257
    >>> x is y
    False             # 超出缓存范围

{C_}正确用法：is 用于 None 和单例{END}
    >>> x = None
    >>> x is None     # 推荐！
    True
    >>> x == None     # 不推荐
    True

{BD}[!] 补充陷阱{END}
• 位运算优先级低于比较：a > 0 & b 要写成 a > (0 & b)
• 链式比较的每个条件都会求值（没有短路）
• is 判断 None：用 x is None，不要用 x == None

""", ["op_arithmetic", "op_compare", "op_logical", "op_assign", "op_precedence", "op_bitwise", "op_chained", "op_is_vs_eq"]),

    3: (f"""{B}阶段3：条件语句 — 让程序做选择{END}

{C_}生活类比：条件语句就是路口的选择{END}
         输入成绩
            │
      ┌──────┴──────┐
      │ 成绩 >= 60？│
      └──────┬──────┘
        Yes/    \\No
        /        \\
    "及格"     "不及格"

{BD}一、if 语句 — 如果...就...{END}
    >>> age = 20
    >>> if age >= 18:
    ...     print("你成年了")
    ...
    你成年了

{C_}注意缩进！4个空格表示"属于if的代码块"：{END}
    if 条件:
        这行缩进了 → 属于 if    ← 4个空格
        这行也缩进了 → 也属于 if
    这行没缩进 → 不属于 if

{BD}二、if-else — 如果...否则...{END}
    >>> score = 75
    >>> if score >= 60:
    ...     print("及格了！")
    ... else:
    ...     print("再接再厉！")
    ...
    及格了！

{C_}实际场景：成绩评级{END}
    >>> score = 85
    >>> if score >= 90:
    ...     grade = "A"
    ... elif score >= 80:
    ...     grade = "B"
    ... elif score >= 70:
    ...     grade = "C"
    ... elif score >= 60:
    ...     grade = "D"
    ... else:
    ...     grade = "F"
    ...
    >>> print(f"等级：{{grade}}")
    等级：B

{BD}三、if-elif-else — 多个选择{END}

{C_}elif = else if 的缩写，可以有多个：{END}
    >>> day = "周六"
    >>> if day == "周一":
    ...     print("新的一周开始了")
    ... elif day == "周五":
    ...     print("快放假了！")
    ... elif day == "周六" or day == "周日":
    ...     print("周末愉快！")
    ... else:
    ...     print("普通工作日")
    ...
    周末愉快！

{C_}实际场景：猜数字大小{END}
    >>> num = 42
    >>> guess = 50
    >>> if guess > num:
    ...     print("猜大了！")
    ... elif guess < num:
    ...     print("猜小了！")
    ... else:
    ...     print("猜对了！")
    ...
    猜大了！

{BD}四、嵌套条件 — 条件里套条件{END}
    >>> age = 20
    >>> has_id = True
    >>> if age >= 18:
    ...     if has_id:
    ...         print("可以进入")
    ...     else:
    ...         print("请出示证件")
    ... else:
    ...     print("未成年不可进入")
    ...
    可以进入

{C_}但嵌套太深不好读，可以用 and 简化：{END}
    >>> if age >= 18 and has_id:
    ...     print("可以进入")
    ...
    可以进入

{BD}五、条件表达式（三元运算符）— 一行写条件{END}
    >>> age = 20
    >>> status = "成年" if age >= 18 else "未成年"
    >>> print(status)
    成年

{C_}等价于：{END}
    if age >= 18:
        status = "成年"
    else:
        status = "未成年"

{BD}[!] 常见陷阱{END}
• 忘记冒号 `:` → SyntaxError
• 缩进不一致（Tab 和空格混用）→ IndentationError
• 用 = 代替 == 做比较 → SyntaxError（Python 保护了你！）
• elif 写成 else if → Python 里是 elif
• 条件后面别写分号

{M}>> 动手试试！{END}
    temperature = 35
    if temperature > 35:
        print("高温预警！")
    elif temperature > 28:
        print("天气炎热")
    elif temperature > 15:
        print("天气舒适")
    else:
        print("注意保暖")


{BD}六、三元表达式详解 — 一行写条件{END}

{C_}标准语法：{END}
    值1 if 条件 else 值2

{C_}执行流程：{END}
    条件为真 → 返回值1
    条件为假 → 返回值2

{Y}1. 基础用法{END}
    >>> age = 20
    >>> status = "成年" if age >= 18 else "未成年"
    >>> status
    '成年'

{Y}2. 嵌套三元（不推荐，可读性差）{END}
    >>> score = 75
    >>> grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
    >>> grade
    'C'

{C_}上面等价于（更清晰）：{END}
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"

{Y}3. 实际场景：取默认值{END}
    >>> user_input = ""
    >>> name = user_input if user_input else "匿名"
    >>> name
    '匿名'

{Y}4. 实际场景：列表推导式中使用{END}
    >>> nums = [-2, 5, -1, 8, -3]
    >>> signed = ["正" if n > 0 else "零" if n == 0 else "负" for n in nums]
    >>> signed
    ['负', '正', '负', '正', '负']

{BD}七、match-case 语句 — Python 3.10+ 模式匹配{END}

{C_}类似其他语言的 switch-case，但更强大{END}
    >>> def describe_point(point):
    ...     match point:
    ...         case (0, 0):
    ...             return "原点"
    ...         case (0, y):
    ...             return f"在Y轴上，y={{y}}"
    ...         case (x, 0):
    ...             return f"在X轴上，x={{x}}"
    ...         case (x, y):
    ...             return f"坐标({{x}}, {{y}})"
    ...
    >>> describe_point((0, 0))
    '原点'
    >>> describe_point((3, 4))
    '坐标(3, 4)'

{C_}带守卫条件：{END}
    >>> def check_number(n):
    ...     match n:
    ...         case x if x < 0:
    ...             return "负数"
    ...         case 0:
    ...             return "零"
    ...         case x if x > 0:
    ...             return "正数"
    ...
    >>> check_number(-5)
    '负数'
    >>> check_number(42)
    '正数'

{C_}匹配类型：{END}
    >>> def process(value):
    ...     match value:
    ...         case int():
    ...             return f"整数: {{value}}"
    ...         case str():
    ...             return f"字符串: {{value}}"
    ...         case list():
    ...             return f"列表，长度: {{len(value)}}"
    ...         case _:
    ...             return "未知类型"
    ...
    >>> process(42)
    '整数: 42'
    >>> process([1, 2, 3])
    '列表，长度: 3'

{C_}_ 是通配符，匹配所有剩余情况{END}

{BD}八、嵌套条件优化技巧{END}

{Y}问题：嵌套太深难阅读{END}
    if user:
        if user.is_active:
            if user.has_permission("admin"):
                return "管理员"
            else:
                return "普通用户"
        else:
            return "用户已停用"
    else:
        return "请登录"

{Y}优化1：提前返回（Guard Clause）{END}
    if not user:
        return "请登录"
    if not user.is_active:
        return "用户已停用"
    if user.has_permission("admin"):
        return "管理员"
    return "普通用户"

{Y}优化2：用 and 合并条件{END}
    if user and user.is_active and user.has_permission("admin"):
        return "管理员"

{Y}优化3：用字典映射{END}
    def get_status(user):
        if not user:
            return "请登录"
        
        permissions = {{
            "admin": "管理员",
            "editor": "编辑",
            "viewer": "查看者"
        }}
        return permissions.get(user.role, "普通用户")

{BD}九、布尔短路求值详解{END}

{C_}and 短路：遇到 False 就停{END}
    >>> def risky():
    ...     print("执行了！")
    ...     return True
    ...
    >>> False and risky()      # 不执行 risky()
    False
    >>> True and risky()       # 执行 risky()
    执行了！
    True

{C_}or 短路：遇到 True 就停{END}
    >>> True or risky()        # 不执行 risky()
    True
    >>> False or risky()       # 执行 risky()
    执行了！
    True

{C_}实际场景：安全获取字典值{END}
    >>> data = {{}}
    >>> name = data.get("name") or "默认名"
    >>> name
    '默认名'

{C_}实际场景：默认值设置{END}
    >>> user_input = ""
    >>> value = user_input or "默认值"
    >>> value
    '默认值'

{BD}[!] 补充陷阱{END}
• 三元表达式不要嵌套太多，可读性差
• match-case 需要 Python 3.10+，旧版本会报 SyntaxError
• 短路求值可以用于性能优化，但要注意副作用

""", ["if_basic", "if_else", "if_elif", "if_nested", "if_ternary", "if_match_case", "if_optimize", "if_short_circuit"]),

    4: (f"""{B}阶段4：循环 — 让程序重复做事{END}

{C_}生活类比：循环就像每天的生活{END}
    while 星期没结束:
        起床 → 上课 → 吃饭 → 睡觉

    for 每道菜 in 一桌菜:
        吃一口

{BD}一、while 循环 — 当...就继续{END}
    >>> count = 0
    >>> while count < 5:
    ...     print(f"第{{count}}次")
    ...     count += 1
    ...
    第0次
    第1次
    第2次
    第3次
    第4次

{C_}实际场景：猜数字游戏{END}
    >>> secret = 42
    >>> guess = 0
    >>> while guess != secret:
    ...     guess = int(input("猜猜看："))
    ...     if guess > secret:
    ...         print("大了！")
    ...     elif guess < secret:
    ...         print("小了！")
    ... print("恭喜猜对！")

{BD}二、for 循环 — 遍历每个元素{END}
    >>> fruits = ["苹果", "香蕉", "橙子"]
    >>> for fruit in fruits:
    ...     print(f"我喜欢{{fruit}}")
    ...
    我喜欢苹果
    我喜欢香蕉
    我喜欢橙子

{C_}实际场景：求1到100的和{END}
    >>> total = 0
    >>> for i in range(1, 101):
    ...     total += i
    ...
    >>> print(f"1+2+...+100 = {{total}}")
    1+2+...+100 = 5050

{BD}三、range() 函数 — 生成数字序列{END}

{C_}range 就像一把尺子：{END}
    range(5)         → 0, 1, 2, 3, 4      （从0开始，不到5）
    range(1, 6)      → 1, 2, 3, 4, 5      （从1开始，不到6）
    range(0, 10, 2)  → 0, 2, 4, 6, 8      （步长2）
    range(5, 0, -1)  → 5, 4, 3, 2, 1      （倒着数）

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 6))
    [1, 2, 3, 4, 5]
    >>> list(range(0, 10, 2))
    [0, 2, 4, 6, 8]

{BD}四、break 和 continue — 控制循环{END}

{C_}break = 紧急出口（直接跳出整个循环）{END}
    >>> for i in range(10):
    ...     if i == 5:
    ...         break        # 到5就停
    ...     print(i, end=" ")
    ...
    0 1 2 3 4

{C_}continue = 跳过这次（继续下一次）{END}
    >>> for i in range(6):
    ...     if i == 3:
    ...         continue     # 跳过3
    ...     print(i, end=" ")
    ...
    0 1 2 4 5

{C_}实际场景：找第一个能被7整除的数{END}
    >>> for i in range(1, 100):
    ...     if i % 7 == 0:
    ...         print(f"找到了：{{i}}")
    ...         break
    ...
    找到了：7

{C_}实际场景：只打印奇数{END}
    >>> for i in range(10):
    ...     if i % 2 == 0:
    ...         continue     # 跳过偶数
    ...     print(i, end=" ")
    ...
    1 3 5 7 9

{BD}五、嵌套循环 — 循环里套循环{END}

{C_}经典例子：九九乘法表{END}
    >>> for i in range(1, 10):
    ...     for j in range(1, i+1):
    ...         print(f"{{j}}x{{i}}={{i*j}}", end=" ")
    ...     print()    # 换行
    ...
    1x1=1
    1x2=2 2x2=4
    1x3=3 2x3=6 3x3=9
    ...（省略）

{C_}实际场景：画直角三角形{END}
    >>> for i in range(1, 6):
    ...     print("*" * i)
    ...
    *
    **
    ***
    ****
    *****

{C_}实际场景：找100以内的素数{END}
    >>> for n in range(2, 101):
    ...     is_prime = True
    ...     for i in range(2, n):
    ...         if n % i == 0:
    ...             is_prime = False
    ...             break
    ...     if is_prime:
    ...         print(n, end=" ")
    ...
    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

{BD}六、while vs for 怎么选？{END}
    • 知道循环几次 → 用 for
    • 不知道几次，直到某条件才停 → 用 while
    • 大多数情况 for 更安全（不容易死循环）

{BD}[!] 常见陷阱{END}
• 死循环：while True 忘记 break
• 修改循环变量导致无限循环
• for 循环中修改列表导致跳过元素
• range(n) 是 0 到 n-1，不包含 n！

{M}>> 动手试试！{END}
    # 画一个倒三角
    for i in range(5, 0, -1):
        print("*" * i)
""", ["while_loop", "for_loop", "range_func", "break_continue", "nested_loop"]),

    5: (f"""{B}阶段5：函数 — 把代码打包复用{END}

{C_}生活类比：函数就像菜谱{END}
    ┌─────────────────┐
    │ 菜谱：炒鸡蛋    │ ← 函数名
    │ 材料：鸡蛋x2, 盐│ ← 参数
    │ 步骤：打蛋→搅拌 │ ← 函数体
    │ 成品：一盘炒蛋  │ ← 返回值
    └─────────────────┘

{BD}一、定义函数{END}
    >>> def greet(name):
    ...     \"\"\"向某人问好\"\"\"         # 文档字符串
    ...     return f"你好，{{name}}！"
    ...
    >>> greet("张三")
    '你好，张三！'

{C_}函数的四个部分：{END}
    def 函数名(参数1, 参数2):    ← 定义
        \"\"\"文档字符串\"\"\"           ← 说明（可选但推荐）
        函数体                        ← 做什么
        return 返回值                 ← 结果

{BD}二、return — 函数的产出{END}
    >>> def add(a, b):
    ...     return a + b
    ...
    >>> result = add(3, 5)
    >>> print(result)
    8

{C_}return 后函数立即结束：{END}
    >>> def check_age(age):
    ...     if age < 0:
    ...         return "年龄无效"
    ...     if age >= 18:
    ...         return "成年"
    ...     return "未成年"
    ...
    >>> check_age(20)
    '成年'

{C_}可以返回多个值（实际是元组）：{END}
    >>> def divide(a, b):
    ...     quotient = a // b
    ...     remainder = a % b
    ...     return quotient, remainder
    ...
    >>> q, r = divide(17, 5)
    >>> print(f"商={{q}}，余={{r}}")
    商=3，余=2

{C_}没有 return 则返回 None：{END}
    >>> def say_hi():
    ...     print("Hi!")
    ...
    >>> result = say_hi()
    Hi!
    >>> print(result)
    None

{BD}三、参数类型{END}

{Y}1. 位置参数 — 按顺序传{END}
    >>> def power(base, exp):
    ...     return base ** exp
    ...
    >>> power(2, 3)      # 2是base，3是exp
    8

{Y}2. 关键字参数 — 按名字传（不怕顺序）{END}
    >>> power(exp=3, base=2)    # 名字指定，顺序随意
    8

{Y}3. 默认参数 — 不传就用默认值{END}
    >>> def greet(name, msg="你好"):
    ...     return f"{{msg}}，{{name}}！"
    ...
    >>> greet("张三")
    '你好，张三！'
    >>> greet("张三", "欢迎")
    '欢迎，张三！'

{BD}四、*args 和 **kwargs — 灵活参数（进阶）{END}

{C_}*args：接收任意数量的位置参数{END}
    >>> def total(*numbers):
    ...     return sum(numbers)
    ...
    >>> total(1, 2, 3)
    6
    >>> total(1, 2, 3, 4, 5)
    15

{C_}**kwargs：接收任意数量的关键字参数{END}
    >>> def show_info(**info):
    ...     for key, value in info.items():
    ...         print(f"{{key}}: {{value}}")
    ...
    >>> show_info(name="张三", age=25, city="上海")
    name: 张三
    age: 25
    city: 上海

{BD}五、lambda — 匿名函数（一句话函数）{END}
    >>> double = lambda x: x * 2
    >>> double(5)
    10
    >>> add = lambda a, b: a + b
    >>> add(3, 4)
    7

{C_}常和 map/filter 一起用：{END}
    >>> nums = [1, 2, 3, 4, 5]
    >>> list(map(lambda x: x ** 2, nums))     # 每个元素平方
    [1, 4, 9, 16, 25]
    >>> list(filter(lambda x: x > 3, nums))   # 过滤出大于3的
    [4, 5]

{BD}六、变量作用域 — 变量在哪里能用{END}

{C_}生活类比：全局变量是大喇叭（谁都能听到），局部变量是耳语（只有内部听得到）{END}
    x = 10              # 全局变量（大喇叭）
    def func():
        y = 20          # 局部变量（耳语）
        print(x)        # 可以读全局变量
        print(y)        # 可以读局部变量

    func()              # 输出 10 和 20
    print(x)            # 可以访问 → 10
    # print(y)          # 报错！y 是局部的，外面看不到

{C_}在函数内修改全局变量需要 global：{END}
    >>> count = 0
    >>> def increment():
    ...     global count     # 声明我要改全局变量
    ...     count += 1
    ...
    >>> increment()
    >>> print(count)
    1

{BD}[!] 常见陷阱{END}
• 可变默认参数：def f(x=[]) 会共享同一个列表！用 None 代替
  >>> def add_item(item, lst=None):
  ...     if lst is None:
  ...         lst = []
  ...     lst.append(item)
  ...     return lst
  ...
  >>> add_item(1)
  [1]
  >>> add_item(2)       # 如果用 lst=[]，这里会得到 [1, 2]！
  [2]

• 忘记 return：函数默认返回 None
• 在函数内修改全局变量需要 global 声明
• lambda 只能写一个表达式，不能写多行

{M}>> 动手试试！{END}
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    for i in range(10):
        print(fibonacci(i), end=" ")
""", ["func_def", "func_return", "func_params", "func_default", "func_docstring", "func_args_kwargs", "func_lambda", "func_scope"]),

    6: (f"""{B}阶段6：列表 — 有序的数据队列{END}

{C_}生活类比：列表就像排队{END}
    位置:  0     1     2     3
         ┌─────┬─────┬─────┬─────┐
         │苹果 │香蕉 │橙子 │葡萄 │
         └─────┴─────┴─────┴─────┘
    反向: -4    -3    -2    -1

{BD}一、创建{END}
    >>> fruits = ["苹果", "香蕉", "橙子"]
    >>> numbers = [1, 2, 3, 4, 5]
    >>> empty = []
    >>> mixed = [1, "hello", True, 3.14]    # 可以混合类型

{BD}二、索引和切片 — 取出想要的{END}
    >>> fruits = ["苹果", "香蕉", "橙子", "葡萄"]
    >>> fruits[0]       # 第一个
    '苹果'
    >>> fruits[-1]      # 最后一个
    '葡萄'
    >>> fruits[1:3]     # 第1到第2个（不含3）
    ['香蕉', '橙子']
    >>> fruits[:2]      # 从头到第2个
    ['苹果', '香蕉']
    >>> fruits[1:]      # 从第1个到末尾
    ['香蕉', '橙子', '葡萄']
    >>> fruits[::2]     # 每隔一个取
    ['苹果', '橙子']
    >>> fruits[::-1]    # 反转
    ['葡萄', '橙子', '香蕉', '苹果']

{BD}三、常用方法{END}
    >>> fruits = ["苹果", "香蕉"]
    >>> fruits.append("橙子")       # 末尾添加
    >>> fruits
    ['苹果', '香蕉', '橙子']

    >>> fruits.insert(1, "西瓜")    # 在位置1插入
    >>> fruits
    ['苹果', '西瓜', '香蕉', '橙子']

    >>> fruits.remove("西瓜")       # 删除指定元素
    >>> fruits
    ['苹果', '香蕉', '橙子']

    >>> last = fruits.pop()         # 删除并返回最后一个
    >>> last
    '橙子'
    >>> fruits
    ['苹果', '香蕉']

    >>> nums = [3, 1, 4, 1, 5]
    >>> nums.sort()                 # 排序（原地修改）
    >>> nums
    [1, 1, 3, 4, 5]

    >>> nums.reverse()              # 反转
    >>> nums
    [5, 4, 3, 1, 1]

{C_}注意：sort() 和 reverse() 返回 None！不是新列表！{END}
    >>> nums = [3, 1, 4]
    >>> result = nums.sort()
    >>> print(result)              # None！不是排序后的列表
    None
    >>> sorted(nums)               # 这个才返回新列表
    [1, 3, 4]

{BD}四、遍历{END}
    >>> fruits = ["苹果", "香蕉", "橙子"]
    >>> for fruit in fruits:
    ...     print(fruit)
    ...
    苹果
    香蕉
    橙子

{C_}同时获取索引和值：{END}
    >>> for i, fruit in enumerate(fruits):
    ...     print(f"第{{i}}个：{{fruit}}")
    ...
    第0个：苹果
    第1个：香蕉
    第2个：橙子

{BD}五、列表推导式 — 一行创建列表{END}

{C_}普通写法 vs 推导式：{END}
    # 普通：1到10的平方
    squares = []
    for x in range(1, 11):
        squares.append(x ** 2)

    # 推导式：一行搞定
    >>> squares = [x ** 2 for x in range(1, 11)]
    >>> squares
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

{C_}带条件过滤：{END}
    >>> evens = [x for x in range(10) if x % 2 == 0]
    >>> evens
    [0, 2, 4, 6, 8]

{C_}实际场景：提取名字首字母{END}
    >>> names = ["Alice", "Bob", "Charlie"]
    >>> initials = [name[0] for name in names]
    >>> initials
    ['A', 'B', 'C']

{BD}六、列表的拷贝{END}
    >>> a = [1, 2, 3]
    >>> b = a           # 这不是拷贝！b 和 a 指向同一个列表
    >>> b[0] = 99
    >>> a               # a 也变了！
    [99, 2, 3]

    >>> c = a.copy()    # 这才是真正的拷贝
    >>> c[0] = 1
    >>> a               # a 不受影响
    [99, 2, 3]

{BD}[!] 常见陷阱{END}
• 遍历时删除元素会跳过：用列表推导式或 copy
• 列表赋值是引用不是拷贝：用 .copy() 或 list()
• sort() 返回 None，不是排序后的列表
• 索引越界：list[5] 当列表只有3个元素时


{C_}常用方法速查：{END}
    append(x)    # 末尾添加
    insert(i, x) # 指定位置插入
    pop()        # 弹出末尾元素
    remove(x)    # 删除第一个匹配值
    count(x)     # 统计出现次数
    extend(lst)  # 合并另一个列表

{M}>> 动手试试！{END}
    words = ["hello", "world", "python", "is", "great"]
    long_words = [w for w in words if len(w) > 4]
    print(long_words)
    print(sorted(words))
    print(words[::-1])
""", ["list_create", "list_index", "list_methods", "list_iter", "list_comprehension"]),

    7: (f"""{B}阶段7：元组 — 不可变的列表{END}

{C_}生活类比：元组就像刻在石头上的名单，写定了就不能改{END}
    列表 = 白板（能擦能改）
    元组 = 石碑（刻上去就定了）

{BD}一、创建{END}
    >>> point = (3, 4)
    >>> rgb = (255, 128, 0)
    >>> single = (1,)        # 单元素必须加逗号！
    >>> empty = ()
    >>> type(point)
    <class 'tuple'>

{C_}为什么要加逗号？{END}
    >>> x = (1)       # 这只是数字1，不是元组！
    >>> type(x)
    <class 'int'>
    >>> y = (1,)      # 这才是单元素元组
    >>> type(y)
    <class 'tuple'>

{BD}二、不可变 — 这是元组的核心特点{END}
    >>> t = (1, 2, 3)
    >>> t[0] = 99
    TypeError: 'tuple' object does not support item assignment

{C_}但元组里的列表是可变的：{END}
    >>> t = (1, [2, 3], 4)
    >>> t[1].append(5)       # 可以改列表内容
    >>> t
    (1, [2, 3, 5], 4)
    # 元组"指向"没变，只是列表内部变了

{BD}三、元组解包 — 一次取出多个值{END}
    >>> point = (3, 4)
    >>> x, y = point          # 一一对应
    >>> print(x, y)
    3 4

{C_}交换变量（Python 特色写法）：{END}
    >>> a, b = 1, 2
    >>> a, b = b, a          # 一行交换！
    >>> print(a, b)
    2 1

{C_}实际场景：函数返回多个值{END}
    >>> def min_max(numbers):
    ...     return min(numbers), max(numbers)
    ...
    >>> low, high = min_max([3, 1, 4, 1, 5, 9])
    >>> print(f"最小={{low}}，最大={{high}}")
    最小=1，最大=9

{C_}用 * 收集多余元素：{END}
    >>> first, *rest = (1, 2, 3, 4, 5)
    >>> first
    1
    >>> rest
    [2, 3, 4, 5]

{BD}四、为什么要用元组？{END}
• 不可变 = 更安全（不会意外修改）
• 可以作为字典的键（列表不行）
• 函数返回多个值时自动是元组
• 性能比列表略好（创建和访问更快）

{BD}五、常用操作{END}
    >>> t = (1, 2, 3, 2, 2)
    >>> len(t)
    5
    >>> t.count(2)
    3
    >>> t.index(3)
    2
    >>> 3 in t
    True
    >>> 2 in t
    True

{C_}元组也支持切片（返回新元组）：{END}
    >>> t = (0, 1, 2, 3, 4)
    >>> t[1:4]
    (1, 2, 3)

{BD}[!] 常见陷阱{END}
• 单元素元组忘加逗号：(1) 是整数不是元组，(1,) 才是
• 元组不可变，不能 append/remove
• 元组里的列表是可变的：t = ([1,2],) 里 t[0].append(3) 可以

{M}>> 动手试试！{END}
    # 元组解包实战
    student = ("张三", 20, 85.5)
    name, age, score = student
    print(f"{{name}}，{{age}}岁，成绩{{score}}")

    # 交换变量
    a, b = 100, 200
    a, b = b, a
    print(f"a={{a}}, b={{b}}")


{BD}六、元组 vs 列表对比{END}

{C_}核心区别：{END}
    特性          列表              元组
    ─────────────────────────────────────
    可变性        可变              不可变
    符号          [1, 2, 3]         (1, 2, 3)
    作为字典键    不能             可以
    性能          稍慢              稍快
    方法          多（9个）         少（2个）
    内存占用      较大              较小

{Y}选择建议：{END}
• 数据不会变 → 用元组（如坐标、RGB颜色）
• 需要增删改 → 用列表（如待办事项）
• 函数返回多个值 → 用元组（约定俗成）
• 需要作为字典键 → 必须用元组

{C_}性能对比：{END}
    >>> import sys
    >>> lst = [1, 2, 3, 4, 5]
    >>> tpl = (1, 2, 3, 4, 5)
    >>> sys.getsizeof(lst)
    104        # 字节
    >>> sys.getsizeof(tpl)
    80         # 更小

{BD}七、命名元组 namedtuple{END}

{C_}普通元组的问题：记不住位置含义{END}
    >>> point = (3, 4)
    >>> point[0]    # 这是x还是y？
    3

{C_}命名元组：给位置起名字{END}
    >>> from collections import namedtuple
    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> p = Point(3, 4)
    >>> p.x
    3
    >>> p.y
    4
    >>> p[0]        # 仍然可以用索引
    3
    >>> p
    Point(x=3, y=4)

{Y}实际场景：表示学生信息{END}
    >>> Student = namedtuple('Student', ['name', 'age', 'score'])
    >>> s = Student('张三', 20, 85.5)
    >>> s.name
    '张三'
    >>> f"{{s.name}}，{{s.age}}岁，成绩{{s.score}}"
    '张三，20岁，成绩85.5'

{Y}转换为字典：{END}
    >>> s._asdict()
    {{'name': '张三', 'age': 20, 'score': 85.5}}

{C_}命名元组仍然不可变：{END}
    >>> s.name = "李四"
    AttributeError: can't set attribute

{BD}八、元组作为字典键{END}

{C_}列表不能作为键（可变）：{END}
    >>> d = {{}}
    >>> key = [1, 2, 3]
    >>> d[key] = "value"
    TypeError: unhashable type: 'list'

{C_}元组可以作为键（不可变）：{END}
    >>> d = {{}}
    >>> key = (1, 2, 3)
    >>> d[key] = "value"
    >>> d
    {{(1, 2, 3): 'value'}}
    >>> d[(1, 2, 3)]
    'value'

{Y}实际场景：棋盘坐标{END}
    >>> board = {{}}
    >>> board[(0, 0)] = "车"
    >>> board[(0, 1)] = "马"
    >>> board[(7, 7)] = "将"
    >>> board.get((0, 0))
    '车'

{Y}实际场景：稀疏矩阵{END}
    >>> matrix = {{}}    # 只存非零元素
    >>> matrix[(0, 0)] = 1
    >>> matrix[(1, 1)] = 2
    >>> matrix[(2, 2)] = 3
    >>> matrix.get((5, 5), 0)    # 没存的位置返回0
    0

{C_}注意：元组内的元素也必须是不可变类型{END}
    >>> d = {{}}
    >>> key = ([1, 2], 3)     # 包含列表
    >>> d[key] = "value"
    TypeError: unhashable type: 'list'

{BD}九、元组方法详解{END}

{Y}count() — 统计元素出现次数{END}
    >>> t = (1, 2, 3, 2, 2, 4, 2)
    >>> t.count(2)
    4
    >>> t.count(5)    # 不存在返回0
    0

{Y}index() — 找元素第一次出现的位置{END}
    >>> t = ('a', 'b', 'c', 'b', 'd')
    >>> t.index('b')
    1
    >>> t.index('b', 2)    # 从位置2开始找
    3
    >>> t.index('x')       # 不存在会报错
    ValueError: tuple.index(x): x not in tuple

{C_}安全查找（避免报错）：{END}
    >>> def safe_index(t, value):
    ...     try:
    ...         return t.index(value)
    ...     except ValueError:
    ...         return -1
    ...
    >>> safe_index(t, 'x')
    -1

{Y}len()、in、切片等通用操作{END}
    >>> t = (1, 2, 3, 4, 5)
    >>> len(t)
    5
    >>> 3 in t
    True
    >>> 10 in t
    False
    >>> t[1:4]
    (2, 3, 4)
    >>> min(t), max(t), sum(t)
    (1, 5, 15)

{BD}十、元组的其他用途{END}

{Y}1. 函数返回多个值{END}
    >>> def stats(numbers):
    ...     return min(numbers), max(numbers), sum(numbers)
    ...
    >>> low, high, total = stats([1, 2, 3, 4, 5])
    >>> print(f"最小={{low}}，最大={{high}}，总和={{total}}")
    最小=1，最大=5，总和=15

{Y}2. 格式化字符串 % 格式{END}
    >>> "%s 今年 %d 岁" % ("张三", 25)
    '张三 今年 25 岁'

{Y}3. 不可变配置{END}
    >>> CONFIG = ('localhost', 8080, 'debug')
    >>> # 配置不会意外被修改

{BD}[!] 补充陷阱{END}
• namedtuple 的名字用下划线开头的方法（如 _asdict）
• 元组做字典键时，内部不能有列表
• index() 找不到元素会抛异常，要处理
• 单元素元组必须加逗号：(1,) 不是 (1)

""", ["tuple_create", "tuple_unpack", "tuple_immutable", "tuple_vs_list", "tuple_namedtuple", "tuple_as_key", "tuple_methods"]),
}
