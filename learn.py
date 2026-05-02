"""Python 互动学习系统 v5.0 - 主程序 — 六大篇章"""
import random
from typing import Tuple

from .ui import (C, clear, pause, show_banner, print_banner, show_snake,
                 read_multiline, KNOWLEDGE, STAGE_NAMES, CHAPTERS)
from .sandbox import run_code, run_and_compare, code_match_fallback
from .game import GameState, save_state, load_state
from .theory_1_7 import THEORY_1_7
from .theory_8_13 import THEORY_8_13
from .theory_14_18 import THEORY_14_18
from .theory_19_21 import THEORY_19_21
from .theory_22_25 import THEORY_22_25
from .theory_26_29 import THEORY_26_29
from .theory_30_33 import THEORY_30_33
from .theory_34_37 import THEORY_34_37
from .exercises_1_7 import EXERCISES_1_7
from .exercises_8_13 import EXERCISES_8_13
from .exercises_14_18 import EXERCISES_14_18
from .exercises_19_21 import EXERCISES_19_21
from .exercises_22_25 import EXERCISES_22_25
from .exercises_26_29 import EXERCISES_26_29
from .exercises_30_33 import EXERCISES_30_33
from .exercises_34_37 import EXERCISES_34_37
from .projects import PROJECTS
from .pitfalls import PITFALL_EXERCISES
from .review import REVIEW_STAGES
from .challenges import CHALLENGE_EXERCISES
from .kamacoder_practice import KAMACODER_PRACTICE

THEORY = {**THEORY_1_7, **THEORY_8_13, **THEORY_14_18, **THEORY_19_21,
          **THEORY_22_25, **THEORY_26_29, **THEORY_30_33, **THEORY_34_37}
EXERCISES = {**EXERCISES_1_7, **EXERCISES_8_13, **EXERCISES_14_18, **EXERCISES_19_21,
             **EXERCISES_22_25, **EXERCISES_26_29, **EXERCISES_30_33, **EXERCISES_34_37}

DIFF_ICONS = {"basic": "[*]", "intermediate": "[**]", "challenge": "[***]"}

# Review triggers: after these stages, suggest a review
REVIEW_TRIGGERS = {3, 6, 9, 12, 16, 18, 21, 25, 29, 33, 37}


def get_theory(stage: int) -> Tuple[str, list]:
    data = THEORY.get(stage, ("", []))
    if isinstance(data, str):
        return (data, [])
    return data


def get_exercises(stage: int) -> list:
    return EXERCISES.get(stage, [])


def get_ex_display(ex: dict) -> str:
    """Get display text for an exercise, supporting both old (q) and new (title+desc) formats."""
    if "q" in ex:
        return ex["q"]
    title = ex.get("title", "")
    desc = ex.get("desc", "")
    if desc and desc != title:
        return f"{title}\n{desc}"
    return title


def get_project(stage: int) -> dict:
    return PROJECTS.get(stage, {})


# ===================== 答案展示 =====================

def show_answer(code: str, explain: str = ""):
    """展示答案代码 + 解释说明"""
    print(f"{C.G}参考答案：{C.END}")
    for line in code.strip().split('\n'):
        print(f"  {C.C}{line}{C.END}")
    if explain:
        print(f"\n{C.Y}解题思路：{C.END}")
        for line in explain.strip().split('\n'):
            print(f"  {line}")
    print()


# ===================== 核心验证逻辑 =====================

def check_answer(user_code: str, answer_code: str, test_input: str = "") -> Tuple[bool, str, str]:
    """执行用户代码和标准答案，比较输出"""
    matched, out_u, expected, msg = run_and_compare(user_code, answer_code, test_input)
    if matched:
        return (True, expected, "")
    # 降级：输出不匹配但代码逻辑接近
    if code_match_fallback(user_code, answer_code):
        return (True, expected, "")
    return (False, expected, msg)


