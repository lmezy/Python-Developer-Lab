import subprocess
import sys
import tempfile
import time
from pathlib import Path

from app.config import get_settings
from app.executor.models import ExecutionResult
from app.executor.safety import validate_code


def _text(value: str | bytes | None) -> str:
    if value is None:
        return ""
    return value.decode(errors="replace") if isinstance(value, bytes) else value


def run_python(code: str, input_data: str = "") -> ExecutionResult:
    if err := validate_code(code):
        return ExecutionResult(
            "SYNTAX_ERROR" if err.startswith("SyntaxError") else "JUDGE_ERROR", stderr=err
        )
    settings = get_settings()
    started = time.perf_counter()
    with tempfile.TemporaryDirectory(prefix="pdl-") as work:
        path = Path(work) / "solution.py"
        path.write_text(code, encoding="utf-8")
        try:
            p = subprocess.run(
                [sys.executable, str(path)],
                input=input_data,
                text=True,
                capture_output=True,
                cwd=work,
                timeout=settings.execution_timeout_seconds,
                shell=False,
            )
            out = p.stdout[: settings.max_output_bytes]
            err = p.stderr[: settings.max_output_bytes]
            status = "PASSED" if p.returncode == 0 else "RUNTIME_ERROR"
            if (
                len(p.stdout) > settings.max_output_bytes
                or len(p.stderr) > settings.max_output_bytes
            ):
                status = "RUNTIME_ERROR"
                err += "\n输出超过限制"
            return ExecutionResult(
                status, out, err, p.returncode, int((time.perf_counter() - started) * 1000)
            )
        except subprocess.TimeoutExpired as e:
            return ExecutionResult(
                "TIMEOUT",
                _text(e.stdout)[: settings.max_output_bytes],
                "执行超时",
                None,
                int((time.perf_counter() - started) * 1000),
            )
        except OSError as e:
            return ExecutionResult("JUDGE_ERROR", stderr=str(e), returncode=None)
