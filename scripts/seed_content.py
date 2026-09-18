from app.db.base import Base
from app.db.models import Course, KnowledgePoint, Lesson, Problem, TestCase
from app.db.session import SessionLocal, engine


def seed():
    Base.metadata.create_all(engine)
    db = SessionLocal()
    try:
        if db.query(Course).count():
            print("Seed already present")
            return
        course = Course(
            code="PY-FOUNDATION",
            name="Python 基础",
            description="从语法、控制流到函数与文件，建立可靠的 Python 基础。",
            level="beginner",
            sort_order=1,
        )
        db.add(course)
        db.flush()
        lesson = Lesson(
            course_id=course.id,
            code="PY-BASICS-01",
            name="第一阶段：写出第一个程序",
            description="变量、输入输出、条件与循环",
            sort_order=1,
        )
        db.add(lesson)
        db.flush()
        data = [
            (
                "PY-BAS-001",
                "你好，Python",
                "编写程序输出 Hello, Python!。",
                "print('Hello, Python!')",
                "Hello, Python!\n",
                "输出与 print",
                "先确认输出内容和标点。",
            ),
            (
                "PY-BAS-002",
                "认识变量",
                "创建变量 name 存储字符串 Python，并输出 Hello, Python。",
                "name = 'Python'\nprint('Hello, ' + name)",
                "Hello, Python",
                "变量,字符串",
                "先把数据存进变量，再使用变量。",
            ),
            (
                "PY-BAS-003",
                "判断温度",
                "读取一个整数温度：大于等于 30 输出 hot，否则输出 cool。",
                "temperature = int(input())\nif temperature >= 30:\n    print('hot')\nelse:\n    print('cool')",  # noqa: E501
                "hot\n",
                "if/elif/else",
                "把边界 30 单独想清楚。",
            ),
            (
                "PY-BAS-004",
                "累计求和",
                "读取一个整数 n，输出从 1 到 n 的和。",
                "n = int(input())\ntotal = 0\nfor i in range(1, n + 1):\n    total += i\nprint(total)",  # noqa: E501
                "15",
                "for循环,累加器",
                "循环需要一个保存结果的累加器。",
            ),
            (
                "PY-BAS-005",
                "列表平均值",
                "读取一行以空格分隔的整数，输出平均值，保留两位小数。",
                "numbers = list(map(int, input().split()))\nprint(f'{sum(numbers) / len(numbers):.2f}')",  # noqa: E501
                "2.00",
                "列表,函数",
                "先拆分输入，再转换为整数。",
            ),
            (
                "PY-BAS-006",
                "安全除法",
                "定义函数 safe_divide(a, b)。正常返回商，除数为 0 时返回 None。",
                "def safe_divide(a, b):\n    if b == 0:\n        return None\n    return a / b",
                "",
                "函数,异常处理",
                "先处理特殊情况，再计算普通情况。",
            ),
            (
                "PY-BAS-007",
                "统计单词",
                "读取一行文本，输出其中单词数量。",
                "text = input()\nprint(len(text.split()))",
                "3",
                "字符串,列表",
                "字符串的 split 方法可以按空白切分。",
            ),
            (
                "PY-BAS-008",
                "偶数过滤",
                "读取一行整数，输出所有偶数，使用空格分隔。",
                "numbers = map(int, input().split())\nprint(' '.join(str(n) for n in numbers if n % 2 == 0))",  # noqa: E501
                "2 4",
                "列表推导,条件",
                "逐个检查数字是否能被 2 整除。",
            ),
        ]
        for order, (code, title, desc, starter, expected, concept, hint) in enumerate(data, 1):
            p = Problem(
                code=code,
                title=title,
                lesson_id=lesson.id,
                difficulty=1 if order < 4 else 2,
                type="BASIC",
                description=desc,
                input_spec="按题目描述从标准输入读取。",
                output_spec="按题目描述输出。",
                starter_code=starter,
                expected_concepts=concept,
                hint_0="检查输出是否符合题目要求。",
                hint_1=hint,
                hint_2="拆成输入、处理、输出三个步骤。",
                hint_3=starter,
                solution_code=starter,
                sort_order=order,
            )
            db.add(p)
            db.flush()
            input_data = (
                ""
                if order == 1
                else (
                    "30"
                    if order == 3
                    else ("5" if order == 4 else ("1 2 3 4" if order == 8 else "1 2 3"))
                )
            )
            db.add(
                TestCase(
                    problem_id=p.id,
                    input_data=input_data,
                    expected_stdout=expected,
                    expected_exit_code=0,
                    is_hidden=False,
                    sort_order=0,
                )
            )
            db.add(
                TestCase(
                    problem_id=p.id,
                    input_data=input_data,
                    expected_stdout=expected,
                    expected_exit_code=0,
                    is_hidden=True,
                    sort_order=99,
                )
            )
            [
                db.add(
                    KnowledgePoint(
                        code=kp_code.strip(),
                        name=kp_code.strip(),
                        category="基础",
                        description=f"{title}相关知识点",
                    )
                )
                for kp_code in concept.split(",")
                if not db.query(KnowledgePoint).filter_by(code=kp_code.strip()).first()
            ]
        db.commit()
        print("Seeded", len(data), "problems")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