def offer_redo(question: str, answer_code: str, test_input: str, state: GameState):
    """看完答案后提供重做机会"""
    redo = input(f"{C.Y}要不要再试一次？(y=重做 / 其他=下一题)：{C.END}").strip().lower()
    if redo == "y":
        print(f"\n{C.C}再来一次！这次你可以的！{C.END}")
        print(f"{C.DIM}（答案已经看过了，试着凭记忆写出来）{C.END}\n")
        for line in question.strip().split('\n'):
            print(f"  {line}")
        print()
        print(f"{C.G}输入答案代码：{C.END}")
        user_code = read_multiline()
        if user_code.strip():
            ok_u, out_u, err_u = run_code(user_code, test_input)
            matched, expected, _ = check_answer(user_code, answer_code, test_input)
            if matched:
                state.add_xp(8, "重做答对")
                state.streak += 1
                state.max_streak = max(state.max_streak, state.streak)
                print(f"{C.G}这次对了！+8 XP（重做奖励）{C.END}")
                show_snake("happy")
            else:
                if not ok_u:
                    print(f"{C.R}代码运行出错：{err_u[:100]}{C.END}")
                else:
                    print(f"{C.DIM}输出不太对，但没关系，下次一定会！{C.END}")
                    print(f"{C.DIM}你的输出：{out_u.strip()[:100]}{C.END}")
                    print(f"{C.DIM}期望输出：{expected[:100]}{C.END}")
                state.streak = 0
        pause()


# ===================== 理论阶段代码交互 =====================

def run_theory_code_interactive():
    """让用户输入代码并实时执行查看结果"""
    print(f"\n{C.BD}{C.M}>> 代码实验室{C.END}")
    print(f"{C.DIM}输入任意 Python 代码，实时运行看结果！输入空行退出实验{C.END}")
    while True:
        print(f"{C.G}输入代码：{C.END}")
        code = read_multiline()
        if not code.strip():
            print(f"{C.DIM}退出代码实验室{C.END}")
            break
        ok, out, err = run_code(code)
        if ok:
            print(f"{C.G}运行结果：{C.END}")
            for line in out.splitlines()[:10]:
                print(f"  {line}")
            if len(out.splitlines()) > 10:
                print(f"  {C.DIM}... (省略){C.END}")
        else:
            print(f"{C.R}出错：{C.END}")
            for el in err.strip().splitlines()[-3:]:
                print(f"  {C.R}{el}{C.END}")
        print()


# ===================== 陷阱题练习 =====================

def do_pitfalls(state: GameState):
    """易错陷阱题练习"""
    clear()
    show_snake("think")
    print_banner("  易错陷阱题")

    undone = []
    for stage_id, pit_list in PITFALL_EXERCISES.items():
        for p in pit_list:
            if p["id"] not in state.pitfalls_done:
                undone.append(p)
    if not undone:
        print(f"{C.G}所有陷阱题都完成了！真厉害！{C.END}")
        pause()
        return

    back_count = 0
    for p in undone:
        r = pause(f"按 Enter 继续 / b 返回... ({back_count}道已做)")
        if r == "back":
            return
        print(f"\n{C.BD}{C.R}!! {p['title']}{C.END}")
        print(f"{C.DIM}涉及阶段：{p['stage']}{C.END}\n")
        print(f"{C.Y}有问题的代码：{C.END}")
        for line in p["buggy_code"].strip().split('\n'):
            print(f"  {C.R}{line}{C.END}")
        print()
        print(f"{C.Y}{p['question']}{C.END}")
        if p.get("hint"):
            print(f"{C.DIM}提示：{p['hint']}{C.END}")
        print(f"{C.G}输入修正后的代码（或 skip 跳过）：{C.END}")

        user_code = read_multiline()
        if user_code.strip().lower() == "skip":
            print(f"{C.DIM}已跳过{C.END}")
            print(f"\n{C.Y}正确答案：{C.END}")
            print(p["answer"])
            print(f"\n{C.B}{C.C}解析：{C.END}")
            print(f"  {p['explanation']}")
            if pause("按 Enter 继续 / b 返回...") == "back":
                return
            continue

        matched, expected, _ = check_answer(user_code, p["answer"], "")
        if matched:
            print(f"{C.G}正确！{C.END}")
            state.pitfalls_done.add(p["id"])
            state.add_xp(20, "陷阱题答对")
            back_count += 1
        else:
            print(f"{C.R}还不对，来看看正确答案{C.END}")
            print(f"\n{C.Y}正确答案：{C.END}")
            print(p["answer"])

        print(f"\n{C.B}{C.C}解析：{C.END}")
        print(f"  {p['explanation']}")
        state.check_achievements()
        if pause("按 Enter 继续 / b 返回...") == "back":
            return


# ===================== 复习关卡 =====================

