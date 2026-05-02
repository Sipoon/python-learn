"""代码执行沙盒 - 在子进程中安全运行用户代码"""
import os
import sys
import subprocess
from typing import Tuple

# 隔离目录，文件操作在此执行
SANDBOX_DIR = os.path.join(os.path.expanduser("~"), ".python_learn_tmp")
os.makedirs(SANDBOX_DIR, exist_ok=True)


def run_code(code: str, test_input: str = "", timeout: int = 5) -> Tuple[bool, str, str]:
    """
    在子进程中安全执行用户代码。
    返回 (是否成功, 标准输出, 错误信息)
    """
    try:
        proc = subprocess.run(
            [sys.executable, '-c', code],
            input=test_input,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding='utf-8',
            errors='replace',
            cwd=SANDBOX_DIR,
        )
        return (proc.returncode == 0, proc.stdout, proc.stderr)
    except subprocess.TimeoutExpired:
        return (False, "", "Timeout: 代码运行超过5秒，可能存在死循环")
    except Exception as e:
        return (False, "", f"执行错误: {e}")


def run_and_compare(user_code: str, answer_code: str, test_input: str = "") -> Tuple[bool, str, str, str]:
    """
    执行用户代码和标准答案，比较输出。
    返回 (是否匹配, 用户输出, 答案输出, 比较信息)
    """
    ok_a, out_a, _ = run_code(answer_code, test_input)
    expected = out_a.strip() if ok_a else ""

    ok_u, out_u, err_u = run_code(user_code, test_input)
    if not ok_u:
        return (False, out_u, expected, err_u)

    match = out_u.strip() == expected
    msg = "" if match else f"输出是 {out_u.strip()!r}，期望 {expected!r}"
    return (match, out_u.strip(), expected, msg)


def code_match_fallback(user: str, answer: str) -> bool:
    """关键词匹配（降级兜底，当输出比较不可用时）"""
    import re
    def tokens(s):
        return set(re.findall(r'\b\w+\b', s.lower()))
    u, a = tokens(user), tokens(answer)
    if not a:
        return True
    overlap = len(u & a) / len(a)
    return overlap >= 0.6
