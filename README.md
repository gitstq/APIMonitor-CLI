# 🛠️ APIMonitor-CLI

> 🔍 LLM API Usage Tracker & Cost Analysis Engine | 轻量级LLM API用量追踪与成本分析引擎 | 零依赖跨平台支持

<p align="center">
  <a href="https://github.com/gitstq/APIMonitor-CLI/actions">
    <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python">
  </a>
  <a href="https://github.com/gitstq/APIMonitor-CLI/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  </a>
  <a href="https://github.com/gitstq/APIMonitor-CLI/stargazers">
    <img src="https://img.shields.io/github/stars/gitstq/APIMonitor-CLI?style=flat" alt="Stars">
  </a>
  <a href="https://github.com/gitstq/APIMonitor-CLI/releases">
    <img src="https://img.shields.io/github/v/release/gitstq/APIMonitor-CLI?include_prereleases" alt="Release">
  </a>
</p>

---

## 🌐 Language | 语言

[简体中文](README.md) | [繁體中文](docs/README_zh-TW.md) | [English](docs/README_en.md) | [日本語](docs/README_ja.md) | [한국어](docs/README_ko.md)

---

## ✨ Features | 功能特点

- 🔍 **全服务商覆盖** - 支持GLM、OpenAI、Anthropic、DeepSeek、Qwen、Moonshot、Yi、Spark等主流LLM服务商
- 💰 **智能成本分析** - 自动计算各模型用量与费用，支持自定义定价
- 📊 **多维度统计** - 按时间、服务商、模型多维度分析API使用情况
- 📈 **趋势可视化** - 每日/周/月用量趋势图表展示
- 🔔 **成本预警** - 设置预算阈值，超出自动提醒
- 📤 **数据导出** - 支持CSV/JSON格式导出，便于二次分析
- 🌐 **多语言支持** - 中文/English/日本語/한국어双语界面
- ⚡ **零依赖设计** - 仅使用Python标准库，无任何外部依赖
- 🔧 **跨平台支持** - Windows、macOS、Linux开箱即用

## 🚀 Quick Start | 快速开始

### 📥 Installation | 安装

```bash
# 方式一：pip安装（推荐）
pip install apimonitor-cli

# 方式二：直接运行
git clone https://github.com/gitstq/APIMonitor-CLI.git
cd APIMonitor-CLI
python cli.py --help
```

### 🖥️ Usage | 使用方法

```bash
# 查看支持的提供商
apimonitor providers

# 记录API调用
apimonitor log --provider glm --model glm-4-flash --input 1000 --output 2000

# 查看使用摘要
apimonitor summary --days 7

# 查看每日统计
apimonitor daily --days 30

# 导出数据
apimonitor export --output usage.csv
```

## 🌐 Supported Providers | 支持的服务商

| 服务商 | 模型 | 输入价格 | 输出价格 |
|--------|------|----------|----------|
| **GLM** | glm-4, glm-4-flash, glm-4-plus, glm-5 | $0.01-0.5/1M | $0.02-1.5/1M |
| **OpenAI** | gpt-4o, gpt-4o-mini, gpt-4-turbo, gpt-3.5-turbo | $0.15-10/1M | $0.6-30/1M |
| **Anthropic** | claude-3.5-sonnet, claude-3-opus, claude-3-haiku | $0.25-15/1M | $1.25-75/1M |
| **DeepSeek** | deepseek-chat, deepseek-coder | $0.1-0.14/1M | $0.28-0.3/1M |
| **Qwen** | qwen-plus, qwen-turbo, qwen-max | $0.3-20/1M | $0.6-60/1M |
| **Moonshot** | moonshot-v1-8k, moonshot-v1-32k, moonshot-v1-128k | $0.6-3/1M | $0.6-3/1M |

## 💡 Code Integration | 代码集成

```python
from apimonitor import APIMonitor

monitor = APIMonitor()

# 记录API调用
record = monitor.log_usage(
    provider="glm",
    model="glm-4-flash",
    input_tokens=1000,
    output_tokens=2000
)

print(f"Cost: ${record['total_cost']}")
```

## 🔧 Configuration | 配置

数据默认存储在 `~/.apimonitor/data.json`

指定自定义路径：

```bash
apimonitor summary --file /path/to/data.json
```

## 📁 Project Structure | 项目结构

```
APIMonitor-CLI/
├── src/
│   └── apimonitor.py       # 核心模块
├── tests/
│   └── test_apimonitor.py  # 测试用例
├── docs/                   # 多语言文档
│   ├── README_en.md
│   ├── README_zh-TW.md
│   ├── README_ja.md
│   └── README_ko.md
├── cli.py                  # CLI入口
├── setup.py                # 安装配置
├── requirements.txt         # 依赖配置
└── README.md              # 主文档
```

## 🤝 Contributing | 贡献

欢迎提交Issue和Pull Request！

## 📄 License | 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

<p align="center">
  <strong>APIMonitor-CLI</strong> - 让LLM API成本可视化 🎯
  <br>
  Made with ❤️ by <a href="https://github.com/gitstq">gitstq</a>
</p>