def do_review(review_stage: int, state: GameState):
    """执行复习关卡"""
    data = REVIEW_STAGES.get(review_stage)
    if not data:
        return

    clear()
    show_snake("happy")
    print_banner(f"  复习：{data['name']}")
    print(f"{C.Y}{data['desc']}{C.END}\n")

    exercises = data["exercises"]
    correct_count = 0

    for idx, ex in enumerate(exercises, 1):
        q = get_ex_display(ex)
        hint = ex.get("hint", "")
        answer_code = ex.get("answer", "")
        kp = ex.get("kp", [])
        test_input = ex.get("test_input", "")

        for attempt in range(3):
            print(f"\n{C.B}{C.C}复习题 {idx}/{len(exercises)} {DIFF_ICONS.get(ex.get('diff',''), '')}{C.END}")
            print(f"{C.DIM}知识点：{' | '.join(kp)}{C.END}\n")
            for line in q.strip().split('\n'):
                print(f"  {line}")
            print()
            template = ex.get("template", "")
            if template:
                print(f"{C.DIM}代码模板：{C.END}")
                for tline in template.strip().split('\n'):
                    print(f"{C.DIM}  {tline}{C.END}")
                print()
            if hint:
                print(f"{C.DIM}提示：{hint}{C.END}")
            print(f"{C.G}输入答案代码：{C.END}")

            user_code = read_multiline()
            if user_code.strip().lower() == "skip":
                break

            matched, expected, cmp_msg = check_answer(user_code, answer_code, test_input)
            state.stats.record_attempt(review_stage, matched, kp)

            if matched:
                state.add_xp(12, "复习题答对")
                state.streak += 1
                state.max_streak = max(state.max_streak, state.streak)
                correct_count += 1
                print(f"{C.G}正确！+12 XP{C.END}")
                break
            else:
                state.wrong_answers += 1
                state.streak = 0
                remaining = 2 - attempt
                if remaining > 0:
                    print(f"{C.R}输出不正确，还剩 {remaining} 次机会{C.END}")
                else:
                    print(f"{C.R}来看答案：{C.END}")
                    show_answer(answer_code, ex.get("explain", ""))
                    offer_redo(q, answer_code, test_input, state)

    # 复习完成
    state.completed_reviews.add(review_stage)
    bonus = correct_count * 5
    state.add_xp(bonus, "复习完成奖励")
    state.check_achievements()
    print(f"\n{C.G}复习完成！答对 {correct_count}/{len(exercises)}，额外 +{bonus} XP{C.END}")
    show_snake("celebrate")
    pause()


# ===================== 挑战模式 =====================

def do_challenges(state: GameState):
    """挑战模式 - 额外难题"""
    clear()
    show_snake("think")
    print_banner("  挑战模式")
    print(f"{C.DIM}额外拔高题，不限次数，挑战自我！{C.END}\n")

    available = []
    for stage in range(1, 38):
        if stage in state.completed_stages:
            ch_list = CHALLENGE_EXERCISES.get(stage, [])
            for ch in ch_list:
                available.append((stage, ch))

    if not available:
        print(f"{C.DIM}先完成一些阶段解锁挑战题吧！{C.END}")
        pause()
        return

    print(f"{C.Y}已解锁 {len(available)} 道挑战题{C.END}")
    for i, (stage, ch) in enumerate(available, 1):
        diff_icon = DIFF_ICONS.get(ch.get("diff", "challenge"), "[***]")
        stage_name = STAGE_NAMES.get(stage, "")
        print(f"  {i}. {diff_icon} [{stage_name}] {get_ex_display(ch)[:40]}...")

    while True:
        print(f"\n{C.Y}输入题号开始挑战（0=返回）：{C.END}")
        try:
            choice = int(input(f"{C.G}> {C.END}").strip())
        except ValueError:
            break
        if choice == 0:
            break

        if choice < 1 or choice > len(available):
            print(f"{C.Y}无效题号{C.END}")
            continue

        stage, ch = available[choice - 1]
        clear()
        print(f"\n{C.BD}{C.M}挑战题 {C.END}")
        print(f"{C.DIM}来自阶段{stage}：{STAGE_NAMES.get(stage, '')}{C.END}\n")
        for line in get_ex_display(ch).strip().split('\n'):
            print(f"  {line}")
        if ch.get("hint"):
            print(f"{C.DIM}提示：{ch['hint']}{C.END}")
        print(f"{C.G}输入答案代码：{C.END}")

        user_code = read_multiline()
        if not user_code.strip():
            continue

        test_input = ch.get("test_input", "")
        matched, expected, _ = check_answer(user_code, ch["answer"], test_input)
        state.stats.record_attempt(stage, matched, ch.get("kp", []))


        if matched:
            print(f"{C.G}挑战成功！+25 XP{C.END}")
            state.add_xp(25, "挑战题答对")
            state.challenges_done += 1
            show_snake("celebrate")
        else:
            print(f"{C.R}这次没过，没关系！{C.END}")
            print(f"{C.DIM}参考答案：{C.END}")
            show_answer(ch["answer"], ch.get("explain", ""))
            state.wrong_answers += 1
            state.streak = 0

        state.check_achievements()
        if pause("按 Enter 继续 / b 返回题库...") == "back":
            break


