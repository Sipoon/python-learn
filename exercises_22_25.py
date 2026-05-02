"""Exercises for stages 22-25"""

EXERCISES_22_25 = {
        22: [
            {
                "id": "s22_01",
                "title": "用 requests.get 获取 https://httpbin.org/get 的状态码并打印",
                "desc": "用 requests.get 获取 https://httpbin.org/get 的状态码并打印",
                "diff": "basic",
                "kp": [
                    "crawl_requests",
                    "print_basic"
                ],
                "hint": "import requests; response.status_code",
                "answer": "import requests\nresponse = requests.get(\"https://httpbin.org/get\", timeout=10)\nprint(response.status_code)",
                "explain": "requests.get() 发起HTTP GET请求，.status_code 获取状态码。200表示成功，4xx/5xx表示错误。",
                "template": "import requests\nresponse = ...  # TODO"
            },
            {
                "id": "s22_02",
                "title": "用 BeautifulSoup 解析 HTML '<p>Hello</p><p>World</p>'，提取所有 p 标签的文本并打印",
                "desc": "用 BeautifulSoup 解析 HTML '<p>Hello</p><p>World</p>'，提取所有 p 标签的文本并打印",
                "diff": "basic",
                "kp": [
                    "crawl_beautifulsoup",
                    "print_basic"
                ],
                "hint": "soup.find_all('p')",
                "answer": "from bs4 import BeautifulSoup\nhtml = \"<p>Hello</p><p>World</p>\"\nsoup = BeautifulSoup(html, \"html.parser\")\nfor p in soup.find_all(\"p\"):\n    print(p.text)",
                "explain": "BeautifulSoup(html, 'html.parser') 解析HTML，.find_all('p') 找所有<p>标签，.text 取文本内容。",
                "template": "from bs4 import BeautifulSoup\nhtml = ...  # TODO\nsoup = ...  # TODO"
            },
            {
                "id": "s22_03",
                "title": "用 BeautifulSoup 的 CSS 选择器提取 '<ul><li>A</li><li>B</li></ul>' 中所有 li 的文本",
                "desc": "用 BeautifulSoup 的 CSS 选择器提取 '<ul><li>A</li><li>B</li></ul>' 中所有 li 的文本",
                "diff": "basic",
                "kp": [
                    "crawl_selectors",
                    "print_basic"
                ],
                "hint": "soup.select('ul li')",
                "answer": "from bs4 import BeautifulSoup\nhtml = \"<ul><li>A</li><li>B</li></ul>\"\nsoup = BeautifulSoup(html, \"html.parser\")\nfor li in soup.select(\"ul li\"):\n    print(li.text)",
                "explain": "CSS选择器 select('ul li') 按CSS规则定位元素。比 find_all 更灵活，支持类名、属性等复杂选择。",
                "template": "from bs4 import BeautifulSoup\nhtml = ...  # TODO\nsoup = ...  # TODO"
            },
            {
                "id": "s22_04",
                "title": "写一个函数 crawl_page(url) 获取网页，加上 timeout=10 和 try-except 处理异常",
                "desc": "写一个函数 crawl_page(url) 获取网页，加上 timeout=10 和 try-except 处理异常",
                "diff": "intermediate",
                "kp": [
                    "crawl_requests",
                    "crawl_ethics",
                    "print_basic"
                ],
                "hint": "try: requests.get(url, timeout=10); except requests.RequestException: ...",
                "answer": "import requests\n\ndef crawl_page(url):\n    try:\n        response = requests.get(url, timeout=10)\n        response.raise_for_status()\n        return response.text[:100]\n    except requests.RequestException as e:\n        return f\"请求失败：{e}\"\n\nprint(crawl_page(\"https://httpbin.org/get\"))",
                "explain": "timeout=10 防止请求卡死，raise_for_status() 检查HTTP状态码。生产爬虫必备的健壮性处理。",
                "template": "import requests\ndef crawl_page(url):\n    pass  # TODO\n        response = ...  # TODO"
            },
            {
                "id": "s22_05",
                "title": "把列表 data=[{\"name\":\"张三\",\"age\":25},{\"name\":\"李四\",\"age\":30}] 保存为 JSON 文件（用代码模拟，直接打印 json 字符串）",
                "desc": "把列表 data=[{\"name\":\"张三\",\"age\":25},{\"name\":\"李四\",\"age\":30}] 保存为 JSON 文件（用代码模拟，直接打印 json 字符串）",
                "diff": "intermediate",
                "kp": [
                    "crawl_save",
                    "print_basic"
                ],
                "hint": "json.dumps(data, ensure_ascii=False, indent=2)",
                "answer": "import json\ndata = [{\"name\": \"张三\", \"age\": 25}, {\"name\": \"李四\", \"age\": 30}]\nresult = json.dumps(data, ensure_ascii=False, indent=2)\nprint(result)",
                "explain": "json.dumps(data, ensure_ascii=False, indent=2) 美化输出中文。ensure_ascii=False 保留中文字符。",
                "template": "import json\ndata = ...  # TODO\nresult = ...  # TODO"
            }
        ],
        23: [
            {
                "id": "s23_01",
                "title": "用 pandas 创建 DataFrame：姓名=[\"张三\",\"李四\",\"王五\"], 薪资=[8000,12000,10000]，打印整个 DataFrame",
                "desc": "用 pandas 创建 DataFrame：姓名=[\"张三\",\"李四\",\"王五\"], 薪资=[8000,12000,10000]，打印整个 DataFrame",
                "diff": "basic",
                "kp": [
                    "pandas_dataframe",
                    "print_basic"
                ],
                "hint": "pd.DataFrame({'姓名':..., '薪资':...})",
                "answer": "import pandas as pd\ndata = {\"姓名\": [\"张三\", \"李四\", \"王五\"], \"薪资\": [8000, 12000, 10000]}\ndf = pd.DataFrame(data)\nprint(df)",
                "explain": "pd.DataFrame() 创建数据框，字典的键是列名，值列表是列数据。pandas 核心数据结构。",
                "template": "import pandas as pd\ndata = ...  # TODO\ndf = ...  # TODO"
            },
            {
                "id": "s23_02",
                "title": "对上面创建的 DataFrame，筛选薪资大于9000的行并打印",
                "desc": "对上面创建的 DataFrame，筛选薪资大于9000的行并打印",
                "diff": "basic",
                "kp": [
                    "pandas_select",
                    "print_basic"
                ],
                "hint": "df[df['薪资'] > 9000]",
                "answer": "import pandas as pd\ndata = {\"姓名\": [\"张三\", \"李四\", \"王五\"], \"薪资\": [8000, 12000, 10000]}\ndf = pd.DataFrame(data)\nprint(df[df[\"薪资\"] > 9000])",
                "explain": "布尔索引 df[df['薪资']>9000] 筛选满足条件的行，类似SQL的 WHERE 子句。",
                "template": "import pandas as pd\ndata = ...  # TODO\ndf = ...  # TODO"
            },
            {
                "id": "s23_03",
                "title": "创建 DataFrame 并添加一列 \"年薪\" = 薪资*12，按薪资降序排列打印",
                "desc": "创建 DataFrame 并添加一列 \"年薪\" = 薪资*12，按薪资降序排列打印",
                "diff": "intermediate",
                "kp": [
                    "pandas_process",
                    "print_basic"
                ],
                "hint": "df['年薪'] = df['薪资'] * 12; df.sort_values('薪资', ascending=False)",
                "answer": "import pandas as pd\ndata = {\"姓名\": [\"张三\", \"李四\", \"王五\"], \"薪资\": [8000, 12000, 10000]}\ndf = pd.DataFrame(data)\ndf[\"年薪\"] = df[\"薪资\"] * 12\nprint(df.sort_values(\"薪资\", ascending=False))",
                "explain": "df['新列'] = 表达式 添加新列，df.sort_values(by, ascending=False) 降序排列。",
                "template": "import pandas as pd\ndata = ...  # TODO\ndf = ...  # TODO\ndf[\"年薪\"] = ...  # TODO"
            },
            {
                "id": "s23_04",
                "title": "用 csv.DictReader 读取字符串数据（用 io.StringIO 模拟文件），打印每行的 name 字段",
                "desc": "用 csv.DictReader 读取字符串数据（用 io.StringIO 模拟文件），打印每行的 name 字段",
                "diff": "intermediate",
                "kp": [
                    "csv_advanced",
                    "print_basic"
                ],
                "hint": "import io, csv; f = io.StringIO('name,age\\n张三,25\\n'); reader = csv.DictReader(f)",
                "answer": "import csv\nimport io\ncsv_data = \"name,age\\n张三,25\\n李四,30\\n\"\nf = io.StringIO(csv_data)\nreader = csv.DictReader(f)\nfor row in reader:\n    print(row[\"name\"])",
                "explain": "csv.DictReader 将每行转为字典，io.StringIO 模拟文件对象，适合测试无需创建真实文件。",
                "template": "import csv\nimport io\ncsv_data = ...  # TODO\nf = ...  # TODO\nreader = ...  # TODO"
            },
            {
                "id": "s23_05",
                "title": "用 json.loads 解析 '{\"name\":\"张三\",\"scores\":[90,85,92]}'，打印平均分",
                "desc": "用 json.loads 解析 '{\"name\":\"张三\",\"scores\":[90,85,92]}'，打印平均分",
                "diff": "intermediate",
                "kp": [
                    "json_advanced",
                    "print_basic"
                ],
                "hint": "json.loads(s); sum(data['scores'])/len(data['scores'])",
                "answer": "import json\ntext = '{\"name\":\"张三\",\"scores\":[90,85,92]}'\ndata = json.loads(text)\navg = sum(data[\"scores\"]) / len(data[\"scores\"])\nprint(f\"{data['name']}的平均分：{avg:.1f}\")",
                "explain": "json.loads() 解析JSON字符串为Python对象。嵌套数据用 ['key']['subkey'] 逐层访问。",
                "template": "import json\ntext = ...  # TODO\ndata = ...  # TODO\navg = ...  # TODO"
            }
        ],
        24: [
            {
                "id": "s24_01",
                "title": "用 matplotlib 画折线图：x=[1,2,3,4,5], y=[10,20,15,25,30]，保存为 trend.png",
                "desc": "用 matplotlib 画折线图：x=[1,2,3,4,5], y=[10,20,15,25,30]，保存为 trend.png",
                "diff": "basic",
                "kp": [
                    "viz_line",
                    "print_basic"
                ],
                "hint": "plt.plot(x, y); plt.savefig('trend.png')",
                "answer": "import matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nx = [1, 2, 3, 4, 5]\ny = [10, 20, 15, 25, 30]\nplt.figure(figsize=(8, 5))\nplt.plot(x, y, marker=\"o\")\nplt.title(\"Trend\")\nplt.savefig(\"trend.png\", dpi=100, bbox_inches=\"tight\")\nprint(\"图表已保存\")",
                "explain": "plt.plot(x, y) 画折线图，plt.title/plt.xlabel/plt.ylabel 添加标题和轴标签，plt.show() 显示。",
                "template": "import matplotlib\nimport matplotlib.pyplot as plt\nx = ...  # TODO\ny = ...  # TODO\nplt.figure(figsize = ...  # TODO\nplt.plot(x, y, marker = ...  # TODO\nplt.savefig(\"trend.png\", dpi = ...  # TODO"
            },
            {
                "id": "s24_02",
                "title": "用 plt.bar 画柱状图：标签=[\"A\",\"B\",\"C\"]，值=[30,50,40]，保存为 bar.png",
                "desc": "用 plt.bar 画柱状图：标签=[\"A\",\"B\",\"C\"]，值=[30,50,40]，保存为 bar.png",
                "diff": "basic",
                "kp": [
                    "viz_bar",
                    "print_basic"
                ],
                "hint": "plt.bar(labels, values)",
                "answer": "import matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nlabels = [\"A\", \"B\", \"C\"]\nvalues = [30, 50, 40]\nplt.figure(figsize=(8, 5))\nplt.bar(labels, values)\nplt.title(\"Bar Chart\")\nplt.savefig(\"bar.png\", dpi=100, bbox_inches=\"tight\")\nprint(\"图表已保存\")",
                "explain": "plt.bar(labels, values) 画柱状图。barh() 画水平柱状图。color 参数指定颜色。",
                "template": "import matplotlib\nimport matplotlib.pyplot as plt\nlabels = ...  # TODO\nvalues = ...  # TODO\nplt.figure(figsize = ...  # TODO\nplt.savefig(\"bar.png\", dpi = ...  # TODO"
            },
            {
                "id": "s24_03",
                "title": "用 plt.pie 画饼图：labels=[\"A\",\"B\",\"C\"], sizes=[40,35,25]，autopct='%1.1f%%'，保存为 pie.png",
                "desc": "用 plt.pie 画饼图：labels=[\"A\",\"B\",\"C\"], sizes=[40,35,25]，autopct='%1.1f%%'，保存为 pie.png",
                "diff": "intermediate",
                "kp": [
                    "viz_pie",
                    "print_basic"
                ],
                "hint": "plt.pie(sizes, labels=labels, autopct='%1.1f%%')",
                "answer": "import matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nlabels = [\"A\", \"B\", \"C\"]\nsizes = [40, 35, 25]\nplt.figure(figsize=(7, 7))\nplt.pie(sizes, labels=labels, autopct=\"%1.1f%%\")\nplt.title(\"Pie Chart\")\nplt.savefig(\"pie.png\", dpi=100, bbox_inches=\"tight\")\nprint(\"图表已保存\")",
                "explain": "plt.pie(sizes, labels=, autopct='%1.1f%%') 画饼图，autopct 显示百分比。startangle 控制起始角度。",
                "template": "import matplotlib\nimport matplotlib.pyplot as plt\nlabels = ...  # TODO\nsizes = ...  # TODO\nplt.figure(figsize = ...  # TODO\nplt.pie(sizes, labels = ...  # TODO\nplt.savefig(\"pie.png\", dpi = ...  # TODO"
            },
            {
                "id": "s24_04",
                "title": "用 plt.subplots(1,2) 画两个子图：左边折线图，右边柱状图，保存为 subplots.png",
                "desc": "用 plt.subplots(1,2) 画两个子图：左边折线图，右边柱状图，保存为 subplots.png",
                "diff": "challenge",
                "kp": [
                    "viz_subplots",
                    "print_basic"
                ],
                "hint": "fig, axes = plt.subplots(1, 2); axes[0].plot(...); axes[1].bar(...)",
                "answer": "import matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nfig, axes = plt.subplots(1, 2, figsize=(12, 5))\naxes[0].plot([1, 2, 3], [10, 20, 15], marker=\"o\")\naxes[0].set_title(\"Line\")\naxes[1].bar([\"A\", \"B\", \"C\"], [30, 50, 40])\naxes[1].set_title(\"Bar\")\nplt.tight_layout()\nplt.savefig(\"subplots.png\", dpi=100, bbox_inches=\"tight\")\nprint(\"图表已保存\")",
                "explain": "plt.subplots(1,2) 创建1行2列子图，axes[0]/axes[1] 分别操作。plt.savefig() 保存为文件。",
                "template": "import matplotlib\nimport matplotlib.pyplot as plt\nfig, axes = ...  # TODO\naxes[0].plot([1, 2, 3], [10, 20, 15], marker = ...  # TODO\nplt.savefig(\"subplots.png\", dpi = ...  # TODO"
            }
        ],
        25: [
            {
                "id": "crawl_selenium_wait",
                "title": "Selenium 显式等待",
                "desc": "补全代码，等待 class='title' 的元素出现后获取文本",
                "diff": "basic",
                "kp": [
                    "crawl_selenium",
                    "crawl_wait"
                ],
                "template": "from selenium.webdriver.common.by import By\nfrom selenium.webdriver.support.ui import WebDriverWait\nfrom selenium.webdriver.support import expected_conditions as EC\n\n# driver 已启动并打开了页面\nwait = WebDriverWait(driver, 10)\nelement = wait.until(\n    EC.____________((\n        By.____________, \"title\"\n    ))\n)\nprint(element.text)",
                "test_input": "",
                "answer": "from selenium.webdriver.common.by import By\nfrom selenium.webdriver.support.ui import WebDriverWait\nfrom selenium.webdriver.support import expected_conditions as EC\n\nwait = WebDriverWait(driver, 10)\nelement = wait.until(\n    EC.presence_of_element_located((\n        By.CLASS_NAME, \"title\"\n    ))\n)\nprint(element.text)",
                "expected": "标题文本",
                "explain": "WebDriverWait 显式等待：等某个条件满足再继续，比 time.sleep() 更智能高效。",
                "difficulty": "basic"
            },
            {
                "id": "crawl_session_login",
                "title": "Session 保持登录态",
                "desc": "用 requests.Session 先登录再访问需要登录的页面",
                "diff": "basic",
                "kp": [
                    "crawl_session",
                    "crawl_requests"
                ],
                "template": "import requests\n\nsession = requests.____________()\nlogin_data = {\"username\": \"admin\", \"password\": \"123456\"}\nsession.post(\"https://httpbin.org/post\", data=login_data)\n\nresp = session.____________(\"https://httpbin.org/cookies\")\nprint(resp.status_code)",
                "test_input": "",
                "answer": "import requests\n\nsession = requests.Session()\nlogin_data = {\"username\": \"admin\", \"password\": \"123456\"}\nsession.post(\"https://httpbin.org/post\", data=login_data)\n\nresp = session.get(\"https://httpbin.org/cookies\")\nprint(resp.status_code)",
                "expected": "200",
                "explain": "requests.Session() 保持 cookies 和连接，登录后的请求自动携带 session 信息。",
                "difficulty": "basic"
            },
            {
                "id": "crawl_ua_delay",
                "title": "反爬：UA伪装+随机延时",
                "desc": "写一个带UA伪装和随机延时的请求函数",
                "diff": "intermediate",
                "kp": [
                    "crawl_anti",
                    "crawl_requests"
                ],
                "template": "import requests\nimport time\nimport random\n\ndef safe_fetch(url):\n    headers = {\n        \"____________\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64)\"\n    }\n    time.____________(random.uniform(1, 3))\n    resp = requests.get(url, ____________=headers, timeout=10)\n    return resp.status_code\n\nprint(safe_fetch(\"https://httpbin.org/get\"))",
                "test_input": "",
                "answer": "import requests\nimport time\nimport random\n\ndef safe_fetch(url):\n    headers = {\n        \"User-Agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64)\"\n    }\n    time.sleep(random.uniform(1, 3))\n    resp = requests.get(url, headers=headers, timeout=10)\n    return resp.status_code\n\nprint(safe_fetch(\"https://httpbin.org/get\"))",
                "expected": "200",
                "explain": "User-Agent 伪装浏览器，random.uniform() 随机延时避免被反爬检测。基本爬虫礼仪。",
                "difficulty": "intermediate"
            },
            {
                "id": "crawl_proxy_retry",
                "title": "代理+重试机制",
                "desc": "配置代理和自动重试3次的请求",
                "diff": "intermediate",
                "kp": [
                    "crawl_anti",
                    "crawl_proxy"
                ],
                "template": "import requests\nfrom urllib3.util.retry import Retry\nfrom requests.adapters import HTTPAdapter\n\nsession = requests.Session()\nretry = Retry(____________=3, backoff_factor=1)\nadapter = HTTPAdapter(max_retries=retry)\nsession.____________(\"https://\", adapter)\n\nresp = session.get(\"https://httpbin.org/get\", timeout=10)\nprint(resp.status_code)",
                "test_input": "",
                "answer": "import requests\nfrom urllib3.util.retry import Retry\nfrom requests.adapters import HTTPAdapter\n\nsession = requests.Session()\nretry = Retry(total=3, backoff_factor=1)\nadapter = HTTPAdapter(max_retries=retry)\nsession.mount(\"https://\", adapter)\n\nresp = session.get(\"https://httpbin.org/get\", timeout=10)\nprint(resp.status_code)",
                "expected": "200",
                "explain": "代理 proxies={'http':'url'} 隐藏真实IP，retry 循环处理连接失败。反封禁策略。",
                "difficulty": "intermediate"
            },
            {
                "id": "crawl_playwright_basic",
                "title": "Playwright 基础",
                "desc": "用 Playwright 打开页面并等待元素",
                "diff": "challenge",
                "kp": [
                    "crawl_playwright"
                ],
                "template": "from playwright.sync_api import sync_playwright\n\nwith sync_playwright() as p:\n    browser = p.chromium.launch(____________=True)\n    page = browser.new_page()\n    page.goto(\"https://example.com\")\n    page.____________(\"h1\")\n    title = page.query_selector(\"h1\").inner_text()\n    print(title)\n    browser.close()",
                "test_input": "",
                "answer": "from playwright.sync_api import sync_playwright\n\nwith sync_playwright() as p:\n    browser = p.chromium.launch(headless=True)\n    page = browser.new_page()\n    page.goto(\"https://example.com\")\n    page.wait_for_selector(\"h1\")\n    title = page.query_selector(\"h1\").inner_text()\n    print(title)\n    browser.close()",
                "expected": "Example Domain",
                "explain": "Playwright 是新一代浏览器自动化工具，支持 Chromium/Firefox/WebKit，API 比 Selenium 更现代。",
                "difficulty": "challenge"
            }
        ]
    }
