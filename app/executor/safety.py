import ast

FORBIDDEN = {"os", "sys", "subprocess", "socket", "shutil", "pathlib", "ctypes", "multiprocessing"}


def validate_code(code: str) -> str | None:
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return f"SyntaxError: {e.msg} (line {e.lineno})"
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            if any(alias.name.split(".")[0] in FORBIDDEN for alias in node.names):
                return "安全检查拒绝：不允许导入系统/网络模块"
        if isinstance(node, ast.ImportFrom) and (node.module or "").split(".")[0] in FORBIDDEN:
            return "安全检查拒绝：不允许导入系统/网络模块"
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in {"eval", "exec", "compile", "__import__"}
        ):
            return "安全检查拒绝：不允许动态执行"
    return None