# ===================== 卡码网精选算法 =====================

def do_kamacoder(state: GameState):
    """卡码网精选算法练习 — ACM模式"""
    clear()
    show_snake("think")
    print_banner("  卡码网精选算法")
    print(f"{C.DIM}来自 kamacoder.com 的经典算法题，练习 ACM 输入输出模式{C.END}")
    print(f"{C.DIM}入门篇 → 进阶篇 → 挑战篇，循序渐进{C.END}\n")

    levels = [("basic", "入门篇", C.G), ("intermediate", "进阶篇", C.Y), ("challenge", "挑战篇", C.R)]

    for key, label, color in levels:
        problems = KAMACODER_PRACTICE[key]
        done_count = 0  # TODO: track kamacoder completion
        print(f"  {color}{label} ({len(problems)}题){C.END}")
    print()
    print(f"  {C.Y}1{C.END} - 入门篇 (10题)")
    print(f"  {C.Y}2{C.END} - 进阶篇 (10题)")
    print(f"  {C.Y}3{C.END} - 挑战篇 (10题)")
    print(f"  {C.Y}4{C.END} - 随机一题")
    print(f"  {C.Y}0{C.END} - 返回")

    choice = input(f"{C.G}> {C.END}").strip()

    if choice == "0":
        return

    level_map = {"1": "basic", "2": "intermediate", "3": "challenge"}
    if choice in level_map:
        level_key = level_map[choice]
    elif choice == "4":
        all_probs = KAMACODER_PRACTICE["basic"] + KAMACODER_PRACTICE["intermediate"] + KAMACODER_PRACTICE["challenge"]
        import random as _r
        prob = _r.choice(all_probs)
        _do_kamacoder_problem(prob, state)
        return
    else:
        return

    problems = KAMACODER_PRACTICE[level_key]
    level_names = {"basic": "入门篇", "intermediate": "进阶篇", "challenge": "挑战篇"}

    while True:
        clear()
        print_banner(f"  {level_names[level_key]}")

        for i, p in enumerate(problems, 1):
            diff_icon = DIFF_ICONS.get(p.get("diff", "basic"), "[*]")
            cat = p.get("category", "")
            print(f"  {C.C}{i:2d}.{C.END} {diff_icon} [{cat}] {p['title']} (#{p['id']})")
        print()
        print(f"{C.Y}输入题号 (1-{len(problems)})，0=返回：{C.END}")

        try:
            idx = int(input(f"{C.G}> {C.END}").strip())
        except ValueError:
            break
        if idx < 1 or idx > len(problems):
            break

        _do_kamacoder_problem(problems[idx - 1], state)
        if pause("按 Enter 继续 / b 返回题库列表...") == "back":
            break


