# 🛠️ APIMonitor-CLI

> 🔍 LLM API Usage Tracker & Cost Analysis Engine | English README

<p align="center">
  <a href="https://github.com/gitstq/APIMonitor-CLI/actions">
    <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python">
  </a>
  <a href="https://github.com/gitstq/APIMonitor-CLI/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  </a>
</p>

---

## 🌐 Language

[简体中文](README.md) | [繁體中文](README_zh-TW.md) | **English** | [日本語](README_ja.md) | [한국어](README_ko.md)

---

## ✨ Features

- 🔍 **Multi-Provider Support** - Supports GLM, OpenAI, Anthropic, DeepSeek, Qwen, Moonshot, Yi, Spark and more
- 💰 **Smart Cost Analysis** - Automatically calculates usage and costs for all models
- 📊 **Multi-Dimensional Statistics** - Analyze API usage by time, provider, and model
- 📈 **Trend Visualization** - Daily/weekly/monthly usage trend charts
- 🔔 **Cost Alerts** - Set budget thresholds with automatic notifications
- 📤 **Data Export** - Export to CSV/JSON for further analysis
- 🌐 **Multi-Language** - Chinese/English/Japanese/Korean interface
- ⚡ **Zero Dependencies** - Uses Python standard library only
- 🔧 **Cross-Platform** - Works on Windows, macOS, Linux

## 🚀 Quick Start

### 📥 Installation

```bash
# Method 1: pip install (recommended)
pip install apimonitor-cli

# Method 2: Direct run
git clone https://github.com/gitstq/APIMonitor-CLI.git
cd APIMonitor-CLI
python cli.py --help
```

### 🖥️ Usage

```bash
# View supported providers
apimonitor providers

# Log an API call
apimonitor log --provider glm --model glm-4-flash --input 1000 --output 2000

# View usage summary
apimonitor summary --days 7

# View daily statistics
apimonitor daily --days 30

# Export data
apimonitor export --output usage.csv
```

## 🌐 Supported Providers

| Provider | Models | Input Price | Output Price |
|----------|--------|-------------|---------------|
| **GLM** | glm-4, glm-4-flash, glm-4-plus, glm-5 | $0.01-0.5/1M | $0.02-1.5/1M |
| **OpenAI** | gpt-4o, gpt-4o-mini, gpt-4-turbo, gpt-3.5-turbo | $0.15-10/1M | $0.6-30/1M |
| **Anthropic** | claude-3.5-sonnet, claude-3-opus, claude-3-haiku | $0.25-15/1M | $1.25-75/1M |
| **DeepSeek** | deepseek-chat, deepseek-coder | $0.1-0.14/1M | $0.28-0.3/1M |
| **Qwen** | qwen-plus, qwen-turbo, qwen-max | $0.3-20/1M | $0.6-60/1M |
| **Moonshot** | moonshot-v1-8k, moonshot-v1-32k, moonshot-v1-128k | $0.6-3/1M | $0.6-3/1M |

## 💡 Code Integration

```python
from apimonitor import APIMonitor

monitor = APIMonitor()

# Log API call
record = monitor.log_usage(
    provider="glm",
    model="glm-4-flash",
    input_tokens=1000,
    output_tokens=2000
)

print(f"Cost: ${record['total_cost']}")
```

## 🔧 Configuration

Data is stored in `~/.apimonitor/data.json` by default.

Specify custom path:

```bash
apimonitor summary --file /path/to/data.json
```

## 📁 Project Structure

```
APIMonitor-CLI/
├── src/
│   └── apimonitor.py       # Core module
├── tests/
│   └── test_apimonitor.py  # Unit tests
├── docs/                   # Multi-language docs
├── cli.py                  # CLI entry point
├── setup.py                # Setup configuration
├── requirements.txt        # Dependencies
└── README.md             # Main documentation
```

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 📄 License

MIT License - See [LICENSE](LICENSE) file

---

<p align="center">
  <strong>APIMonitor-CLI</strong> - Make LLM API costs visible 🎯
  <br>
  Made with ❤️ by <a href="https://github.com/gitstq">gitstq</a>
</p>
