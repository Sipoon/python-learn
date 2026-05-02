#!/usr/bin/env python3
"""Python 互动学习系统 v5.0 启动入口"""
import sys, os, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from python_learn.learn import main

if __name__ == "__main__":
 main()
