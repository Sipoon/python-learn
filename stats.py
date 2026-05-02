"""学习统计面板 — v5.0 六大篇章"""
import time
from typing import Dict, Set

from .ui import C, CHAPTERS


class StudyStats:
    TOTAL_STAGES = 37

    def __init__(self):
        self.total_study_seconds = 0
        self.session_start = None
        self.daily_streak = 0
        self.last_study_date = None
        self.attempts: Dict = {}   # stage_id -> {"correct": int, "total": int, "kp": {kp: {c, t}}}

    def start_session(self):
        self.session_start = time.time()
        today = time.strftime("%Y-%m-%d")
        if self.last_study_date != today:
            yesterday = time.strftime("%Y-%m-%d", time.localtime(time.time() - 86400))
            if self.last_study_date == yesterday:
                self.daily_streak += 1
            elif self.last_study_date != today:
                self.daily_streak = 1
            self.last_study_date = today

    def end_session(self):
        if self.session_start:
            self.total_study_seconds += time.time() - self.session_start
            self.session_start = None

    def record_attempt(self, stage_id: int, correct: bool, kp_list: list = None):
        if stage_id not in self.attempts:
            self.attempts[stage_id] = {"correct": 0, "total": 0, "kp": {}}
        self.attempts[stage_id]["total"] += 1
        if correct:
            self.attempts[stage_id]["correct"] += 1
        if kp_list:
            for kp in kp_list:
                if kp not in self.attempts[stage_id]["kp"]:
                    self.attempts[stage_id]["kp"][kp] = {"c": 0, "t": 0}
                self.attempts[stage_id]["kp"][kp]["t"] += 1
                if correct:
                    self.attempts[stage_id]["kp"][kp]["c"] += 1

    def get_weak_stages(self) -> list:
        weak = []
        for sid, data in self.attempts.items():
            if data["total"] >= 2:
                rate = data["correct"] / data["total"]
                if rate < 0.8:
                    weak.append((sid, rate))
        return sorted(weak, key=lambda x: x[1])

    def get_weak_kp(self) -> list:
        weak = []
        for sid, data in self.attempts.items():
            for kp, kd in data["kp"].items():
                if kd["t"] >= 2:
                    rate = kd["c"] / kd["t"]
                    if rate < 0.8:
                        weak.append((kp, rate))
        return sorted(weak, key=lambda x: x[1])

    @staticmethod
    def format_duration(seconds: float) -> str:
        if seconds < 60:
            return f"{seconds:.0f}秒"
        elif seconds < 3600:
            return f"{seconds/60:.1f}分钟"
        else:
            h = int(seconds // 3600)
            m = int((seconds % 3600) // 60)
            return f"{h}小时{m}分钟"

    def to_dict(self) -> dict:
        return {
            "total_study_seconds": self.total_study_seconds,
            "daily_streak": self.daily_streak,
            "last_study_date": self.last_study_date,
            "attempts": self.attempts,
        }

    def from_dict(self, data: dict):
        self.total_study_seconds = data.get("total_study_seconds", 0)
        self.daily_streak = data.get("daily_streak", 0)
        self.last_study_date = data.get("last_study_date", None)
        self.attempts = data.get("attempts", {})

    def show_panel(self, state, knowledge, stage_names):
        print(f"\n{C.BD}{C.C}{'='*50}{C.END}")
        print(f"{C.BD}{C.C}  学习统计面板{C.END}")
        print(f"{C.BD}{C.C}{'='*50}{C.END}\n")

        # 基本数据
        study_time = self.format_duration(self.total_study_seconds)
        total_q = sum(d["total"] for d in self.attempts.values())
        total_correct = sum(d["correct"] for d in self.attempts.values())
        accuracy = (total_correct / total_q * 100) if total_q > 0 else 0

        print(f"  {C.Y}学习时长：{C.END}{study_time}")
        print(f"  {C.Y}连续天数：{C.END}{self.daily_streak} 天")
        print(f"  {C.Y}答题总数：{C.END}{total_q} 道")
        print(f"  {C.Y}正确率：{C.END}{accuracy:.1f}%")
        print(f"  {C.Y}完成阶段：{C.END}{len(state.completed_stages)}/{self.TOTAL_STAGES}")
        print(f"  {C.Y}完成项目：{C.END}{state.projects_done}/{self.TOTAL_STAGES}")

        # 篇章进度
        print(f"\n  {C.BD}篇章进度{C.END}")
        for ch_name, ch_title, start, end in CHAPTERS:
            done = sum(1 for s in range(start, end+1) if s in state.completed_stages)
            total = end - start + 1
            bar_len = 20
            filled = int(bar_len * done / total) if total > 0 else 0
            bar = "#" * filled + "-" * (bar_len - filled)
            pct = done / total * 100 if total > 0 else 0
            print(f"  {ch_name} {ch_title}: [{bar}] {done}/{total} ({pct:.0f}%)")

        # 弱项分析
        weak_stages = self.get_weak_stages()
        if weak_stages:
            print(f"\n  {C.R}薄弱阶段（正确率<80%）{C.END}")
            for sid, rate in weak_stages[:5]:
                name = stage_names.get(sid, "")
                print(f"    阶段{sid} {name}: {rate*100:.0f}%")

        weak_kp = self.get_weak_kp()
        if weak_kp:
            print(f"\n  {C.R}薄弱知识点（正确率<80%）{C.END}")
            for kp, rate in weak_kp[:5]:
                stage, desc = knowledge.get(kp, (0, kp))
                print(f"    {desc} (阶段{stage}): {rate*100:.0f}%")

        print(f"\n{C.DIM}{'─'*50}{C.END}")
