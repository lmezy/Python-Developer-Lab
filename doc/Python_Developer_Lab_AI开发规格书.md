# Python Developer Lab
## Python 0 基础 → 生产级开发：AI 驱动学习与软件工程训练平台

> 文档用途：这是给“开发型 AI Agent”的主规格书。AI 读取本文件后，应能够直接创建仓库、设计数据库、实现第一版产品，并按题目编号持续生成课程、运行测试、校验代码、记录学习状态、推进项目版本。
>
> 目标不是制作一个普通 Python 刷题网站，而是制作一个“真实软件项目驱动的 Python 学习系统”：学习者通过完成题目逐步构建软件，同时学习 Python 语言、标准库、数据库、Web、测试、并发、工程化、Docker、CI/CD、监控与安全。

---

# 1. 项目总目标

## 1.1 产品目标

建立一个本地优先（Local-first）的学习开发平台，名称暂定：**Python Developer Lab**。

平台必须同时具备三条主线：

1. **课程线**：Python 0 基础 → 高级 Python → Web / 数据库 → 工程化 → 生产级开发。
2. **题目线**：每个知识点必须落到可执行题目上，题目可运行、可测试、可判定。
3. **项目线**：学习者完成的代码逐步合并到一个真实项目——**PyOps 运维/自动化助手**。

## 1.2 最终学习结果

学习者完成路线后应能够独立完成：

- Python 基础程序
- 多模块 Python 项目
- 配置、日志、异常处理
- OOP 与类型标注
- SQLite / PostgreSQL 数据库开发
- REST API
- FastAPI Web 后端
- HTML / Jinja2 基础前端
- 异步 / 并发 / 后台任务
- 自动化测试
- Git / 包管理 / lint / formatting
- Docker 容器化
- CI/CD
- 安全、审计、监控、性能优化
- 一个可部署、可维护、可扩展的完整软件

---

# 2. 核心原则

## 2.1 AI 的角色

AI 不是“代写程序的人”，而是：

- 教师
- 任务设计器
- 测试工程师
- Debug 助手
- Code Reviewer
- 项目 Tech Lead

默认禁止 AI 在学习者首次提交前直接给出完整答案。

## 2.2 学习闭环

```text
知识点
  ↓
题目
  ↓
学习者编写代码
  ↓
自动测试
  ↓
结果分析
  ↓
错误提示
  ↓
学习者修改
  ↓
再次测试
  ↓
AI Review
  ↓
通过
  ↓
合入项目
  ↓
下一题
```

## 2.3 提示等级

- Hint-0：只告诉错误类别，不给实现方式。
- Hint-1：给思考方向。
- Hint-2：给伪代码 / API 名称。
- Hint-3：给关键代码片段。
- Hint-4：给完整参考答案。

默认只有在学习者主动请求或多次失败后才逐级开放。

## 2.4 通过条件

题目不能仅依赖 AI 判断“像不像正确答案”。必须优先采用：

1. 自动测试
2. 边界测试
3. 异常测试
4. 静态代码检查
5. AI Review

其中 1~3 是功能正确性的主要依据。

---

# 3. 技术选型

## 3.1 V1 必选技术

| 层 | 技术 |
|---|---|
| Python | Python 3.13+ |
| 后端 | FastAPI |
| ASGI | Uvicorn |
| 模板 | Jinja2 |
| 前端 | HTML + CSS + 原生 JavaScript |
| 数据库 | SQLite |
| ORM | SQLAlchemy 2.x |
| 数据校验 | Pydantic 2.x |
| 测试 | pytest |
| HTTP 测试 | httpx |
| 包管理 | uv 或 pip + pyproject.toml，V1 统一使用 uv 优先 |
| 格式化 | Ruff formatter |
| Lint | Ruff |
| 类型检查 | mypy 或 pyright，V1 默认 pyright |
| 配置 | pydantic-settings |
| 日志 | Python logging，结构化 JSON 日志可作为扩展 |
| Git | Git |
| AI | OpenAI-compatible API，可配置 Base URL / API Key / Model |

## 3.2 V1 暂不引入

- React / Vue
- Redis
- Celery
- Kubernetes
- 微服务
- Elasticsearch
- PostgreSQL
- 第三方在线代码沙箱

这些内容进入后续版本或高级课程。

## 3.3 生产升级路线

```text
V1 SQLite
 → V2 PostgreSQL
 → V2 Redis
 → V2 Docker Executor
 → V2 Background Worker
 → V3 CI/CD
 → V3 Observability
```

---

# 4. 软件版本规划

```text
v0.1 题库 + 用户本地学习记录 + 代码执行 + 自动判题
v0.2 课程 / 知识图谱 / 错题本 / 提示系统
v0.3 项目任务与 Git 集成
v0.4 AI Review / AI 题目生成
v0.5 FastAPI + 数据库项目实训
v0.6 Web UI 完整化
v0.7 Docker Executor + 后台任务
v0.8 测试 / CI / 日志 / 权限 / 审计
v0.9 性能、安全、监控
v1.0 生产级部署版本
```

本规格书要求 **V1 只实现 v0.1**，但代码结构必须为后续版本预留扩展点。

---

# 5. V1 产品边界

## 5.1 V1 必须实现

### 学习

- 课程列表
- 阶段列表
- 知识点列表
- 题目列表
- 题目详情
- 题目依赖关系
- 当前学习进度

### 编程

- 浏览器提交 Python 代码
- 本地 Python 解释器执行
- 测试用例执行
- stdout / stderr 捕获
- exit code 捕获
- 超时控制
- 测试结果展示

### 判题

- 基础输出测试
- 多输入测试
- 边界测试
- 异常测试
- 测试汇总
- 通过 / 失败

### 学习记录

- 尝试次数
- 最后一次提交
- 通过时间
- 当前提示等级
- 是否看过答案
- 知识点掌握状态

### AI

- 读取题目
- 读取学习者代码
- 读取测试结果
- 分析错误
- 输出 Hint
- 输出 Code Review

## 5.2 V1 明确不做

- 多用户在线注册
- 公网部署
- 在线多人协作
- 任意代码远程执行
- 积分商城
- 社交系统
- 广告

---

# 6. 安全要求：代码执行器

这是 V1 最大的安全风险点。

## 6.1 默认运行范围

- 仅允许 `127.0.0.1` 访问。
- 不允许默认监听 `0.0.0.0`。
- 不允许直接向公网提供代码执行接口。

## 6.2 Python 执行

后端不得使用：

```python
subprocess.run(user_code, shell=True)
```

必须：

- 将代码写入临时目录
- 使用 `sys.executable` 调用 Python
- 参数数组形式，不使用 `shell=True`
- 设置 timeout
- 独立工作目录
- 限制输出长度
- 超时后杀掉进程树
- 清理临时文件

## 6.3 强化隔离为后续版本

真正部署到 NAS / LAN 前必须增加 Docker Executor：

- `--network none`
- CPU 限制
- 内存限制
- PID 限制
- 临时文件系统
- 非 root 用户
- 超时
- 工作目录只读挂载公共测试资源

---

# 7. 第一版项目目录

