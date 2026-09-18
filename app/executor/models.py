from dataclasses import dataclass


@dataclass
class ExecutionResult:
    status: str
    stdout: str = ""
    stderr: str = ""
    returncode: int | None = 0
    execution_ms: int = 0
