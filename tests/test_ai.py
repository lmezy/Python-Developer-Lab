import asyncio

from app.services.ai_review_service import MockAIProvider


def test_mock_hint_has_content():
    class Problem:
        hint_0 = "检查输出"
        hint_1 = "先看失败用例"
        hint_2 = "拆成三步"
        hint_3 = "参考片段"

    result = asyncio.run(MockAIProvider().generate_hint(Problem(), "print(1)", 1, {}))
    assert result["level"] == 1
    assert result["hint"] == "先看失败用例"