```text
python-developer-lab/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── logging_config.py
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── models.py
│   ├── api/
│   │   ├── routes_health.py
│   │   ├── routes_courses.py
│   │   ├── routes_problems.py
│   │   ├── routes_submissions.py
│   │   ├── routes_progress.py
│   │   └── routes_ai.py
│   ├── schemas/
│   │   ├── course.py
│   │   ├── problem.py
│   │   ├── submission.py
│   │   └── progress.py
│   ├── services/
│   │   ├── course_service.py
│   │   ├── problem_service.py
│   │   ├── submission_service.py
│   │   ├── judge_service.py
│   │   ├── hint_service.py
│   │   └── ai_review_service.py
│   ├── executor/
│   │   ├── models.py
│   │   ├── runner.py
│   │   └── safety.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── course.html
│   │   ├── problem.html
│   │   └── submission.html
│   └── static/
│       ├── css/
│       └── js/
├── content/
│   ├── courses/
│   ├── knowledge/
│   └── problems/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── scripts/
│   ├── seed_content.py
│   ├── run_local.py
│   └── export_progress.py
├── data/
│   └── app.db
├── docs/
├── pyproject.toml
├── README.md
└── .env.example
```

---

# 8. 核心数据模型

## 8.1 course

字段：

```text
id
code
name
description
level
sort_order
is_active
created_at
updated_at
```

## 8.2 lesson

```text
id
course_id
code
name
description
sort_order
estimated_minutes
```

## 8.3 knowledge_point

```text
id
code
name
category
description
prerequisite_ids
```

## 8.4 problem

```text
id
code
title
lesson_id
difficulty
type
description
input_spec
output_spec
constraints
starter_code
expected_concepts
hint_0
hint_1
hint_2
hint_3
solution_code
sort_order
is_active
```

## 8.5 test_case

```text
id
problem_id
input_data
expected_stdout
expected_exit_code
is_hidden
sort_order
```

## 8.6 submission

```text
id
problem_id
code
status
passed_count
total_count
stdout
stderr
execution_ms
hint_level
used_solution
created_at
```

## 8.7 knowledge_progress

```text
id
knowledge_point_id
status
attempt_count
pass_count
last_attempt_at
mastered_at
```

状态：

```text
unseen
learning
practiced
mastered
```

---

# 9. V1 API

## Health

```http
GET /api/health
```

返回：

```json
{"status":"ok"}
```

## 课程

```http
GET /api/courses
GET /api/courses/{course_id}
```

## 题目

```http
GET /api/problems
GET /api/problems/{problem_id}
```

## 提交

```http
POST /api/submissions
```

请求示例：

```json
{
  "problem_id": 1,
  "code": "print('hello')"
}
```

## 查询提交

```http
GET /api/submissions/{submission_id}
```

## 进度

```http
GET /api/progress
```

## AI Hint

```http
POST /api/ai/hint
```

## AI Review

```http
POST /api/ai/review
```

---

# 10. 判题引擎设计

## 10.1 输入

```text
problem
submission_code
visible_test_cases
hidden_test_cases
```

## 10.2 执行流程

```text
收到代码
 ↓
静态检查
 ↓
建立 temp workspace
 ↓
写 solution.py
 ↓
逐个执行测试
 ↓
捕获 stdout/stderr/returncode/time
 ↓
规范化输出
 ↓
断言 expected
 ↓
生成 JudgeResult
 ↓
保存 submission
```

## 10.3 判题结果

```json
{
  "status": "passed",
  "passed": 3,
  "total": 3,
  "tests": [
    {
      "name": "case_1",
      "passed": true,
      "execution_ms": 12
    }
  ]
}
```

状态：

```text
PASSED
FAILED
TIMEOUT
RUNTIME_ERROR
SYNTAX_ERROR
JUDGE_ERROR
```

---

# 11. 评分与掌握模型

V1 不使用复杂积分体系，避免学习者追求刷分。

每题记录：

```text
功能通过：        必须
边界通过：        必须
异常处理：        按题目要求
静态检查：        推荐
AI Review：       解释性反馈
```

知识点掌握规则：

```text
首次通过       practiced
连续 2 次独立通过 masterable
在复习题再次通过 mastered
```

若使用 Hint-3 或查看答案，不计作“独立通过”。

---

# 12. 题目编号体系

格式：

```text
PY-{阶段}-{三位序号}
```

例如：

```text
PY-ENV-001
PY-BAS-001
PY-CTL-001
PY-DAT-001
PY-FUN-001
PY-FIL-001
PY-OOP-001
PY-TST-001
PY-DB-001
PY-API-001
PY-WEB-001
PY-ASY-001
PY-ENG-001
PY-OPS-001
PY-CAP-001
```

阶段代码：

| Code | 阶段 |
|---|---|
| ENV | 环境与开发工具 |
| BAS | 基础语法 |
| CTL | 条件与循环 |
| DAT | 数据结构 |
| FUN | 函数与模块 |
| FIL | 文件、异常、标准库 |
| OOP | 面向对象与类型系统 |
| TST | 测试与调试 |
| DB | 数据库 |
| API | HTTP / FastAPI |
| WEB | Web 前端 |
| ASY | 异步、并发、任务 |
| ENG | 工程化 |
| OPS | 生产运维 |
| CAP | 综合项目 |

---

# 13. 单题统一格式

AI 创建新题目时，必须输出以下字段：

```yaml
code: PY-BAS-001
title: 打印软件欢迎信息
stage: BAS
lesson: BAS-01
difficulty: 1
knowledge_points:
  - print
  - string
prerequisites: []
objective: 学会使用 print 输出固定文本
task: |
  编写程序输出指定内容。
input_spec: 无
output_spec: 两行固定文本
constraints:
  - 不使用第三方库
starter_code: ""
tests:
  visible: []
  hidden: []
hints:
  hint_0: ...
  hint_1: ...
  hint_2: ...
  hint_3: ...
solution: ...
acceptance:
  functional: ...
  edge_cases: ...
  static_checks: ...
```

---

# 14. 全路线知识点树

