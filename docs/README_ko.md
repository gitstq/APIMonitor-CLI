# 🛠️ APIMonitor-CLI

> 🔍 LLM API 사용량 추적기 & 비용 분석 엔진 | 한국어 README

<p align="center">
  <a href="https://github.com/gitstq/APIMonitor-CLI/actions">
    <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python">
  </a>
  <a href="https://github.com/gitstq/APIMonitor-CLI/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  </a>
</p>

---

## 🌐 Language | 언어

[简体中文](../README.md) | [繁�체中文](../docs/README_zh-TW.md) | [English](../docs/README_en.md) | [日本語](../docs/README_ja.md) | **한국어**

---

## ✨ 기능 특징

- 🔍 **멀티 프로바이더 지원** - GLM, OpenAI, Anthropic, DeepSeek, Qwen, Moonshot, Yi, Spark 등 지원
- 💰 **스마트 비용 분석** - 각 모델의 사용량과 비용 자동 계산
- 📊 **다차원 통계** - 시간, 프로바이더, 모델별로 API 사용 현황 분석
- 📈 **트렌드 시각화** - 일일/주간/월간 사용량 트렌드 차트
- 🔔 **비용 알림** - 예산 임계값 설정 및 자동 알림
- 📤 **데이터 내보내기** - CSV/JSON 형식으로 내보내기 지원
- 🌐 **다국어 지원** - 중국어/영어/일본어/한국어 인터페이스
- ⚡ **제로 의존성** - Python 표준 라이브러리만 사용
- 🔧 **크로스 플랫폼** - Windows, macOS, Linux에서 작동

## 🚀 빠른 시작

### 📥 설치

```bash
# 방법1: pip 설치 (권장)
pip install apimonitor-cli

# 방법2: 직접 실행
git clone https://github.com/gitstq/APIMonitor-CLI.git
cd APIMonitor-CLI
python cli.py --help
```

### 🖥️ 사용 방법

```bash
# 지원 프로바이더 보기
apimonitor providers

# API 호출 기록
apimonitor log --provider glm --model glm-4-flash --input 1000 --output 2000

# 사용량 요약 보기
apimonitor summary --days 7

# 일일 통계 보기
apimonitor daily --days 30

# 데이터 내보내기
apimonitor export --output usage.csv
```

## 🌐 지원 프로바이더

| 프로바이더 | 모델 | 입력 가격 | 출력 가격 |
|-----------|------|----------|----------|
| **GLM** | glm-4, glm-4-flash, glm-4-plus, glm-5 | $0.01-0.5/1M | $0.02-1.5/1M |
| **OpenAI** | gpt-4o, gpt-4o-mini, gpt-4-turbo, gpt-3.5-turbo | $0.15-10/1M | $0.6-30/1M |
| **Anthropic** | claude-3.5-sonnet, claude-3-opus, claude-3-haiku | $0.25-15/1M | $1.25-75/1M |
| **DeepSeek** | deepseek-chat, deepseek-coder | $0.1-0.14/1M | $0.28-0.3/1M |
| **Qwen** | qwen-plus, qwen-turbo, qwen-max | $0.3-20/1M | $0.6-60/1M |
| **Moonshot** | moonshot-v1-8k, moonshot-v1-32k, moonshot-v1-128k | $0.6-3/1M | $0.6-3/1M |

## 💡 코드 통합

```python
from apimonitor import APIMonitor

monitor = APIMonitor()

# API 호출 기록
record = monitor.log_usage(
    provider="glm",
    model="glm-4-flash",
    input_tokens=1000,
    output_tokens=2000
)

print(f"Cost: ${record['total_cost']}")
```

## 🔧 설정

데이터는 기본적으로 `~/.apimonitor/data.json`에 저장됩니다.

사용자 지정 경로 지정:

```bash
apimonitor summary --file /path/to/data.json
```

## 🤝 기여

Issue와 Pull Request를 환영합니다!

## 📄 라이선스

MIT License - [LICENSE](../LICENSE) 파일 참조

---

<p align="center">
  <strong>APIMonitor-CLI</strong> - LLM API 비용 시각화 🎯
  <br>
  Made with ❤️ by <a href="https://github.com/gitstq">gitstq</a>
</p>
