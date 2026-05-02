"""UI 辅助 - 颜色、显示、吉祥物 — v5.0 六大篇章"""
import os
import sys


# Windows 控制台 UTF-8
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass


class C:
    """ANSI 颜色常量"""
    G = '\033[92m'   # 绿
    Y = '\033[93m'   # 黄
    R = '\033[91m'   # 红
    B = '\033[94m'   # 蓝
    C = '\033[96m'   # 青
    M = '\033[95m'   # 紫
    BD = '\033[1m'   # 粗体
    DIM = '\033[2m'  # 暗淡
    END = '\033[0m'


def clear():
    os.system('cls' if sys.platform == 'win32' else 'clear')


def pause(msg="按 Enter 继续...") -> str:
    """
    返回 "continue" 或 "back"。
    msg 支持两种形式：
      - "按 Enter 继续..."          → 只显示继续提示
      - "按 Enter 继续 / b 返回..."  → 显示继续+返回两个选项
    """
    if " / " in msg:
        prompt = msg
    else:
        prompt = f"{msg}  [{C.Y}b{C.END} 返回]"
    try:
        ans = input(f"{C.C}{prompt}{C.END}").strip().lower()
    except EOFError:
        ans = ""
    if ans in ("b", "back"):
        print(f"{C.DIM}← 返回主菜单{C.END}")
        return "back"
    return "continue"


def show_banner():
    print(f"""{C.BD}{C.C}
    +==========================================+
    |                                          |
    |     Python 互动学习系统 v5.0             |
    |                                          |
    |     六大篇章 | 真实执行 | 趣味闯关       |
    |                                          |
    +==========================================+{C.END}
""")


def print_banner(title: str):
    print(f"\n{C.BD}{C.C}{'='*50}{C.END}")
    print(f"{C.BD}{C.C}  {title}{C.END}")
    print(f"{C.BD}{C.C}{'='*50}{C.END}\n")


def show_snake(mood: str = "happy"):
    if mood == "happy":
        print(f"{C.G}")
        print("    +------+") 
        print("    | ^  ^ |  太棒了！")
        print("    +------+") 
        print(f"{C.END}")
    elif mood == "think":
        print(f"{C.Y}")
        print("    +------+") 
        print("    | -  - |  思考中...") 
        print("    +------+") 
        print(f"{C.END}")
    elif mood == "sad":
        print(f"{C.R}")
        print("    +------+") 
        print("    | T  T |  再试一次！") 
        print("    +------+") 
        print(f"{C.END}")
    elif mood == "celebrate":
        print(f"{C.Y}")
        print("    * * * * * *") 
        print("    恭喜完成！")
        print(f"{C.END}")


def read_multiline() -> str:
    """读取多行代码输入，空行结束"""
    lines = []
    print(f"{C.DIM}（输入代码，单独一行空行结束）{C.END}")
    while True:
        try:
            line = input(f"{C.Y}  {C.END}")
        except EOFError:
            break
        if line == "" and lines:
            break
        lines.append(line)
    return "\n".join(lines)


# ===================== 篇章定义 =====================

CHAPTERS = [
    ("第一篇", "Python基础",   1, 13),
    ("第二篇", "Python进阶",  14, 18),
    ("第三篇", "工程基础",    19, 21),
    ("第四篇", "数据方向",    22, 29),
    ("第五篇", "自动化与桌面", 30, 33),
    ("第六篇", "架构与算法",  34, 37),
]