```text
Python Developer Lab
│
├─ 00 环境
│  ├─ Python 安装
│  ├─ REPL
│  ├─ 脚本运行
│  ├─ venv / uv
│  ├─ pip
│  ├─ IDE / VS Code
│  └─ Git 基础
│
├─ 01 基础语法
│  ├─ print / input
│  ├─ 变量
│  ├─ int / float / str / bool / None
│  ├─ 类型转换
│  ├─ 运算符
│  └─ f-string
│
├─ 02 控制流
│  ├─ if / elif / else
│  ├─ for
│  ├─ while
│  ├─ range
│  ├─ break / continue
│  └─ 条件表达式
│
├─ 03 数据结构
│  ├─ list
│  ├─ tuple
│  ├─ dict
│  ├─ set
│  ├─ slicing
│  ├─ unpacking
│  └─ comprehensions
│
├─ 04 函数与模块
│  ├─ def
│  ├─ return
│  ├─ 参数
│  ├─ 默认参数
│  ├─ *args / **kwargs
│  ├─ lambda
│  ├─ import
│  ├─ package
│  └─ __name__
│
├─ 05 文件与标准库
│  ├─ pathlib
│  ├─ open / with
│  ├─ JSON
│  ├─ CSV
│  ├─ datetime
│  ├─ re
│  ├─ os / sys
│  └─ shutil / subprocess
│
├─ 06 异常与健壮性
│  ├─ try / except
│  ├─ else / finally
│  ├─ raise
│  ├─ 自定义异常
│  └─ 输入校验
│
├─ 07 OOP
│  ├─ class / object
│  ├─ __init__
│  ├─ 属性 / 方法
│  ├─ classmethod / staticmethod
│  ├─ inheritance
│  ├─ composition
│  ├─ dataclass
│  ├─ property
│  ├─ protocol
│  └─ dependency injection
│
├─ 08 类型与现代 Python
│  ├─ type hints
│  ├─ Optional / Union
│  ├─ Generic
│  ├─ TypedDict
│  ├─ Literal
│  └─ typing
│
├─ 09 测试与调试
│  ├─ pytest
│  ├─ fixtures
│  ├─ parametrization
│  ├─ mock
│  ├─ coverage
│  ├─ logging
│  └─ debugger
│
├─ 10 数据库
│  ├─ SQL
│  ├─ CRUD
│  ├─ schema
│  ├─ transaction
│  ├─ index
│  ├─ SQLite
│  ├─ SQLAlchemy
│  └─ PostgreSQL
│
├─ 11 HTTP / API
│  ├─ HTTP
│  ├─ request / response
│  ├─ JSON
│  ├─ status code
│  ├─ headers
│  ├─ auth
│  ├─ REST
│  └─ FastAPI
│
├─ 12 Web
│  ├─ HTML
│  ├─ CSS
│  ├─ JavaScript 基础
│  ├─ fetch
│  ├─ Jinja2
│  ├─ forms
│  └─ 前后端交互
│
├─ 13 异步与并发
│  ├─ async / await
│  ├─ asyncio
│  ├─ Task
│  ├─ semaphore
│  ├─ thread
│  ├─ process
│  ├─ queue
│  └─ background worker
│
├─ 14 工程化
│  ├─ pyproject.toml
│  ├─ uv
│  ├─ dependency management
│  ├─ lint / format
│  ├─ typing
│  ├─ env config
│  ├─ semantic versioning
│  ├─ Git
│  ├─ branching
│  └─ code review
│
├─ 15 生产级
│  ├─ Docker
│  ├─ reverse proxy
│  ├─ secrets
│  ├─ permissions
│  ├─ auditing
│  ├─ rate limiting
│  ├─ caching
│  ├─ metrics
│  ├─ tracing
│  ├─ alerting
│  ├─ backup / restore
│  ├─ deployment
│  └─ rollback
│
└─ 16 综合项目 PyOps
   ├─ system inventory
   ├─ network check
   ├─ file analysis
   ├─ log analysis
   ├─ scheduled tasks
   ├─ reports
   ├─ REST API
   ├─ Web UI
   ├─ user / role
   ├─ audit
   └─ Docker production deployment
```

---

# 15. 完整题目路线与验收标准

以下题目是“主线题”。AI 可在两题之间增加补充题，但不能跳过主线题。

## ENV：环境与工具

| 编号 | 题目 | 核心知识 | 验收标准 |
|---|---|---|---|
| PY-ENV-001 | 安装并运行 Python | Python / CLI | `python --version` 成功；脚本可运行 |
| PY-ENV-002 | REPL 计算器 | REPL / expression | 能在 REPL 完成基本计算 |
| PY-ENV-003 | 创建第一个脚本 | `.py` | `main.py` 可从命令行执行 |
| PY-ENV-004 | 创建虚拟环境 | venv / uv | 新环境可激活且解释器路径正确 |
| PY-ENV-005 | 安装并冻结依赖 | pip / uv | 依赖可安装；项目可在新环境运行 |
| PY-ENV-006 | 初始化 Git | Git | Git 仓库建立；首次 commit 成功 |
| PY-ENV-007 | 创建 pyproject.toml | packaging | 项目能通过标准方式运行 |
| PY-ENV-008 | 编写 README | 文档 | README 含安装、运行、测试方法 |

## BAS：基础语法

| 编号 | 题目 | 核心知识 | 验收标准 |
|---|---|---|---|
| PY-BAS-001 | 欢迎信息 | print / str | 输出完全匹配要求 |
| PY-BAS-002 | 用户问候 | input / variable | 输入姓名后输出正确问候 |
| PY-BAS-003 | 服务器信息 | f-string | 名称、IP 拼接结果准确 |
| PY-BAS-004 | 温度换算 | arithmetic | 转换公式和结果正确 |
| PY-BAS-005 | 磁盘容量换算 | float / arithmetic | 单位转换正确，保留指定精度 |
| PY-BAS-006 | 布尔状态 | bool | 正确产生 True / False |
| PY-BAS-007 | 类型识别 | type / isinstance | 正确识别指定类型 |
| PY-BAS-008 | 字符串清洗 | strip / lower | 前后空白及大小写按要求处理 |
| PY-BAS-009 | IP 字符串拆分 | split | 每个字段提取正确 |
| PY-BAS-010 | 数值类型转换 | int / float | 合法输入转换成功 |
| PY-BAS-011 | 基本运算器 | operators | + - * / // % ** 结果正确 |
| PY-BAS-012 | 百分比计算 | arithmetic | 百分比结果正确 |
| PY-BAS-013 | 时间换算 | divmod | 小时、分钟、秒拆分正确 |
| PY-BAS-014 | 格式化状态 | f-string | 输出格式精确 |
| PY-BAS-015 | 第一版 PyOps 菜单 | print / input | 菜单可显示；选择后进入对应分支 |

## CTL：条件与循环

| 编号 | 题目 | 核心知识 | 验收标准 |
|---|---|---|---|
| PY-CTL-001 | CPU 状态判断 | if | 60 以下 NORMAL；边界正确 |
| PY-CTL-002 | CPU 三档告警 | if / elif / else | 60/80 边界全部正确 |
| PY-CTL-003 | 磁盘空间告警 | comparison | 多阈值正确 |
| PY-CTL-004 | 登录结果判断 | bool / if | 成功、失败路径正确 |
| PY-CTL-005 | 多条件健康检查 | and / or | 所有组合符合规格 |
| PY-CTL-006 | 判断工作日 | 条件表达式 | 周末与工作日正确 |
| PY-CTL-007 | 1~100 求和 | for / range | 与数学结果一致 |
| PY-CTL-008 | 批量打印服务器 | for | 每台服务器均处理且顺序正确 |
| PY-CTL-009 | 统计在线数量 | for / counter | 数量正确 |
| PY-CTL-010 | 查找异常服务器 | for / break | 找到首个异常即停止 |
| PY-CTL-011 | 跳过维护节点 | continue | 指定节点被跳过 |
| PY-CTL-012 | 菜单循环 | while | 用户选择退出后才结束 |
| PY-CTL-013 | 输入重试 | while | 非法输入会重试，合法输入结束 |
| PY-CTL-014 | 批量健康检查 | nested loop | 所有主机和检查项均执行 |
| PY-CTL-015 | PyOps CLI v0.1 | control flow | 四项核心功能均可执行且能退出 |

