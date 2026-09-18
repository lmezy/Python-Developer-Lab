# ruff: noqa: E501

from app.db.base import Base
from app.db.models import Course, KnowledgePoint, Lesson, Problem, TestCase
from app.db.session import SessionLocal, engine
from app.executor.runner import run_python


def _norm(value: str) -> str:
    return value.replace("\r\n", "\n").rstrip("\n")


def _validate_reference(solution: str, cases: list[tuple[str, str]], problem_type: str = "BASIC") -> None:
    for input_data, expected in cases:
        execution_code = solution
        if problem_type == "FUNCTION":
            execution_code = f"{solution}\n{input_data}"
            input_data = ""
        result = run_python(execution_code, input_data)
        if result.status != "PASSED" or _norm(result.stdout) != _norm(expected):
            raise RuntimeError(
                f"参考答案验证失败: status={result.status}, "
                f"stdout={result.stdout!r}, expected={expected!r}"
            )


PROBLEMS = [
    {
        "code": "PY-BAS-001", "title": "输出第一行 Python 文本",
        "description": "编写一个程序，向标准输出打印一行文本。程序运行后必须只输出下面的目标内容，不要输出额外说明。",
        "input_spec": "本题没有输入。",
        "output_spec": "输出一行，内容必须是：Hello, Python!\n注意：Hello 后有一个空格；逗号后有一个空格；末尾有英文感叹号。",
        "constraints": "可能用到的工具：print()。\n判定方式：程序实际运行后的标准输出与目标输出一致。",
        "starter": "# 在这里编写你的程序\n",
        "solution": "print('Hello, Python!')",
        "expected": "Hello, Python!\n", "concepts": "输出与 print",
        "hint": "先确认目标字符串中的大小写、空格、逗号和感叹号。",
    },
    {
        "code": "PY-BAS-002", "title": "使用变量输出问候语",
        "description": "创建变量 name 保存字符串 Python，并输出一行完整问候语。变量名必须为 name；输出结果必须符合目标格式。",
        "input_spec": "本题没有输入。",
        "output_spec": "输出：Hello, Python!\n注意：Hello 后和逗号后各有一个空格，末尾有英文感叹号。",
        "constraints": "可能用到的工具：变量赋值、字符串、print()。\n判定方式：只检查程序运行结果，不限制字符串拼接或格式化的具体写法。",
        "starter": "# 创建变量 name，并输出目标问候语\nname = ''\n",
        "solution": "name = 'Python'\nprint('Hello, ' + name + '!')",
        "expected": "Hello, Python!\n", "concepts": "变量,字符串",
        "hint": "先把 Python 保存到 name，再思考如何把它放进问候语。",
    },
    {
        "code": "PY-BAS-003", "title": "根据温度输出状态",
        "description": "读取一个整数温度，根据温度输出状态：温度大于等于 30 时输出 hot，否则输出 cool。",
        "input_spec": "输入一行整数 temperature，范围为 -100 到 100。",
        "output_spec": "只输出一行：满足 temperature >= 30 时输出 hot，否则输出 cool。",
        "constraints": "可能用到的工具：input()、int()、if/else。\n边界要求：temperature 等于 30 时必须输出 hot。",
        "starter": "temperature = int(input())\n# 根据题目要求输出 hot 或 cool\n",
        "solution": "temperature = int(input())\nif temperature >= 30:\n    print('hot')\nelse:\n    print('cool')",
        "expected": "hot\n", "concepts": "if/elif/else",
        "hint": "先处理边界 30，再分别写出两个输出分支。",
    },
    {
        "code": "PY-BAS-004", "title": "计算 1 到 n 的总和",
        "description": "读取一个正整数 n，计算从 1 加到 n 的总和并输出结果。",
        "input_spec": "输入一行正整数 n，范围为 1 到 10000。",
        "output_spec": "输出一个整数，表示 1 + 2 + ... + n 的结果。",
        "constraints": "可能用到的工具：input()、int()、for 循环或数学公式。\n不限制实现方式，只要求结果正确。",
        "starter": "n = int(input())\n# 计算并输出 1 到 n 的总和\n",
        "solution": "n = int(input())\nprint(n * (n + 1) // 2)",
        "expected": "15\n", "concepts": "for循环,累加器",
        "hint": "可以使用累加器循环，也可以推导 1 到 n 的求和公式。",
    },
    {
        "code": "PY-BAS-005", "title": "计算列表平均值",
        "description": "读取一行空格分隔的整数，计算它们的平均值并输出，结果保留两位小数。",
        "input_spec": "输入一行 1 到 100 个整数，整数之间以一个或多个空格分隔。",
        "output_spec": "输出平均值，固定保留两位小数。例如输入 1 2 3 时输出 2.00。",
        "constraints": "可能用到的工具：input()、split()、map()、sum()、len()、格式化字符串。\n输入至少包含一个整数。",
        "starter": "values = input().split()\n# 将输入转换为数字，计算平均值并按两位小数输出\n",
        "solution": "numbers = list(map(int, input().split()))\nprint(f'{sum(numbers) / len(numbers):.2f}')",
        "expected": "2.00\n", "concepts": "列表,函数",
        "hint": "先切分输入并转换成整数列表，再用总和除以元素数量。",
    },
    {
        "code": "PY-BAS-006", "title": "实现安全除法函数", "type": "FUNCTION",
        "description": "定义函数 safe_divide(a, b)。当 b 不为 0 时返回 a 除以 b 的结果；当 b 为 0 时返回 None。",
        "input_spec": "本题不要求读取标准输入，评测程序会直接调用 safe_divide。",
        "output_spec": "函数返回值必须符合要求：safe_divide(6, 3) 返回 2.0，safe_divide(6, 0) 返回 None。",
        "constraints": "可能用到的工具：def、return、if。\n不要在函数内部打印结果，评测程序会检查返回值。",
        "starter": "def safe_divide(a, b):\n    # 处理除数为 0 和正常除法两种情况\n    pass\n",
        "solution": "def safe_divide(a, b):\n    if b == 0:\n        return None\n    return a / b",
        "expected": "", "concepts": "函数,异常处理",
        "hint": "先判断 b 是否为 0；特殊情况返回 None，其余情况再执行除法。",
    },
    {
        "code": "PY-BAS-007", "title": "统计一行文本中的单词",
        "description": "读取一行文本，统计其中由空白分隔的单词数量并输出。",
        "input_spec": "输入一行文本，单词之间可能有一个或多个空格。",
        "output_spec": "输出单词数量。例如输入 Python is fun 时输出 3。",
        "constraints": "可能用到的工具：input()、字符串 split()、len()。\n不需要区分大小写。",
        "starter": "text = input()\n# 统计文本中的单词数量并输出\n",
        "solution": "text = input()\nprint(len(text.split()))",
        "expected": "3\n", "concepts": "字符串,列表",
        "hint": "字符串的 split() 可以按连续空白切分出单词。",
    },
    {
        "code": "PY-BAS-008", "title": "筛选并输出偶数",
        "description": "读取一行整数，筛选其中的偶数，并按照原有顺序输出。",
        "input_spec": "输入一行空格分隔的整数，范围为 -100 到 100。",
        "output_spec": "输出所有偶数，数字之间用一个空格分隔；如果没有偶数，输出空行。",
        "constraints": "可能用到的工具：split()、int()、for 循环、取模运算 %、join()。\n只保留能被 2 整除的数字。",
        "starter": "numbers = input().split()\n# 筛选偶数并按一个空格连接后输出\n",
        "solution": "numbers = map(int, input().split())\nprint(' '.join(str(n) for n in numbers if n % 2 == 0))",
        "expected": "2 4\n", "concepts": "列表推导,条件",
        "hint": "对每个数字判断 n % 2 是否等于 0，最后将保留的数字转换为字符串。",
    },
]


