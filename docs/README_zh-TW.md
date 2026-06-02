# 🛠️ APIMonitor-CLI

> 🔍 LLM API 用量追蹤與成本分析引擎 | 繁體中文說明文件

<p align="center">
  <a href="https://github.com/gitstq/APIMonitor-CLI/actions">
    <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python">
  </a>
  <a href="https://github.com/gitstq/APIMonitor-CLI/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  </a>
</p>

---

## 🌐 Language | 語言

[簡體中文](../README.md) | **繁體中文** | [English](../docs/README_en.md) | [日本語](../docs/README_ja.md) | [한국어](../docs/README_ko.md)

---

## ✨ 功能特點

- 🔍 **全服務商覆蓋** - 支持GLM、OpenAI、Anthropic、DeepSeek、Qwen、Moonshot、Yi、Spark等主流LLM服務商
- 💰 **智能成本分析** - 自動計算各模型用量與費用，支持自定義定價
- 📊 **多維度統計** - 按時間、服務商、模型多維度分析API使用情況
- 📈 **趨勢可視化** - 每日/週/月用量趨勢圖表展示
- 🔔 **成本預警** - 設置預算閾值，超出自動提醒
- 📤 **數據導出** - 支持CSV/JSON格式導出，便於二次分析
- 🌐 **多語言支持** - 中文/English/日本語/한국어雙語界面
- ⚡ **零依賴設計** - 僅使用Python標準庫，無任何外部依賴
- 🔧 **跨平台支持** - Windows、macOS、Linux開箱即用

## 🚀 快速開始

### 📥 安裝

```bash
# 方式一：pip安裝（推薦）
pip install apimonitor-cli

# 方式二：直接運行
git clone https://github.com/gitstq/APIMonitor-CLI.git
cd APIMonitor-CLI
python cli.py --help
```

### 🖥️ 使用方法

```bash
# 查看支持的提供商
apimonitor providers

# 記錄API調用
apimonitor log --provider glm --model glm-4-flash --input 1000 --output 2000

# 查看使用摘要
apimonitor summary --days 7

# 查看每日統計
apimonitor daily --days 30

# 導出數據
apimonitor export --output usage.csv
```

## 🌐 支持的服務商

| 服務商 | 模型 | 輸入價格 | 輸出價格 |
|--------|------|----------|----------|
| **GLM** | glm-4, glm-4-flash, glm-4-plus, glm-5 | $0.01-0.5/1M | $0.02-1.5/1M |
| **OpenAI** | gpt-4o, gpt-4o-mini, gpt-4-turbo, gpt-3.5-turbo | $0.15-10/1M | $0.6-30/1M |
| **Anthropic** | claude-3.5-sonnet, claude-3-opus, claude-3-haiku | $0.25-15/1M | $1.25-75/1M |
| **DeepSeek** | deepseek-chat, deepseek-coder | $0.1-0.14/1M | $0.28-0.3/1M |
| **Qwen** | qwen-plus, qwen-turbo, qwen-max | $0.3-20/1M | $0.6-60/1M |
| **Moonshot** | moonshot-v1-8k, moonshot-v1-32k, moonshot-v1-128k | $0.6-3/1M | $0.6-3/1M |

## 💡 代碼集成

```python
from apimonitor import APIMonitor

monitor = APIMonitor()

# 記錄API調用
record = monitor.log_usage(
    provider="glm",
    model="glm-4-flash",
    input_tokens=1000,
    output_tokens=2000
)

print(f"Cost: ${record['total_cost']}")
```

## 🔧 配置

數據默認存儲在 `~/.apimonitor/data.json`

指定自定義路徑：

```bash
apimonitor summary --file /path/to/data.json
```

## 🤝 貢獻

歡迎提交Issue和Pull Request！

## 📄 許可證

MIT License - 詳見 [LICENSE](../LICENSE) 文件

---

<p align="center">
  <strong>APIMonitor-CLI</strong> - 讓LLM API成本可視化 🎯
  <br>
  Made with ❤️ by <a href="https://github.com/gitstq">gitstq</a>
</p>