def _do_kamacoder_problem(prob: dict, state: GameState):
    """执行单道卡码网题目"""
    clear()
    show_snake("think")

    diff_icon = DIFF_ICONS.get(prob.get("diff", "basic"), "[*]")
    print_banner(f"  {diff_icon} {prob['title']}")
    print(f"{C.DIM}来源：kamacoder.com #{prob['id']}{C.END}")
    if prob.get("url"):
        print(f"{C.DIM}题目链接：{prob['url']}{C.END}")
    print(f"{C.DIM}分类：{prob.get('category', '')}{C.END}")
    print(f"{C.DIM}知识点：{' | '.join(prob.get('kp', []))}{C.END}\n")

    print(f"{C.Y}题目描述：{C.END}")
    for line in prob["desc"].strip().split('\n'):
        print(f"  {line}")
    print()

    if prob.get("hint"):
        print(f"{C.DIM}提示：{prob['hint']}{C.END}\n")

    print(f"{C.C}代码模板：{C.END}")
    print(f"{C.DIM}{'─'*50}{C.END}")
    for line in prob.get("template", "").strip().split('\n'):
        print(f"  {C.DIM}{line}{C.END}")
    print(f"{C.DIM}{'─'*50}{C.END}\n")

    print(f"{C.Y}输入测试数据（ACM模式，可粘贴多行，空行结束）：{C.END}")
    test_input = prob.get("test_input", "")
    print(f"{C.DIM}默认测试数据：{C.END}")
    for line in test_input.strip().split('\n'):
        print(f"  {C.DIM}{line}{C.END}")
    print(f"{C.DIM}(直接 Enter 使用默认测试数据){C.END}")

    custom_input = read_multiline()
    if custom_input.strip():
        test_input = custom_input

    print(f"\n{C.G}输入你的代码（或 skip 直接看答案）：{C.END}")
    user_code = read_multiline()

    if user_code.strip().lower() == "skip":
        print(f"\n{C.B}{C.Y}参考答案：{C.END}")
        print(f"{C.DIM}{'─'*50}{C.END}")
        show_answer(prob["answer"], prob.get("explain", ""))
        print(f"{C.DIM}{'─'*50}{C.END}")
        pause()
        return

    if not user_code.strip():
        return

    # 执行用户代码
    ok_u, out_u, err_u = run_code(user_code, test_input)

    # 执行参考答案
    ok_a, out_a, err_a = run_code(prob["answer"], test_input)

    if not ok_u:
        print(f"{C.R}代码运行出错：{C.END}")
        for el in err_u.strip().splitlines()[-5:]:
            print(f"  {C.R}{el}{C.END}")
        print(f"\n{C.DIM}来看参考答案...{C.END}")
        pause()
        print(f"\n{C.B}{C.Y}参考答案：{C.END}")
        show_answer(prob["answer"], prob.get("explain", ""))
        if prob.get("expected"):
            print(f"\n{C.DIM}期望输出：{prob['expected']}{C.END}")
        state.wrong_answers += 1
        state.streak = 0
        pause()
        return

    expected = prob.get("expected", out_a)
    if out_u.strip() == expected.strip():
        xp_gain = {"basic": 15, "intermediate": 25, "challenge": 40}.get(prob.get("diff", "basic"), 15)
        print(f"{C.G}正确！+{xp_gain} XP{C.END}")
        state.add_xp(xp_gain, f"卡码网{prob['title']}答对")
        state.streak += 1
        state.max_streak = max(state.max_streak, state.streak)
        show_snake("celebrate")
    else:
        print(f"{C.Y}输出不太对，来看看差异：{C.END}")
        print(f"  {C.DIM}你的输出：{C.END}")
        for line in out_u.strip().splitlines()[:8]:
            print(f"    {C.DIM}{line}{C.END}")
        print(f"  {C.DIM}期望输出：{C.END}")
        for line in expected.strip().splitlines()[:8]:
            print(f"    {C.DIM}{line}{C.END}")
        print(f"\n{C.Y}参考答案：{C.END}")
        show_answer(prob["answer"], prob.get("explain", ""))
        state.wrong_answers += 1
        state.streak = 0

    state.check_achievements()
    pause()


# ===================== 统计面板 =====================

def show_stats_panel(state: GameState):
    """显示学习统计面板"""
    clear()
    state.stats.show_panel(state, KNOWLEDGE, STAGE_NAMES)
    pause()


# ===================== 学习流程 =====================

