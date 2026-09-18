# ADR-0001：V1 使用本地受限执行器

## Context
V1 面向本机学习，必须支持快速反馈；代码执行又是最高风险边界。

## Decision
将用户代码写入临时工作目录，使用 sys.executable 与参数数组执行，禁止 shell，设置超时、输出上限、静态导入检查，并在上下文退出时清理目录。服务默认仅由本机访问。

## Alternatives
Docker Executor 提供更强隔离，作为后续版本能力加入；第三方沙箱不符合本地优先目标。

## Consequences
V1 不适合公网部署；部署到 NAS/LAN 前必须升级 Docker Executor。
