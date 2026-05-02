"""Exercises for stages 30-33"""

EXERCISES_30_33 = {
        30: [
            {
                "id": "s30_01",
                "title": "用 pathlib 获取当前目录下所有 .py 文件名并打印",
                "desc": "用 pathlib 获取当前目录下所有 .py 文件名并打印",
                "diff": "basic",
                "kp": [
                    "auto_pathlib",
                    "print_basic"
                ],
                "hint": "Path('.').glob('*.py')",
                "answer": "from pathlib import Path\nfor f in Path(\".\").glob(\"*.py\"):\n    print(f.name)",
                "explain": "Path.glob('*.py') 匹配文件模式，比 os.listdir+endswith 更优雅。pathlib 是现代路径库。",
                "template": "from pathlib import Path"
            },
            {
                "id": "s30_02",
                "title": "用 os.path 拼接路径 'data' 和 'report.csv'，打印结果",
                "desc": "用 os.path 拼接路径 'data' 和 'report.csv'，打印结果",
                "diff": "basic",
                "kp": [
                    "auto_os",
                    "print_basic"
                ],
                "hint": "os.path.join('data', 'report.csv')",
                "answer": "import os\nprint(os.path.join(\"data\", \"report.csv\"))",
                "explain": "os.path.join() 按系统规则拼接路径，Windows用反斜杠，Linux用正斜杠。避免硬编码分隔符。",
                "template": "import os"
            },
            {
                "id": "s30_03",
                "title": "用 hashlib.md5 计算字符串 'hello' 的 MD5 值并打印（注意编码）",
                "desc": "用 hashlib.md5 计算字符串 'hello' 的 MD5 值并打印（注意编码）",
                "diff": "basic",
                "kp": [
                    "auto_backup",
                    "print_basic"
                ],
                "hint": "hashlib.md5('hello'.encode()).hexdigest()",
                "answer": "import hashlib\nresult = hashlib.md5(\"hello\".encode()).hexdigest()\nprint(result)",
                "explain": "hashlib.md5(s.encode()).hexdigest() 计算MD5哈希。encode() 先转字节，hexdigest() 返回16进制字符串。",
                "template": "import hashlib\nresult = ...  # TODO"
            },
            {
                "id": "s30_04",
                "title": "写一个函数 count_by_ext(directory) 统计目录下各扩展名的文件数量（用字典），打印结果",
                "desc": "写一个函数 count_by_ext(directory) 统计目录下各扩展名的文件数量（用字典），打印结果",
                "diff": "intermediate",
                "kp": [
                    "auto_pathlib",
                    "dict_basic",
                    "print_basic"
                ],
                "hint": "Path(dir).iterdir(); 统计 suffix",
                "answer": "from pathlib import Path\nfrom collections import Counter\n\ndef count_by_ext(directory):\n    exts = [f.suffix for f in Path(directory).iterdir() if f.is_file()]\n    return dict(Counter(exts))\n\nprint(count_by_ext(\".\"))",
                "explain": "os.walk() 递归遍历目录树，每次 yield (dirpath, dirnames, filenames)。统计各扩展名文件数。",
                "template": "from pathlib import Path\nfrom collections import Counter\ndef count_by_ext(directory):\n    pass  # TODO"
            },
            {
                "id": "s30_05",
                "title": "用 subprocess.run 获取 python 版本号并打印",
                "desc": "用 subprocess.run 获取 python 版本号并打印",
                "diff": "intermediate",
                "kp": [
                    "auto_subprocess",
                    "print_basic"
                ],
                "hint": "subprocess.run(['python', '--version'], capture_output=True, text=True)",
                "answer": "import subprocess\nresult = subprocess.run([\"python\", \"--version\"], capture_output=True, text=True)\nprint(result.stdout.strip())",
                "explain": "subprocess.run() 调用外部命令，capture_output=True 捕获输出。比 os.system 更安全灵活。",
                "template": "import subprocess\nresult = ...  # TODO"
            },
            {
                "id": "s30_06",
                "title": "写一个函数 batch_rename_demo()，模拟将文件列表 ['photo1.jpg','photo2.jpg'] 重命名为 'img_001.jpg', 'img_002.jpg'（只打印重命名映射，不实际操作）",
                "desc": "写一个函数 batch_rename_demo()，模拟将文件列表 ['photo1.jpg','photo2.jpg'] 重命名为 'img_001.jpg', 'img_002.jpg'（只打印重命名映射，不实际操作）",
                "diff": "challenge",
                "kp": [
                    "auto_batch_rename",
                    "list_basic",
                    "print_basic"
                ],
                "hint": "enumerate(files, 1); f-string 格式化",
                "answer": "files = [\"photo1.jpg\", \"photo2.jpg\", \"photo3.jpg\"]\nfor i, f in enumerate(files, 1):\n    new_name = f\"img_{i:03d}.jpg\"\n    print(f\"{f} -> {new_name}\")",
                "explain": "os.rename() 重命名文件。模拟操作用列表推导式展示逻辑，实际应用中遍历目录批量改名。",
                "template": "files = ...  # TODO\n    new_name = ...  # TODO"
            }
        ],
        31: [
            {
                "id": "s31_01",
                "title": "用 pyautogui 获取屏幕分辨率并打印",
                "desc": "用 pyautogui 获取屏幕分辨率并打印",
                "diff": "basic",
                "kp": [
                    "auto_pyautogui",
                    "print_basic"
                ],
                "hint": "pyautogui.size()",
                "answer": "import pyautogui\nsize = pyautogui.size()\nprint(f\"屏幕分辨率：{size.width}x{size.height}\")",
                "explain": "pyautogui.size() 返回屏幕分辨率(宽,高)。自动化操作前先获取屏幕尺寸定位坐标。",
                "template": "import pyautogui\nsize = ...  # TODO"
            },
            {
                "id": "s31_02",
                "title": "用 pyautogui 截屏并保存为 test_screenshot.png",
                "desc": "用 pyautogui 截屏并保存为 test_screenshot.png",
                "diff": "basic",
                "kp": [
                    "auto_pyautogui",
                    "print_basic"
                ],
                "hint": "pyautogui.screenshot().save('test_screenshot.png')",
                "answer": "import pyautogui\nscreenshot = pyautogui.screenshot()\nscreenshot.save(\"test_screenshot.png\")\nprint(\"截图已保存\")",
                "explain": "pyautogui.screenshot() 截屏，save() 保存文件。自动化测试中常用截图做视觉验证。",
                "template": "import pyautogui\nscreenshot = ...  # TODO"
            },
            {
                "id": "s31_03",
                "title": "写一个函数，用 Selenium 打开百度，搜索 'Python' 并打印页面标题（模拟代码，只打印步骤说明）",
                "desc": "写一个函数，用 Selenium 打开百度，搜索 'Python' 并打印页面标题（模拟代码，只打印步骤说明）",
                "diff": "intermediate",
                "kp": [
                    "auto_selenium",
                    "print_basic"
                ],
                "hint": "driver.get(); find_element; send_keys",
                "answer": "steps = [\n    \"1. driver = webdriver.Chrome()\",\n    \"2. driver.get('https://www.baidu.com')\",\n    \"3. search = driver.find_element(By.ID, 'kw')\",\n    \"4. search.send_keys('Python')\",\n    \"5. search.send_keys(Keys.RETURN)\",\n    \"6. print(driver.title)\",\n    \"7. driver.quit()\",\n]\nfor step in steps:\n    print(step)",
                "explain": "Selenium WebDriver 控制浏览器：get() 打开网页，find_element() 定位元素，send_keys() 输入文本。",
                "template": "steps = ...  # TODO\n    \"1. driver = ...  # TODO\n    \"3. search = ...  # TODO"
            },
            {
                "id": "s31_04",
                "title": "写一个 Selenium 无头模式的配置代码，打印配置信息",
                "desc": "写一个 Selenium 无头模式的配置代码，打印配置信息",
                "diff": "intermediate",
                "kp": [
                    "auto_headless",
                    "print_basic"
                ],
                "hint": "Options(); add_argument('--headless')",
                "answer": "from selenium.webdriver.chrome.options import Options\noptions = Options()\noptions.add_argument(\"--headless\")\noptions.add_argument(\"--disable-gpu\")\noptions.add_argument(\"--window-size=1920,1080\")\nprint(\"无头模式配置完成\")\nprint(f\"参数: --headless, --disable-gpu, --window-size=1920,1080\")",
                "explain": "无头模式 Options() 不显示浏览器窗口，适合服务器运行。add_argument('--headless') 启用。",
                "template": "from selenium.webdriver.chrome.options import Options\noptions = ...  # TODO\noptions.add_argument(\"--window-size = ...  # TODO"
            },
            {
                "id": "s31_05",
                "title": "写一个函数 simulate_typing(text, interval=0.1)，模拟逐字输入（不实际调用 pyautogui，只打印每步操作）",
                "desc": "写一个函数 simulate_typing(text, interval=0.1)，模拟逐字输入（不实际调用 pyautogui，只打印每步操作）",
                "diff": "challenge",
                "kp": [
                    "auto_pyautogui",
                    "func_def",
                    "print_basic"
                ],
                "hint": "for char in text: print(char)",
                "answer": "def simulate_typing(text, interval=0.1):\n    for char in text:\n        print(f\"输入: {char} (间隔{interval}秒)\")\n\nsimulate_typing(\"Hello\")",
                "explain": "pyautogui.typewrite() 模拟键盘输入，interval 参数控制按键间隔。pyautogui.press() 按单个键。",
                "template": "def simulate_typing(text, interval=0.1):\n    pass  # TODO"
            }
        ],
        32: [
            {
                "id": "gui_window_label",
                "title": "创建窗口和标签",
                "desc": "创建一个带标签的窗口",
                "diff": "basic",
                "kp": [
                    "gui_tkinter",
                    "gui_widget"
                ],
                "template": "import tkinter as tk\n\nroot = tk.Tk()\nroot.title(\"My App\")\nroot.geometry(\"300x200\")\n\nlabel = tk.____________(root, text=\"Hello, GUI!\", font=(\"Arial\", 14))\nlabel.____________(pady=20)\n\nprint(\"Window created\")",
                "test_input": "",
                "answer": "import tkinter as tk\n\nroot = tk.Tk()\nroot.title(\"My App\")\nroot.geometry(\"300x200\")\n\nlabel = tk.Label(root, text=\"Hello, GUI!\", font=(\"Arial\", 14))\nlabel.pack(pady=20)\n\nprint(\"Window created\")",
                "expected": "Window created",
                "explain": "tkinter.Tk() 创建主窗口，Label() 创建标签，pack() 布局管理。mainloop() 启动事件循环。",
                "difficulty": "basic"
            },
            {
                "id": "gui_button_callback",
                "title": "按钮回调",
                "desc": "点击按钮改变标签文字",
                "diff": "basic",
                "kp": [
                    "gui_tkinter",
                    "gui_event"
                ],
                "template": "import tkinter as tk\n\nroot = tk.Tk()\nroot.title(\"Click Me\")\n\nlabel = tk.Label(root, text=\"Press the button\")\nlabel.pack()\n\ndef on_click():\n    label.____________(text=\"Button clicked!\")\n\nbtn = tk.Button(root, text=\"Click\", ____________=on_click)\nbtn.pack()\n\nprint(\"Button created\")",
                "test_input": "",
                "answer": "import tkinter as tk\n\nroot = tk.Tk()\nroot.title(\"Click Me\")\n\nlabel = tk.Label(root, text=\"Press the button\")\nlabel.pack()\n\ndef on_click():\n    label.config(text=\"Button clicked!\")\n\nbtn = tk.Button(root, text=\"Click\", command=on_click)\nbtn.pack()\n\nprint(\"Button created\")",
                "expected": "Button created",
                "explain": "Button(command=func) 绑定点击事件到回调函数。command 参数接收函数引用（不带括号）。",
                "difficulty": "basic"
            },
            {
                "id": "gui_entry_input",
                "title": "输入框获取",
                "desc": "从输入框获取文本并显示",
                "diff": "intermediate",
                "kp": [
                    "gui_tkinter",
                    "gui_widget"
                ],
                "template": "import tkinter as tk\n\nroot = tk.Tk()\nroot.title(\"Input Demo\")\n\nentry = tk.____________(root, font=(\"Arial\", 12))\nentry.pack(pady=10)\n\ndef show_text():\n    text = entry.____________()\n    label.config(text=f\"You typed: {{text}}\")\n\nlabel = tk.Label(root, text=\"\")\nlabel.pack()\n\nbtn = tk.Button(root, text=\"Show\", command=show_text)\nbtn.pack()\n\nprint(\"Entry demo created\")",
                "test_input": "",
                "answer": "import tkinter as tk\n\nroot = tk.Tk()\nroot.title(\"Input Demo\")\n\nentry = tk.Entry(root, font=(\"Arial\", 12))\nentry.pack(pady=10)\n\ndef show_text():\n    text = entry.get()\n    label.config(text=f\"You typed: {{text}}\")\n\nlabel = tk.Label(root, text=\"\")\nlabel.pack()\n\nbtn = tk.Button(root, text=\"Show\", command=show_text)\nbtn.pack()\n\nprint(\"Entry demo created\")",
                "expected": "Entry demo created",
                "explain": "Entry 文本输入框，.get() 获取内容。StringVar 变量绑定实现动态更新。",
                "difficulty": "intermediate"
            },
            {
                "id": "gui_grid_layout",
                "title": "Grid 布局",
                "desc": "用 grid 实现表单布局",
                "diff": "intermediate",
                "kp": [
                    "gui_tkinter",
                    "gui_layout"
                ],
                "template": "import tkinter as tk\n\nroot = tk.Tk()\nroot.title(\"Login Form\")\n\ntk.Label(root, text=\"Username:\").____________(row=0, column=0, padx=5, pady=5)\ntk.Entry(root).grid(row=0, ____________=1, padx=5, pady=5)\n\ntk.Label(root, text=\"Password:\").grid(row=1, column=0, padx=5, pady=5)\ntk.Entry(root, show=\"*\").grid(row=1, column=1, padx=5, pady=5)\n\ntk.Button(root, text=\"Login\").grid(row=2, column=0, columnspan=2, pady=10)\n\nprint(\"Login form created\")",
                "test_input": "",
                "answer": "import tkinter as tk\n\nroot = tk.Tk()\nroot.title(\"Login Form\")\n\ntk.Label(root, text=\"Username:\").grid(row=0, column=0, padx=5, pady=5)\ntk.Entry(root).grid(row=0, column=1, padx=5, pady=5)\n\ntk.Label(root, text=\"Password:\").grid(row=1, column=0, padx=5, pady=5)\ntk.Entry(root, show=\"*\").grid(row=1, column=1, padx=5, pady=5)\n\ntk.Button(root, text=\"Login\").grid(row=2, column=0, columnspan=2, pady=10)\n\nprint(\"Login form created\")",
                "expected": "Login form created",
                "explain": "Grid 布局：row/column 定位，sticky 对齐方向，padx/pady 间距。比 pack 更精确控制位置。",
                "difficulty": "intermediate"
            },
            {
                "id": "gui_menu_dialog",
                "title": "菜单栏与文件对话框",
                "desc": "创建带文件打开功能的菜单",
                "diff": "challenge",
                "kp": [
                    "gui_tkinter",
                    "gui_menu"
                ],
                "template": "import tkinter as tk\nfrom tkinter import filedialog\n\nroot = tk.Tk()\nroot.title(\"Notepad\")\n\ndef open_file():\n    path = filedialog.____________()\n    if path:\n        with open(path, \"r\", encoding=\"utf-8\") as f:\n            content = f.read()\n        text.delete(\"1.0\", tk.END)\n        text.insert(\"1.0\", content)\n\nmenubar = tk.Menu(root)\nfile_menu = tk.____________(menubar, tearoff=0)\nfile_menu.add_command(label=\"Open\", command=open_file)\nmenubar.add_cascade(label=\"File\", menu=file_menu)\nroot.config(menu=menubar)\n\ntext = tk.Text(root, wrap=tk.WORD)\ntext.pack(fill=tk.BOTH, expand=True)\n\nprint(\"Notepad created\")",
                "test_input": "",
                "answer": "import tkinter as tk\nfrom tkinter import filedialog\n\nroot = tk.Tk()\nroot.title(\"Notepad\")\n\ndef open_file():\n    path = filedialog.askopenfilename()\n    if path:\n        with open(path, \"r\", encoding=\"utf-8\") as f:\n            content = f.read()\n        text.delete(\"1.0\", tk.END)\n        text.insert(\"1.0\", content)\n\nmenubar = tk.Menu(root)\nfile_menu = tk.Menu(menubar, tearoff=0)\nfile_menu.add_command(label=\"Open\", command=open_file)\nmenubar.add_cascade(label=\"File\", menu=file_menu)\nroot.config(menu=menubar)\n\ntext = tk.Text(root, wrap=tk.WORD)\ntext.pack(fill=tk.BOTH, expand=True)\n\nprint(\"Notepad created\")",
                "expected": "Notepad created",
                "explain": "Menu 创建菜单栏，filedialog.askopenfilename() 弹出文件选择对话框。Tkinter 标准对话框。",
                "difficulty": "challenge"
            }
        ],
        33: [
            {
                "id": "s33_01",
                "title": "用 pathlib + hashlib 写一个函数 file_hash(path) 计算文件的 MD5 值并返回",
                "desc": "用 pathlib + hashlib 写一个函数 file_hash(path) 计算文件的 MD5 值并返回",
                "diff": "basic",
                "kp": [
                    "auto_backup",
                    "auto_pathlib",
                    "print_basic"
                ],
                "hint": "with open(path, 'rb') as f: hashlib.md5(chunk).hexdigest()",
                "answer": "import hashlib\nfrom pathlib import Path\n\ndef file_hash(filepath):\n    h = hashlib.md5()\n    with open(filepath, \"rb\") as f:\n        for chunk in iter(lambda: f.read(8192), b\"\"):\n            h.update(chunk)\n    return h.hexdigest()\n\n# 用自身文件测试\nprint(file_hash(__file__)[:16] + \"...\")",
                "explain": "pathlib+hashlib 组合：遍历文件计算哈希值，用于检测文件篡改或去重。二进制模式'rb'读取文件。",
                "template": "import hashlib\nfrom pathlib import Path\ndef file_hash(filepath):\n    pass  # TODO\n    h = ...  # TODO"
            },
            {
                "id": "s33_02",
                "title": "创建 DailyReport 类，有 date/done/in_progress 属性，实现 add_done(task) 和 to_markdown() 方法，打印 Markdown 日报",
                "desc": "创建 DailyReport 类，有 date/done/in_progress 属性，实现 add_done(task) 和 to_markdown() 方法，打印 Markdown 日报",
                "diff": "intermediate",
                "kp": [
                    "oop_class_object",
                    "oop_init_self",
                    "print_basic"
                ],
                "hint": "class DailyReport: def add_done, def to_markdown",
                "answer": "from datetime import datetime\n\nclass DailyReport:\n    def __init__(self, date=None):\n        self.date = date or datetime.now().strftime(\"%Y-%m-%d\")\n        self.done = []\n        self.in_progress = []\n\n    def add_done(self, task):\n        self.done.append(task)\n\n    def add_in_progress(self, task):\n        self.in_progress.append(task)\n\n    def to_markdown(self):\n        lines = [f\"# 日报 {self.date}\", \"\"]\n        if self.done:\n            lines.append(\"## 已完成\")\n            for t in self.done:\n                lines.append(f\"- [x] {t}\")\n        if self.in_progress:\n            lines.append(\"## 进行中\")\n            for t in self.in_progress:\n                lines.append(f\"- [ ] {t}\")\n        return chr(10).join(lines)\n\nreport = DailyReport(\"2025-05-02\")\nreport.add_done(\"完成Python学习\")\nreport.add_in_progress(\"写自动化脚本\")\nprint(report.to_markdown())",
                "explain": "面向对象+JSON持久化：类封装数据，save/load 方法序列化。__dict__ 获取实例属性字典。",
                "template": "from datetime import datetime\nclass DailyReport:\n    pass  # TODO\n    def __init__(self, date=None):\n        pass  # TODO\n        self.date = ...  # TODO\n        self.done = ...  # TODO\n        self.in_progress = ...  # TODO\n    def add_done(self, task):\n        pass  # TODO\n    def add_in_progress(self, task):\n        pass  # TODO\n    def to_markdown(self):\n        pass  # TODO\n        lines = ...  # TODO\nreport = ...  # TODO"
            },
            {
                "id": "s33_03",
                "title": "写一个函数 scan_duplicates(directory)，扫描目录找出相同大小的文件对（用大小初步判断，不用MD5），打印结果",
                "desc": "写一个函数 scan_duplicates(directory)，扫描目录找出相同大小的文件对（用大小初步判断，不用MD5），打印结果",
                "diff": "intermediate",
                "kp": [
                    "auto_pathlib",
                    "dict_basic",
                    "print_basic"
                ],
                "hint": "用字典 size->files 映射; 找 len>1 的",
                "answer": "from pathlib import Path\nfrom collections import defaultdict\n\ndef scan_duplicates(directory):\n    size_map = defaultdict(list)\n    for f in Path(directory).iterdir():\n        if f.is_file():\n            size_map[f.stat().st_size].append(f.name)\n    for size, files in size_map.items():\n        if len(files) > 1:\n            print(f\"大小{size}字节: {files}\")\n\nprint(\"扫描当前目录:\")\nscan_duplicates(\".\")",
                "explain": "文件去重：计算每个文件的哈希值，相同哈希即为重复文件。大文件可分块读取避免内存溢出。",
                "template": "from pathlib import Path\nfrom collections import defaultdict\ndef scan_duplicates(directory):\n    pass  # TODO\n    size_map = ...  # TODO"
            },
            {
                "id": "s33_04",
                "title": "综合挑战：写一个函数 rename_by_pattern(directory, pattern, replacement)，用正则批量重命名（只打印映射不实际操作），测试将 test_01.txt, test_02.txt 改为 data_01.txt, data_02.txt",
                "desc": "综合挑战：写一个函数 rename_by_pattern(directory, pattern, replacement)，用正则批量重命名（只打印映射不实际操作），测试将 test_01.txt, test_02.txt 改为 data_01.txt, data_02.txt",
                "diff": "challenge",
                "kp": [
                    "regex_sub",
                    "auto_batch_rename",
                    "print_basic"
                ],
                "hint": "re.sub(pattern, replacement, name)",
                "answer": "import re\nfrom pathlib import Path\n\ndef rename_by_pattern(directory, pattern, replacement):\n    for f in Path(directory).iterdir():\n        if f.is_file():\n            new_name = re.sub(pattern, replacement, f.name)\n            if new_name != f.name:\n                print(f\"  {f.name} -> {new_name}\")\n\n# 模拟测试\nfiles = [\"test_01.txt\", \"test_02.txt\", \"test_03.txt\"]\nfor f in files:\n    new_name = re.sub(r\"test\", \"data\", f)\n    print(f\"  {f} -> {new_name}\")",
                "explain": "正则+pathlib组合：re.sub() 按模式替换文件名，Path.rename() 执行重命名。批量处理利器。",
                "template": "import re\nfrom pathlib import Path\ndef rename_by_pattern(directory, pattern, replacement):\n    pass  # TODO\n            new_name = ...  # TODO\nfiles = ...  # TODO\n    new_name = ...  # TODO"
            },
            {
                "id": "s33_05",
                "title": "最终挑战：写一个 WebMonitor 类，有 check_page(url) 方法（用 requests 获取页面并计算内容 hash）和 log_change() 方法，模拟监控流程",
                "desc": "最终挑战：写一个 WebMonitor 类，有 check_page(url) 方法（用 requests 获取页面并计算内容 hash）和 log_change() 方法，模拟监控流程",
                "diff": "challenge",
                "kp": [
                    "oop_class_object",
                    "crawl_requests",
                    "auto_backup",
                    "print_basic"
                ],
                "hint": "class WebMonitor: def check_page, def log_change",
                "answer": "import hashlib\n\nclass WebMonitor:\n    def __init__(self):\n        self.history = {}\n\n    def check_page(self, url, content=None):\n        # content 参数模拟页面内容（实际用 requests 获取）\n        if content is None:\n            content = \"default page content\"\n        content_hash = hashlib.md5(content.encode()).hexdigest()\n        changed = False\n        if url in self.history and self.history[url] != content_hash:\n            changed = True\n        self.history[url] = content_hash\n        return content_hash, changed\n\n    def log_change(self, url, content_hash):\n        from datetime import datetime\n        timestamp = datetime.now().strftime(\"%Y-%m-%d %H:%M:%S\")\n        print(f\"[{timestamp}] {url} hash={content_hash[:8]}...\")\n\nmonitor = WebMonitor()\nh1, changed = monitor.check_page(\"https://example.com\", \"version 1\")\nmonitor.log_change(\"https://example.com\", h1)\nh2, changed = monitor.check_page(\"https://example.com\", \"version 2\")\nprint(f\"内容变化: {changed}\")\nmonitor.log_change(\"https://example.com\", h2)",
                "explain": "综合挑战：Web监控=requests+hashlib+logging。定时检测网页变化，hashlib 比较内容差异。",
                "template": "import hashlib\nclass WebMonitor:\n    pass  # TODO\n    def __init__(self):\n        pass  # TODO\n        self.history = ...  # TODO\n    def check_page(self, url, content=None):\n        pass  # TODO\n            content = ...  # TODO\n        content_hash = ...  # TODO\n        changed = ...  # TODO\n            changed = ...  # TODO\n        self.history[url] = ...  # TODO\n    def log_change(self, url, content_hash):\n        pass  # TODO\n        from datetime import datetime\n        timestamp = ...  # TODO\nmonitor = ...  # TODO\nh1, changed = ...  # TODO\nh2, changed = ...  # TODO"
            }
        ]
    }
