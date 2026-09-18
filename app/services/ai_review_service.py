from typing import Protocol

import httpx

from app.config import get_settings


class AIProvider(Protocol):
    async def generate_hint(self, problem, code, level, judge_result): ...
    async def review_submission(self, problem, code, judge_result): ...


class MockAIProvider:
    async def generate_hint(self, problem, code, level, judge_result):
        hints = [problem.hint_0, problem.hint_1, problem.hint_2, problem.hint_3]
        hint = hints[min(level, 3)].strip() if hints else ""
        return {"level": level, "hint": hint or "检查失败测试与输入输出。"}

    async def review_submission(self, problem, code, judge_result):
        passed = judge_result.get("status") == "PASSED"
        return {
            "summary": "所有测试通过。" if passed else "仍有测试未通过，请根据失败用例继续调试。",
            "correctness": "pass" if passed else "partial",
            "issues": [],
            "knowledge_assessment": [
                {
                    "knowledge_point": problem.expected_concepts,
                    "level": "understood" if passed else "partial",
                }
            ],
            "next_action": "continue" if passed else "fix",
        }


class OpenAICompatibleProvider:
    def __init__(self):
        settings = get_settings()
        self.base_url = settings.ai_base_url.rstrip("/")
        self.api_key = settings.ai_api_key
        self.model = settings.ai_model
        self.timeout = settings.ai_timeout_seconds

    async def _chat(self, prompt: str) -> dict:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(
                f"{self.base_url}/chat/completions",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={
                    "model": self.model,
                    "temperature": 0.2,
                    "messages": [
                        {"role": "system", "content": "你是 Python 学习教练。只返回合法 JSON。"},
                        {"role": "user", "content": prompt},
                    ],
                },
            )
            response.raise_for_status()
            data = response.json()
            content = data["choices"][0]["message"]["content"]
            import json

            return json.loads(content)

    async def generate_hint(self, problem, code, level, judge_result):
        return await self._chat(
            (f"题目：{problem.description}\n代码：{code}\n"
             f"判题：{judge_result}\n只给 Hint-{level}，不要给超出该等级的答案。")
        )

    async def review_submission(self, problem, code, judge_result):
        return await self._chat(
            (f"题目：{problem.description}\n代码：{code}\n"
             f"实际判题结果：{judge_result}\n按结构化 Review JSON 返回。")
        )


def get_ai_provider():
    settings = get_settings()
    return (
        OpenAICompatibleProvider()
        if settings.ai_base_url and settings.ai_api_key and settings.ai_model
        else MockAIProvider()
    )