def learn(stage_id: int, state: GameState):
    """学习一个阶段"""
    clear()
    show_snake("happy")

    theory_text, kp_list = get_theory(stage_id)
    exercises = get_exercises(stage_id)
    project = get_project(stage_id)

    title = f"阶段{stage_id}：{STAGE_NAMES.get(stage_id, '')}"
    print_banner(f"  {title}")

    # 知识点列表
    print(f"{C.Y}本阶段知识点：{C.END}")
    for kp in kp_list:
        stage_kp, name_kp = KNOWLEDGE.get(kp, (0, kp))
        print(f"  {C.C}*{C.END} {C.B}{name_kp}{C.END}")
    print()

    # ---- 理论学习 ----
    print(f"{C.BD}{C.Y}>> 理论讲解{C.END}")
    print(f"{C.Y}{'='*50}{C.END}")
    for i, line in enumerate(theory_text.strip().split('\n'), 1):
        print(f"{C.DIM}{i:3d}|{C.END} {line}")
    print()

    # 理论后提供代码实验
    lab = input(f"{C.M}想动手试试代码吗？(y=打开代码实验室 / Enter=继续)：{C.END}").strip().lower()
    if lab == "y":
        run_theory_code_interactive()

    # ---- 练习题 ----
    if exercises:
        print(f"\n{C.BD}{C.Y}>> 练习题 ({len(exercises)} 道){C.END}")
        print(f"{C.Y}{'='*50}{C.END}")

        for idx, ex in enumerate(exercises, 1):
            r = pause(f"第 {idx}/{len(exercises)} 题，按 Enter 开始 / b 返回主菜单...")
            if r == "back":
                return

            q = get_ex_display(ex)
            hint = ex.get("hint", "")
            answer_code = ex.get("answer", "")
            kp = ex.get("kp", [])
            test_input = ex.get("test_input", "")
            diff = ex.get("diff", "basic")
            diff_icon = DIFF_ICONS.get(diff, "[?]")

            for attempt in range(3):
                print(f"\n{C.B}{C.C}第 {idx}/{len(exercises)} 题 {diff_icon}{C.END}")
                print(f"{C.DIM}知识点：{' | '.join(kp)}{C.END}")
                print()
                for line in q.strip().split('\n'):
                    print(f"  {line}")
                print()

                # Show template if available (new format)
                template = ex.get("template", "")
                if template:
                    print(f"{C.DIM}代码模板：{C.END}")
                    for tline in template.strip().split('\n'):
                        print(f"{C.DIM}  {tline}{C.END}")
                    print()

                if hint and attempt > 0:
                    print(f"{C.Y}提示：{hint}{C.END}")
                print(f"{C.G}输入答案代码（或 skip 跳过）：{C.END}")

                user_code = read_multiline()

                if user_code.strip().lower() == "skip":
                    print(f"{C.DIM}已跳过{C.END}")
                    break

                # ---- 真实执行用户代码 ----
                ok_u, out_u, err_u = run_code(user_code, test_input)

                if not ok_u:
                    state.wrong_answers += 1
                    state.streak = 0
                    state.stats.record_attempt(stage_id, False, kp)
                    remaining = 2 - attempt
                    print(f"{C.R}代码运行出错！{C.END}")
                    for el in err_u.strip().splitlines()[-3:]:
                        print(f"{C.R}  {el}{C.END}")
                    if remaining > 0:
                        print(f"{C.Y}还剩 {remaining} 次机会{C.END}")
                    else:
                        print(f"{C.R}次数用完，来看正确答案：{C.END}")
                        show_snake("sad")
                        show_answer(answer_code, ex.get("explain", ""))
                        if pause("\u6309 Enter \u7ee7\u7eed / b \u8fd4\u56de\u4e3b\u83dc\u5355...") == "back":
                            return
                        offer_redo(q, answer_code, test_input, state)
                    continue

                # ---- 执行成功，比较输出 ----
                matched, expected, cmp_msg = check_answer(user_code, answer_code, test_input)
                state.stats.record_attempt(stage_id, matched, kp)

                if matched:
                    xp_gain = 15 if attempt == 0 else 10
                    state.add_xp(xp_gain, f"练习题答对({attempt+1}次)")
                    if attempt == 0:
                        state.perfect_exercises += 1
                        state.streak += 1
                        state.max_streak = max(state.max_streak, state.streak)
                    print(f"{C.G}正确！+{xp_gain} XP{C.END}")
                    print(f"{C.DIM}你的输出：{C.END}")
                    for line in out_u.strip().splitlines()[:5]:
                        print(f"{C.DIM}  {line}{C.END}")
                    show_snake("happy")
                    state.total_exercises_done += 1
                    state.check_achievements()
                    if pause("\u6309 Enter \u7ee7\u7eed / b \u8fd4\u56de\u4e3b\u83dc\u5355...") == "back":
                        return
                    break
                else:
                    state.wrong_answers += 1
                    state.streak = 0
                    remaining = 2 - attempt
                    print(f"{C.R}输出不正确{C.END}")
                    print(f"{C.DIM}你的输出：{C.END}")
                    for line in out_u.strip().splitlines()[:5]:
                        print(f"{C.DIM}  {line}{C.END}")
                    if expected:
                        print(f"{C.DIM}期望输出：{C.END}")
                        for line in expected.strip().splitlines()[:5]:
                            print(f"{C.DIM}  {line}{C.END}")
                    if remaining > 0:
                        print(f"{C.Y}还剩 {remaining} 次机会{C.END}")
                        if hint:
                            print(f"{C.Y}提示：{hint}{C.END}")
                    else:
                        print(f"{C.R}次数用完，来看正确答案：{C.END}")
                        show_snake("sad")
                        show_answer(answer_code, ex.get("explain", ""))
                        if pause("\u6309 Enter \u7ee7\u7eed / b \u8fd4\u56de\u4e3b\u83dc\u5355...") == "back":
                            return
                        offer_redo(q, answer_code, test_input, state)

    # ---- 实战项目 ----
    if project:
        print(f"\n{C.BD}{C.G}>> 实战项目：{project['name']}{C.END}")
        print(f"{C.G}{'='*50}{C.END}")
        print(f"{C.Y}项目描述：{project['desc']}{C.END}\n")
        print(f"{C.DIM}要求：{C.END}")
        for req in project.get("requirements", []):
            print(f"  {C.C}*{C.END} {req}")
        print()

        print(f"{C.G}请自己动手实现，然后粘贴代码提交（或 skip 直接看答案）：{C.END}")
        user_project = read_multiline()

        if user_project.strip().lower() != "skip":
            test_in = project.get("test_input", "")
            ok_u, out_u, err_u = run_code(user_project, test_in)
            if ok_u:
                expected = project.get("expected", "")
                if expected and out_u.strip() == expected.strip():
                    print(f"{C.G}完美通过！输出完全正确！{C.END}")
                else:
                    print(f"{C.Y}代码运行成功！你的输出：{C.END}")
                    for line in out_u.strip().splitlines()[:8]:
                        print(f"  {line}")
                    if expected:
                        print(f"{C.DIM}参考输出：{C.END}")
                        for line in expected.strip().splitlines()[:8]:
                            print(f"{C.DIM}  {line}{C.END}")
            else:
                print(f"{C.R}代码运行出错：{C.END}")
                for el in err_u.strip().splitlines()[-3:]:
                    print(f"{C.R}  {el}{C.END}")
            print()
            pause("按 Enter 查看参考方案...")

        print(f"\n{C.B}{C.Y}参考方案（带详细注释）：{C.END}")
        print("-" * 50)
        show_answer(project.get("answer", ""), project.get("explain", ""))
        print("-" * 50)
        show_snake("celebrate")
        state.add_xp(30, "完成实战项目")
        state.projects_done += 1
        state.completed_stages.add(stage_id)
        print(f"{C.G}项目完成！+30 XP{C.END}")
        state.check_achievements()
        pause()


