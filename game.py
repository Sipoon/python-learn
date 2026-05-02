"""游戏状态 - 积分、段位、成就、存档、统计 — v5.0"""
import os
import json
import time
from typing import Set

from .stats import StudyStats


class GameState:
    TOTAL_STAGES = 37

    def __init__(self):
        self.xp = 0
        self.level = 0
        self.streak = 0
        self.max_streak = 0
        self.completed_stages: Set[int] = set()
        self.completed_reviews: Set[int] = set()
        self.perfect_exercises = 0
        self.projects_done = 0
        self.total_exercises_done = 0
        self.wrong_answers = 0
        self.achievements: Set[str] = set()
        self.pitfalls_done: Set[str] = set()
        self.challenges_done = 0
        self.stats = StudyStats()

    def add_xp(self, amount: int, reason: str = ""):
        self.xp += amount
        old_level = self.level
        self.level = self.calc_level(self.xp)
        if self.level > old_level:
            self.show_level_up(old_level, self.level)
            self.xp += 50  # 升级奖励

    @staticmethod
    def calc_level(xp: int) -> int:
        if xp >= 2000: return 6
        if xp >= 1200: return 5
        if xp >= 700: return 4
        if xp >= 350: return 3
        if xp >= 150: return 2
        if xp >= 50: return 1
        return 0

    @staticmethod
    def level_name(lv: int) -> str:
        names = ["小白", "入门", "初级", "中级", "高级", "大师", "码神"]
        icons = ["Lv0", "Lv1", "Lv2", "Lv3", "Lv4", "Lv5", "Lv6"]
        return f"{icons[lv]} {names[lv]}" if lv < len(names) else f"Lv6 {names[-1]}"

    def show_level_up(self, old, new):
        from .ui import C, clear, pause
        clear()
        print(f"""
{C.BD}{C.Y}
   +--------------------------------------+
   |                                      |
   |        恭喜升级！                    |
   |                                      |
   |   {self.level_name(old):14s}  ->  {self.level_name(new):14s}   |
   |                                      |
   |     获得 50 XP 升级奖励！            |
   |                                      |
   +--------------------------------------+{C.END}
""")
        pause("按 Enter 继续...")

    def check_achievements(self):
        T = self.TOTAL_STAGES
        checks = [
            # 基础成就
            ("perfect_ten", "完美十连", "10道题一次答对", self.perfect_exercises >= 10),
            ("all_stages", "学业有成", f"完成所有{T}个阶段", len(self.completed_stages) >= T),
            ("streak_5", "连胜达人", "连续5题答对", self.max_streak >= 5),
            ("streak_10", "连胜王者", "连续10题答对", self.max_streak >= 10),
            ("all_projects", "实战大师", f"完成所有{T}个实战项目", self.projects_done >= T),
            ("zero_error", "零失误", "20道题全部一次答对", self.wrong_answers == 0 and self.total_exercises_done >= 20),
            ("speed_runner", "速通达人", "完成5个阶段", len(self.completed_stages) >= 5),
            ("exercise_50", "题海战术", "完成50道练习题", self.total_exercises_done >= 50),
            ("first_blood", "初出茅庐", "完成第一个阶段", len(self.completed_stages) >= 1),
            ("exercise_20", "勤学苦练", "完成20道练习题", self.total_exercises_done >= 20),
            ("exercise_100", "百题斩", "完成100道练习题", self.total_exercises_done >= 100),
            ("pitfall_5", "避坑达人", "完成5道陷阱题", len(self.pitfalls_done) >= 5),
            ("pitfall_all", "陷阱大师", "完成20道陷阱题", len(self.pitfalls_done) >= 20),
            ("challenge_5", "挑战者", "完成5道挑战题", self.challenges_done >= 5),
            ("challenge_10", "极限挑战", "完成10道挑战题", self.challenges_done >= 10),
            ("review_first", "温故知新", "完成第一个复习关", len(self.completed_reviews) >= 1),
            ("review_all", "复习达人", "完成所有复习关", len(self.completed_reviews) >= 9),
            ("streak_20", "不可阻挡", "连续20题答对", self.max_streak >= 20),
            ("half_done", "半程达人", f"完成{T//2}个阶段", len(self.completed_stages) >= T // 2),
            ("project_5", "项目实战家", "完成5个实战项目", self.projects_done >= 5),
            # 篇章成就
            ("chapter1_done", "基础毕业", "完成第一篇Python基础(1-13)", all(s in self.completed_stages for s in range(1, 14))),
            ("chapter2_done", "进阶之路", "完成第二篇Python进阶(14-18)", all(s in self.completed_stages for s in range(14, 19))),
            ("chapter3_done", "工程基石", "完成第三篇工程基础(19-21)", all(s in self.completed_stages for s in range(19, 22))),
            ("chapter4_done", "数据达人", "完成第四篇数据方向(22-29)", all(s in self.completed_stages for s in range(22, 30))),
            ("chapter5_done", "自动化专家", "完成第五篇自动化与桌面(30-33)", all(s in self.completed_stages for s in range(30, 34))),
            ("chapter6_done", "架构算法师", "完成第六篇架构与算法(34-37)", all(s in self.completed_stages for s in range(34, 38))),
            ("oop_master", "OOP大师", "完成阶段15和16", {15, 16}.issubset(self.completed_stages)),
            ("crawler_first", "初代爬虫", "完成爬虫入门阶段", 22 in self.completed_stages),
            ("auto_first", "自动化入门", "完成脚本自动化阶段", 30 in self.completed_stages),
            ("rpa_first", "RPA先锋", "完成桌面自动化阶段", 31 in self.completed_stages),
            ("algo_master", "算法入门", "完成算法基础阶段", 35 in self.completed_stages),
            ("pattern_master", "模式大师", "完成设计模式阶段", 34 in self.completed_stages),
        ]
        for ach_id, name, desc, cond in checks:
            if cond and ach_id not in self.achievements:
                self.achievements.add(ach_id)
                self._show_achievement(name, desc)

    def _show_achievement(self, name, desc):
        from .ui import C, pause
        print(f"\n{C.BD}{C.Y}")
        print(f"  >> 解锁成就：{name}")
        print(f"     {desc}")
        print(f"     +100 XP{C.END}\n")
        self.xp += 100
        pause()

    def show_status(self):
        from .ui import C
        study_time = self.stats.format_duration(self.stats.total_study_seconds)
        print(f"\n{C.DIM}{'─'*50}{C.END}")
        print(f"  {C.BD}状态栏{C.END}")
        print(f"  段位: {C.Y}{self.level_name(self.level)}{C.END}")
        print(f"  XP: {C.C}{self.xp}{C.END}")
        print(f"  连胜: {C.G if self.streak > 0 else C.DIM}{self.streak}{C.END} (最高: {self.max_streak})")
        print(f"  进度: {len(self.completed_stages)}/{self.TOTAL_STAGES} 阶段")
        print(f"  学习: {C.DIM}{study_time}{C.END}")
        print(f"{C.DIM}{'─'*50}{C.END}\n")


# ===================== 存档 =====================
SAVE_FILE = os.path.join(os.path.expanduser("~"), ".python_learning_v5_save.json")


def save_state(state: GameState):
    state.stats.end_session()
    data = {
        "version": 5,
        "xp": state.xp,
        "level": state.level,
        "streak": state.streak,
        "max_streak": state.max_streak,
        "completed_stages": list(state.completed_stages),
        "completed_reviews": list(state.completed_reviews),
        "perfect_exercises": state.perfect_exercises,
        "projects_done": state.projects_done,
        "total_exercises_done": state.total_exercises_done,
        "wrong_answers": state.wrong_answers,
        "achievements": list(state.achievements),
        "pitfalls_done": list(state.pitfalls_done),
        "challenges_done": state.challenges_done,
        "stats": state.stats.to_dict(),
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_state() -> GameState:
    state = GameState()
    # Try v5 save first, fall back to v3/v4
    for sf in [SAVE_FILE, os.path.join(os.path.expanduser("~"), ".python_learning_v3_save.json")]:
        if os.path.exists(sf):
            try:
                with open(sf, "r", encoding="utf-8") as f:
                    d = json.load(f)
                state.xp = d.get("xp", 0)
                state.level = d.get("level", 0)
                state.streak = d.get("streak", 0)
                state.max_streak = d.get("max_streak", 0)
                state.completed_stages = set(d.get("completed_stages", []))
                state.completed_reviews = set(d.get("completed_reviews", []))
                state.perfect_exercises = d.get("perfect_exercises", 0)
                state.projects_done = d.get("projects_done", 0)
                state.total_exercises_done = d.get("total_exercises_done", 0)
                state.wrong_answers = d.get("wrong_answers", 0)
                state.achievements = set(d.get("achievements", []))
                state.pitfalls_done = set(d.get("pitfalls_done", []))
                state.challenges_done = d.get("challenges_done", 0)
                stats_data = d.get("stats", {})
                if stats_data:
                    state.stats.from_dict(stats_data)
                break
            except Exception:
                pass
    state.stats.start_session()
    return state