def seed() -> None:
    Base.metadata.create_all(engine)
    db = SessionLocal()
    try:
        course = db.query(Course).filter_by(code="PY-FOUNDATION").first()
        if not course:
            course = Course(
                code="PY-FOUNDATION", name="Python 基础",
                description="从语法、控制流到函数与文件，建立可靠的 Python 基础。",
                level="beginner", sort_order=1,
            )
            db.add(course)
            db.flush()
        lesson = db.query(Lesson).filter_by(code="PY-BASICS-01").first()
        if not lesson:
            lesson = Lesson(
                course_id=course.id, code="PY-BASICS-01",
                name="第一阶段：写出第一个程序",
                description="变量、输入输出、条件与循环", sort_order=1,
            )
            db.add(lesson)
            db.flush()

        for order, item in enumerate(PROBLEMS, 1):
            cases = [("30", "hot\n"), ("29", "cool\n")] if order == 3 else [("5", "15\n"), ("1", "1\n")] if order == 4 else [("1 2 3 4", "2 4\n"), ("1 3 5", "\n")] if order == 8 else [("1 2 3", item["expected"]) ]
            if order == 1:
                cases = [("", item["expected"])]
            if order == 6:
                cases = [("print(repr(safe_divide(6, 3)))", "2.0\n"), ("print(repr(safe_divide(6, 0)))", "None\n")]
            _validate_reference(item["solution"], cases, item.get("type", "BASIC"))
            problem = db.query(Problem).filter_by(code=item["code"]).first()
            if not problem:
                problem = Problem(code=item["code"], lesson_id=lesson.id)
                db.add(problem)
            for key, value in {
                "title": item["title"], "difficulty": 1 if order < 4 else 2,
                "type": item.get("type", "BASIC"), "description": item["description"],
                "input_spec": item["input_spec"], "output_spec": item["output_spec"],
                "constraints": item["constraints"], "starter_code": item["starter"],
                "expected_concepts": item["concepts"], "hint_0": "先阅读输入、输出和边界要求，确认目标结果。",
                "hint_1": item["hint"], "hint_2": "把程序拆成输入、处理、输出三个步骤。",
                "hint_3": "先自己完成实现；参考答案会在通过测试后展示。",
                "solution_code": item["solution"], "sort_order": order, "is_active": True,
            }.items():
                setattr(problem, key, value)
            db.flush()
            db.query(TestCase).filter_by(problem_id=problem.id).delete()
            for sort_order, (input_data, expected) in enumerate(cases):
                db.add(TestCase(problem_id=problem.id, input_data=input_data, expected_stdout=expected, expected_exit_code=0, is_hidden=sort_order > 0, sort_order=sort_order))
            for concept in [x.strip() for x in item["concepts"].split(",") if x.strip()]:
                kp = db.query(KnowledgePoint).filter_by(code=concept).first()
                if not kp:
                    db.add(KnowledgePoint(code=concept, name=concept, category="基础", description=f"{item['title']}相关知识点"))
        db.commit()
        print("Seeded or updated", len(PROBLEMS), "problems")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