# ===================== 主菜单 =====================

def main():
    state = load_state()
    clear()
    show_banner()

    if state.total_exercises_done > 0:
        print(f"{C.Y}欢迎回来！继续学习吧{C.END}")
    else:
        print(f"{C.Y}从零开始学 Python！{C.END}")
        print(f"{C.DIM}v5.0 六大篇章：基础→进阶→工程基础→数据方向→自动化→架构算法 | 37阶段完整体系{C.END}")
    state.show_status()
    pause()

    while True:
        clear()
        show_snake("think")
        print_banner("  Python 互动学习系统 v5.0")
        state.show_status()

        print(f"{C.G}请选择阶段（1-37）：{C.END}")
        print(f"  {C.DIM}标记：[v]已学  [r]复习待做  [R]复习完成{C.END}")
        for ch_name, ch_title, start, end in CHAPTERS:
            print(f"  {C.DIM}--- {ch_name} {ch_title} (S{start}-S{end}) ---{C.END}")
            for sid in range(start, end + 1):
                name = STAGE_NAMES.get(sid, "")
                done = "[v]" if sid in state.completed_stages else "   "
                review_mark = ""
                if sid in REVIEW_TRIGGERS:
                    r_done = "[R]" if sid in state.completed_reviews else "[r]"
                    review_mark = f" {C.DIM}{r_done}{C.END}"
                print(f"  {done} {C.C}{sid:2d}.{C.END} {name}{review_mark}")

        print()
        print(f"  {C.Y}0  - 查看成就{C.END}")
        print(f"  {C.Y}p  - 易错陷阱题{C.END}")
        print(f"  {C.Y}c  - 挑战模式{C.END}")
        print(f"  {C.Y}s  - 学习统计{C.END}")
        print(f"  {C.Y}l  - 代码实验室{C.END}")
        print(f"  {C.Y}k  - 卡码网精选算法{C.END}")
        print(f"  {C.Y}q  - 保存退出{C.END}")

        choice = input(f"{C.G}> {C.END}").strip()

        if choice == "q":
            save_state(state)
            clear()
            show_snake("happy")
            print(f"{C.C}再见！下次继续学习{C.END}")
            print(f"{C.DIM}进度已保存{C.END}")
            break

        if choice == "0":
            clear()
            print_banner("  成就墙")
            print(f"  段位：{C.Y}{GameState.level_name(state.level)}{C.END}")
            print(f"  XP：{C.C}{state.xp}{C.END}")
            print(f"  连胜最高：{C.G}{state.max_streak}{C.END}")
            print(f"  零失误答题：{state.perfect_exercises}")
            print(f"  完成阶段：{len(state.completed_stages)}/37")
            print(f"  完成项目：{state.projects_done}/37")
            print(f"  陷阱题：{len(state.pitfalls_done)}")
            print(f"  挑战题：{state.challenges_done}")
            ach_names = {
                "perfect_ten": "完美十连", "all_stages": "学业有成",
                "streak_5": "连胜达人", "streak_10": "连胜王者",
                "all_projects": "实战大师", "zero_error": "零失误",
                "speed_runner": "速通达人", "exercise_50": "题海战术",
                "first_blood": "初出茅庐", "exercise_20": "勤学苦练",
                "exercise_100": "百题斩", "pitfall_5": "避坑达人",
                "pitfall_all": "陷阱大师", "challenge_5": "挑战者",
                "challenge_10": "极限挑战", "review_first": "温故知新",
                "review_all": "复习达人", "streak_20": "不可阻挡",
                "half_done": "半程达人", "project_5": "项目实战家",
                "chapter1_done": "基础毕业", "chapter2_done": "进阶之路",
                "chapter3_done": "工程基石", "chapter4_done": "数据达人",
                "chapter5_done": "自动化专家", "chapter6_done": "架构算法师",
                "oop_master": "OOP大师", "crawler_first": "初代爬虫",
                "auto_first": "自动化入门", "rpa_first": "RPA先锋",
                "algo_master": "算法入门", "pattern_master": "模式大师",
            }
            print(f"\n  {C.Y}已解锁成就（{len(state.achievements)}/{len(ach_names)}）：{C.END}")
            if state.achievements:
                for ach in sorted(state.achievements):
                    print(f"    {C.G}[v]{C.END} {ach_names.get(ach, ach)}")
            else:
                print(f"    {C.DIM}暂无成就，继续努力！{C.END}")

            locked = [a for a in ach_names if a not in state.achievements]
            if locked:
                print(f"\n  {C.DIM}未解锁：{C.END}")
                for ach in locked:
                    print(f"    {C.DIM}[ ] {ach_names[ach]}{C.END}")
            pause()
            continue

        if choice == "p":
            do_pitfalls(state)
            continue

        if choice == "c":
            do_challenges(state)
            continue

        if choice == "s":
            show_stats_panel(state)
            continue

        if choice == "l":
            clear()
            print_banner("  代码实验室")
            run_theory_code_interactive()
            continue

        if choice == "k":
            do_kamacoder(state)
            continue

        try:
            sid = int(choice)
            if 1 <= sid <= 37:
                learn(sid, state)
                # 学完自动触发复习提示
                if sid in REVIEW_TRIGGERS and sid not in state.completed_reviews:
                    do_review_now = input(f"{C.Y}检测到可用的复习关！要挑战吗？(y/n)：{C.END}").strip().lower()
                    if do_review_now == "y":
                        do_review(sid, state)
            else:
                print(f"{C.R}请输入 1-37 之间的数字{C.END}")
                pause()
        except ValueError:
            print(f"{C.R}无效输入！{C.END}")
            pause()
