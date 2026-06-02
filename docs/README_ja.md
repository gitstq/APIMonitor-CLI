# 🛠️ APIMonitor-CLI

> 🔍 LLM API使用量トラッカー＆コスト分析エンジン | 日本語 README

<p align="center">
  <a href="https://github.com/gitstq/APIMonitor-CLI/actions">
    <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python">
  </a>
  <a href="https://github.com/gitstq/APIMonitor-CLI/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  </a>
</p>

---

## 🌐 Language | 言語

[简体中文](../README.md) | [繁體中文](../docs/README_zh-TW.md) | [English](../docs/README_en.md) | **日本語** | [한국어](../docs/README_ko.md)

---

## ✨ 機能特徴

- 🔍 **マルチプロバイダー対応** - GLM、OpenAI、Anthropic、DeepSeek、Qwen、Moonshot、Yi、Sparkなどをサポート
- 💰 **スマートコスト分析** - 各モデルの使用量とコストを自動計算
- 📊 **多次元統計** - 時間、プロバイダー、モデル別にAPI使用状況を分析
- 📈 **トレンド可視化** - 日次/週次/月次の使用量トレンドチャート
- 🔔 **コストアラート** - 予算閾値を設定して自動通知
- 📤 **データエクスポート** - CSV/JSON形式でのエクスポートに対応
- 🌐 **多言語対応** - 中国語/英語/日本語/韓国語インターフェース
- ⚡ **ゼロ依存** - Python標準ライブラリのみ使用
- 🔧 **クロスプラットフォーム** - Windows、macOS、Linuxで動作

## 🚀 クイックスタート

### 📥 インストール

```bash
# 方法1：pipインストール（推奨）
pip install apimonitor-cli

# 方法2：直接実行
git clone https://github.com/gitstq/APIMonitor-CLI.git
cd APIMonitor-CLI
python cli.py --help
```

### 🖥️ 使用方法

```bash
# 対応プロバイダーを表示
apimonitor providers

# API呼び出しを記録
apimonitor log --provider glm --model glm-4-flash --input 1000 --output 2000

# 使用量サマリーを表示
apimonitor summary --days 7

# 日次統計を表示
apimonitor daily --days 30

# データをエクスポート
apimonitor export --output usage.csv
```

## 🌐 対応プロバイダー

| プロバイダー | モデル | 入力価格 | 出力価格 |
|-------------|--------|----------|----------|
| **GLM** | glm-4, glm-4-flash, glm-4-plus, glm-5 | $0.01-0.5/1M | $0.02-1.5/1M |
| **OpenAI** | gpt-4o, gpt-4o-mini, gpt-4-turbo, gpt-3.5-turbo | $0.15-10/1M | $0.6-30/1M |
| **Anthropic** | claude-3.5-sonnet, claude-3-opus, claude-3-haiku | $0.25-15/1M | $1.25-75/1M |
| **DeepSeek** | deepseek-chat, deepseek-coder | $0.1-0.14/1M | $0.28-0.3/1M |
| **Qwen** | qwen-plus, qwen-turbo, qwen-max | $0.3-20/1M | $0.6-60/1M |
| **Moonshot** | moonshot-v1-8k, moonshot-v1-32k, moonshot-v1-128k | $0.6-3/1M | $0.6-3/1M |

## 💡 コード統合

```python
from apimonitor import APIMonitor

monitor = APIMonitor()

# API呼び出しを記録
record = monitor.log_usage(
    provider="glm",
    model="glm-4-flash",
    input_tokens=1000,
    output_tokens=2000
)

print(f"Cost: ${record['total_cost']}")
```

## 🔧 設定

データはデフォルトで `~/.apimonitor/data.json` に保存されます。

カスタムパス指定：

```bash
apimonitor summary --file /path/to/data.json
```

## 🤝 コントリビューション

IssueとPull Requestを歓迎します！

## 📄 ライセンス

MIT License - [LICENSE](../LICENSE)ファイルを参照

---

<p align="center">
  <strong>APIMonitor-CLI</strong> - LLM APIコストを可視化 🎯
  <br>
  Made with ❤️ by <a href="https://github.com/gitstq">gitstq</a>
</p>