# 知识点定义（阶段, 名称）— v5.0 重构
KNOWLEDGE = {
    # ===== 第一篇：Python基础 =====
    "var_create": (1, "变量创建与赋值"),
    "var_naming": (1, "变量命名规则"),
    "type_int": (1, "整数 int"),
    "type_float": (1, "浮点数 float"),
    "type_str": (1, "字符串 str"),
    "type_bool": (1, "布尔值 bool"),
    "type_none": (1, "空值 None"),
    "type_check": (1, "type() 查看类型"),
    "type_convert": (1, "类型转换"),
    "print_basic": (1, "print() 输出"),
    "op_arithmetic": (2, "算术运算符"),
    "op_compare": (2, "比较运算符"),
    "op_logical": (2, "逻辑运算符"),
    "op_assign": (2, "赋值运算符"),
    "op_precedence": (2, "运算符优先级"),
    "if_basic": (3, "if 语句"),
    "if_else": (3, "if-else 语句"),
    "if_elif": (3, "if-elif-else 语句"),
    "if_nested": (3, "嵌套条件"),
    "while_loop": (4, "while 循环"),
    "for_loop": (4, "for 循环"),
    "range_func": (4, "range() 函数"),
    "break_continue": (4, "break 和 continue"),
    "nested_loop": (4, "嵌套循环"),
    "func_def": (5, "函数定义 def"),
    "func_return": (5, "return 返回值"),
    "func_params": (5, "函数参数"),
    "func_default": (5, "默认参数"),
    "func_docstring": (5, "文档字符串"),
    "func_args_kwargs": (5, "*args 和 **kwargs"),
    "func_lambda": (5, "lambda 匿名函数"),
    "func_scope": (5, "变量作用域"),
    "list_create": (6, "列表创建 []"),
    "list_index": (6, "列表索引和切片"),
    "list_methods": (6, "列表方法"),
    "list_iter": (6, "遍历列表"),
    "list_comprehension": (6, "列表推导式"),
    "tuple_create": (7, "元组创建 ()"),
    "tuple_unpack": (7, "元组解包"),
    "tuple_immutable": (7, "元组不可变"),
    "dict_create": (8, "字典创建 {}"),
    "dict_access": (8, "字典访问"),
    "dict_methods": (8, "字典方法"),
    "dict_update": (8, "字典修改和删除"),
    "set_create": (9, "集合创建 set()"),
    "set_ops": (9, "集合运算 交集/并集/差集"),
    "set_methods": (9, "集合方法 add/remove"),
    "str_methods": (10, "字符串方法"),
    "str_format": (10, "字符串格式化 f-string"),
    "str_find": (10, "字符串查找"),
    "str_check": (10, "字符串判断 isdigit/isalpha"),
    # str_regex REMOVED from S10 — unified in S14
    "file_open": (11, "打开文件 open()"),
    "file_read": (11, "读取文件"),
    "file_write": (11, "写入文件"),
    "file_context": (11, "with 语句"),
    "file_csv": (11, "CSV 文件处理"),
    "file_json": (11, "JSON 文件处理"),
    "try_except": (12, "try-except 捕获异常"),
    "exception_types": (12, "常见异常类型"),
    "raise_error": (12, "raise 抛出异常"),
    "custom_exception": (12, "自定义异常"),
    "import_module": (13, "导入模块 import"),
    "json_io": (13, "JSON 读写"),
    "datetime_mod": (13, "datetime 模块"),
    "os_module": (13, "os 模块"),
    # ===== 第二篇：Python进阶 =====
    "regex_basic": (14, "re 模块基础"),
    "regex_meta": (14, "正则元字符"),
    "regex_quantifier": (14, "量词 *+?{n,m}"),
    "regex_charset": (14, "字符类 \\d\\w\\s"),
    "regex_group": (14, "分组和或"),
    "regex_sub": (14, "re.sub 替换"),
    "regex_compile": (14, "re.compile 编译"),
    "regex_practice": (14, "正则实战"),
    "oop_class_object": (15, "类和对象"),
    "oop_init_self": (15, "__init__ 和 self"),
    "oop_inheritance": (15, "继承"),
    "oop_polymorphism": (15, "多态"),
    "oop_encapsulation": (15, "封装"),
    "oop_super": (15, "super() 调用父类"),
    "oop_property": (15, "@property 属性装饰器"),
    "oop_magic_method": (16, "魔术方法 __str__ __add__"),
    "oop_classmethod": (16, "@classmethod 类方法"),
    "oop_staticmethod": (16, "@staticmethod 静态方法"),
    "oop_abstract": (16, "抽象类 ABC"),
    "oop_composition": (16, "组合 vs 继承"),
    "mod_import": (17, "import 导入方式"),
    "mod_name_main": (17, "__name__ == '__main__'"),
    "mod_package": (17, "包和 __init__.py"),
    "mod_pip": (17, "pip 包管理器"),
    "mod_venv": (17, "虚拟环境 venv"),
    "mod_stdlib": (17, "常用标准库"),
    "gen_yield": (18, "yield 生成器"),
    "gen_expression": (18, "生成器表达式"),
    "dec_basic": (18, "装饰器基础"),
    "dec_args": (18, "带参数的装饰器"),
    "dec_wraps": (18, "functools.wraps"),
    "ctx_manager": (18, "上下文管理器 with"),
    # ===== 第三篇：工程基础 =====
    "db_sqlite": (19, "SQLite 进阶"),
    "db_mysql": (19, "MySQL 连接"),
    "db_sqlalchemy": (19, "SQLAlchemy ORM"),
    "db_transaction": (19, "数据库事务"),
    "test_unittest": (20, "unittest 标准库"),
    "test_pytest": (20, "pytest 框架"),
    "test_fixture": (20, "pytest fixture"),
    "test_parametrize": (20, "参数化测试"),
    "test_logging": (20, "logging 日志"),
    "test_exception": (20, "异常测试"),
    "api_fastapi": (21, "FastAPI 框架"),
    "api_route": (21, "路由与HTTP方法"),
    "api_params": (21, "路径/查询参数"),
    "api_pydantic": (21, "Pydantic 数据验证"),
    "api_crud": (21, "CRUD 接口"),
    "api_jwt": (21, "JWT 认证"),
    # ===== 第四篇：数据方向 =====
    "crawl_requests": (22, "requests HTTP请求"),
    "crawl_beautifulsoup": (22, "BeautifulSoup 解析"),
    "crawl_selectors": (22, "CSS 选择器"),
    "crawl_ethics": (22, "爬虫礼仪"),
    "crawl_save": (22, "数据保存 JSON/CSV"),
    "pandas_dataframe": (23, "DataFrame 数据框"),
    "pandas_select": (23, "数据选择和筛选"),
    "pandas_process": (23, "数据处理 groupby/sort"),
    "pandas_io": (23, "pandas 读写文件"),
    "csv_advanced": (23, "CSV 进阶 DictReader"),
    "json_advanced": (23, "JSON 进阶"),
    "viz_line": (24, "折线图 plt.plot"),
    "viz_bar": (24, "柱状图 plt.bar"),
    "viz_pie": (24, "饼图 plt.pie"),
    "viz_scatter": (24, "散点图 plt.scatter"),
    "viz_subplots": (24, "子图 plt.subplots"),
    "viz_style": (24, "样式美化"),
    "viz_pandas": (24, "pandas 绑图"),
    # S25: 浏览器自动化与爬虫进阶（合并旧S24浏览器+旧S26）
    "crawl_selenium": (25, "Selenium 动态页面"),
    "crawl_playwright": (25, "Playwright 浏览器自动化"),
    "crawl_session": (25, "Session 登录态"),
    "crawl_anti": (25, "反爬策略 UA/延时/代理"),
    "crawl_proxy": (25, "代理池"),
    "crawl_wait": (25, "显式等待"),
    "crawl_headless": (25, "无头模式"),
    "crawl_best_practice": (25, "爬虫最佳实践"),
    "async_def": (26, "async/await 协程"),
    "async_await": (26, "await 等待"),
    "async_gather": (26, "asyncio.gather 并发"),
    "async_aiohttp": (26, "aiohttp 异步HTTP"),
    "async_semaphore": (26, "Semaphore 并发控制"),
    "crawl_scrapy": (27, "Scrapy 框架"),
    "crawl_concurrent": (27, "多线程/多进程爬虫"),
    "crawl_incremental": (27, "增量爬取"),
    "crawl_mysql": (28, "MySQL 存储"),
    "crawl_redis": (28, "Redis 缓存与去重"),
    "crawl_logging": (28, "日志与监控"),
    "data_pipeline": (29, "数据流水线"),
    "data_cleaning": (29, "数据清洗"),
    "data_automation": (29, "自动化数据分析"),
    "project_crawl_analyze": (29, "爬取->分析项目"),
    "project_weather": (29, "天气数据分析"),
    "project_account_oop": (29, "OOP记账本"),
    # ===== 第五篇：自动化与桌面 =====
    "auto_os": (30, "os 文件目录操作"),
    "auto_pathlib": (30, "pathlib 路径操作"),
    "auto_shutil": (30, "shutil 批量文件"),
    "auto_batch_rename": (30, "批量重命名"),
    "auto_organize": (30, "自动整理文件"),
    "auto_backup": (30, "自动备份"),
    "auto_subprocess": (30, "subprocess 调用命令"),
    "auto_schedule": (30, "schedule 定时任务"),
    "auto_pyautogui": (31, "pyautogui 桌面自动化"),
    "auto_clipboard": (31, "剪贴板操作"),
    "auto_screenshot": (31, "截图与图像识别"),
    "auto_keyboard": (31, "键盘自动化"),
    "auto_desktop_best": (31, "桌面自动化最佳实践"),
    "gui_tkinter": (32, "tkinter 入门"),
    "gui_widget": (32, "常用组件"),
    "gui_layout": (32, "布局管理"),
    "gui_event": (32, "事件驱动"),
    "gui_menu": (32, "菜单栏"),
    "project_file_manager": (33, "智能文件管理器"),
    "project_daily_report": (33, "日报生成器"),
    "project_web_monitor": (33, "网页监控机器人"),
    "auto_integration": (33, "自动化集成项目"),
    # ===== 第六篇：架构与算法 =====
    "pattern_singleton": (34, "单例模式"),
    "pattern_factory": (34, "工厂模式"),
    "pattern_strategy": (34, "策略模式"),
    "pattern_observer": (34, "观察者模式"),
    "pattern_decorator": (34, "装饰器模式"),
    "algo_bigo": (35, "时间复杂度 Big O"),
    "algo_sort_basic": (35, "冒泡/选择/插入排序"),
    "algo_sort_adv": (35, "归并/快速排序"),
    "algo_search": (35, "线性搜索/二分查找"),
    "algo_recursive": (35, "递归思想"),
    "algo_dp": (36, "动态规划"),
    "algo_greedy": (36, "贪心算法"),
    "algo_backtrack": (36, "回溯法"),
    "algo_graph_bfs": (36, "BFS 广度优先"),
    "algo_graph_dfs": (36, "DFS 深度优先"),
    "algo_stack_queue": (36, "栈与队列"),
    "project_pattern_lib": (37, "设计模式库"),
    "project_algo_toolbox": (37, "算法工具箱"),
    "project_code_review": (37, "代码审查工具"),
}

STAGE_NAMES = {
    # 第一篇：Python基础
    1: "变量与数据类型", 2: "运算符", 3: "条件语句", 4: "循环",
    5: "函数", 6: "列表", 7: "元组", 8: "字典", 9: "集合",
    10: "字符串", 11: "文件读写", 12: "异常处理", 13: "综合实战",
    # 第二篇：Python进阶
    14: "正则表达式", 15: "面向对象基础", 16: "面向对象进阶",
    17: "模块与包", 18: "生成器与装饰器",
    # 第三篇：工程基础
    19: "数据库基础", 20: "测试与调试", 21: "API开发",
    # 第四篇：数据方向
    22: "爬虫入门", 23: "数据处理基础", 24: "数据可视化",
    25: "浏览器自动化与爬虫进阶", 26: "异步编程",
    27: "爬虫高级", 28: "爬虫工程化", 29: "综合实战：数据方向",
    # 第五篇：自动化与桌面
    30: "脚本自动化", 31: "桌面自动化", 32: "GUI开发",
    33: "综合实战：自动化方向",
    # 第六篇：架构与算法
    34: "设计模式", 35: "算法基础", 36: "算法进阶",
    37: "综合实战：架构与算法",
}
