"""理论讲解数据 - 阶段26~29 — v5.0 第四篇：数据方向续（异步/爬虫高级/工程化/综合实战）"""
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

THEORY_26_29 = {
    # ==================== 阶段26：异步编程 ====================
    26: (f"""{B}阶段26：异步编程 — 同时做多件事{END}

{C_}生活类比：同步 vs 异步 = 排队 vs 取号{END}
    同步（排队）：在银行排2小时队办3件事 → 2小时
    异步（取号）：取3个号，等叫号时再办 → 30分钟

{BD}一、async/await 基础{END}
    >>> import asyncio

    >>> async def say_hello(name, seconds):
    ...     print(f"Hello {{name}}!")
    ...     await asyncio.sleep(seconds)   # 模拟耗时操作
    ...     print(f"Bye {{name}}!")

    >>> # 运行协程
    >>> asyncio.run(say_hello("World", 1))

{BD}二、asyncio.gather — 并发执行{END}
    >>> async def fetch(url):
    ...     print(f"Fetching {{url}}...")
    ...     await asyncio.sleep(1)  # 模拟网络请求
    ...     return f"Data from {{url}}"

    >>> async def main():
    ...     # 3个请求同时发出，总共只需1秒（而不是3秒）
    ...     results = await asyncio.gather(
    ...         fetch("url1"),
    ...         fetch("url2"),
    ...         fetch("url3"),
    ...     )
    ...     print(results)

    >>> asyncio.run(main())

{BD}三、aiohttp — 异步 HTTP 请求{END}
    >>> # pip install aiohttp
    >>> import aiohttp

    >>> async def fetch_page(url):
    ...     async with aiohttp.ClientSession() as session:
    ...         async with session.get(url) as response:
    ...             return await response.text()

    >>> async def crawl_many(urls):
    ...     tasks = [fetch_page(url) for url in urls]
    ...     return await asyncio.gather(*tasks)

    >>> # 100个URL，并发下载，比同步快10倍+

{BD}四、Semaphore — 控制并发数量{END}
    >>> # 防止一次性发太多请求被服务器拒绝
    >>> sem = asyncio.Semaphore(10)  # 最多同时10个

    >>> async def limited_fetch(url):
    ...     async with sem:
    ...         return await fetch_page(url)

{BD}五、异步 vs 多线程 vs 多进程{END}
    | 场景         | 最佳选择   | 原因               |
    |-------------|-----------|-------------------|
    | 网络请求多    | asyncio   | 等待时自动切换      |
    | CPU密集计算   | 多进程     | 绕过GIL限制        |
    | 简单并发      | 多线程     | 写法简单           |


{BD}六、asyncio.TaskGroup — Python 3.11+ 任务组{END}
    TaskGroup 比 gather 更优雅：任一任务失败会立即取消其他任务。

    >>> async def fetch(url):
    ...     async with aiohttp.ClientSession() as session:
    ...         async with session.get(url) as resp:
    ...             return await resp.text()

    >>> async def main():
    ...     async with asyncio.TaskGroup() as tg:
    ...         t1 = tg.create_task(fetch("https://example.com/1"))
    ...         t2 = tg.create_task(fetch("https://example.com/2"))
    ...         t3 = tg.create_task(fetch("https://example.com/3"))
    ...     print("结果:", t1.result(), t2.result(), t3.result())

    >>> asyncio.run(main())
    注意：如果任一任务抛出异常，其他任务会被立即取消。

{BD}七、asyncio.wait — 带超时的等待{END}
    wait() 返回 (done, pending) 两组任务，适合超时控制。

    >>> async def delay_task(name, sec):
    ...     await asyncio.sleep(sec)
    ...     return name

    >>> async def main():
    ...     done, pending = await asyncio.wait([
    ...         delay_task("快速", 0.5),
    ...         delay_task("慢速", 2),
    ...         delay_task("中速", 1),
    ...     ], timeout=1)  # 1秒后强制返回
    ...     for t in pending:
    ...         t.cancel()
    ...     results = [t.result() for t in done]
    ...     print("已完成:", results)

    >>> asyncio.run(main())
    结果：只有 timeout 前完成的任务会被保留。

{BD}八、异步上下文管理器与异步迭代器{END}
    异步上下文管理器：用 async with 管理资源，生命周期清晰。

    >>> class AsyncDB:
    ...     async def __aenter__(self):
    ...         self.conn = await connect_db()
    ...         return self
    ...     async def __aexit__(self, *args):
    ...         await self.conn.close()

    >>> async def main():
    ...     async with AsyncDB() as db:
    ...         result = await db.query("SELECT * FROM users")

    异步迭代器：支持 async for 遍历异步生成的数据源。

    >>> class AsyncPageFetcher:
    ...     def __init__(self, base_url):
    ...         self.page = 1
    ...         self.base_url = base_url
    ...     def __aiter__(self):
    ...         return self
    ...     async def __anext__(self):
    ...         if self.page > 3:
    ...             raise StopAsyncIteration
    ...         url = f"{{self.base_url}}/page/{{self.page}}"
    ...         self.page += 1
    ...         return await fetch_page(url)

    >>> async def main():
    ...     async for html in AsyncPageFetcher("https://example.com/blog"):
    ...         print(html[:50])

{BD}九、aiofiles — 异步文件I/O{END}
    aiofiles 让文件读写不阻塞事件循环，适合批量处理大量文件。

    >>> # pip install aiofiles
    >>> import aiofiles

    >>> async def save_file(path, content):
    ...     async with aiofiles.open(path, "w", encoding="utf-8") as f:
    ...         await f.write(content)

    >>> async def batch_save(items):
    ...     tasks = [save_file(p, c) for p, c in items.items()]
    ...     await asyncio.gather(*tasks)  # 并发写多个文件

    对比同步写法：同步写10个文件要串行等待，aiofiles 同时写快10倍+。

{BD}十、常见错误与调试技巧{END}
    错误1：忘记 await，协程对象不会被执行。

    >>> async def bad():
    ...     result = asyncio.sleep(1)  # 只创建了协程对象，永远不会执行！
    ...     return result

    >>> async def good():
    ...     result = await asyncio.sleep(1)  # 真正执行
    ...     return result

    错误2：用 time.sleep 阻塞整个事件循环。

    >>> import time
    >>> # wrong: time.sleep(10) 会阻塞整个事件循环 10 秒
    >>> # correct: await asyncio.sleep(10) 允许其他任务继续执行

    错误3：在同步函数中调用异步函数。

    >>> def sync_wrapper():
    ...     # 可以在此处用 asyncio.run() 调用，但不要嵌套事件循环
    ...     asyncio.run(async_main())

    调试技巧：打印所有任务状态。

    >>> async def debug():
    ...     for t in asyncio.all_tasks():
    ...         print(f"task: {{t.get_name()}}, done: {{t.done()}}")
    
{DIM}>> 动手试试！{END}
    {C_}在代码实验室里写一个 async 函数，用 gather 并发执行{END}

""",
    ["async_def", "asyncio_gather", "aiohttp", "semaphore"]),
    # ==================== 阶段27：爬虫高级 ====================
    27: (f"""{B}阶段27：爬虫高级 — 框架与并发{END}

{C_}生活类比：爬虫框架 = 装配流水线{END}
    手工爬虫：一个人做所有事
    Scrapy：流水线分工 — 下载→解析→存储，各司其职

{BD}一、Scrapy 框架{END}
    >>> # pip install scrapy
    >>> # scrapy startproject myspider

    >>> import scrapy

    >>> class QuoteSpider(scrapy.Spider):
    ...     name = "quotes"
    ...     start_urls = ["https://quotes.toscrape.com/"]
    ...
    ...     def parse(self, response):
    ...         for quote in response.css("div.quote"):
    ...             yield {{
    ...                 "text": quote.css("span.text::text").get(),
    ...                 "author": quote.css("small.author::text").get(),
    ...             }}
    ...         # 自动翻页
    ...         next_page = response.css("li.next a::attr(href)").get()
    ...         if next_page:
    ...             yield response.follow(next_page, self.parse)

    >>> # 运行：scrapy crawl quotes -o quotes.json

{BD}二、多线程爬虫{END}
    >>> from concurrent.futures import ThreadPoolExecutor

    >>> def crawl_one(url):
    ...     response = requests.get(url, timeout=10)
    ...     return response.text[:100]

    >>> urls = ["https://example.com/page/1",
    ...         "https://example.com/page/2",
    ...         "https://example.com/page/3"]

    >>> with ThreadPoolExecutor(max_workers=5) as pool:
    ...     results = list(pool.map(crawl_one, urls))

{BD}三、多进程爬虫{END}
    >>> from concurrent.futures import ProcessPoolExecutor

    >>> # CPU 密集任务用多进程（绕过 GIL）
    >>> with ProcessPoolExecutor(max_workers=4) as pool:
    ...     results = list(pool.map(heavy_parse, raw_htmls))

{BD}四、增量爬取 — 只爬新的{END}
    >>> seen_urls = set()
    >>> # 从数据库/文件加载已爬 URL
    >>> with open("seen_urls.txt") as f:
    ...     seen_urls = set(f.read().splitlines())

    >>> new_urls = [u for u in all_urls if u not in seen_urls]
    >>> # 只爬 new_urls
    >>> # 爬完后更新 seen_urls

{BD}五、断点续爬{END}
    >>> # 每爬一批就保存进度
    >>> with open("progress.json", "w") as f:
    ...     json.dump({{"last_page": 42, "items": len(results)}}, f)

    >>> # 重启时从断点继续
    >>> with open("progress.json") as f:
    ...     progress = json.load(f)
    ...     start_page = progress["last_page"] + 1

{DIM}>> 动手试试！{END}
    {C_}在代码实验室里用 ThreadPoolExecutor 并发下载3个URL{END}

{BD}六、反爬策略与应对{END}
    >>> # 常见反爬手段
    >>> # 1. User-Agent 检测 -> 设置真实 UA
    >>> headers = {{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}}
    >>> response = requests.get(url, headers=headers)

    >>> # 2. IP 封禁 -> 使用代理池
    >>> proxies = {{"http": "http://proxy.example.com:8080"}}
    >>> response = requests.get(url, proxies=proxies)

    >>> # 3. 验证码 -> OCR识别或人工介入
    >>> # 4. 动态渲染 -> Selenium/Playwright

{BD}七、Selenium 自动化{END}
    >>> # pip install selenium
    >>> from selenium import webdriver
    >>> from selenium.webdriver.common.by import By
    >>> from selenium.webdriver.support.ui import WebDriverWait
    >>> from selenium.webdriver.support import expected_conditions as EC

    >>> driver = webdriver.Chrome()  # 需对应版本 chromedriver
    >>> driver.get("https://quotes.toscrape.com/js/")

    >>> # 等待元素出现（显式等待）
    >>> element = WebDriverWait(driver, 10).until(
    ...     EC.presence_of_element_located((By.CSS_SELECTOR, ".quote"))
    ... )

    >>> # 提取数据
    >>> quotes = driver.find_elements(By.CSS_SELECTOR, ".quote .text")
    >>> texts = [q.text for q in quotes]
    >>> driver.quit()  # 记得关闭浏览器

{BD}八、分布式爬虫概念{END}
    多机协作爬取大规模网站：
    - 主节点：调度任务、维护 URL 队列
    - 从节点：执行下载、解析任务
    - Redis：共享队列 + 去重集合

    >>> # 从节点：从 Redis 取 URL
    >>> url = r.rpop("crawl_queue")
    >>> # 爬取后将新 URL 推回队列
    >>> for new_url in extracted_urls:
    ...     r.lpush("crawl_queue", new_url)

{C_}分布式爬虫是高级话题，这里了解概念即可{END}


""",
    ["scrapy", "thread_pool", "incremental_crawl", "checkpoint"]),
    # ==================== 阶段28：爬虫工程化 ====================
    28: (f"""{B}阶段28：爬虫工程化 — 从脚本到系统{END}

{C_}生活类比：爬虫工程化 = 从地摊到工厂{END}
    脚本爬虫：手动运行、结果存文件、挂了不知道
    工程化爬虫：定时运行、数据库存储、监控告警、自动恢复

{BD}一、MySQL 存储{END}
    >>> import pymysql

    >>> conn = pymysql.connect(host="localhost", user="root",
    ...                        password="123456", database="crawl")
    >>> cursor = conn.cursor()

    >>> cursor.execute('CREATE TABLE IF NOT EXISTS articles (
    ...     id INT PRIMARY KEY AUTO_INCREMENT,
    ...     title VARCHAR(200),
    ...     url VARCHAR(500) UNIQUE,
    ...     content TEXT,
    ...     crawled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ... )')

    >>> # 插入数据（自动去重）
    >>> try:
    ...     cursor.execute("INSERT INTO articles (title, url) VALUES (%s, %s)",
    ...                    (title, url))
    ...     conn.commit()
    ... except pymysql.IntegrityError:
    ...     print("已存在，跳过")  # url UNIQUE 自动去重

{BD}二、Redis 缓存与去重{END}
    >>> # pip install redis
    >>> import redis

    >>> r = redis.Redis(host="localhost", port=6379, db=0)

    >>> # URL 去重 — 用 Set
    >>> url_hash = hashlib.md5(url.encode()).hexdigest()
    >>> if r.sismember("crawled_urls", url_hash):
    ...     print("已爬过，跳过")
    ... else:
    ...     r.sadd("crawled_urls", url_hash)
    ...     # 爬取并存储

    >>> # 请求队列 — 用 List
    >>> r.lpush("crawl_queue", "https://example.com/page/1")
    >>> url = r.rpop("crawl_queue")  # FIFO 取出

    >>> # 缓存网页 — 用 String + 过期时间
    >>> r.setex(f"page:{{url_hash}}", 3600, html_content)  # 1小时过期

{BD}三、日志与监控{END}
    >>> import logging

    >>> logging.basicConfig(
    ...     level=logging.INFO,
    ...     format='%(asctime)s [%(levelname)s] %(message)s',
    ...     handlers=[
    ...         logging.FileHandler("crawl.log"),
    ...         logging.StreamHandler(),
    ...     ]
    ... )

    >>> logging.info(f"开始爬取: {{url}}")
    >>> logging.warning(f"请求失败: {{url}}, 状态码 {{status}}")
    >>> logging.error(f"解析异常: {{url}}, 错误 {{e}}")

    >>> # 监控指标
    >>> stats = {{"success": 0, "fail": 0, "total": 0}}
    >>> stats["success"] += 1
    >>> rate = stats["success"] / stats["total"] * 100
    >>> logging.info(f"成功率: {{rate:.1f}}%")

{BD}四、爬虫架构设计{END}
    调度器 → 下载器 → 解析器 → 存储器
       |         |         |         |
    URL队列   请求网页   提取数据   写入数据库
       |                   |
       +---- 新URL --------+  (自动发现新链接)

{BD}五、合规与道德{END}
    1. 遵守 robots.txt
    2. 控制频率，不给服务器造成压力
    3. 不爬取个人隐私数据
    4. 尊重版权，标明数据来源
    5. 商业用途需获得授权

{DIM}>> 动手试试！{END}
    {C_}在代码实验室里写一个简单的 URL 去重函数{END}

{BD}六、分布式任务队列 Celery{END}
    >>> # pip install celery redis
    >>> from celery import Celery

    >>> app = Celery('tasks', broker='redis://localhost:6379/0')

    >>> @app.task
    ... def crawl_url(url):
    ...     # 耗时的爬取任务
    ...     return requests.get(url).text[:100]

    >>> # 调用：crawl_url.delay("https://example.com")
    >>> # Worker 启动：celery -A tasks worker --loglevel=info

{BD}七、错误处理与重试{END}
    >>> import time
    >>> from functools import wraps

    >>> def retry(times=3, delay=2):
    ...     def decorator(func):
    ...         @wraps(func)
    ...         def wrapper(*args, **kwargs):
    ...             for i in range(times):
    ...                 try:
    ...                     return func(*args, **kwargs)
    ...                 except Exception as e:
    ...                     if i == times - 1:
    ...                         raise
    ...                     time.sleep(delay)
    ...         return wrapper
    ...     return decorator

    >>> @retry(times=3, delay=1)
    ... def fetch(url):
    ...     return requests.get(url, timeout=10)

{BD}八、性能优化技巧{END}
    1. 批量写入数据库（1000条一写）
    2. 使用连接池（requests.Session）
    3. 压缩存储（gzip）
    4. 异步 I/O（aiohttp）

    >>> # 批量写入示例
    >>> batch = []
    >>> for item in items:
    ...     batch.append(item)
    ...     if len(batch) >= 1000:
    ...         cursor.executemany(sql, batch)
    ...         conn.commit()
    ...         batch.clear()
    >>> # 剩余数据
    >>> if batch:
    ...     cursor.executemany(sql, batch)
    ...     conn.commit()

{C_}爬虫工程化是生产环境必备技能{END}


""",
    ["mysql_store", "redis_cache", "logging_monitor", "crawl_architecture"]),
    # ==================== 阶段29：综合实战 — 数据方向 ====================
    29: (f"""{B}阶段29：综合实战 — 数据方向{END}

{C_}这一阶段带你完成完整的数据流水线{END}
    爬取数据 -> 清洗整理 -> 分析统计 -> 可视化呈现
    这就是数据分析师的日常工作流程！

{BD}一、数据流水线概念{END}
    数据流水线 = 数据从原始到可用的完整路径

    原始数据（脏）→ 清洗（去重/补缺/格式化）→ 分析（统计/分组/建模）→ 输出（图表/报告）

{BD}二、数据清洗实战技巧{END}
    >>> # 常见脏数据问题
    >>> # 1. 缺失值
    >>> df.dropna()                    # 删除缺失行
    >>> df.fillna(0)                   # 填充默认值
    >>> df["age"].fillna(df["age"].mean())  # 用均值填充

    >>> # 2. 重复数据
    >>> df.drop_duplicates()

    >>> # 3. 异常值
    >>> q1 = df["score"].quantile(0.25)
    >>> q3 = df["score"].quantile(0.75)
    >>> iqr = q3 - q1
    >>> mask = (df["score"] >= q1 - 1.5*iqr) & (df["score"] <= q3 + 1.5*iqr)
    >>> df_clean = df[mask]

    >>> # 4. 格式统一
    >>> df["date"] = pd.to_datetime(df["date"])
    >>> df["name"] = df["name"].str.strip().str.title()

{BD}三、自动化数据分析{END}
    >>> def analyze_data(filepath):
    ...     df = pd.read_csv(filepath)
    ...     # 自动报告
    ...     print(f"数据量: {{len(df)}} 行")
    ...     print(f"缺失率:\n{{df.isnull().mean()}}")
    ...     print(f"数值统计:\n{{df.describe()}}")
    ...     # 自动保存图表
    ...     df.hist(figsize=(10, 8))
    ...     plt.tight_layout()
    ...     plt.savefig("auto_analysis.png")

{BD}四、实战项目一：爬取名言 -> 保存 -> 分析{END}
    流程：
    1. requests 获取网页
    2. BeautifulSoup 提取名言、作者、标签
    3. 保存为 JSON/CSV
    4. pandas 读取分析
    5. matplotlib 可视化

{BD}五、实战项目二：天气数据分析{END}
    流程：
    1. 读取本地天气 CSV 数据
    2. pandas 清洗缺失值、异常值
    3. 计算月均温、最高温、最低温
    4. 画温度趋势图 + 降雨量柱状图
    5. 生成分析报告

{BD}六、实战项目三：个人记账本（OOP版）{END}
    流程：
    1. 用 OOP 设计 Account/Transaction 类
    2. 支持收入/支出/转账
    3. JSON 持久化存储
    4. 统计月度/年度报告表
    5. 数据可视化（支出分类饼图）

{C_}数据方向到此一段落，接下来进入自动化与桌面篇！{END}

{DIM}>> 动手试试！{END}
    {C_}选择一个项目，完整走一遍数据流水线{END}

{BD}七、数据质量检查{END}
    >>> def check_data_quality(df):
    ...     report = {{}}
    ...     report['total_rows'] = len(df)
    ...     report['null_counts'] = df.isnull().sum().to_dict()
    ...     report['duplicates'] = df.duplicated().sum()
    ...     report['dtypes'] = df.dtypes.astype(str).to_dict()
    ...     
    ...     # 数值列异常值检测
    ...     for col in df.select_dtypes(include='number'):
    ...         q1 = df[col].quantile(0.25)
    ...         q3 = df[col].quantile(0.75)
    ...         iqr = q3 - q1
    ...         outliers = ((df[col] < q1 - 1.5*iqr) | (df[col] > q3 + 1.5*iqr)).sum()
    ...         report[f'{{col}}_outliers'] = outliers
    ...     
    ...     return report

{BD}八、自动化报告生成{END}
    >>> def generate_report(df, output_path):
    ...     # 保存数据统计
    ...     with pd.ExcelWriter(output_path) as writer:
    ...         df.describe().to_excel(writer, sheet_name='统计')
    ...         df.head(100).to_excel(writer, sheet_name='样本')
    ...         
    ...         # 各列缺失率
    ...         missing = df.isnull().mean().sort_values(ascending=False)
    ...         missing.to_excel(writer, sheet_name='缺失率')
    ...     
    ...     print(f"报告已生成: {{output_path}}")

{BD}九、实战：爬取名言网站完整流程{END}
    >>> # Step 1: 分析网站结构
    >>> # quotes.toscrape.com
    >>>
    >>> # Step 2: 编写爬虫
    >>> import requests
    >>> from bs4 import BeautifulSoup
    >>> import pandas as pd
    >>>
    >>> quotes_data = []
    >>> for page in range(1, 11):  # 10页
    ...     url = f"https://quotes.toscrape.com/page/{{page}}/"
    ...     resp = requests.get(url)
    ...     soup = BeautifulSoup(resp.text, 'html.parser')
    ...     
    ...     for quote in soup.select('.quote'):
    ...         quotes_data.append({{
    ...             'text': quote.select_one('.text').text,
    ...             'author': quote.select_one('.author').text,
    ...             'tags': ', '.join(t.text for t in quote.select('.tag'))
    ...         }})
    >>>
    >>> # Step 3: 保存数据
    >>> df = pd.DataFrame(quotes_data)
    >>> df.to_csv('quotes.csv', index=False, encoding='utf-8')
    >>> print(f"爬取完成，共 {{len(df)}} 条名言")

{C_}完整数据流水线从爬取到分析，你已经掌握！{END}

""",
        ["crawl_requests", "data_cleaning", "pandas_basic", "matplotlib_vis"]),
}