## DAT：数据结构

| 编号 | 题目 | 核心知识 | 验收标准 |
|---|---|---|---|
| PY-DAT-001 | 服务器列表 | list | 可增加、删除、遍历服务器 |
| PY-DAT-002 | 服务器元组 | tuple | 只读配置不能被意外修改 |
| PY-DAT-003 | 服务器字典 | dict | 通过 key 正确读取字段 |
| PY-DAT-004 | 服务器集合 | set | 重复 IP 被去重 |
| PY-DAT-005 | 列表切片 | slicing | 指定区间与步长正确 |
| PY-DAT-006 | 解包配置 | unpacking | 多变量正确接收序列值 |
| PY-DAT-007 | 字典遍历 | items / keys / values | 输出与数据一致 |
| PY-DAT-008 | 嵌套服务器数据 | nested dict | 指定嵌套字段可准确访问 |
| PY-DAT-009 | 过滤异常主机 | list comprehension | 结果仅包含目标主机 |
| PY-DAT-010 | 生成 IP 集合 | set comprehension | 无重复结果 |
| PY-DAT-011 | 统计状态 | dict aggregation | online/offline 数量准确 |
| PY-DAT-012 | 排序服务器 | sorted / key | 按指定字段排序且稳定 |
| PY-DAT-013 | 分组服务器 | dict of lists | 同类主机正确归类 |
| PY-DAT-014 | 清洗设备数据 | comprehensions | 无效数据按规则过滤 |
| PY-DAT-015 | PyOps 数据模型 v0.2 | list/dict | 菜单功能改为基于结构化数据运行 |

## FUN：函数与模块

| 编号 | 题目 | 核心知识 | 验收标准 |
|---|---|---|---|
| PY-FUN-001 | 第一个函数 | def | 函数可调用并返回正确结果 |
| PY-FUN-002 | CPU 判断函数 | parameter / return | 输入和输出清晰、无全局状态依赖 |
| PY-FUN-003 | 两参数函数 | multiple args | 结果正确 |
| PY-FUN-004 | 默认参数 | default arg | 不传参数时行为正确 |
| PY-FUN-005 | 关键字参数 | keyword args | 调用顺序变化不影响结果 |
| PY-FUN-006 | 可变参数 | *args | 任意数量输入均可处理 |
| PY-FUN-007 | **kwargs 配置 | **kwargs | 任意配置字段可接收 |
| PY-FUN-008 | 返回多个值 | tuple return | 调用方能正确解包 |
| PY-FUN-009 | 函数组合 | composition | 小函数组合得到正确结果 |
| PY-FUN-010 | Lambda 排序 | lambda | 按自定义字段排序 |
| PY-FUN-011 | 工具模块 | import | utils 模块可复用 |
| PY-FUN-012 | 包结构 | package | 多模块项目可正常导入 |
| PY-FUN-013 | `__main__` | module entry | `python -m` 可运行 |
| PY-FUN-014 | CLI 服务化重构 | modularization | main.py 不再承载全部业务逻辑 |
| PY-FUN-015 | PyOps v0.3 | functions/modules | 每个菜单功能均由独立函数/模块实现 |

## FIL：文件、标准库与异常

| 编号 | 题目 | 核心知识 | 验收标准 |
|---|---|---|---|
| PY-FIL-001 | 读取文本 | open / read | 文件内容读取正确 |
| PY-FIL-002 | 写日志文件 | write | 文件创建成功且内容准确 |
| PY-FIL-003 | `with open` | context manager | 文件始终正确关闭 |
| PY-FIL-004 | pathlib 路径 | pathlib | 相对/绝对路径处理正确 |
| PY-FIL-005 | 遍历目录 | Path.iterdir | 文件和目录分类准确 |
| PY-FIL-006 | JSON 写入 | json.dump | JSON 有效且结构正确 |
| PY-FIL-007 | JSON 读取 | json.load | 配置恢复一致 |
| PY-FIL-008 | CSV 导出 | csv | 行列数据准确 |
| PY-FIL-009 | 日期时间 | datetime | 时间格式转换正确 |
| PY-FIL-010 | 日志提取 | re | 指定模式全部找到 |
| PY-FIL-011 | 文件复制 | shutil | 源文件不被破坏；目标正确 |
| PY-FIL-012 | 命令执行 | subprocess | 命令参数数组调用；退出码被正确处理 |
| PY-FIL-013 | 捕获异常 | try/except | 指定异常被捕获；其他异常不被吞掉 |
| PY-FIL-014 | 自定义异常 | raise / class | 错误类型可被调用方区分 |
| PY-FIL-015 | 输入校验器 | validation | 非法输入返回明确错误 |
| PY-FIL-016 | PyOps 配置文件 | pathlib + JSON | 程序首次运行生成默认配置并能重新加载 |
| PY-FIL-017 | PyOps 日志系统 | logging | INFO/WARNING/ERROR 均有标准格式 |
| PY-FIL-018 | PyOps v0.4 | files/exceptions | 文件不存在、JSON 损坏、权限错误均不会导致无提示崩溃 |

## OOP：面向对象与现代 Python

| 编号 | 题目 | 核心知识 | 验收标准 |
|---|---|---|---|
| PY-OOP-001 | Server 类 | class / __init__ | 对象可创建并保存属性 |
| PY-OOP-002 | Server 方法 | method | 方法返回正确状态 |
| PY-OOP-003 | 属性校验 | property | 非法值无法通过公开接口写入 |
| PY-OOP-004 | dataclass | dataclass | 数据模型字段明确且可实例化 |
| PY-OOP-005 | CheckResult 类 | object composition | 检查结果可独立表达 |
| PY-OOP-006 | HealthChecker | composition | Checker 使用 Server 和 Result 完成一次检查 |
| PY-OOP-007 | 继承 | inheritance | 子类继承公共行为且能扩展 |
| PY-OOP-008 | 抽象接口 | ABC / protocol | 新检查器遵守统一接口 |
| PY-OOP-009 | 多态检查器 | polymorphism | CPU/Disk/Network checker 可统一调用 |
| PY-OOP-010 | 依赖注入 | DI | 检查器依赖由外部提供，便于测试 |
| PY-OOP-011 | 类型标注 | typing | 公共函数全部有参数与返回值类型 |
| PY-OOP-012 | TypedDict / Literal | typing | 配置字段和值类型约束明确 |
| PY-OOP-013 | 泛型容器 | Generic | 通用 Result 容器可复用 |
| PY-OOP-014 | OOP 重构 | design | PyOps 核心业务从脚本式代码重构为可测试对象 |
| PY-OOP-015 | 插件式检查器 | registry | 新增 Checker 不需修改核心执行流程 |
| PY-OOP-016 | PyOps v0.5 | OOP/type system | 至少 3 种检查器均可通过统一接口运行 |

## TST：测试、调试与质量

