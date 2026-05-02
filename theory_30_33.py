"""理论讲解数据 - 阶段30~33 — v5.0 第五篇：自动化与桌面（脚本/桌面/GUI/综合实战）"""
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

THEORY_30_33 = {
    # ==================== 阶段30：脚本自动化 ====================
    30: (f"""{B}阶段30：脚本自动化 — 让电脑替你干活{END}

{C_}生活类比：自动化 = 录制宏，按一下播放，重复动作自动执行{END}
    手动操作：每天打开5个网页 → 5分钟
    自动化：运行一个脚本 → 5秒钟
    这就是自动化的价值

{BD}一、os 模块 — 文件和目录操作{END}
    >>> import os

    >>> # 当前目录
    >>> os.getcwd()                     # 获取当前工作目录
    'C:\\\\Users'

    >>> # 目录操作
    >>> os.listdir(".")                 # 列出当前目录文件
    >>> os.makedirs("test/a/b", exist_ok=True)  # 递归创建目录
    >>> os.path.exists("test")          # 检查路径是否存在
    True
    >>> os.path.isfile("test")          # 是否是文件
    False
    >>> os.path.isdir("test")           # 是否是目录
    True

    >>> # 路径拼接（推荐用 os.path 或 pathlib）
    >>> os.path.join("folder", "file.txt")
    'folder\\\\file.txt'

{BD}二、pathlib — 更优雅的路径操作{END}
    >>> from pathlib import Path

    >>> p = Path("docs/notes.txt")
    >>> p.name          # 'notes.txt'
    >>> p.stem          # 'notes'
    >>> p.suffix        # '.txt'
    >>> p.parent        # Path('docs')
    >>> p.exists()      # True/False

    >>> # 批量操作
    >>> for f in Path(".").glob("*.py"):
    ...     print(f.name)

{BD}三、shutil — 文件批量操作{END}
    >>> import shutil

    >>> shutil.copy("a.txt", "backup/a.txt")     # 复制文件
    >>> shutil.copytree("docs", "backup/docs")    # 复制目录
    >>> shutil.move("old.txt", "new.txt")         # 移动/重命名
    >>> shutil.rmtree("temp")                      # 删除目录树

{BD}四、批量重命名实战{END}
    >>> from pathlib import Path

    >>> for f in Path("photos").glob("*.jpg"):
    ...     new_name = f"vacation_{{f.stem.zfill(3)}}{{f.suffix}}"
    ...     f.rename(f.parent / new_name)

{BD}五、自动整理文件{END}
    >>> # 按扩展名分类到不同文件夹
    >>> ext_map = {{
    ...     ".jpg": "Images", ".png": "Images", ".gif": "Images",
    ...     ".mp4": "Videos", ".avi": "Videos",
    ...     ".pdf": "Documents", ".docx": "Documents",
    ... }}

    >>> for f in Path("Downloads").iterdir():
    ...     if f.is_file():
    ...         dest = ext_map.get(f.suffix.lower(), "Others")
    ...         dest_dir = Path("Sorted") / dest
    ...         dest_dir.mkdir(parents=True, exist_ok=True)
    ...         shutil.move(str(f), str(dest_dir / f.name))

{BD}六、subprocess — 调用系统命令{END}
    >>> import subprocess

    >>> result = subprocess.run(["ping", "-n", "1", "baidu.com"],
    ...                        capture_output=True, text=True)
    >>> print(result.stdout[:100])

{BD}七、schedule — 定时任务{END}
    >>> # pip install schedule
    >>> import schedule

    >>> def backup():
    ...     shutil.copytree("data", f"backup/data_{{date}}")

    >>> schedule.every().day.at("02:00").do(backup)
    >>> schedule.every().hour.do(check_status)
    >>> schedule.every().monday.do(weekly_report)

    >>> while True:
    ...     schedule.run_pending()
    ...     time.sleep(60)


{BD}三、日志记录 — logging 模块{END}

{C_}比 print 更专业的日志方式{END}
    >>> import logging
    >>> logging.basicConfig(
    ...     level=logging.INFO,
    ...     format='%(asctime)s - %(levelname)s - %(message)s',
    ...     filename='app.log'
    ... )
    >>> logging.info("任务开始")
    >>> logging.warning("磁盘空间不足")
    >>> logging.error("连接失败", exc_info=True)

{C_}日志级别：DEBUG < INFO < WARNING < ERROR < CRITICAL{END}

{DIM}>> 动手试试！{END}
    {C_}在代码实验室里用 pathlib 列出当前目录下所有 .py 文件{END}
""", ["auto_pathlib", "auto_os", "auto_batch", "auto_schedule", "auto_watchdog"]),

    # ==================== 阶段31：桌面自动化 ====================
    31: (f"""{B}阶段31：桌面自动化 — 让鼠标键盘听指挥{END}

{C_}生活类比：桌面自动化 = 你的数字替身{END}
    你坐在电脑前点鼠标敲键盘 → 慢、累
    pyautogui 替你操作 → 快、不知疲倦

{BD}一、pyautogui 基础{END}
    >>> # pip install pyautogui
    >>> import pyautogui

    >>> # 安全机制：快速移动鼠标到角落可中止
    >>> pyautogui.FAILSAFE = True

    >>> # 屏幕尺寸
    >>> pyautogui.size()
    Size(width=1920, height=1080)

    >>> # 鼠标位置
    >>> pyautogui.position()
    Point(x=500, y=300)

{BD}二、鼠标控制{END}
    >>> # 移动鼠标
    >>> pyautogui.moveTo(500, 300, duration=1)   # 1秒移过去
    >>> pyautogui.moveRel(100, 0, duration=0.5)  # 相对移动

    >>> # 点击
    >>> pyautogui.click()                    # 左键单击
    >>> pyautogui.click(500, 300)            # 点击指定位置
    >>> pyautogui.doubleClick()
    >>> pyautogui.rightClick()

    >>> # 拖拽
    >>> pyautogui.dragTo(800, 400, duration=1)
    >>> pyautogui.dragRel(200, 0, duration=0.5)

    >>> # 滚轮
    >>> pyautogui.scroll(-3)    # 向下滚3格

{BD}三、键盘控制{END}
    >>> # 打字
    >>> pyautogui.typewrite("Hello World!", interval=0.1)

    >>> # 中文输入需要用 pyperclip 剪贴板
    >>> # pip install pyperclip
    >>> import pyperclip
    >>> pyperclip.copy("你好世界")
    >>> pyautogui.hotkey("ctrl", "v")   # 粘贴

    >>> # 特殊键
    >>> pyautogui.press("enter")
    >>> pyautogui.press("tab")
    >>> pyautogui.hotkey("ctrl", "c")   # 复制
    >>> pyautogui.hotkey("ctrl", "s")   # 保存

{BD}四、截图与图像识别{END}
    >>> # 截全屏
    >>> screenshot = pyautogui.screenshot()
    >>> screenshot.save("screen.png")

    >>> # 截区域
    >>> region = pyautogui.screenshot(region=(0, 0, 500, 300))

    >>> # 图像识别 — 找到按钮位置
    >>> btn_pos = pyautogui.locateOnScreen("button.png", confidence=0.9)
    >>> if btn_pos:
    ...     pyautogui.click(btn_pos)

{BD}五、剪贴板操作{END}
    >>> import pyperclip

    >>> pyperclip.copy("Hello from Python!")
    >>> text = pyperclip.paste()
    >>> print(text)
    Hello from Python!

{BD}六、实用技巧与最佳实践{END}
    1. 操作前先 time.sleep() 等待页面加载
    2. 用 try/except 包裹，防止失焦导致误操作
    3. 加随机延迟，更拟人化
    4. 先截图确认画面再操作
    5. 用 locateOnScreen 定位比绝对坐标更可靠

    >>> import time, random

    >>> def safe_click(image_path, timeout=10):
    ...     for _ in range(timeout):
    ...         pos = pyautogui.locateOnScreen(image_path, confidence=0.9)
    ...         if pos:
    ...             time.sleep(random.uniform(0.3, 0.8))
    ...             pyautogui.click(pos)
    ...             return True
    ...         time.sleep(1)
    ...     return False

{C_}注意：桌面自动化在远程/服务器环境可能不适用，需要真实桌面环境{END}

{DIM}>> 动手试试！{END}
    {C_}在代码实验室里写一个模拟键盘输入的小脚本{END}


{BD}七、键盘操作详解{END}

{C_}typewrite — 模拟打字（英文）{END}
    >>> pyautogui.typewrite("Hello", interval=0.25)  # 每个字符间隔0.25秒
    >>> pyautogui.typewrite(["enter", "tab", "a", "b"])  # 逐个按键

{C_}press — 单键按下{END}
    >>> pyautogui.press("enter")
    >>> pyautogui.press("f5")         # 刷新
    >>> pyautogui.press("esc")
    >>> pyautogui.press("down")       # 方向键

{C_}hotkey — 组合键{END}
    >>> pyautogui.hotkey("ctrl", "a")     # 全选
    >>> pyautogui.hotkey("ctrl", "c")     # 复制
    >>> pyautogui.hotkey("ctrl", "v")     # 粘贴
    >>> pyautogui.hotkey("alt", "f4")     # 关闭窗口
    >>> pyautogui.hotkey("ctrl", "shift", "n")  # 三键组合

{C_}keyDown / keyUp — 按住和释放{END}
    >>> pyautogui.keyDown("shift")    # 按住 Shift
    >>> pyautogui.press("left")       # 按左箭头（选中文字）
    >>> pyautogui.press("left")
    >>> pyautogui.keyUp("shift")      # 释放 Shift

{BD}八、截图与图像识别{END}

{C_}截取全屏并保存{END}
    >>> img = pyautogui.screenshot()
    >>> img.save("full_screen.png")

{C_}截取指定区域{END}
    >>> # region=(left, top, width, height)
    >>> region_img = pyautogui.screenshot(region=(100, 200, 400, 300))
    >>> region_img.save("partial.png")

{C_}获取像素颜色{END}
    >>> color = pyautogui.pixel(500, 300)      # 返回 (R, G, B)
    >>> pyautogui.pixelMatchesColor(500, 300, (255, 0, 0))  # 是否匹配

{C_}图像识别点击 — 自动找按钮{END}
    >>> # 先截一张按钮的图保存为 button.png
    >>> location = pyautogui.locateOnScreen("button.png", confidence=0.9)
    >>> if location:
    ...     center = pyautogui.center(location)
    ...     pyautogui.click(center)
    ... else:
    ...     print("未找到目标图像")

    >>> # locateAllOnScreen — 找所有匹配
    >>> for loc in pyautogui.locateAllOnScreen("icon.png", confidence=0.8):
    ...     print(f"找到图标：{{loc}}")

{BD}九、异常恢复与容错{END}

{C_}ImageNotFoundException 处理{END}
    >>> try:
    ...     pos = pyautogui.locateOnScreen("btn.png", confidence=0.9)
    ...     pyautogui.click(pos)
    ... except pyautogui.ImageNotFoundException:
    ...     print("按钮未找到，尝试备选方案")
    ...     pyautogui.click(500, 300)  # 退而使用坐标

{C_}通用异常恢复模式{END}
    >>> def robust_automation(steps):
    ...     for step_name, action in steps:
    ...         for attempt in range(3):
    ...             try:
    ...                 action()
    ...                 break
    ...             except Exception as e:
    ...                 print(f"[{{step_name}}] 第{{attempt+1}}次失败：{{e}}")
    ...                 time.sleep(2)
    ...         else:
    ...             print(f"[{{step_name}}] 跳过（3次均失败）")

{BD}十、组合自动化实战{END}

{C_}自动填写表单示例{END}
    >>> import time, pyperclip
    >>>
    >>> def fill_form(name, email, message):
    ...     # 1. 点击姓名输入框
    ...     time.sleep(1)
    ...     pyautogui.click(300, 400)
    ...     pyperclip.copy(name)
    ...     pyautogui.hotkey("ctrl", "v")
    ...
    ...     # 2. Tab 到邮箱框
    ...     pyautogui.press("tab")
    ...     pyperclip.copy(email)
    ...     pyautogui.hotkey("ctrl", "v")
    ...
    ...     # 3. Tab 到消息框
    ...     pyautogui.press("tab")
    ...     pyperclip.copy(message)
    ...     pyautogui.hotkey("ctrl", "v")
    ...
    ...     # 4. 点击提交按钮
    ...     time.sleep(0.5)
    ...     pyautogui.click(400, 600)""", ["auto_selenium", "auto_pyautogui", "auto_wait", "auto_screen"]),

    # ==================== 阶段32：GUI开发 ====================
    32: (f"""{B}阶段32：GUI 开发 — 给程序做个界面{END}

{C_}生活类比：GUI = 给程序装修门面{END}
    命令行程序 = 毛坯房（能用但不好看）
    GUI 程序 = 精装修（好看好用）

{BD}一、tkinter 入门{END}
    >>> import tkinter as tk

    >>> root = tk.Tk()
    >>> root.title("My First GUI")
    >>> root.geometry("400x300")
    >>> root.mainloop()         # 启动主循环

{BD}二、常用组件{END}
    >>> # 标签
    >>> label = tk.Label(root, text="Hello!", font=("Arial", 16))

    >>> # 按钮
    >>> def on_click():
    ...     label.config(text="Clicked!")
    >>> btn = tk.Button(root, text="Click Me", command=on_click)

    >>> # 输入框
    >>> entry = tk.Entry(root, width=20)

    >>> # 文本框
    >>> text = tk.Text(root, width=40, height=10)

    >>> # 复选框
    >>> var = tk.BooleanVar()
    >>> check = tk.Checkbutton(root, text="Enable", variable=var)

    >>> # 列表
    >>> listbox = tk.Listbox(root)
    >>> listbox.insert(0, "Item 1")
    >>> listbox.insert(1, "Item 2")

{BD}三、布局管理{END}
    >>> # pack — 顺序排列
    >>> label.pack()
    >>> btn.pack()

    >>> # grid — 表格布局（推荐！）
    >>> label.grid(row=0, column=0)
    >>> entry.grid(row=0, column=1)
    >>> btn.grid(row=1, column=0, columnspan=2)

    >>> # place — 精确定位
    >>> btn.place(x=100, y=50, width=120, height=30)

{BD}四、事件驱动{END}
    >>> def on_key(event):
    ...     print(f"Pressed: {{event.char}}")

    >>> def on_enter(event):
    ...     entry.config(bg="lightyellow")

    >>> root.bind("<Key>", on_key)
    >>> entry.bind("<Enter>", on_enter)
    >>> entry.bind("<Leave>", lambda e: entry.config(bg="white"))

{BD}五、菜单栏{END}
    >>> menubar = tk.Menu(root)

    >>> file_menu = tk.Menu(menubar, tearoff=0)
    >>> file_menu.add_command(label="New", command=new_file)
    >>> file_menu.add_command(label="Open", command=open_file)
    >>> file_menu.add_separator()
    >>> file_menu.add_command(label="Exit", command=root.quit)
    >>> menubar.add_cascade(label="File", menu=file_menu)

    >>> root.config(menu=menubar)

{BD}六、实战：记事本{END}
    >>> def open_file():
    ...     filepath = tk.filedialog.askopenfilename()
    ...     if filepath:
    ...         with open(filepath, encoding="utf-8") as f:
    ...             text.delete("1.0", tk.END)
    ...             text.insert(tk.END, f.read())

    >>> def save_file():
    ...     filepath = tk.filedialog.asksaveasfilename()
    ...     if filepath:
    ...         with open(filepath, "w", encoding="utf-8") as f:
    ...             f.write(text.get("1.0", tk.END))

{DIM}>> 动手试试！{END}
    {C_}在代码实验室里创建一个带按钮和标签的简单窗口{END}


{BD}七、布局管理器深度对比{END}

{C_}pack — 流式布局（简单场景）{END}
    >>> # 从上到下依次排列
    >>> tk.Label(root, text="标题").pack(side="top")
    >>> tk.Button(root, text="左").pack(side="left")
    >>> tk.Button(root, text="右").pack(side="right")
    >>> # fill=tk.X 水平填满, fill=tk.BOTH 双向填满
    >>> # expand=True 随窗口缩放

{C_}grid — 表格布局（推荐！最常用）{END}
    >>> # row/column 定位，sticky 对齐方向
    >>> tk.Label(root, text="姓名：").grid(row=0, column=0, sticky="e")
    >>> tk.Entry(root).grid(row=0, column=1)
    >>> tk.Label(root, text="年龄：").grid(row=1, column=0, sticky="e")
    >>> tk.Entry(root).grid(row=1, column=1)
    >>> tk.Button(root, text="提交").grid(row=2, column=0, columnspan=2)
    >>> # sticky: n(上) s(下) e(右) w(左) 或组合 "nsew"
    >>> # padx/pady 内边距, ipadx/ipady 内部填充
    >>> # columnconfigure(row, weight=1) 让列随窗口拉伸

{C_}place — 绝对定位（精确控制）{END}
    >>> tk.Button(root, text="固定").place(x=50, y=100, width=120, height=30)
    >>> # relx/rely 相对坐标 (0.0~1.0)
    >>> tk.Label(root, text="居中").place(relx=0.5, rely=0.5, anchor="center")

{C_}三种布局选择指南：{END}
    pack  → 简单纵向/横向排列（工具栏、状态栏）
    grid  → 表单、设置面板（最常用！）
    place → 精确像素定位（画布叠加、自定义布局）
    ⚠️ 同一容器内不要混用！选一个用到底

{BD}八、事件绑定详解{END}

{C_}bind — 绑定任意事件{END}
    >>> # 鼠标事件
    >>> canvas.bind("<Button-1>", on_left_click)    # 左键点击
    >>> canvas.bind("<Double-1>", on_double_click)  # 双击
    >>> canvas.bind("<B1-Motion>", on_drag)         # 拖拽
    >>> canvas.bind("<MouseWheel>", on_scroll)      # 滚轮

    >>> # 键盘事件
    >>> root.bind("<Return>", on_enter)             # 回车
    >>> root.bind("<Control-s>", on_save)           # Ctrl+S
    >>> root.bind("<Key>", on_any_key)              # 任意键

    >>> # 窗口事件
    >>> root.bind("<Configure>", on_resize)         # 窗口大小改变
    >>> root.bind("<FocusIn>", on_focus)            # 获得焦点

{C_}event 对象常用属性：{END}
    >>> def on_click(event):
    ...     print(f"x={{event.x}}, y={{event.y}}")       # 相对坐标
    ...     print(f"keysym={{event.keysym}}")             # 按键名称
    ...     print(f"widget={{event.widget}}")             # 触发的组件

{BD}九、对话框{END}

    >>> from tkinter import messagebox, filedialog, colorchooser

    >>> # 消息对话框
    >>> messagebox.showinfo("提示", "操作成功！")
    >>> messagebox.showwarning("警告", "数据可能丢失")
    >>> messagebox.showerror("错误", "文件无法打开")
    >>> result = messagebox.askyesno("确认", "确定删除？")

    >>> # 文件选择对话框
    >>> filepath = filedialog.askopenfilename(
    ...     title="选择文件",
    ...     filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
    ... )

    >>> save_path = filedialog.asksaveasfilename(
    ...     defaultextension=".txt",
    ...     filetypes=[("文本文件", "*.txt")]
    ... )

    >>> # 颜色选择
    >>> color = colorchooser.askcolor(title="选择颜色")
    >>> # 返回 ((R,G,B), "#rrggbb") 或 (None, None)

{BD}十、打包发布{END}

{C_}用 PyInstaller 把 .py 打包成 .exe：{END}
    >>> # pip install pyinstaller
    >>> # 打包成单个 exe
    >>> # pyinstaller --onefile --windowed my_app.py
    >>> # --onefile    打包成单个文件
    >>> # --windowed   不显示控制台窗口
    >>> # --icon=app.ico  设置图标
    >>> # --add-data "images;images"  打包资源文件""", ["gui_tkinter", "gui_layout", "gui_event", "gui_widget"]),

    # ==================== 阶段33: 综合实战 - 自动化方向 ====================
    33: (f"""{B}阶段33: 综合实战 - 自动化方向{END}

{C_}三个实战项目, 把自动化技能串起来! 每个项目都有完整代码框架{END}

{BD}一、智能文件管理器{END}
    核心思路: os扫描 + shutil移动 + hashlib去重

    >>> import os, hashlib, shutil
    >>> from pathlib import Path
    >>> from collections import defaultdict

    >>> # 1. 按扩展名分类
    >>> TYPE_MAP = {{
    ...     '.jpg': '图片', '.png': '图片', '.gif': '图片',
    ...     '.mp4': '视频', '.avi': '视频', '.mkv': '视频',
    ...     '.mp3': '音乐', '.wav': '音乐', '.flac': '音乐',
    ...     '.pdf': '文档', '.docx': '文档', '.txt': '文档',
    ...     '.zip': '压缩', '.rar': '压缩', '.7z': '压缩',
    ... }}

    >>> def classify_files(directory):
    ...     # 扫描目录, 按类型分类文件
    ...     groups = defaultdict(list)
    ...     for f in Path(directory).rglob('*'):
    ...         if f.is_file():
    ...             cat = TYPE_MAP.get(f.suffix.lower(), '其他')
    ...             groups[cat].append(f)
    ...     return groups

    >>> # 2. MD5 去重
    >>> def file_md5(filepath):
    ...     # 计算文件 MD5 哈希值
    ...     h = hashlib.md5()
    ...     with open(filepath, 'rb') as f:
    ...         for chunk in iter(lambda: f.read(8192), b''):
    ...             h.update(chunk)
    ...     return h.hexdigest()

    >>> def find_duplicates(directory):
    ...     # 查找重复文件
    ...     seen = {{}}
    ...     dups = []
    ...     for f in Path(directory).rglob('*'):
    ...         if f.is_file() and f.stat().st_size > 0:
    ...             md5 = file_md5(f)
    ...             if md5 in seen:
    ...                 dups.append((seen[md5], f))
    ...             else:
    ...                 seen[md5] = f
    ...     return dups

    >>> # 3. 移动文件到分类目录
    >>> def organize(directory, dest):
    ...     # 按类型整理文件到目标目录
    ...     groups = classify_files(directory)
    ...     report = []
    ...     for cat, files in groups.items():
    ...         cat_dir = Path(dest) / cat
    ...         cat_dir.mkdir(parents=True, exist_ok=True)
    ...         for f in files:
    ...             target = cat_dir / f.name
    ...             if not target.exists():
    ...                 shutil.move(str(f), str(target))
    ...                 report.append(f'Moved: {{f.name}} -> {{cat}}/')
    ...     return report

{BD}二、日报生成器{END}
    核心思路: subprocess + datetime + 模板

    >>> import subprocess, datetime

    >>> def get_git_log(repo_path, since='today'):
    ...     # 获取今日 Git 提交记录
    ...     cmd = ['git', 'log', f'--since={{since}}', '--oneline', '--all']
    ...     result = subprocess.run(
    ...         cmd, cwd=repo_path,
    ...         capture_output=True, text=True
    ...     )
    ...     return result.stdout.strip().split('\n') if result.stdout else []

    >>> def generate_daily_report(author, commits, tasks_done, tasks_plan):
    ...     # 生成 Markdown 日报
    ...     today = datetime.date.today().strftime('%Y-%m-%d')
    ...     report = f'# 日报 - {{today}}\n\n## 今日完成\n'
    ...     for task in tasks_done:
    ...         report += f'- [x] {{task}}\n'
    ...     report += '\n## 提交记录\n'
    ...     for c in commits[:5]:
    ...         report += f'- {{c}}\n'
    ...     report += '\n## 明日计划\n'
    ...     for task in tasks_plan:
    ...         report += f'- [ ] {{task}}\n'
    ...     return report

    >>> # 保存报告
    >>> def save_report(content, output_dir='reports'):
    ...     Path(output_dir).mkdir(exist_ok=True)
    ...     fname = f'{{output_dir}}/report_{{datetime.date.today()}}.md'
    ...     with open(fname, 'w', encoding='utf-8') as f:
    ...         f.write(content)
    ...     return fname

{BD}三、网页监控机器人{END}
    核心思路: requests + hash对比 + 定时循环

    >>> import requests, time, hashlib
    >>> from datetime import datetime

    >>> class WebMonitor:
    ...     def __init__(self):
    ...         self.baselines = {{}}  # url -> content_hash
    ...         self.history = []       # 变更记录
    ...
    ...     def check(self, url):
    ...         # 检查网页是否有变化
    ...         try:
    ...             resp = requests.get(url, timeout=10)
    ...             current = hashlib.md5(
    ...                 resp.content
    ...             ).hexdigest()
    ...             if url not in self.baselines:
    ...                 self.baselines[url] = current
    ...                 return '首次记录'
    ...             if current != self.baselines[url]:
    ...                 old = self.baselines[url]
    ...                 self.baselines[url] = current
    ...                 record = {{
    ...                     'url': url,
    ...                     'time': datetime.now(),
    ...                     'old_hash': old,
    ...                     'new_hash': current
    ...                 }}
    ...                 self.history.append(record)
    ...                 return '检测到变化!'
    ...             return '无变化'
    ...         except Exception as e:
    ...             return f'错误: {{e}}'
    ...
    ...     def run(self, urls, interval=300):
    ...         # 定时监控多个网页
    ...         while True:
    ...             for url in urls:
    ...                 status = self.check(url)
    ...                 now = datetime.now().strftime('%H:%M:%S')
    ...                 print(f'[{{now}}] {{url}}: {{status}}')
    ...             time.sleep(interval)

{BD}四、综合技巧{END}
    >>> # 配置文件管理
    >>> import json
    >>> config = {{'interval': 300, 'urls': [], 'report_dir': 'reports'}}
    >>> with open('config.json', 'w') as f:
    ...     json.dump(config, f, indent=2, ensure_ascii=False)

    >>> # 日志记录
    >>> import logging
    >>> logging.basicConfig(
    ...     filename='monitor.log',
    ...     level=logging.INFO,
    ...     format='%(asctime)s %(message)s'
    ... )
    >>> logging.info('监控启动')

    >>> # 异常重试装饰器
    >>> def retry(max_retries=3, delay=5):
    ...     def decorator(func):
    ...         def wrapper(*args, **kwargs):
    ...             for i in range(max_retries):
    ...                 try:
    ...                     return func(*args, **kwargs)
    ...                 except Exception as e:
    ...                     if i == max_retries - 1:
    ...                         raise
    ...                     time.sleep(delay)
    ...         return wrapper
    ...     return decorator

{C_}自动化与桌面篇到此完成, 接下来进入架构与算法篇!{END}

{DIM}>> 动手试试!{END}
    {C_}选择一个项目, 用之前学过的自动化技能实现{END}
""", ["auto_project", "auto_file_manager", "auto_daily_report", "auto_web_monitor", "auto_hashlib", "auto_retry_decorator"]),
}
