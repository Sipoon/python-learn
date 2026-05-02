"""Exercises for stages 26-29"""

EXERCISES_26_29 = {
        26: [
            {
                "id": "async_basic",
                "title": "异步函数定义",
                "desc": "定义一个异步函数并用 await 调用",
                "diff": "basic",
                "kp": [
                    "async_def",
                    "async_await"
                ],
                "template": "import asyncio\n\n____________ def greet(name):\n    print(f\"Hello, {{name}}!\")\n    ____________ asyncio.sleep(0.1)\n    print(f\"Goodbye, {{name}}!\")\n\nasyncio.run(greet(\"World\"))",
                "test_input": "",
                "answer": "import asyncio\n\nasync def greet(name):\n    print(f\"Hello, {{name}}!\")\n    await asyncio.sleep(0.1)\n    print(f\"Goodbye, {{name}}!\")\n\nasyncio.run(greet(\"World\"))",
                "expected": "Hello, World!\nGoodbye, World!",
                "explain": "async def 定义异步函数，await 等待异步操作完成。asyncio.run() 是事件循环的入口。",
                "difficulty": "basic"
            },
            {
                "id": "async_gather",
                "title": "并发执行 asyncio.gather",
                "desc": "用 gather 同时运行多个协程",
                "diff": "basic",
                "kp": [
                    "async_gather",
                    "async_def"
                ],
                "template": "import asyncio\n\nasync def task(name, seconds):\n    print(f\"{{name}} 开始\")\n    await asyncio.sleep(seconds)\n    return f\"{{name}} 完成\"\n\nasync def main():\n    results = ____________ asyncio.____________(\n        task(\"A\", 0.1),\n        task(\"B\", 0.1),\n    )\n    for r in results:\n        print(r)\n\nasyncio.run(main())",
                "test_input": "",
                "answer": "import asyncio\n\nasync def task(name, seconds):\n    print(f\"{{name}} 开始\")\n    await asyncio.sleep(seconds)\n    return f\"{{name}} 完成\"\n\nasync def main():\n    results = await asyncio.gather(\n        task(\"A\", 0.1),\n        task(\"B\", 0.1),\n    )\n    for r in results:\n        print(r)\n\nasyncio.run(main())",
                "expected": "A 开始\nB 开始\nA 完成\nB 完成",
                "explain": "asyncio.gather() 并发执行多个协程，比串行 await 快得多。返回结果顺序与输入一致。",
                "difficulty": "basic"
            },
            {
                "id": "async_aiohttp",
                "title": "异步HTTP请求",
                "desc": "用 aiohttp 异步获取网页",
                "diff": "intermediate",
                "kp": [
                    "async_aiohttp"
                ],
                "template": "import asyncio\nimport aiohttp\n\nasync def fetch(url):\n    ____________ aiohttp.ClientSession() as session:\n        async ____________ session.get(url) as resp:\n            return resp.status\n\nasync def main():\n    status = await fetch(\"https://httpbin.org/get\")\n    print(status)\n\nasyncio.run(main())",
                "test_input": "",
                "answer": "import asyncio\nimport aiohttp\n\nasync def fetch(url):\n    async with aiohttp.ClientSession() as session:\n        async with session.get(url) as resp:\n            return resp.status\n\nasync def main():\n    status = await fetch(\"https://httpbin.org/get\")\n    print(status)\n\nasyncio.run(main())",
                "expected": "200",
                "explain": "aiohttp 是异步HTTP客户端，async with session.get() 发起异步请求。配合 asyncio 高效爬取。",
                "difficulty": "intermediate"
            },
            {
                "id": "async_queue",
                "title": "异步队列 生产者-消费者",
                "desc": "用 asyncio.Queue 实现生产者-消费者模式",
                "diff": "intermediate",
                "kp": [
                    "async_def",
                    "async_gather"
                ],
                "template": "import asyncio\n\nasync def producer(queue, items):\n    for item in items:\n        await queue.____________(item)\n        print(f\"Produced: {{item}}\")\n    await queue.put(None)\n\nasync def consumer(queue):\n    while True:\n        item = await queue.____________()\n        if item is None:\n            break\n        print(f\"Consumed: {{item}}\")\n\nasync def main():\n    q = asyncio.Queue()\n    await asyncio.gather(producer(q, [1, 2, 3]), consumer(q))\n\nasyncio.run(main())",
                "test_input": "",
                "answer": "import asyncio\n\nasync def producer(queue, items):\n    for item in items:\n        await queue.put(item)\n        print(f\"Produced: {{item}}\")\n    await queue.put(None)  # sentinel\n\nasync def consumer(queue):\n    while True:\n        item = await queue.get()\n        if item is None:\n            queue.task_done()\n            break\n        print(f\"Consumed: {{item}}\")\n        queue.task_done()\n\nasync def main():\n    q = asyncio.Queue()\n    await asyncio.gather(producer(q, [1, 2, 3]), consumer(q))\n\nasyncio.run(main())",
                "expected": "Produced: 1\nConsumed: 1",
                "explain": "asyncio.Queue 异步队列，生产者 put() 放入数据，消费者 get() 取出。await queue.join() 等待全部处理完。",
                "difficulty": "intermediate"
            },
            {
                "id": "async_timeout",
                "title": "异步超时控制",
                "desc": "用 asyncio.wait_for 设置超时",
                "diff": "intermediate",
                "kp": [
                    "async_def",
                    "async_await"
                ],
                "template": "import asyncio\n\nasync def timeout_task():\n    try:\n        await asyncio.____________(asyncio.sleep(5), timeout=1.0)\n    except asyncio.____________:\n        print(\"Task timed out!\")\n\nasyncio.run(timeout_task())",
                "test_input": "",
                "answer": "import asyncio\n\nasync def timeout_task():\n    try:\n        await asyncio.wait_for(asyncio.sleep(5), timeout=1.0)\n    except asyncio.TimeoutError:\n        print(\"Task timed out!\")\n\nasyncio.run(timeout_task())",
                "expected": "Task timed out!",
                "explain": "asyncio.wait_for(coro, timeout) 设置超时，超时抛 asyncio.TimeoutError。防止请求永久挂起。",
                "difficulty": "intermediate"
            },
            {
                "id": "async_retry",
                "title": "异步重试机制",
                "desc": "异步函数中实现重试逻辑",
                "diff": "challenge",
                "kp": [
                    "async_def",
                    "async_await"
                ],
                "template": "import asyncio\n\nasync def task_with_retry(url, retries=3):\n    for i in range(retries):\n        try:\n            await asyncio.sleep(0.1)\n            if i < 2:\n                raise ConnectionError(f\"Attempt {{i+1}} failed\")\n            print(f\"Success on attempt {{i+1}}\")\n            return \"OK\"\n        except ConnectionError as e:\n            if i == ____________:\n                raise\n            print(f\"{{e}}, retrying...\")\n\nasyncio.run(task_with_retry(\"https://example.com\"))",
                "test_input": "",
                "answer": "import asyncio\n\nasync def task_with_retry(url, retries=3):\n    for i in range(retries):\n        try:\n            await asyncio.sleep(0.1)\n            if i < 2:\n                raise ConnectionError(f\"Attempt {{i+1}} failed\")\n            print(f\"Success on attempt {{i+1}}\")\n            return \"OK\"\n        except ConnectionError as e:\n            if i == retries - 1:\n                raise\n            print(f\"{{e}}, retrying...\")\n\nasyncio.run(task_with_retry(\"https://example.com\"))",
                "expected": "Attempt 1 failed, retrying...\nAttempt 2 failed, retrying...\nSuccess on attempt 3",
                "explain": "异步重试：while 循环 + try-except + await asyncio.sleep() 延迟。指数退避 backoff 更优雅。",
                "difficulty": "challenge"
            }
        ],
        27: [
            {
                "id": "scrapy_spider",
                "title": "Scrapy 爬虫定义",
                "desc": "补全一个 Scrapy Spider，解析 quote 的 text 和 author",
                "diff": "basic",
                "kp": [
                    "crawl_scrapy"
                ],
                "template": "import scrapy\n\nclass QuotesSpider(scrapy.Spider):\n    name = \"quotes\"\n    start_urls = [\"https://quotes.toscrape.com/\"]\n\n    def parse(self, response):\n        for quote in response.____________(\"div.quote\"):\n            yield {{\n                \"text\": quote.css(\"span.text::text\").____________(),\n                \"author\": quote.css(\"small.author::text\").get(),\n            }}",
                "test_input": "",
                "answer": "import scrapy\n\nclass QuotesSpider(scrapy.Spider):\n    name = \"quotes\"\n    start_urls = [\"https://quotes.toscrape.com/\"]\n\n    def parse(self, response):\n        for quote in response.css(\"div.quote\"):\n            yield {{\n                \"text\": quote.css(\"span.text::text\").get(),\n                \"author\": quote.css(\"small.author::text\").get(),\n            }}",
                "expected": "",
                "explain": "Scrapy Spider：name 唯一标识，start_urls 起始URL，parse() 解析响应并 yield 数据/请求。",
                "difficulty": "basic"
            },
            {
                "id": "scrapy_pipeline",
                "title": "Scrapy Pipeline",
                "desc": "写一个 Pipeline 把 item 写入 JSON 文件",
                "diff": "basic",
                "kp": [
                    "crawl_scrapy"
                ],
                "template": "import json\n\nclass JsonPipeline:\n    def open_spider(self, spider):\n        self.file = open(\"output.json\", \"w\", encoding=\"utf-8\")\n\n    def close_spider(self, spider):\n        self.file.____________()\n\n    def process_item(self, item, spider):\n        line = json.dumps(____________(item), ensure_ascii=False) + \"\\n\"\n        self.file.write(line)\n        return item",
                "test_input": "",
                "answer": "import json\n\nclass JsonPipeline:\n    def open_spider(self, spider):\n        self.file = open(\"output.json\", \"w\", encoding=\"utf-8\")\n\n    def close_spider(self, spider):\n        self.file.close()\n\n    def process_item(self, item, spider):\n        line = json.dumps(dict(item), ensure_ascii=False) + \"\\n\"\n        self.file.write(line)\n        return item",
                "expected": "",
                "explain": "Pipeline 处理 item：process_item() 接收每条数据，可做清洗、验证、存储。需在 settings 启用。",
                "difficulty": "intermediate"
            },
            {
                "id": "crawl_threadpool",
                "title": "线程池并发爬取",
                "desc": "用 ThreadPoolExecutor 并发获取多个URL的状态码",
                "diff": "intermediate",
                "kp": [
                    "crawl_concurrent"
                ],
                "template": "from concurrent.futures import ThreadPoolExecutor, as_completed\nimport requests\n\nurls = [\"https://httpbin.org/get\"] * 3\n\ndef fetch(url):\n    resp = requests.get(url, timeout=10)\n    return resp.status_code\n\nwith ThreadPoolExecutor(____________=5) as pool:\n    futures = {{pool.____________(fetch, url): url for url in urls}}\n    for future in as_completed(futures):\n        print(future.result())",
                "test_input": "",
                "answer": "from concurrent.futures import ThreadPoolExecutor, as_completed\nimport requests\n\nurls = [\"https://httpbin.org/get\"] * 3\n\ndef fetch(url):\n    resp = requests.get(url, timeout=10)\n    return resp.status_code\n\nwith ThreadPoolExecutor(max_workers=5) as pool:\n    futures = {{pool.submit(fetch, url): url for url in urls}}\n    for future in as_completed(futures):\n        print(future.result())",
                "expected": "200",
                "explain": "ThreadPoolExecutor 线程池并发：submit() 提交任务，as_completed() 按完成顺序获取结果。IO密集型首选。",
                "difficulty": "intermediate"
            },
            {
                "id": "crawl_incremental",
                "title": "增量爬取",
                "desc": "用 SQLite 记录已爬URL，跳过重复",
                "diff": "intermediate",
                "kp": [
                    "crawl_incremental"
                ],
                "template": "import sqlite3\n\nconn = sqlite3.connect(\"crawled.db\")\nconn.execute(\"CREATE TABLE IF NOT EXISTS urls (url TEXT PRIMARY KEY)\")\n\ndef is_crawled(url):\n    row = conn.execute(\"SELECT 1 FROM urls WHERE url=____________\", (url,)).fetchone()\n    return row ____________\n\ndef mark_crawled(url):\n    conn.execute(\"____________ INTO urls VALUES (?)\", (url,))\n    conn.commit()\n\n# 测试\nmark_crawled(\"https://example.com/1\")\nprint(is_crawled(\"https://example.com/1\"))\nprint(is_crawled(\"https://example.com/2\"))",
                "test_input": "",
                "answer": "import sqlite3\n\nconn = sqlite3.connect(\"crawled.db\")\nconn.execute(\"CREATE TABLE IF NOT EXISTS urls (url TEXT PRIMARY KEY)\")\n\ndef is_crawled(url):\n    row = conn.execute(\"SELECT 1 FROM urls WHERE url=?\", (url,)).fetchone()\n    return row is not None\n\ndef mark_crawled(url):\n    conn.execute(\"INSERT OR IGNORE INTO urls VALUES (?)\", (url,))\n    conn.commit()\n\nmark_crawled(\"https://example.com/1\")\nprint(is_crawled(\"https://example.com/1\"))\nprint(is_crawled(\"https://example.com/2\"))",
                "expected": "True\nFalse",
                "explain": "增量爬取：记录已爬URL（set/文件/数据库），跳过重复。节省时间避免重复数据。",
                "difficulty": "challenge"
            },
            {
                "id": "crawl_scrapy_follow",
                "title": "Scrapy 自动翻页",
                "desc": "在 parse 方法中添加自动翻页逻辑",
                "diff": "challenge",
                "kp": [
                    "crawl_scrapy"
                ],
                "template": "import scrapy\n\nclass QuotesSpider(scrapy.Spider):\n    name = \"quotes\"\n    start_urls = [\"https://quotes.toscrape.com/\"]\n\n    def parse(self, response):\n        for quote in response.css(\"div.quote\"):\n            yield {{\n                \"text\": quote.css(\"span.text::text\").get(),\n            }}\n        next_page = response.css(\"li.next a::attr(href)\").get()\n        if next_page:\n            yield response.____________(next_page, callback=self.____________)",
                "test_input": "",
                "answer": "import scrapy\n\nclass QuotesSpider(scrapy.Spider):\n    name = \"quotes\"\n    start_urls = [\"https://quotes.toscrape.com/\"]\n\n    def parse(self, response):\n        for quote in response.css(\"div.quote\"):\n            yield {{\n                \"text\": quote.css(\"span.text::text\").get(),\n            }}\n        next_page = response.css(\"li.next a::attr(href)\").get()\n        if next_page:\n            yield response.follow(next_page, callback=self.parse)",
                "expected": "",
                "explain": "Scrapy 自动翻页：response.follow(url, callback) 生成新请求，parse 内 yield 递归爬取下一页。",
                "difficulty": "challenge"
            }
        ],
        28: [
            {
                "id": "spider_mysql_insert",
                "title": "MySQL 插入数据",
                "desc": "用 pymysql 插入一条文章记录并去重",
                "diff": "basic",
                "kp": [
                    "crawl_mysql"
                ],
                "template": "import pymysql\n\nconn = pymysql.connect(host=\"localhost\", user=\"root\",\n                       password=\"\", database=\"spider_db\")\ncursor = conn.cursor()\n\nsql = \"____________ INTO articles (title, url) VALUES (%s, %s)\"\ncursor.execute(sql, (\"Python入门\", \"https://example.com/1\"))\nconn.____________()\nconn.close()",
                "test_input": "",
                "answer": "import pymysql\n\nconn = pymysql.connect(host=\"localhost\", user=\"root\",\n                       password=\"\", database=\"spider_db\")\ncursor = conn.cursor()\n\nsql = \"INSERT IGNORE INTO articles (title, url) VALUES (%s, %s)\"\ncursor.execute(sql, (\"Python入门\", \"https://example.com/1\"))\nconn.commit()\nconn.close()",
                "expected": "",
                "explain": "pymysql 连接 MySQL，cursor.executemany() 批量插入比循环 execute() 高效。参数化查询防SQL注入。",
                "difficulty": "basic"
            },
            {
                "id": "spider_redis_dedup",
                "title": "Redis URL去重",
                "desc": "用 Redis Set 检查和记录已爬URL",
                "diff": "basic",
                "kp": [
                    "crawl_redis"
                ],
                "template": "import redis\n\nr = redis.Redis(host=\"localhost\", port=6379, db=0)\n\ndef is_crawled(url):\n    return r.____________(\"crawled:urls\", url)\n\ndef mark_crawled(url):\n    r.____________(\"crawled:urls\", url)\n\nmark_crawled(\"https://example.com/1\")\nprint(is_crawled(\"https://example.com/1\"))\nprint(is_crawled(\"https://example.com/2\"))",
                "test_input": "",
                "answer": "import redis\n\nr = redis.Redis(host=\"localhost\", port=6379, db=0)\n\ndef is_crawled(url):\n    return r.sismember(\"crawled:urls\", url)\n\ndef mark_crawled(url):\n    r.sadd(\"crawled:urls\", url)\n\nmark_crawled(\"https://example.com/1\")\nprint(is_crawled(\"https://example.com/1\"))\nprint(is_crawled(\"https://example.com/2\"))",
                "expected": "",
                "explain": "Redis Set 去重：sadd() 添加URL，返回1表示新URL，0表示已存在。O(1) 查询效率极高。",
                "difficulty": "basic"
            },
            {
                "id": "spider_logging",
                "title": "爬虫日志配置",
                "desc": "配置同时输出到文件和终端的日志",
                "diff": "intermediate",
                "kp": [
                    "crawl_logging"
                ],
                "template": "import logging\n\nlogging.basicConfig(\n    level=logging.____________,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    handlers=[\n        logging.FileHandler(\"spider.log\", encoding=\"utf-8\"),\n        logging.____________(),\n    ]\n)\nlogger = logging.getLogger(\"spider\")\nlogger.info(\"爬虫启动\")",
                "test_input": "",
                "answer": "import logging\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    handlers=[\n        logging.FileHandler(\"spider.log\", encoding=\"utf-8\"),\n        logging.StreamHandler(),\n    ]\n)\nlogger = logging.getLogger(\"spider\")\nlogger.info(\"爬虫启动\")",
                "expected": "",
                "explain": "logging 模块配置：FileHandler 写文件，Formatter 定义格式。按级别 DEBUG/INFO/ERROR 过滤日志。",
                "difficulty": "intermediate"
            },
            {
                "id": "spider_queue_redis",
                "title": "Redis 请求队列",
                "desc": "用 Redis List 实现 FIFO 爬取队列",
                "diff": "challenge",
                "kp": [
                    "crawl_redis"
                ],
                "template": "import redis\n\nr = redis.Redis(host=\"localhost\", port=6379, db=0)\n\n# 入队（生产者）\ndef push_url(url):\n    r.____________(\"queue:urls\", url)\n\n# 出队（消费者）— FIFO\ndef pop_url():\n    return r.____________(\"queue:urls\")\n\npush_url(\"https://example.com/1\")\npush_url(\"https://example.com/2\")\nprint(pop_url())  # 应该是第一个入队的",
                "test_input": "",
                "answer": "import redis\n\nr = redis.Redis(host=\"localhost\", port=6379, db=0)\n\ndef push_url(url):\n    r.lpush(\"queue:urls\", url)\n\ndef pop_url():\n    return r.rpop(\"queue:urls\")\n\npush_url(\"https://example.com/1\")\npush_url(\"https://example.com/2\")\nprint(pop_url())",
                "expected": "",
                "explain": "Redis List 做请求队列：lpush/rpush 入队，rpop/lpop 出队。支持多消费者分布式爬虫。",
                "difficulty": "challenge"
            }
        ],
        29: [
            {
                "id": "s29_01",
                "title": "综合题：用 json.dumps 把列表 [{'name':'张三','score':90}] 转为格式化 JSON 字符串并打印",
                "desc": "综合题：用 json.dumps 把列表 [{'name':'张三','score':90}] 转为格式化 JSON 字符串并打印",
                "diff": "basic",
                "kp": [
                    "json_advanced",
                    "print_basic"
                ],
                "hint": "json.dumps(data, ensure_ascii=False, indent=2)",
                "answer": "import json\ndata = [{\"name\": \"张三\", \"score\": 90}]\nresult = json.dumps(data, ensure_ascii=False, indent=2)\nprint(result)",
                "explain": "json.dumps() 序列化，ensure_ascii=False 保留中文，indent=2 美化格式。综合文件+模块知识。",
                "template": "import json\ndata = ...  # TODO\nresult = ...  # TODO"
            },
            {
                "id": "s29_02",
                "title": "综合题：创建 Student 类（name, scores列表），有 average() 方法，用 @classmethod from_dict 创建对象",
                "desc": "综合题：创建 Student 类（name, scores列表），有 average() 方法，用 @classmethod from_dict 创建对象",
                "diff": "intermediate",
                "kp": [
                    "oop_classmethod",
                    "oop_class_object",
                    "print_basic"
                ],
                "hint": "@classmethod def from_dict(cls, d): return cls(d['name'], d['scores'])",
                "answer": "class Student:\n    def __init__(self, name, scores):\n        self.name = name\n        self.scores = scores\n    def average(self):\n        return sum(self.scores) / len(self.scores)\n    @classmethod\n    def from_dict(cls, data):\n        return cls(data[\"name\"], data[\"scores\"])\n\ns = Student.from_dict({\"name\": \"张三\", \"scores\": [90, 85, 92]})\nprint(f\"{s.name}的平均分：{s.average():.1f}\")",
                "explain": "类+方法组合：__init__ 初始化，average() 计算均值(sum/len)。面向对象封装数据和行为。",
                "template": "class Student:\n    pass  # TODO\n    def __init__(self, name, scores):\n        pass  # TODO\n        self.name = ...  # TODO\n        self.scores = ...  # TODO\n    def average(self):\n        pass  # TODO\n    def from_dict(cls, data):\n        pass  # TODO\ns = ...  # TODO"
            },
            {
                "id": "s29_03",
                "title": "综合题：写一个 @timer 装饰器，打印被装饰函数的执行时间，应用到 add 函数上测试",
                "desc": "综合题：写一个 @timer 装饰器，打印被装饰函数的执行时间，应用到 add 函数上测试",
                "diff": "intermediate",
                "kp": [
                    "dec_basic",
                    "print_basic"
                ],
                "hint": "import time; def timer(func): wrapper...",
                "answer": "import time\n\ndef timer(func):\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        elapsed = time.time() - start\n        print(f\"{func.__name__}耗时{elapsed:.6f}秒\")\n        return result\n    return wrapper\n\n@timer\ndef add(a, b):\n    return a + b\n\nprint(add(3, 5))",
                "explain": "装饰器+模块：time.perf_counter() 高精度计时，@timer 装饰器自动包裹函数。两种知识融合。",
                "template": "import time\ndef timer(func):\n    pass  # TODO\n    def wrapper(*args, **kwargs):\n        pass  # TODO\n        start = ...  # TODO\n        result = ...  # TODO\n        elapsed = ...  # TODO\ndef add(a, b):\n    pass  # TODO"
            },
            {
                "id": "s29_04",
                "title": "综合题：用 pandas 创建 DataFrame，groupby 分组计算均值，打印结果",
                "desc": "综合题：用 pandas 创建 DataFrame，groupby 分组计算均值，打印结果",
                "diff": "challenge",
                "kp": [
                    "pandas_process",
                    "print_basic"
                ],
                "hint": "df.groupby('列名')['值列'].mean()",
                "answer": "import pandas as pd\ndata = {\"班级\": [\"A\", \"A\", \"B\", \"B\"], \"成绩\": [90, 85, 88, 92]}\ndf = pd.DataFrame(data)\nprint(df.groupby(\"班级\")[\"成绩\"].mean())",
                "explain": "pandas groupby 分组聚合：df.groupby('列名').mean() 求各组均值。数据分析核心操作。",
                "template": "import pandas as pd\ndata = ...  # TODO\ndf = ...  # TODO"
            },
            {
                "id": "s29_05",
                "title": "综合挑战：用 re + json 组合，提取字符串中的所有数字，构建 {\"numbers\":[...]} 的 JSON 并打印",
                "desc": "综合挑战：用 re + json 组合，提取字符串中的所有数字，构建 {\"numbers\":[...]} 的 JSON 并打印",
                "diff": "challenge",
                "kp": [
                    "regex_basic",
                    "json_advanced",
                    "print_basic"
                ],
                "hint": "re.findall(r'\\d+', text); json.dumps(...)",
                "answer": "import re\nimport json\ntext = \"价格25元，优惠10元，合计15元\"\nnums = re.findall(r\"\\d+\", text)\nresult = json.dumps({\"numbers\": nums}, ensure_ascii=False)\nprint(result)",
                "explain": "re.findall 提取数字 + json.dumps 构建结构化数据。正则+JSON组合处理文本。",
                "template": "import re\nimport json\ntext = ...  # TODO\nnums = ...  # TODO\nresult = ...  # TODO"
            }
        ]
    }
