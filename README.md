# APIMonitor-CLI

🛠️ LLM API Usage Tracker & Cost Analysis Engine

> 轻量级LLM API用量追踪与成本分析引擎 | 支持GLM-5.1等多服务商 | 零依赖、跨平台、TUI可视化

## Features | 功能特点

- 🔍 **全服务商覆盖** - 支持GLM、OpenAI、Anthropic、DeepSeek、Qwen等主流LLM服务商
- 💰 **智能成本分析** - 自动计算各模型用量与费用，支持自定义定价
- 📊 **多维度统计** - 按时间、服务商、模型多维度分析API使用情况
- 📈 **趋势可视化** - 每日/周/月用量趋势图表展示
- 🔔 **成本预警** - 设置预算阈值，超出自动提醒
- 📤 **数据导出** - 支持CSV/JSON格式导出，便于二次分析
- 🌐 **多语言支持** - 中文/English双语界面

## Installation | 安装

### 方式一：pip安装（推荐）

```bash
pip install apimonitor-cli
```

### 方式二：手动安装

```bash
git clone https://github.com/gitstq/APIMonitor-CLI.git
cd APIMonitor-CLI
pip install -e .
```

### 方式三：直接运行

```bash
python cli.py --help
```

## Quick Start | 快速开始

### 1. 查看支持的提供商

```bash
apimonitor providers
```

### 2. 记录API调用

```bash
# 记录GLM-4调用
apimonitor log --provider glm --model glm-4-flash --input 1000 --output 2000

# 记录OpenAI调用
apimonitor log -p openai -m gpt-4o-mini -i 500 -o 1500

# 带元数据记录
apimonitor log -p glm -m glm-4 --input 1000 --output 2000 --meta '{"user": "alice"}'
```

### 3. 查看使用摘要

```bash
# 最近7天摘要（默认）
apimonitor summary

# 最近30天摘要
apimonitor summary --days 30

# 按服务商筛选
apimonitor summary --provider glm

# 按模型筛选
apimonitor summary --model glm-4-flash
```

### 4. 查看每日统计

```bash
apimonitor daily --days 30
```

### 5. 导出数据

```bash
apimonitor export --output usage.csv
```

### 6. 清理数据

```bash
# 清理30天前的数据
apimonitor clear --days 30

# 清理所有数据
apimonitor clear
```

## Supported Providers | 支持的服务商

| Provider | Models | Input Price | Output Price |
|----------|--------|-------------|--------------|
| **GLM** | glm-4, glm-4-flash, glm-4-plus, glm-5 | $0.01-0.5/1M | $0.02-1.5/1M |
| **OpenAI** | gpt-4o, gpt-4o-mini, gpt-4-turbo, gpt-3.5-turbo | $0.15-10/1M | $0.6-30/1M |
| **Anthropic** | claude-3.5-sonnet, claude-3-opus, claude-3-haiku | $0.25-15/1M | $1.25-75/1M |
| **DeepSeek** | deepseek-chat, deepseek-coder | $0.1-0.14/1M | $0.28-0.3/1M |
| **Qwen** | qwen-plus, qwen-turbo, qwen-max | $0.3-20/1M | $0.6-60/1M |
| **Moonshot** | moonshot-v1-8k, moonshot-v1-32k, moonshot-v1-128k | $0.6-3/1M | $0.6-3/1M |
| **Yi** | yi-large, yi-medium | $0.3-3/1M | $0.3-3/1M |
| **Spark** | spark-3.5, spark-4.0 | $0.1-0.5/1M | $0.3-1.5/1M |

## Configuration | 配置

### 数据文件位置

默认数据存储在 `~/.apimonitor/data.json`

指定自定义路径：

```bash
apimonitor summary --file /path/to/data.json
```

### 自定义定价

编辑 `src/apimonitor.py` 中的 `PRICING` 字典添加自定义定价：

```python
PRICING = {
    "custom-model": {"input": 0.1, "output": 0.2},
}
```

## Integration | 集成使用

### 在代码中集成

```python
from apimonitor import APIMonitor

monitor = APIMonitor()

# 调用API后记录
record = monitor.log_usage(
    provider="glm",
    model="glm-4-flash",
    input_tokens=1000,
    output_tokens=2000,
    metadata={"user_id": "123"}
)

print(f"Cost: ${record['total_cost']}")
```

### 在应用启动时初始化

```python
# 建议在应用启动时初始化
monitor = APIMonitor()

# 在API调用后自动记录
```

## Development | 开发

### 本地运行

```bash
# 克隆项目
git clone https://github.com/gitstq/APIMonitor-CLI.git
cd APIMonitor-CLI

# 安装依赖（开发模式）
pip install -e .

# 运行测试
python -m pytest tests/

# 直接运行
python cli.py --help
```

### 运行测试

```bash
python -m pytest tests/ -v
```

## License | 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## Contributing | 贡献

欢迎提交 Issue 和 Pull Request！

## Support | 支持

如有问题，请提交 [Issue](https://github.com/gitstq/APIMonitor-CLI/issues)

---

<p align="center">
  <strong>APIMonitor-CLI</strong> - 让LLM API成本可视化 🎯
</p>