| 编号 | 题目 | 核心知识 | 验收标准 |
|---|---|---|---|
| PY-TST-001 | 第一个 pytest | pytest | 测试通过 |
| PY-TST-002 | CPU 判定测试 | unit test | 正常值和边界值均通过 |
| PY-TST-003 | 参数化测试 | parametrize | 同一逻辑覆盖多输入 |
| PY-TST-004 | 异常测试 | pytest.raises | 指定异常正确抛出 |
| PY-TST-005 | fixture | fixture | 测试数据可复用 |
| PY-TST-006 | monkeypatch | patch | 外部依赖可隔离 |
| PY-TST-007 | mock | unittest.mock | 调用次数/参数可验证 |
| PY-TST-008 | 文件系统测试 | tmp_path | 测试不会污染真实数据 |
| PY-TST-009 | HTTP 客户端测试基础 | httpx | 请求可被测试并断言 |
| PY-TST-010 | 代码覆盖率 | coverage | 能生成覆盖率报告 |
| PY-TST-011 | Ruff 检查 | lint | 项目无阻断级 lint 错误 |
| PY-TST-012 | Ruff format | formatting | 格式化后 Git diff 可控 |
| PY-TST-013 | 类型检查 | pyright | 核心模块无 error |
| PY-TST-014 | Bug 修复任务 | debugging | 给定故障测试恢复绿色 |
| PY-TST-015 | PyOps 测试套件 | test architecture | 核心业务覆盖关键分支和异常路径 |
| PY-TST-016 | CI 本地门禁 | quality gate | test + lint + typecheck 全部成功才视为可合并 |

## DB：数据库

| 编号 | 题目 | 核心知识 | 验收标准 |
|---|---|---|---|
| PY-DB-001 | 数据库连接 | SQLite | 数据库可连接、可创建 |
| PY-DB-002 | 建表 | SQL DDL | 表结构按规格创建 |
| PY-DB-003 | INSERT | CRUD | 数据正确写入 |
| PY-DB-004 | SELECT | query | 条件查询结果正确 |
| PY-DB-005 | UPDATE | CRUD | 更新仅影响目标行 |
| PY-DB-006 | DELETE | CRUD | 删除仅影响目标行 |
| PY-DB-007 | 主键与唯一约束 | constraints | 重复数据被拒绝 |
| PY-DB-008 | Index | index | 指定查询字段存在索引 |
| PY-DB-009 | Transaction | transaction | 失败时能 rollback |
| PY-DB-010 | SQLAlchemy model | ORM | Python 对象可映射到表 |
| PY-DB-011 | Session 管理 | SQLAlchemy | request 生命周期内 session 正确释放 |
| PY-DB-012 | Repository | repository pattern | 业务层不直接散落 SQL |
| PY-DB-013 | Migration 基础 | Alembic | schema 变更可追踪 |
| PY-DB-014 | PyOps server 持久化 | ORM | server 增删改查全部持久化 |
| PY-DB-015 | submission 持久化 | ORM | 每次提交都有历史记录 |
| PY-DB-016 | progress 持久化 | DB | 通过题目后进度准确更新 |
| PY-DB-017 | 数据库异常处理 | integrity | 约束冲突向 API 转换为明确错误 |
| PY-DB-018 | PostgreSQL 迁移演练 | PostgreSQL | 核心查询无需大规模改写即可迁移 |

## API：HTTP 与 FastAPI

| 编号 | 题目 | 核心知识 | 验收标准 |
|---|---|---|---|
| PY-API-001 | HTTP 基础 | method/status | 能解释并处理 GET/POST/PUT/DELETE |
| PY-API-002 | 第一个 FastAPI | route | `/api/health` 返回 200 |
| PY-API-003 | Query 参数 | query | 缺省值和非法值有明确行为 |
| PY-API-004 | Path 参数 | path | 指定资源可准确读取 |
| PY-API-005 | Pydantic 请求模型 | schema | 非法请求被 422 或明确错误拒绝 |
| PY-API-006 | Response model | Pydantic | 返回结构稳定 |
| PY-API-007 | 状态码 | HTTP status | 创建/删除/错误均使用合理状态码 |
| PY-API-008 | CRUD API | REST | Server CRUD 完整可用 |
| PY-API-009 | 分页 | pagination | page/limit 结果正确且有边界限制 |
| PY-API-010 | 错误处理 | exception handler | 统一 JSON 错误结构 |
| PY-API-011 | 依赖注入 | Depends | DB session / service 正确注入 |
| PY-API-012 | API 测试 | TestClient/httpx | 核心 endpoint 自动化覆盖 |
| PY-API-013 | OpenAPI | docs | `/docs` 可用且 schema 完整 |
| PY-API-014 | PyOps API v1 | FastAPI | server/check/report/submission API 可调用 |
| PY-API-015 | AI API | external API | API Key、Base URL、Model 均由配置驱动 |
| PY-API-016 | API 超时与重试 | httpx | AI 服务异常不会阻塞请求无限等待 |
| PY-API-017 | API 安全基础 | validation | 任意用户输入都经过 schema 校验 |

## WEB：Web UI

| 编号 | 题目 | 核心知识 | 验收标准 |
|---|---|---|---|
| PY-WEB-001 | HTML 页面 | HTML | 页面可在浏览器显示 |
| PY-WEB-002 | CSS 基础 | CSS | 布局和可读性达到规格 |
| PY-WEB-003 | Jinja2 模板 | template | 后端变量成功渲染 |
| PY-WEB-004 | 课程列表页 | GET + template | 全部课程可显示 |
| PY-WEB-005 | 题目详情页 | template | 题干、约束、提示正确展示 |
| PY-WEB-006 | 代码编辑区 | textarea/editor | 可编辑并提交代码 |
| PY-WEB-007 | 提交结果页 | form/result | 测试结果逐项展示 |
| PY-WEB-008 | fetch API | JS | 无刷新提交可工作 |
| PY-WEB-009 | 进度页 | API + UI | 已完成/未完成可区分 |
| PY-WEB-010 | Hint 面板 | UI state | 提示按等级逐步显示 |
| PY-WEB-011 | 错误详情 | UI | stdout/stderr/失败测试明确显示 |
| PY-WEB-012 | PyOps Dashboard | dashboard | 服务器、检查、最近提交均可查看 |

## ASY：异步、并发与任务

| 编号 | 题目 | 核心知识 | 验收标准 |
|---|---|---|---|
| PY-ASY-001 | async 基础 | async/await | 异步函数可正确执行 |
| PY-ASY-002 | asyncio.gather | concurrency | 多任务并发执行且结果完整 |
| PY-ASY-003 | timeout | asyncio | 超时任务被取消且有明确状态 |
| PY-ASY-004 | semaphore | concurrency limit | 并发数不超过指定上限 |
| PY-ASY-005 | async HTTP | httpx.AsyncClient | 多主机请求可并发 |
| PY-ASY-006 | thread pool | ThreadPoolExecutor | 阻塞任务不会卡死主线程 |
| PY-ASY-007 | process pool | ProcessPoolExecutor | CPU 密集计算可并行 |
| PY-ASY-008 | queue | producer/consumer | 任务可靠进出队列 |
| PY-ASY-009 | background task | FastAPI | 长任务返回后可继续执行 |
| PY-ASY-010 | 任务状态机 | job state | pending/running/success/failed/cancelled 正确切换 |
| PY-ASY-011 | PyOps 批量扫描 | concurrency | 100 台模拟服务器可并发扫描且有上限 |
| PY-ASY-012 | 定时任务 | scheduler concept | 指定任务按时间执行且结果持久化 |

