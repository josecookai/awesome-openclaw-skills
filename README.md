# Awesome OpenClaw Skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 精选 OpenClaw 技能清单，让你的 AI Agent 更强大

[English](./README.md) | [中文](./README.zh.md)

---

## 📋 目录

- [核心必备](#核心必备)
- [生产力工具](#生产力工具)
- [开发工具](#开发工具)
- [社交媒体](#社交媒体)
- [数据分析](#数据分析)
- [多媒体处理](#多媒体处理)
- [生活服务](#生活服务)
- [消费者工具](#消费者工具)
- [贡献指南](#贡献指南)

---

## 🎯 核心必备

| 技能 | 描述 | 安装命令 | 使用场景 |
|------|------|---------|---------|
| [browser-use](https://clawdhub.com/skills/browser-use) | 浏览器自动化 | `clawdhub install browser-use` | 网页操作、数据采集、自动化测试 |
| [gog](https://clawdhub.com/skills/gog) | Google 全家桶 | `clawdhub install gog` | Gmail、日历、Drive、文档管理 |
| [notion](https://clawdhub.com/skills/notion) | 知识库管理 | `clawdhub install notion` | 笔记、数据库、项目管理 |
| [github](https://clawdhub.com/skills/github) | GitHub 操作 | `clawdhub install github` | 代码托管、PR、Issue 管理 |
| [slack](https://clawdhub.com/skills/slack) | 团队沟通 | `clawdhub install slack` | 消息通知、频道管理 |
| [telegram](https://clawdhub.com/skills/telegram) | 即时通讯 | `clawdhub install telegram` | Bot 开发、消息推送 |

---

## 💼 生产力工具

| 技能 | 描述 | 安装命令 |
|------|------|---------|
| [himalaya](https://clawdhub.com/skills/himalaya) | 邮件客户端 | `clawdhub install himalaya` |
| [nano-pdf](https://clawdhub.com/skills/nano-pdf) | PDF 编辑 | `clawdhub install nano-pdf` |
| [session-logs](https://clawdhub.com/skills/session-logs) | 会话分析 | `clawdhub install session-logs` |
| [canvas](https://clawdhub.com/skills/canvas) | 可视化展示 | `clawdhub install canvas` |
| [skill-creator](https://clawdhub.com/skills/skill-creator) | 创建自定义技能 | `clawdhub install skill-creator` |
| [capability-evolver](https://clawdhub.com/skills/capability-evolver) | 能力进化 | `clawdhub install capability-evolver` |

---

## 💻 开发工具

| 技能 | 描述 | 安装命令 |
|------|------|---------|
| [coding-agent](https://clawdhub.com/skills/coding-agent) | 编程助手 | `clawdhub install coding-agent` |
| [oracle](https://clawdhub.com/skills/oracle) | 代码分析 | `clawdhub install oracle` |
| [skyvern-mcp](https://github.com/Skyvern-AI/skyvern) | AI 浏览器自动化 (MCP) | 见下方配置 |
| [tmux](https://clawdhub.com/skills/tmux) | 终端管理 | `clawdhub install tmux` |
| [clawdhub](https://clawdhub.com/skills/clawdhub) | 技能管理 | `clawdhub install clawdhub` |

### skyvern-mcp 配置

AI 驱动的浏览器自动化，支持自然语言控制。YC 背景团队开发，使用 LLM + 计算机视觉代替传统 XPath。

```json
{
  "mcpServers": {
    "skyvern": {
      "command": "python",
      "args": ["-m", "skyvern", "run", "mcp"],
      "env": {
        "SKYVERN_BASE_URL": "https://api.skyvern.com",
        "SKYVERN_API_KEY": "your-api-key"
      }
    }
  }
}
```

**使用场景:** 自动填表、数据抓取、文件下载、复杂工作流自动化

---

## 📱 社交媒体

| 技能 | 描述 | 安装命令 |
|------|------|---------|
| [bird](https://clawdhub.com/skills/bird) | X/Twitter | `clawdhub install bird` |
| [slack](https://clawdhub.com/skills/slack) | Slack | `clawdhub install slack` |
| [telegram](https://clawdhub.com/skills/telegram) | Telegram | `clawdhub install telegram` |

---

## 📊 数据分析

| 技能 | 描述 | 安装命令 |
|------|------|---------|
| [web_search](https://clawdhub.com/skills/web_search) | 网页搜索 | `clawdhub install web_search` |
| [web_fetch](https://clawdhub.com/skills/web_fetch) | 网页抓取 | `clawdhub install web_fetch` |
| [weather](https://clawdhub.com/skills/weather) | 天气查询 | `clawdhub install weather` |

---

## 🎨 多媒体处理

| 技能 | 描述 | 安装命令 |
|------|------|---------|
| [canvas](https://clawdhub.com/skills/canvas) | 图像生成 | `clawdhub install canvas` |
| [tts](https://clawdhub.com/skills/tts) | 文本转语音 | 内置支持 |

---

## 🏠 生活服务

| 技能 | 描述 | 使用场景 |
|------|------|---------|
| [weather](https://clawdhub.com/skills/weather) | 天气查询 | 天气预报、出行规划 |
| [bill-splitter](./consumer/bill-splitter/SKILL.md) | 账单分摊 & 小费计算 | 餐厅分账、旅行账单、债务简化 |
| [health-calculator](./consumer/health-calculator/SKILL.md) | 健康指标计算 | BMI、每日卡路里、宏量营养素、水分需求 |
| [cycle-tracker](./consumer/cycle-tracker/SKILL.md) | 生理期追踪 & 预测 | 月经周期预测、排卵窗口、周期健康建议 |
| [focus-planner](./consumer/focus-planner/SKILL.md) | 专注规划 & 习惯管理 | 番茄钟、任务拆解、习惯设计、抗拖延 |
| [symptom-advisor](./consumer/symptom-advisor/SKILL.md) | 症状分诊建议 | 症状评估、就医紧急度判断、红旗症状筛查 |
| [quit-tracker](./consumer/quit-tracker/SKILL.md) | 戒断进度追踪 | 戒烟/戒酒进度、健康里程碑、省钱计算、渴望管理 |

---

## 📊 技能分类统计

```
总技能数: 26+
核心必备: 6
生产力: 6
开发工具: 4
社交媒体: 3
数据分析: 3
多媒体: 2
生活服务: 7 (新增 6 个消费者技能)
```

---

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 提交新技能

1. **Fork** 本仓库
2. 在相应分类中添加技能信息
3. 提交 **Pull Request**

### PR 格式要求

```markdown
## 新增技能: [技能名称]

**技能信息:**
- 名称: 
- 描述: 
- 安装命令: `clawdhub install [name]`
- 官方链接: 
- 分类: [核心必备/生产力/开发工具/社交媒体/数据分析/多媒体/生活服务]

**使用示例:**
```bash
# 示例代码
```

**测试环境:**
- OpenClaw 版本: 
- 操作系统: 
- 测试日期: 

**附加信息:**
- 是否有已知问题?
- 是否需要特殊配置?
```

### 分类标准

| 分类 | 说明 |
|------|------|
| 核心必备 | 每个 OpenClaw 用户都应该安装的基础技能 |
| 生产力 | 提升工作效率的工具 |
| 开发工具 | 程序员专用工具 |
| 社交媒体 | 社交平台集成 |
| 数据分析 | 数据处理、搜索、分析 |
| 多媒体 | 图像、音频、视频处理 |
| 生活服务 | 日常生活助手 |

### 技能收录标准

✅ **接受收录:**
- 官方维护或社区广泛使用的技能
- 有明确的文档和使用说明
- 通过基本功能测试
- 遵守 OpenClaw 使用规范

❌ **不接受:**
- 恶意软件或侵犯隐私的工具
- 无法验证来源的技能
- 长期无人维护的项目
- 违反法律法规的功能

---

## 📜 License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

本列表采用 [CC0 1.0 Universal](LICENSE) 协议，可自由使用。

---

## 🙏 致谢

感谢所有贡献者和 OpenClaw 社区！

> **注意**: 本清单由社区维护，与 OpenClaw 官方无直接关联。
