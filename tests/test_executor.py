from app.executor.runner import run_python


def test_runner_success():
    r = run_python("print('ok')")
    assert r.status == "PASSED"
    assert r.stdout == "ok\n"


def test_runner_timeout():
    r = run_python("while True: pass")
    assert r.status == "TIMEOUT"


def test_runner_blocks_import():
    r = run_python("import os\nprint(1)")
    assert r.status == "JUDGE_ERROR"