## ENG：工程化

| 编号 | 题目 | 核心知识 | 验收标准 |
|---|---|---|---|
| PY-ENG-001 | 项目配置分离 | settings | dev/test/prod 配置不混写 |
| PY-ENG-002 | 环境变量 | env | Secret 不进入 Git |
| PY-ENG-003 | 统一日志 | logging | 服务日志包含 level/time/logger/message |
| PY-ENG-004 | 结构化错误 | error model | API/CLI 使用统一错误模型 |
| PY-ENG-005 | 服务层拆分 | architecture | route 不直接承载核心业务 |
| PY-ENG-006 | Repository + Service | layering | DB 访问与业务逻辑解耦 |
| PY-ENG-007 | Dependency Injection | DI | 外部依赖可替换 |
| PY-ENG-008 | 配置校验 | Pydantic settings | 缺少必要配置时启动失败并给出原因 |
| PY-ENG-009 | Git 分支 | git flow basics | feature 分支可合并且历史清晰 |
| PY-ENG-010 | Commit 规范 | commit | commit message 清晰表达变更 |
| PY-ENG-011 | Changelog | release | 版本变更有记录 |
| PY-ENG-012 | Semantic Versioning | versioning | 版本号遵循 MAJOR.MINOR.PATCH |
| PY-ENG-013 | Architecture test | dependency rule | 高层模块不会反向依赖低层实现细节 |
| PY-ENG-014 | 配置与 Secret 审计 | security | 仓库扫描无硬编码 Key |
| PY-ENG-015 | PyOps v0.9 | engineering | 核心结构达到可维护项目标准 |

## OPS：生产运维与部署

| 编号 | 题目 | 核心知识 | 验收标准 |
|---|---|---|---|
| PY-OPS-001 | Dockerfile | container | 镜像可构建并启动 |
| PY-OPS-002 | 非 root 容器 | security | 应用进程不以 root 运行 |
| PY-OPS-003 | Healthcheck | container | healthy/unhealthy 可判定 |
| PY-OPS-004 | docker compose | orchestration | app + db 可一键启动 |
| PY-OPS-005 | 持久化卷 | volume | 容器重建后数据不丢失 |
| PY-OPS-006 | Secret 管理 | env / secret | Secret 不写入镜像层 |
| PY-OPS-007 | Reverse Proxy | deployment | 代理到 FastAPI 正常工作 |
| PY-OPS-008 | HTTPS 基础 | TLS | HTTPS 请求可正常到达应用 |
| PY-OPS-009 | Rate limit | security | 高频请求被限制 |
| PY-OPS-010 | Audit log | audit | 关键操作有用户/时间/动作记录 |
| PY-OPS-011 | Metrics | metrics | 请求量、耗时、错误数可统计 |
| PY-OPS-012 | Backup | backup | DB 可备份并验证文件有效 |
| PY-OPS-013 | Restore | restore | 备份可恢复并校验数据 |
| PY-OPS-014 | Graceful shutdown | lifecycle | 服务收到停止信号后正确关闭 |
| PY-OPS-015 | Resource limits | CPU/RAM | 容器有明确资源上限 |
| PY-OPS-016 | Log rotation | logging ops | 日志不会无限增长 |
| PY-OPS-017 | Alert condition | monitoring | 服务不可用/错误率高时可产生告警事件 |
| PY-OPS-018 | Rollback | deployment | 新版本异常可以回滚 |

## CAP：综合项目任务

| 编号 | 题目 | 综合能力 | 验收标准 |
|---|---|---|---|
| PY-CAP-001 | PyOps 项目初始化 | Git / packaging | 仓库、环境、测试、README 均存在 |
| PY-CAP-002 | Server 管理 | CRUD | CLI/API/UI 三端可管理 Server |
| PY-CAP-003 | ICMP/TCP 连通性检查模拟器 | network abstraction | 不依赖真实环境也能完成自动测试 |
| PY-CAP-004 | CPU 检查器 | OOP | checker 插件正确执行 |
| PY-CAP-005 | 磁盘检查器 | file system | 阈值和异常正确处理 |
| PY-CAP-006 | 日志分析器 | regex / files | 指定错误模式能够统计 |
| PY-CAP-007 | 检查结果入库 | DB | 每次执行都有历史记录 |
| PY-CAP-008 | 批量检查任务 | async | 多 Server 并发执行、有上限 |
| PY-CAP-009 | 报告生成 | data processing | 能生成 JSON/CSV 报告 |
| PY-CAP-010 | Dashboard | Web | 服务器数量、健康状态、最近任务可视化 |
| PY-CAP-011 | 定时扫描 | scheduler | 每日/每小时任务可运行 |
| PY-CAP-012 | AI 运维摘要 | AI API | 根据检查结果生成结构化摘要，不直接执行命令 |
| PY-CAP-013 | 权限模型 | auth / role | viewer/operator/admin 权限不同 |
| PY-CAP-014 | 审计系统 | audit | 关键操作可追踪 |
| PY-CAP-015 | 生产部署 | Docker / reverse proxy | 从干净主机按 README 可完成部署 |
| PY-CAP-016 | 故障演练 | troubleshooting | DB down / API error / task timeout 均有可诊断日志 |
| PY-CAP-017 | 完整回归 | test / release | 主线测试、lint、类型检查全部通过 |
| PY-CAP-018 | v1.0 发布 | release engineering | 版本、变更记录、部署说明、回滚说明齐全 |

---

# 16. 题目难度标准

使用 1~5 级：

| 难度 | 定义 | 允许 AI 帮助 |
|---|---|---|
| 1 | 语法入门 | 可多次 Hint |
| 2 | 单一知识点组合 | Hint-1/2 |
| 3 | 多知识点 | 首次不给完整答案 |
| 4 | 工程问题 | 允许 Debug 指导 |
| 5 | 综合项目 | AI 可充当 Tech Lead，但学习者必须提交关键代码 |

---

# 17. 题目类型

```text
BASIC      单知识点
COMBINE    多知识点
DEBUG      修 Bug
REFACTOR   重构
TEST       写测试
DESIGN     设计题
PROJECT    项目功能
REVIEW     Code Review
OPS        部署运维
SECURITY   安全题
```

AI 出题时要控制分布，不能全是“从零写代码”。

建议比例：

```text
40% 编码
20% Debug
15% 测试
10% 重构
5% 设计
5% 安全
5% 运维
```

---

# 18. 自动验收规则

每个题目至少应具备：

- 2 个正常测试
- 1 个边界测试
- 1 个异常测试（若题目适用）
- 1 个隐藏测试

## 18.1 输出题

使用规范化文本比较：

- 统一换行符
- 删除末尾多余空白
- 默认不忽略行内空格

## 18.2 函数题

允许直接 import 学习者模块后调用目标函数。

## 18.3 CLI 题

使用 subprocess 输入 stdin，并校验 stdout / exit code。

## 18.4 API 题

使用 httpx / TestClient 调用接口并验证：

```text
status code
headers
JSON schema
业务结果
```

## 18.5 DB 题

