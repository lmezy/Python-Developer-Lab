from app.db.models import Problem
from app.executor.runner import run_python


def norm(value: str) -> str:
    # Ignore only the final line ending; spaces inside output remain significant.
    return value.replace("\r\n", "\n").rstrip("\n")


def judge(problem: Problem, code: str):
    tests = []
    passed = 0
    overall_ms = 0
    last_out = ""
    last_err = ""
    terminal_status = None
    for i, case in enumerate(sorted(problem.test_cases, key=lambda x: x.sort_order), 1):
        execution_code = code
        input_data = case.input_data
        if problem.type == "FUNCTION":
            execution_code = f"{code}\n{case.input_data}"
            input_data = ""
        result = run_python(execution_code, input_data)
        overall_ms += result.execution_ms
        last_out = result.stdout
        last_err = result.stderr
        ok = (
            result.status == "PASSED"
            and result.returncode == case.expected_exit_code
            and norm(result.stdout) == norm(case.expected_stdout)
        )
        if ok:
            passed += 1
        tests.append(
            {
                "name": f"case_{i}",
                "passed": ok,
                "hidden": case.is_hidden,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode,
                "execution_ms": result.execution_ms,
            }
        )
        if not ok and result.status != "PASSED":
            terminal_status = result.status
        if not ok and result.status != "PASSED":
            break
    total = len(problem.test_cases)
    status = "PASSED" if passed == total and total else (terminal_status or "FAILED")
    return {
        "status": status,
        "passed": passed,
        "total": total,
        "tests": tests,
        "stdout": last_out,
        "stderr": last_err,
        "execution_ms": overall_ms,
    }
