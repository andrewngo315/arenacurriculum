import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent

CHAPTERS = [
    ("01", "*args and **kwargs", HERE / "01_args_kwargs.py"),
    ("02", "Debugging", HERE / "02_debugging.py"),
    ("03", "Generators", HERE / "03_generators.py"),
    ("04", "Map, Filter and Reduce", HERE / "04_map_filter_reduce.py"),
    ("05", "set Data Structure", HERE / "05_sets.py"),
    ("06", "Ternary Operators", HERE / "06_ternary.py"),
    ("07", "Decorators", HERE / "07_decorators.py"),
    ("08", "Global & Return", HERE / "08_global_return.py"),
    ("09", "Mutation", HERE / "09_mutation.py"),
    ("10", "__slots__ Magic", HERE / "10_slots.py"),
    ("11", "Virtual Environment", HERE / "11_virtualenv.md"),
    ("12", "Collections", HERE / "12_collections.py"),
    ("13", "Enumerate", HERE / "13_enumerate.py"),
    ("14", "Zip and unzip", HERE / "14_zip.py"),
    ("15", "Object introspection", HERE / "15_introspection.py"),
    ("16", "Comprehensions", HERE / "16_comprehensions.py"),
    ("17", "Exceptions", HERE / "17_exceptions.py"),
    ("18", "Classes", HERE / "18_classes.py"),
    ("19", "Lambdas", HERE / "19_lambdas.py"),
    ("20", "One-Liners", HERE / "20_one_liners.py"),
    ("21", "for/else", HERE / "21_for_else.py"),
]

GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
GREY = "\033[90m"
RESET = "\033[0m"


def failing_line(stderr, path):
    hits = re.findall(r'File "([^"]+)", line (\d+)', stderr)
    for filename, number in reversed(hits):
        if Path(filename).name == path.name:
            return int(number)
    return None


def run_python(path):
    if not path.exists():
        return "missing", None
    try:
        result = subprocess.run(
            [sys.executable, str(path)],
            capture_output=True,
            text=True,
            cwd=str(path.parent),
            timeout=15,
        )
    except subprocess.TimeoutExpired:
        return "hang", None
    if result.returncode == 0:
        return "pass", None
    line = failing_line(result.stderr, path)
    name = raised_exception(result.stderr)
    if name == "NotImplementedError":
        return "todo", line
    if name == "AssertionError":
        return "wrong", line
    return "error", line


def raised_exception(stderr):
    names = re.findall(
        r"^([A-Za-z_][A-Za-z0-9_]*(?:Error|Exception|Exit|Interrupt))\b", stderr, re.M
    )
    return names[-1] if names else ""


def run_markdown(path):
    if not path.exists():
        return "missing", None
    text = path.read_text()
    blocks = re.findall(
        r"OUTPUT:[ \t]*\n\s*?[ \t]*(?:```|~~~)[^\n]*\n(.*?)(?:```|~~~)", text, re.DOTALL
    )
    answer = re.search(r"ANSWER:\n?(.*)", text, re.DOTALL)
    expected = len(re.findall(r"^OUTPUT:", text, re.M))
    if len(blocks) != expected:
        return "error", None
    filled = [b for b in blocks if b.strip()]
    answered = bool(answer and answer.group(1).strip())
    if not filled and not answered:
        return "todo", None
    if len(filled) < len(blocks) or not answered:
        return "wrong", None
    return "pass", None


def statuses():
    counts = {}
    rows = []
    for chapter in CHAPTERS:
        number, title, path = chapter[0], chapter[1], chapter[2]
        in_progress = len(chapter) > 3 and chapter[3]
        if path.suffix == ".md":
            status, line = run_markdown(path)
        else:
            status, line = run_python(path)
        if in_progress and status in ("todo", "wrong", "error"):
            status = "wip"
        counts[status] = counts.get(status, 0) + 1
        rows.append((number, title, path, status, line))
    return rows, counts


def summary(counts, total):
    return (
        f"{counts.get('pass', 0)}/{total} passing"
        f"  |  {counts.get('wrong', 0)} wrong"
        f"  |  {counts.get('wip', 0)} in progress"
        f"  |  {counts.get('todo', 0)} not started"
        f"  |  {counts.get('error', 0) + counts.get('missing', 0) + counts.get('hang', 0)} broken"
    )


def main():
    labels = {
        "pass": (GREEN, "pass "),
        "wrong": (RED, "wrong"),
        "todo": (GREY, "todo "),
        "error": (YELLOW, "error"),
        "missing": (YELLOW, "gone "),
        "wip": (YELLOW, "wip  "),
        "hang": (YELLOW, "hang "),
    }
    markdown = "--markdown" in sys.argv
    rows, counts = statuses()
    total = len(CHAPTERS)

    if markdown:
        print("| # | Chapter | Status |")
        print("|---|---|---|")
        for number, title, _, status, _ in rows:
            print(f"| {number} | {title} | {labels[status][1].strip()} |")
        print()
        print(f"**{summary(counts, total)}**")
        return 0 if counts.get("pass", 0) == total else 1

    print()
    for number, title, path, status, line in rows:
        colour, label = labels[status]
        where = ""
        if line is not None and status != "pass":
            where = f"{GREY}{path.name}:{line}{RESET}"
        print(f"  {colour}{label}{RESET}  {number}. {title:<24} {where}")

    print()
    print(f"  {summary(counts, total)}")
    print()
    return 0 if counts.get("pass", 0) == total else 1


if __name__ == "__main__":
    sys.exit(main())