在临时数据库中测试，禁止直接污染正式数据库。

---

# 19. AI Review 输出格式

AI 必须使用结构化 JSON，再由 UI 渲染：

```json
{
  "summary": "一句话总结",
  "correctness": "pass|partial|fail",
  "issues": [
    {
      "severity": "critical|major|minor|nit",
      "category": "logic|style|design|security|performance|typing|test",
      "message": "问题描述",
      "hint": "如何思考"
    }
  ],
  "knowledge_assessment": [
    {
      "knowledge_point": "if/elif/else",
      "level": "understood|partial|not_understood"
    }
  ],
  "next_action": "practice|fix|refactor|continue"
}
```

AI Review 禁止直接声称测试未执行；必须以实际 JudgeResult 为依据。

---

# 20. AI Prompt 契约

## 20.1 出题 Prompt

AI 必须读取：

- 当前阶段
- 前置知识
- 最近错误
- 当前项目版本
- 最近 5 次提交

然后生成 1 个题目。

禁止突然跨越当前阶段所需知识。

## 20.2 Hint Prompt

AI 输入：

```text
题目
知识点
学习者代码
失败测试
历史尝试
当前 hint_level
```

输出只允许对应等级的信息。

## 20.3 Review Prompt

AI 必须回答：

1. 功能是否正确
2. 哪些测试失败
3. 哪个知识点存在问题
4. 代码是否有明显工程风险
5. 下一步具体练习什么

---

# 21. 学习者状态机

```text
UNSEEN
  ↓
STARTED
  ↓
ATTEMPTING
  ├─失败 → RETRY
  │          ↓
  │       HINTED
  │
  └─通过 → PASSED
             ↓
         PRACTICED
             ↓
          MASTERED
```

若查看完整答案：

```text
PASSED_WITH_SOLUTION
```

该状态不能直接计为 MASTERED。

---

# 22. 第一版页面

## 首页

显示：

```text
当前阶段
当前题目
完成题数
知识点掌握数
最近错误
继续学习按钮
```

## 课程页

```text
阶段
 ├─ Lesson 1
 │   ├─ PY-BAS-001 ✅
 │   ├─ PY-BAS-002 ✅
 │   └─ PY-BAS-003 ▶
```

## 题目页

布局：

```text
左侧：题目
中间：代码
右侧：测试 / Hint / AI Review
```

## 提交结果

必须明显区分：

```text
✅ PASSED
❌ FAILED
⏱ TIMEOUT
💥 RUNTIME_ERROR
```

---

# 23. V1 开发顺序

AI 必须严格按以下阶段实施，不要一开始把所有功能一次性写完。

## Sprint 1：骨架

完成：

```text
pyproject.toml
FastAPI
SQLite
SQLAlchemy
基础目录
health endpoint
基础测试
```

验收：

```bash
uv run pytest
uv run ruff check .
uv run pyright
```

全部成功。

## Sprint 2：内容引擎

完成：

- course
- lesson
- knowledge_point
- problem
- test_case
- seed_content.py

验收：

```text
能够从 content/ 导入题目并在数据库查询。
```

## Sprint 3：判题器

完成：

- subprocess runner
- timeout
- stdout/stderr
- result model
- test runner

验收：

```text
正确代码 → PASSED
错误代码 → FAILED
死循环 → TIMEOUT
语法错误 → SYNTAX_ERROR
运行异常 → RUNTIME_ERROR
```

## Sprint 4：提交与进度

完成：

- submission API
- history
- progress
- attempt count
- hint state

## Sprint 5：Web UI

完成：

- 首页
- 课程页
- 题目页
- 提交结果
- 进度

## Sprint 6：AI

完成：

- provider config
- AI hint
- AI review
- 超时
- retry
- JSON schema validation

## Sprint 7：质量门禁

完成：

- unit tests
- integration tests
- lint
- type checking
- smoke test

## Sprint 8：发布

完成：

- Dockerfile
- compose
- healthcheck
- backup
- README

---

# 24. Definition of Done

任何 Sprint 只有同时满足以下条件才能结束：

```text
[ ] 功能实现
[ ] 单元测试
[ ] 集成测试（适用时）
[ ] Ruff
[ ] Pyright
[ ] README / docs
[ ] 错误路径处理
[ ] 日志
[ ] 无明显硬编码 Secret
[ ] 数据库变更可追踪
[ ] 关键路径可手工验证
```

---

# 25. AI 开发纪律

## 必须

1. 先读取规格书，再修改代码。
2. 每次只完成一个可验证的小目标。
3. 修改代码后运行对应测试。
4. 优先修复测试失败，再扩展功能。
5. 不得删除测试来“修复”失败。
6. 不得为了通过测试硬编码答案。
7. 不得擅自改变公共 API、数据库字段或题目编号规则。
8. 如需改变架构，先修改本规格书或创建 ADR。
9. 新增题目必须有唯一 code。
10. 新增题目必须有隐藏测试。

## 禁止

- 一次生成整个项目的大量代码后不运行测试。
- 使用 `shell=True` 执行学习者代码。
- 把 API Key 写入代码、测试或 Git。
- 用 AI 生成的解释代替实际测试结果。
- 在 V1 引入不必要的大型依赖。

---

# 26. AI 首次接手项目时的固定流程

AI 第一次接手仓库后必须依次执行：

```text
1. 读取本文件
2. 检查 Python / uv / Git
3. 检查目录
4. 检查 pyproject.toml
5. 创建最小 FastAPI app
6. 创建 SQLite schema
7. 运行 pytest
8. 运行 ruff
9. 运行 pyright
10. 报告当前状态
11. 只实施当前 Sprint
```

AI 首次状态报告格式：

```text
Project: Python Developer Lab
Spec Version: 1.0
Current Sprint: Sprint N
Python: x.y.z
Tests: X passed / Y failed
Ruff: PASS/FAIL
Pyright: PASS/FAIL
Database: PASS/FAIL
Current Problem: PY-XXX-XXX
Blockers: ...
Next Action: ...
```

---

# 27. 学习题与项目题的关系

每个阶段都要区分：

```text
Concept Problems
    ↓
Practice Problems
    ↓
Project Problems
    ↓
Capstone
```

例如：

```text
PY-CTL-002
CPU 三档告警
        ↓
PY-FUN-002
把 CPU 判断封装函数
        ↓
PY-OOP-006
HealthChecker
        ↓
PY-CAP-004
PyOps CPU Checker
```

因此每个知识点至少有一次“脱离项目的小题”，再至少有一次“项目中的真实使用”。

---

# 28. 错题系统

每次失败都保存：

```text
problem_id
knowledge_points
submitted_code
failed_test
error_type
hint_level
whether_solution_seen
```

系统自动形成：

```text
高频错误知识点
高频错误类型
重复失败题目
需要复习题目
```

复习规则：

```text
同一知识点 2 次失败
 → 生成补充题

同一知识点连续 3 次失败
 → 降低难度

同一知识点通过后
 → 7~14 天后安排复习题
```

---

# 29. AI 题目生成约束

AI 可以生成补充题，但必须遵守：

