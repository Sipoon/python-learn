"""理论讲解数据 - 阶段19~21 — v5.0 第三篇：工程基础（数据库/测试/API）"""
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

THEORY_19_21 = {
    # ==================== 阶段19：数据库基础 ====================
    19: (f"""{B}阶段19：数据库基础 — 给数据安个家{END}

{C_}生活类比：数据库 = 超级智能的文件柜{END}
    普通文件：自己翻文件夹找 → 慢
    数据库：告诉管家要什么 → 瞬间找到

{BD}一、SQLite — Python 内置的轻量数据库{END}
    >>> import sqlite3

    >>> # 连接数据库（文件不存在会自动创建）
    >>> conn = sqlite3.connect("my_data.db")
    >>> cursor = conn.cursor()

    >>> # 创建表
    >>> cursor.execute('CREATE TABLE IF NOT EXISTS students ('
    ...     id INTEGER PRIMARY KEY AUTOINCREMENT,
    ...     name TEXT NOT NULL,
    ...     age INTEGER,
    ...     score REAL
    ... )')
    >>> conn.commit()

{BD}二、CRUD — 增删改查{END}
    >>> # 增 (Create)
    >>> cursor.execute("INSERT INTO students (name, age, score) VALUES (?, ?, ?)",
    ...                ("Alice", 20, 92.5))
    >>> cursor.execute("INSERT INTO students (name, age, score) VALUES (?, ?, ?)",
    ...                ("Bob", 22, 85.0))
    >>> conn.commit()

    >>> # 查 (Read)
    >>> cursor.execute("SELECT * FROM students")
    >>> cursor.fetchall()       # 获取全部结果
    [(1, 'Alice', 20, 92.5), (2, 'Bob', 22, 85.0)]

    >>> cursor.execute("SELECT name, score FROM students WHERE score > 90")
    >>> cursor.fetchall()
    [(1, 'Alice', 92.5)]

    >>> # 改 (Update)
    >>> cursor.execute("UPDATE students SET score = ? WHERE name = ?", (95.0, "Alice"))
    >>> conn.commit()

    >>> # 删 (Delete)
    >>> cursor.execute("DELETE FROM students WHERE name = ?", ("Bob",))
    >>> conn.commit()

{BD}三、MySQL — 生产级数据库{END}
    SQLite 够用但性能有限，MySQL 是业界标准

    >>> # 需要安装：pip install pymysql
    >>> import pymysql
    >>> conn = pymysql.connect(
    ...     host="localhost", user="root",
    ...     password="123456", database="test"
    ... )
    >>> cursor = conn.cursor()
    >>> # SQL 语法与 SQLite 几乎一样！

{BD}四、SQLAlchemy ORM — 用 Python 对象操作数据库{END}
    不用写 SQL，用 Python 类来操作

    >>> from sqlalchemy import create_engine, Column, Integer, String, Float
    >>> from sqlalchemy.orm import declarative_base, sessionmaker

    >>> engine = create_engine("sqlite:///my_data.db")
    >>> Base = declarative_base()

    >>> class Student(Base):
    ...     __tablename__ = "students"
    ...     id = Column(Integer, primary_key=True)
    ...     name = Column(String(50))
    ...     age = Column(Integer)
    ...     score = Column(Float)
    ...
    ...     def __repr__(self):
    ...         return f"Student({{self.name}}, {{self.score}})"

    >>> Base.metadata.create_all(engine)
    >>> Session = sessionmaker(bind=engine)
    >>> session = Session()

    >>> # 用 Python 对象插入数据
    >>> s = Student(name="Charlie", age=21, score=88.0)
    >>> session.add(s)
    >>> session.commit()

    >>> # 用 Python 查询
    >>> results = session.query(Student).filter(Student.score > 85).all()
    >>> for r in results:
    ...     print(r)
    Student(Charlie, 88.0)

{BD}五、数据库事务 — 要么全做，要么全不做{END}
    >>> # 转账示例：A 给 B 转 100 元
    >>> try:
    ...     cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE name = 'A'")
    ...     cursor.execute("UPDATE accounts SET balance = balance + 100 WHERE name = 'B'")
    ...     conn.commit()          # 两步都成功，提交
    ... except Exception as e:
    ...     conn.rollback()        # 任何一步失败，回滚
    ...     print(f"转账失败: {{e}}")

{C_}生活类比：事务 = 快递签收{END}
    包裹完整 → 签收（commit）
    包裹破损 → 拒收（rollback）

{BD}六、数据库设计原则{END}
    1. 每张表一个主题（不要把学生和课程塞一张表）
    2. 用主键唯一标识每行（id）
    3. 用外键关联表（student_id → students.id）
    4. 避免数据冗余（不要到处复制同一信息）

{DIM}>> 动手试试！{END}
    {C_}在代码实验室里创建一个 SQLite 数据库，建表插入几条数据{END}
""", ["db_sqlite", "db_create", "db_insert", "db_query", "db_transaction"]),

    # ==================== 阶段20：测试与调试 ====================
    20: (f"""{B}阶段20：测试与调试 — 让代码可靠起来{END}

{C_}生活类比：测试 = 产品质检{END}
    不测试的代码 = 没检查就出厂的产品
    出了 bug 再修 = 召回 → 代价巨大
    先写测试 = 生产线质检 → 一次过

{BD}一、assert — 最简单的测试{END}
    >>> def add(a, b):
    ...     return a + b

    >>> assert add(1, 2) == 3
    >>> assert add(-1, 1) == 0
    >>> # 如果断言失败，抛出 AssertionError

{BD}二、unittest — Python 标准测试库{END}
    >>> import unittest

    >>> class TestMath(unittest.TestCase):
    ...     def test_add(self):
    ...         self.assertEqual(add(1, 2), 3)
    ...         self.assertEqual(add(-1, 1), 0)
    ...
    ...     def test_add_type(self):
    ...         with self.assertRaises(TypeError):
    ...             add("1", 2)   # 字符串+数字应报错

    >>> # 运行：python -m unittest test_file.py

{BD}三、pytest — 更优雅的测试框架{END}
    >>> # pip install pytest
    >>> # 不用写类，直接写函数，更简洁

    >>> def test_add():
    ...     assert add(1, 2) == 3
    ...     assert add(-1, 1) == 0

    >>> # 运行：pytest test_file.py

{BD}四、pytest fixture — 测试的准备工作{END}
    >>> import pytest

    >>> @pytest.fixture
    ... def sample_data():
    ...     return [1, 2, 3, 4, 5]

    >>> def test_sum(sample_data):
    ...     assert sum(sample_data) == 15

    >>> def test_len(sample_data):
    ...     assert len(sample_data) == 5

{BD}五、参数化测试 — 一次测多种情况{END}
    >>> @pytest.mark.parametrize("a, b, expected", [
    ...     (1, 2, 3),
    ...     (-1, 1, 0),
    ...     (0, 0, 0),
    ...     (100, 200, 300),
    ... ])
    ... def test_add_many(a, b, expected):
    ...     assert add(a, b) == expected

{BD}六、logging — 不要用 print 调试！{END}
    >>> import logging

    >>> logging.basicConfig(
    ...     level=logging.DEBUG,
    ...     format='%(asctime)s [%(levelname)s] %(message)s'
    ... )

    >>> logging.debug("调试信息 — 开发时看")
    >>> logging.info("普通信息 — 程序运行记录")
    >>> logging.warning("警告 — 可能有问题")
    >>> logging.error("错误 — 出问题了")
    >>> logging.critical("严重 — 程序要崩了")

{BD}七、pdb — 交互式调试器{END}
    >>> # 在代码里插入断点
    >>> def buggy_function(data):
    ...     result = []
    ...     for item in data:
    ...         import pdb; pdb.set_trace()  # 执行到这里会暂停
    ...         result.append(item * 2)
    ...     return result

    >>> # pdb 常用命令：
    >>> # n = 下一行
    >>> # c = 继续执行
    >>> # p 变量名 = 打印变量
    >>> # q = 退出

{C_}生活类比：测试金字塔{END}
    底层多：单元测试（测函数）→ 中层：集成测试（测模块组合）→ 顶层少：端到端测试（测整个系统）

{DIM}>> 动手试试！{END}
    {C_}在代码实验室里为你之前写过的函数写 3 个测试用例{END}


{BD}八、unittest 框架详解{END}

{C_}unittest 是 Python 内置的测试框架，适合大型项目：{END}
    >>> import unittest

    >>> class TestStringMethods(unittest.TestCase):
    ...     def test_upper(self):
    ...         self.assertEqual("hello".upper(), "HELLO")
    ...
    ...     def test_isupper(self):
    ...         self.assertTrue("HELLO".isupper())
    ...         self.assertFalse("hello".isupper())
    ...
    ...     def test_split(self):
    ...         s = "hello world"
    ...         self.assertEqual(s.split(), ["hello", "world"])
    ...         with self.assertRaises(ValueError):
    ...             s.split(" ")

    >>> # 常用断言方法：
    >>> # assertEqual(a, b)       a == b
    >>> # assertNotEqual(a, b)    a != b
    >>> # assertTrue(x)           x is True
    >>> # assertFalse(x)          x is False
    >>> # assertIn(a, b)          a in b
    >>> # assertRaises(Exc)       期望抛出异常

    >>> # setUp / tearDown — 每个测试方法前后执行
    >>> class TestDatabase(unittest.TestCase):
    ...     def setUp(self):
    ...         self.conn = create_connection()  # 每个测试前连接
    ...
    ...     def tearDown(self):
    ...         self.conn.close()                 # 每个测试后关闭
    ...
    ...     def test_insert(self):
    ...         self.conn.insert("test")
    ...         self.assertEqual(self.conn.count(), 1)

{BD}九、Mock 测试 — 隔离外部依赖{END}

{C_}Mock = 替身演员，替代真实对象{END}
    不想真的发请求/连数据库？用 Mock 替代！

    >>> from unittest.mock import Mock, patch

    >>> # 创建 Mock 对象
    >>> mock_db = Mock()
    >>> mock_db.get_user.return_value = {{"name": "测试用户"}}
    >>> mock_db.get_user(1)
    {{'name': '测试用户'}}

    >>> # 验证是否被调用
    >>> mock_db.get_user.assert_called_once_with(1)

    >>> # patch 替换真实函数
    >>> import requests
    >>> with patch('requests.get') as mock_get:
    ...     mock_get.return_value.status_code = 200
    ...     mock_get.return_value.json.return_value = {{"ok": True}}
    ...     resp = requests.get("https://example.com")
    ...     assert resp.status_code == 200
    ...     assert resp.json() == {{"ok": True}}

{BD}十、性能测试 — cProfile{END}

{C_}找出程序慢在哪里：{END}
    >>> import cProfile

    >>> def slow_function():
    ...     total = 0
    ...     for i in range(100000):
    ...         total += i ** 2
    ...     return total

    >>> # 方式1：直接分析
    >>> cProfile.run('slow_function()')

    >>> # 方式2：命令行分析
    >>> # python -m cProfile -s cumulative my_script.py

{C_}读懂 cProfile 输出：{END}
    ncalls  tottime  percall  cumtime  percall  filename
      1      0.02     0.02     0.02     0.02   slow_function
    • ncalls：调用次数
    • tottime：函数自身耗时（不含子函数）
    • cumtime：总耗时（含子函数）
    • 按 cumtime 排序找瓶颈

{BD}十一、调试技巧进阶{END}

{C_}1. breakpoint() — Python 3.7+ 推荐{END}
    >>> def calculate(data):
    ...     result = 0
    ...     for item in data:
    ...         breakpoint()     # 自动进入 pdb
    ...         result += item
    ...     return result

{C_}2. pdb 常用命令速查{END}
    n(next)      下一行
    s(step)      进入函数
    c(continue)  继续执行
    p var        打印变量
    pp var       美化打印
    l(list)      显示代码
    w(where)     调用栈
    b(line)      设置断点
    q(quit)      退出

{C_}3. 条件断点{END}
    >>> # 只在特定条件暂停
    >>> import pdb; pdb.set_trace()
    # 在 pdb 中输入：b 10, x > 100
    # 表示第10行且 x > 100 时才停""", ["test_pytest", "test_unit", "test_fixture", "test_parametrize", "test_exception"]),

    # ==================== 阶段21：API开发 ====================
    21: (f"""{B}阶段21：API 开发 — 用 FastAPI 构建后端{END}

{C_}生活类比：API = 餐厅的菜单+服务员{END}
    厨房（数据库）做好了菜
    菜单（API文档）告诉客人有什么
    服务员（API接口）把客人的点单传达给厨房，再把菜端回来

{BD}一、FastAPI 入门{END}
    >>> # pip install fastapi uvicorn
    >>> from fastapi import FastAPI

    >>> app = FastAPI()

    >>> @app.get("/")
    ... def home():
    ...     return {{"message": "Hello, API!"}}

    >>> @app.get("/items/{{item_id}}")
    ... def get_item(item_id: int):
    ...     return {{"item_id": item_id}}

    >>> # 启动：uvicorn main:app --reload
    >>> # 访问：http://127.0.0.1:8000
    >>> # 自动文档：http://127.0.0.1:8000/docs

{BD}二、路由与 HTTP 方法{END}
    >>> @app.get("/users")          # 获取用户列表
    ... def list_users():
    ...     return {{"users": []}}

    >>> @app.post("/users")         # 创建用户
    ... def create_user():
    ...     return {{"created": True}}

    >>> @app.put("/users/{{uid}}")  # 更新用户
    ... def update_user(uid: int):
    ...     return {{"updated": uid}}

    >>> @app.delete("/users/{{uid}}")  # 删除用户
    ... def delete_user(uid: int):
    ...     return {{"deleted": uid}}

{BD}三、路径参数与查询参数{END}
    >>> # 路径参数 — URL 的一部分
    >>> @app.get("/students/{{student_id}}")
    ... def get_student(student_id: int):
    ...     return {{"id": student_id}}

    >>> # 查询参数 — ?key=value
    >>> @app.get("/students")
    ... def search_students(name: str = "", age: int = None):
    ...     return {{"name": name, "age": age}}
    >>> # GET /students?name=Alice&age=20

{BD}四、Pydantic 数据验证{END}
    >>> from pydantic import BaseModel

    >>> class StudentCreate(BaseModel):
    ...     name: str
    ...     age: int
    ...     score: float = 0.0

    >>> @app.post("/students")
    ... def create_student(student: StudentCreate):
    ...     return {{"created": student.name, "score": student.score}}
    >>> # 自动验证：name 必须是 str，age 必须是 int
    >>> # 传错类型 → 自动返回 422 错误 + 详细信息

{BD}五、CRUD 完整示例{END}
    >>> students = {{}}  # 内存数据库（演示用）

    >>> @app.get("/students")
    ... def list_students():
    ...     return list(students.values())

    >>> @app.post("/students")
    ... def create_student(student: StudentCreate):
    ...     sid = len(students) + 1
    ...     students[sid] = {{"id": sid, **student.dict()}}
    ...     return students[sid]

    >>> @app.get("/students/{{sid}}")
    ... def get_student(sid: int):
    ...     return students.get(sid, {{"error": "not found"}})

    >>> @app.delete("/students/{{sid}}")
    ... def delete_student(sid: int):
    ...     if sid in students:
    ...         del students[sid]
    ...         return {{"deleted": True}}
    ...     return {{"error": "not found"}}

{BD}六、JWT 认证 — 保护你的 API{END}
    >>> # pip install python-jose[cryptography] passlib[bcrypt]
    >>> from jose import jwt

    >>> SECRET = "your-secret-key"

    >>> def create_token(data: dict):
    ...     return jwt.encode(data, SECRET, algorithm="HS256")

    >>> def verify_token(token: str):
    ...     return jwt.decode(token, SECRET, algorithms=["HS256"])

    >>> # 登录 → 发 token
    >>> # 请求 → 带 token → 验证 → 放行

{C_}生活类比：JWT = 电影票{END}
    买票（登录）→ 拿到票（token）→ 每次进场验票（验证）

{DIM}>> 动手试试！{END}
    {C_}在代码实验室里定义一个 Pydantic 模型，体验数据验证的威力{END}
""", ["api_fastapi", "api_route", "api_pydantic", "api_middleware", "api_deploy"]),
}
