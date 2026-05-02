"""理论讲解数据 - 阶段22~25 — v5.0 第四篇：数据方向（爬虫/数据/可视化/浏览器进阶/异步）"""
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

THEORY_22_25 = {
    # ==================== 阶段22：爬虫入门 ====================
    22: (f"""{B}阶段22：爬虫入门 — 让程序去网上拿数据{END}

{C_}生活类比：爬虫 = 你雇了个助手去图书馆抄书{END}
    1. 告诉助手去哪个书架（URL）
    2. 助手把内容抄回来（requests）
    3. 你从抄本里找你要的信息（BeautifulSoup解析）

{BD}一、requests — HTTP 请求{END}
    >>> import requests

    >>> # GET 请求 — 最常用的请求方式
    >>> response = requests.get("https://httpbin.org/get")
    >>> response.status_code           # 状态码：200=成功
    200
    >>> response.text[:50]             # 响应内容（字符串）
    '<!DOCTYPE html>...'

    >>> # 带参数的 GET
    >>> params = {{"q": "python", "page": 1}}
    >>> response = requests.get("https://httpbin.org/get", params=params)

    >>> # POST 请求 — 提交数据
    >>> data = {{"username": "test", "password": "123"}}
    >>> response = requests.post("https://httpbin.org/post", json=data)

{BD}二、请求头与超时{END}
    >>> # 设置请求头 — 模拟浏览器
    >>> headers = {{
    ...     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    ...     "Accept": "text/html,application/xhtml+xml",
    ... }}
    >>> response = requests.get(url, headers=headers)

    >>> # 超时设置 — 永远不要不加 timeout！
    >>> response = requests.get(url, timeout=10)  # 10秒超时

{BD}三、异常处理{END}
    >>> from requests.exceptions import RequestException, Timeout, ConnectionError

    >>> try:
    ...     response = requests.get(url, timeout=10)
    ...     response.raise_for_status()  # 4xx/5xx 会抛异常
    ... except Timeout:
    ...     print("请求超时")
    ... except ConnectionError:
    ...     print("连接失败")
    ... except RequestException as e:
    ...     print(f"请求错误: {{e}}")

{BD}四、BeautifulSoup — HTML 解析{END}
    >>> from bs4 import BeautifulSoup

    >>> html = "<html><body><h1>Title</h1><p class='info'>Hello</p></body></html>"
    >>> soup = BeautifulSoup(html, "html.parser")

    >>> # 按标签查找
    >>> soup.find("h1").text
    'Title'

    >>> # 按属性查找
    >>> soup.find("p", class_="info").text
    'Hello'

    >>> # 找所有
    >>> soup.find_all("p")
    [<p class='info'>Hello</p>]

    >>> # 获取属性
    >>> soup.find("p")["class"]
    ['info']

{BD}五、CSS 选择器{END}
    >>> soup.select("h1")              # 标签选择器
    >>> soup.select(".info")           # 类选择器
    >>> soup.select("#main")           # ID 选择器
    >>> soup.select("div > p")         # 子元素选择器
    >>> soup.select("div p:first-child")  # 伪类选择器

{BD}六、编码处理{END}
    >>> # requests 通常自动检测编码，但有时会乱码
    >>> response = requests.get(url)
    >>> response.encoding = "utf-8"    # 手动指定编码
    >>> response.text                  # 现在不会乱码了

    >>> # 或者用 apparent_encoding 自动检测
    >>> response.encoding = response.apparent_encoding

{BD}七、爬虫礼仪 — 做个好公民{END}
    1. 看看 robots.txt（网站爬虫规则）
    2. 控制频率（time.sleep(1) 间隔1秒）
    3. 设置 User-Agent（告诉对方你是谁）
    4. 不要恶意刷接口
    5. 尊重版权，不爬隐私数据

{BD}八、数据保存{END}
    >>> import json, csv

    >>> # 保存为 JSON
    >>> data = [{{"name": "Alice", "score": 92}}]
    >>> with open("data.json", "w", encoding="utf-8") as f:
    ...     json.dump(data, f, ensure_ascii=False, indent=2)

    >>> # 保存为 CSV
    >>> with open("data.csv", "w", newline="", encoding="utf-8") as f:
    ...     writer = csv.DictWriter(f, fieldnames=["name", "score"])
    ...     writer.writeheader()
    ...     writer.writerows(data)

{DIM}>> 动手试试！{END}
    {C_}在代码实验室里用 requests 获取一个网页的状态码{END}
""", ["crawl_requests", "crawl_beautifulsoup", "crawl_headers", "crawl_parse"]),

    # ==================== 阶段23：数据处理基础 ====================
    23: (f"""{B}阶段23：数据处理基础 — pandas 让数据听话{END}

{C_}生活类比：pandas = Excel 的超级强化版{END}
    Excel：点击菜单操作 → 慢、不可复现
    pandas：写代码操作 → 快、可复现、可自动化

{BD}一、CSV 进阶 — DictReader{END}
    >>> import csv

    >>> # 读取为字典
    >>> with open("scores.csv", encoding="utf-8") as f:
    ...     reader = csv.DictReader(f)
    ...     for row in reader:
    ...         print(row["name"], row["score"])

{BD}二、JSON 进阶{END}
    >>> import json

    >>> # 嵌套 JSON
    >>> data = '{{"students": [{{"name": "Alice", "scores": [90, 85]}}]}}'
    >>> parsed = json.loads(data)
    >>> parsed["students"][0]["scores"][0]
    90

{BD}三、pandas — 数据处理的瑞士军刀{END}
    >>> # pip install pandas
    >>> import pandas as pd

    >>> # 创建 DataFrame
    >>> df = pd.DataFrame({{
    ...     "name": ["Alice", "Bob", "Charlie"],
    ...     "age": [20, 22, 21],
    ...     "score": [92.5, 85.0, 88.0]
    ... }})
    >>> df
         name  age  score
    0    Alice   20   92.5
    1      Bob   22   85.0
    2  Charlie   21   88.0

{BD}四、数据选择和筛选{END}
    >>> df["name"]                  # 选一列
    >>> df[["name", "score"]]      # 选多列
    >>> df[df["score"] > 88]       # 条件筛选
    >>> df.loc[0]                  # 按索引选行
    >>> df.iloc[0:2]               # 按位置选行

{BD}五、数据处理 — groupby / sort{END}
    >>> # 排序
    >>> df.sort_values("score", ascending=False)

    >>> # 分组统计
    >>> df.groupby("age")["score"].mean()

    >>> # 新增列
    >>> df["grade"] = df["score"].apply(
    ...     lambda x: "A" if x >= 90 else "B" if x >= 80 else "C"
    ... )

{BD}六、pandas 读写文件{END}
    >>> df.to_csv("output.csv", index=False)          # 写 CSV
    >>> df.to_json("output.json", orient="records")   # 写 JSON
    >>> pd.read_csv("data.csv")                       # 读 CSV
    >>> pd.read_json("data.json")                     # 读 JSON

{C_}注意：阶段11学过 CSV/JSON 基础读写，这里是用 pandas 进阶处理{END}

{DIM}>> 动手试试！{END}
    {C_}在代码实验室里创建一个 DataFrame 并尝试筛选和排序{END}
{BD}七、数据合并 — concat 与 merge{END}
    多个 DataFrame 可以纵向或横向合并：
    >>> import pandas as pd
    >>> df1 = pd.DataFrame({{"name": ["Alice", "Bob"], "score": [92, 85]}})
    >>> df2 = pd.DataFrame({{"name": ["Charlie"], "score": [88]}})
    >>> pd.concat([df1, df2], ignore_index=True)   # 纵向拼接
         name  score
    0    Alice   92
    1      Bob   85
    2  Charlie   88
    >>> df3 = pd.DataFrame({{"name": ["Alice"], "age": [20]}})
    >>> df1.merge(df3, on="name")                  # 按 name 列横向合并
         name  score  age
    0    Alice   92   20
{BD}八、数据清洗实战{END}
    真实数据往往有缺失值、重复行、异常值：
    >>> df = pd.DataFrame({{
    ...     "name": ["Alice", "Bob", None, "Alice"],
    ...     "score": [92, None, 88, 92],
    ...     "age": [20, 22, 21, 20]
    ... }})
    >>> df.dropna()                          # 删除有缺失值的行
    >>> df.fillna(0)                         # 用 0 填充缺失值
    >>> df.drop_duplicates()                # 删除重复行
    >>> df["score"] = df["score"].clip(0, 100)  # 异常值截断
{BD}九、综合练习 — 数据分析流程{END}
    完整的数据分析流程示例：
    >>> import pandas as pd
    >>> # 1. 读取数据
    >>> df = pd.read_csv("students.csv")
    >>> # 2. 查看概况
    >>> df.info()          # 列名、类型、缺失值
    >>> df.describe()      # 数值列的统计摘要
    >>> # 3. 数据清洗
    >>> df = df.dropna(subset=["score"])
    >>> df = df.drop_duplicates()
    >>> # 4. 统计分析
    >>> avg = df["score"].mean()
    >>> top = df.nlargest(5, "score")
    >>> # 5. 输出结果
    >>> df.to_csv("cleaned.csv", index=False)
{C_}提示：用 pandas 解决了 Excel 慢、手动操作不可复现的问题{END}
""", ["pandas_dataframe", "pandas_select", "pandas_groupby", "pandas_merge", "pandas_clean"]),

    # ==================== 阶段24：数据可视化 ====================
    24: (f"""{B}阶段24：数据可视化 — 让数据说话{END}

{C_}生活类比：数据可视化 = 把数字变成图画{END}
    一列数字：[23, 45, 12, 67, 34] → 看不出什么
    一张柱状图：一眼看出谁高谁低

{BD}一、matplotlib 折线图{END}
    >>> import matplotlib.pyplot as plt

    >>> months = [1, 2, 3, 4, 5, 6]
    >>> temps = [5, 8, 15, 22, 28, 32]

    >>> plt.plot(months, temps, marker="o", color="red")
    >>> plt.title("Monthly Temperature")
    >>> plt.xlabel("Month")
    >>> plt.ylabel("Temp (C)")
    >>> plt.savefig("temp.png")

{BD}二、柱状图{END}
    >>> names = ["Alice", "Bob", "Charlie"]
    >>> scores = [92, 85, 88]
    >>> plt.bar(names, scores, color=["#FF6B6B", "#4ECDC4", "#45B7D1"])
    >>> plt.title("Student Scores")
    >>> plt.savefig("scores.png")

{BD}三、饼图{END}
    >>> labels = ["Python", "Java", "C++", "Go"]
    >>> sizes = [40, 25, 20, 15]
    >>> plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    >>> plt.title("Language Popularity")
    >>> plt.savefig("langs.png")

{BD}四、散点图{END}
    >>> x = [1, 2, 3, 4, 5]
    >>> y = [2, 4, 5, 4, 5]
    >>> plt.scatter(x, y, color="green", s=100)
    >>> plt.title("Scatter Plot")
    >>> plt.savefig("scatter.png")

{BD}五、子图{END}
    >>> fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    >>> axes[0, 0].plot(months, temps)
    >>> axes[0, 1].bar(names, scores)
    >>> axes[1, 0].pie(sizes, labels=labels)
    >>> axes[1, 1].scatter(x, y)
    >>> plt.tight_layout()
    >>> plt.savefig("dashboard.png")

{BD}六、pandas 绑图{END}
    >>> df.plot(x="name", y="score", kind="bar")
    >>> plt.savefig("pandas_bar.png")

    >>> df["score"].hist(bins=5)
    >>> plt.savefig("pandas_hist.png")

{BD}七、样式美化{END}
    >>> plt.style.use("seaborn-v0_8")    # 使用美观主题
    >>> plt.grid(True, alpha=0.3)         # 网格线
    >>> plt.tight_layout()                # 自动调整间距

{DIM}>> 动手试试！{END}
    {C_}在代码实验室里画一张简单的柱状图{END}
{BD}八、保存图表的细节控制{END}
    savefig 有多种参数控制输出质量：
    >>> plt.savefig("chart.png", dpi=300, bbox_inches="tight")
    {G}# dpi=300 高清 | bbox_inches="tight" 裁掉白边{END}
    >>> plt.savefig("chart.pdf")            # 矢量格式，放大不失真
    >>> plt.savefig("chart.svg")            # SVG 矢量，可编辑
    >>> plt.savefig("chart.png", facecolor="white")  # 白色背景
{BD}九、多系列与图例{END}
    在同一张图上画多条线，并添加图例：
    >>> months = [1, 2, 3, 4, 5]
    >>> sales = [120, 150, 180, 200, 220]
    >>> profit = [30, 40, 50, 60, 70]
    >>> plt.plot(months, sales, label="销售额", color="#2563EB")
    >>> plt.plot(months, profit, label="利润", color="#16A34A")
    >>> plt.legend(loc="upper left")        # 图例位置
    >>> plt.title("月度销售与利润趋势")
    >>> plt.savefig("trend.png")
{BD}十、直方图与箱线图{END}
    分析数据分布的专用图表：
    >>> # 直方图：看数据分布范围
    >>> import numpy as np
    >>> scores = np.random.normal(75, 10, 200)  # 200个模拟成绩
    >>> plt.hist(scores, bins=10, color="#7C3AED", edgecolor="white")
    >>> plt.xlabel("分数")
    >>> plt.ylabel("人数")
    >>> plt.title("成绩分布直方图")
    >>> plt.savefig("hist.png")
    >>> # 箱线图：看异常值和四分位数
    >>> data = [78, 85, 90, 92, 95, 120]
    >>> plt.boxplot(data, labels=["成绩"])
    >>> plt.title("成绩箱线图（120分是异常值）")
    >>> plt.savefig("box.png")
{BD}十一、简单热力图{END}
    用颜色深浅表示数值大小：
    >>> data = [[5, 3, 7], [2, 9, 1], [4, 6, 8]]
    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> plt.imshow(data, cmap="YlOrRd")    # 黄→橙→红配色
    >>> plt.colorbar()                     # 显示颜色条
    >>> plt.title("数据热力图")
    >>> plt.savefig("heatmap.png")
{BD}十二、seaborn 快速入门{END}
    seaborn 是 matplotlib 的高级封装，图表更美观：
    >>> import seaborn as sns
    >>> import matplotlib.pyplot as plt
    >>> # seaborn 内置了一些数据集
    >>> tips = sns.load_dataset("tips")   # 小费数据集
    >>> # 一行代码画散点图（带回归线）
    >>> sns.regplot(x="total_bill", y="tip", data=tips)
    >>> plt.title("账单与小费关系")
    >>> plt.savefig("seaborn.png")
{C_}提示：matplotlib 打基础，seaborn 提升美观度，两者结合最好{END}
""", ["viz_matplotlib", "viz_bar", "viz_line", "viz_scatter", "viz_custom"]),

    # ==================== 阶段25：浏览器自动化与爬虫进阶 ====================
    25: (f"""{B}阶段25：浏览器自动化与爬虫进阶 — 攻克动态页面{END}

{C_}生活类比：进阶爬虫 = 从寄明信片到电话预约{END}
    基础爬虫像寄明信片——发出去等回信
    进阶爬虫像打电话——实时交互，还能应对对方的身份验证

{BD}一、动态页面与 Selenium{END}
    有些网页用 JavaScript 动态加载数据，requests 只能拿到空壳 HTML

    >>> from selenium import webdriver
    >>> from selenium.webdriver.common.by import By
    >>> from selenium.webdriver.support.ui import WebDriverWait
    >>> from selenium.webdriver.support import expected_conditions as EC

    >>> # 启动浏览器（需下载对应 WebDriver）
    >>> driver = webdriver.Chrome()

    >>> # 访问页面
    >>> driver.get("https://example.com")

    >>> # 等待元素加载
    >>> wait = WebDriverWait(driver, 10)
    >>> element = wait.until(EC.presence_of_element_located((By.ID, "content")))

    >>> # 获取动态渲染后的 HTML
    >>> html = driver.page_source

    >>> # 关闭浏览器
    >>> driver.quit()

{BD}二、Playwright — 新一代浏览器自动化{END}
    >>> # pip install playwright
    >>> # playwright install
    >>> from playwright.sync_api import sync_playwright

    >>> with sync_playwright() as p:
    ...     browser = p.chromium.launch(headless=True)
    ...     page = browser.new_page()
    ...     page.goto("https://example.com")
    ...     title = page.title()
    ...     content = page.content()
    ...     browser.close()

{BD}三、Session — 保持登录态{END}
    >>> import requests

    >>> s = requests.Session()
    >>> # 登录
    >>> s.post("https://example.com/login", data={{"user": "test", "pass": "123"}})
    >>> # 后续请求自动带 cookie
    >>> response = s.get("https://example.com/dashboard")

{BD}四、反爬策略应对{END}
    1. User-Agent 伪装
       >>> headers = {{"User-Agent": "Mozilla/5.0 ..."}}
       >>> requests.get(url, headers=headers)

    2. 请求间隔
       >>> import time
       >>> time.sleep(random.uniform(1, 3))

    3. 代理池
       >>> proxies = {{"http": "http://proxy:8080"}}
       >>> requests.get(url, proxies=proxies)

    4. Cookie 池 — 多账号轮换

{BD}五、无头模式{END}
    不显示浏览器窗口，后台运行，节省资源

    >>> # Selenium 无头模式
    >>> from selenium.webdriver.chrome.options import Options
    >>> options = Options()
    >>> options.add_argument("--headless")
    >>> driver = webdriver.Chrome(options=options)

    >>> # Playwright 默认就支持 headless
    >>> browser = p.chromium.launch(headless=True)

{BD}六、显式等待 vs 隐式等待{END}
    >>> # 隐式等待 — 全局等待
    >>> driver.implicitly_wait(10)  # 最多等10秒

    >>> # 显式等待 — 精确等待某个条件（推荐！）
    >>> wait = WebDriverWait(driver, 10)
    >>> wait.until(EC.element_to_be_clickable((By.ID, "btn")))
    >>> wait.until(EC.text_to_be_present_in_element((By.ID, "msg"), "Done"))

{BD}七、最佳实践{END}
    1. 优先用 requests + BS4（快速、轻量）
    2. 动态页面再用 Selenium/Playwright
    3. 加随机延迟，控制频率
    4. 异常处理要完善
    5. 数据及时保存，防止丢失


{BD}八、Playwright — 现代浏览器自动化{END}

{C_}比 Selenium 更快更稳的新选择{END}
    >>> # pip install playwright
    >>> # playwright install chromium
    >>> from playwright.sync_api import sync_playwright

    >>> with sync_playwright() as p:
    ...     browser = p.chromium.launch(headless=True)
    ...     page = browser.new_page()
    ...     page.goto("https://example.com")
    ...     title = page.title()
    ...     browser.close()

{C_}优势：自动等待、支持多浏览器、更简洁 API{END}

{DIM}>> 动手试试！{END}
    {C_}在代码实验室里用 requests.Session 模拟登录流程{END}
""", ["crawl_selenium", "crawl_wait", "crawl_dynamic", "crawl_automation"]),
}