- 不引入尚未学习的核心知识，除非标记为预览题。
- 至少覆盖一个明确知识点。
- 必须有可自动验证结果。
- 必须包含边界情况。
- 不能把答案藏在题目描述里。
- 不能只测试输出样例，必须有隐藏测试。
- 题目必须记录到题库后才能进入正式学习路线。

自动生成题目的 ID 使用：

```text
PY-AI-{知识阶段}-{五位流水号}
```

例如：

```text
PY-AI-FUN-00001
```

---

# 30. 第一批种子题目

项目首次启动时，至少导入：

```text
ENV   8
BAS  15
CTL  15
DAT  15
FUN  15
FIL  18
OOP  16
TST  16
DB   18
API  17
WEB  12
ASY  12
ENG  15
OPS  18
CAP  18
```

总量约 **228 道主线题**。

实际开发时，AI 可以先创建前 30 题作为 v0.1 种子数据，后续按阶段逐步补齐到完整题库。**不要因为一次性创建 223 道题而牺牲判题器、数据模型和测试质量。**

---

# 31. V1 最小可运行验收场景

完成 V1 后，必须能完成以下完整流程：

```text
启动项目
 ↓
打开首页
 ↓
看到“Python 基础”
 ↓
进入 PY-BAS-001
 ↓
查看题目
 ↓
提交错误代码
 ↓
得到 FAILED
 ↓
看到具体失败测试
 ↓
请求 Hint-1
 ↓
修改代码
 ↓
重新提交
 ↓
得到 PASSED
 ↓
submission 写入数据库
 ↓
progress 更新
 ↓
下一题按钮出现
```

再验证失败场景：

```text
语法错误
运行时异常
死循环
超长输出
非法请求
AI API 超时
AI 返回非法 JSON
数据库异常
```

这些场景必须有测试或明确的手工验收步骤。

---

# 32. 后续生产级架构

V1 之后，逐步演进为：

```text
                     Browser
                        │
                     Reverse Proxy
                        │
                 ┌──────┴──────┐
                 │   FastAPI   │
                 └──────┬──────┘
                        │
       ┌────────────────┼────────────────┐
       │                │                │
   Course Service   Judge Service    AI Service
       │                │                │
       │          ┌─────┴─────┐          │
       │          │ Executor  │          │
       │          └─────┬─────┘          │
       │                │                │
       └────────── PostgreSQL ────────────┘
                        │
                      Redis
                        │
                     Worker
```

代码执行器必须与主 Web 进程逻辑隔离。

---

# 33. AI 接口抽象

建立：

```python
class AIProvider(Protocol):
    async def generate_hint(...): ...
    async def review_submission(...): ...
```

实现：

```text
OpenAICompatibleProvider
MockAIProvider
```

配置：

```env
AI_BASE_URL=
AI_API_KEY=
AI_MODEL=
AI_TIMEOUT_SECONDS=30
```

这样未来可接：

```text
OpenAI-compatible relay
Ollama
MiniMax
其他兼容服务
```

但业务层不能直接依赖具体厂商 SDK。

---

# 34. 数据内容与代码分离

题目正文、测试用例、提示、答案不要全部硬编码在 Python 文件中。

建议：

```text
content/problems/PY-BAS-001.yaml
content/problems/PY-BAS-002.yaml
...
```

启动时：

```text
YAML/JSON
 ↓
Schema validation
 ↓
Database seed
```

这样 AI 后续可以独立维护“课程内容”和“程序代码”。

---

# 35. ADR 机制

所有重大架构变化必须建立：

```text
docs/adr/0001-xxx.md
```

格式：

```text
# ADR-0001

## Context

## Decision

## Alternatives

## Consequences
```

例如：

```text
SQLite → PostgreSQL

本地 subprocess → Docker Executor

Jinja2 → SPA
```

---

# 36. 最终开发目标

项目最终应形成两个互相强化的成果：

## 成果 A：学习者能力

```text
Python 语言
 ↓
标准库
 ↓
OOP
 ↓
数据库
 ↓
Web
 ↓
异步并发
 ↓
测试
 ↓
工程化
 ↓
部署与运维
```

## 成果 B：真实软件

```text
Python Developer Lab
+
PyOps
```

也就是说，学习不是“看完课程”，而是：

```text
每完成一组题目
        ↓
获得一个真实开发能力
        ↓
将能力应用到 PyOps
        ↓
PyOps 功能增加
        ↓
最终形成完整软件
```

---

# 37. 给开发型 AI 的最终指令

你现在不是在回答“如何学 Python”，而是在开发一个长期运行的真实项目。

执行时必须遵循以下优先级：

```text
规格书 > 测试 > 当前任务 > AI 自己的偏好
```

当规格书没有明确内容时：

1. 优先选择 Python 官方标准库或当前既定技术栈。
2. 优先最简单、可测试、可维护的实现。
3. 不为了“高级”而增加复杂依赖。
4. 所有新功能必须可测试。
5. 不破坏已有题目、题目编号、数据库兼容性。
6. 不删除现有测试以绕过失败。
7. 对不确定的架构决策建立 ADR。

当前首次实施目标：

```text
实现 Python Developer Lab v0.1

仅完成：
- 项目骨架
- SQLite
- 课程/题目模型
- 题目 seed
- Python subprocess Judge
- submission 记录
- progress 记录
- FastAPI API
- 最小 Jinja2 UI
- pytest
- Ruff
- Pyright

完成后停止扩张范围，先让以下场景完整跑通：

打开题目
 → 提交 Python
 → 自动测试
 → 返回结果
 → 保存历史
 → 更新进度

然后再进入 v0.2。
```

---

# 38. 推荐的第一条 AI 开发指令

将本文件放到仓库根目录，例如：

```text
PYTHON_DEVELOPER_LAB_SPEC.md
```

然后向开发型 AI 输入：

```text
请读取仓库根目录的 PYTHON_DEVELOPER_LAB_SPEC.md。

你现在作为本项目的 Tech Lead + Senior Python Engineer。

不要直接开始编写全部功能。

第一步：
1. 检查当前仓库状态。
2. 检查 Python、uv、Git 是否可用。
3. 检查目录和已有代码。
4. 根据规格书判断当前 Sprint。
5. 列出实施前需要确认的仓库事实；如果事实可以通过命令获取，不要问我。
6. 建立最小可运行项目骨架。
7. 实现 Sprint 1。
8. 创建测试。
9. 运行 pytest、ruff、pyright。
10. 只有全部通过后才进入下一个子任务。

开发原则：
- 不一次生成整个项目。
- 每次只做一个可验证的小目标。
- 所有代码都要有测试。
- 不允许使用 shell=True 执行用户提交代码。
- 不允许硬编码 API Key。
- 不允许删除测试来规避失败。
- 每完成一个阶段，告诉我：修改了哪些文件、为什么、测试结果是什么、下一步是什么。

当前目标：Python Developer Lab v0.1。
```

---

# 39. 版本信息

```text
Document: PYTHON_DEVELOPER_LAB_SPEC.md
Version: 1.0
Status: Ready for implementation
Primary language: Chinese
Target learner: Python beginner → production developer
Initial product: Python Developer Lab
Training project: PyOps
V1 focus: Local-first learning + execution + auto judge + progress
```
