#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APIMonitor-CLI - LLM API Usage Tracker & Cost Analysis Engine
APIMonitor-CLI - LLM API用量追踪与成本分析引擎
Powered by GLM-5.1

Author: gitstq
License: MIT
"""

import argparse
import json
import sys
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
import re

__version__ = "1.0.0"
__author__ = "gitstq"

# Provider pricing per 1M tokens (USD)
PRICING = {
    "glm-5": {"input": 0.1, "output": 0.3},
    "glm-4": {"input": 0.1, "output": 0.3},
    "glm-4-flash": {"input": 0.01, "output": 0.02},
    "glm-4-plus": {"input": 0.5, "output": 1.5},
    "openai-gpt-4o": {"input": 5.0, "output": 15.0},
    "openai-gpt-4o-mini": {"input": 0.15, "output": 0.6},
    "openai-gpt-4-turbo": {"input": 10.0, "output": 30.0},
    "openai-gpt-3.5-turbo": {"input": 0.5, "output": 1.5},
    "anthropic-claude-3-5-sonnet": {"input": 3.0, "output": 15.0},
    "anthropic-claude-3-opus": {"input": 15.0, "output": 75.0},
    "anthropic-claude-3-haiku": {"input": 0.25, "output": 1.25},
    "deepseek-chat": {"input": 0.1, "output": 0.3},
    "deepseek-coder": {"input": 0.14, "output": 0.28},
    "qwen-plus": {"input": 0.6, "output": 1.8},
    "qwen-turbo": {"input": 0.3, "output": 0.6},
    "qwen-max": {"input": 20.0, "output": 60.0},
    "moonshot-v1-8k": {"input": 0.6, "output": 0.6},
    "moonshot-v1-32k": {"input": 1.2, "output": 1.2},
    "moonshot-v1-128k": {"input": 3.0, "output": 3.0},
    "yi-large": {"input": 3.0, "output": 3.0},
    "yi-medium": {"input": 0.3, "output": 0.3},
    "minimax": {"input": 0.1, "output": 0.1},
    "spark-3.5": {"input": 0.1, "output": 0.3},
    "spark-4.0": {"input": 0.5, "output": 1.5},
}


class APIMonitor:
    """Core API monitoring and cost tracking engine"""

    def __init__(self, data_file: str = "~/.apimonitor/data.json"):
        self.data_file = os.path.expanduser(data_file)
        self.usage_records: List[Dict] = []
        self._ensure_data_dir()
        self._load_data()

    def _ensure_data_dir(self):
        """Ensure data directory exists"""
        data_dir = os.path.dirname(self.data_file)
        if data_dir and not os.path.exists(data_dir):
            os.makedirs(data_dir, exist_ok=True)

    def _load_data(self):
        """Load usage data from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.usage_records = data.get('records', [])
            except Exception:
                self.usage_records = []

    def _save_data(self):
        """Save usage data to file"""
        data = {
            "version": __version__,
            "last_updated": datetime.now().isoformat(),
            "records": self.usage_records
        }
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Warning: Failed to save data: {e}")

    def log_usage(
        self,
        provider: str,
        model: str,
        input_tokens: int,
        output_tokens: int,
        request_id: Optional[str] = None,
        metadata: Optional[Dict] = None
    ) -> Dict:
        """Log an API usage record"""
        # Build model key for pricing lookup
        # Try multiple matching strategies
        model_lower = model.lower()
        
        # Strategy 1: Exact match with provider-model format
        model_key = f"{provider.lower()}-{model_lower}"
        price = PRICING.get(model_key)
        
        # Strategy 2: Direct model name match (e.g., glm-4-flash)
        if price is None:
            price = PRICING.get(model_lower)
        
        # Strategy 3: Try common variations
        if price is None:
            for key in PRICING.keys():
                if model_lower in key or key in f"{provider.lower()}-{model_lower}":
                    price = PRICING[key]
                    break
        
        # Default price if not found
        if price is None:
            price = {"input": 0.0, "output": 0.0}
        
        input_cost = (input_tokens / 1_000_000) * price["input"]
        output_cost = (output_tokens / 1_000_000) * price["output"]
        total_cost = input_cost + output_cost

        record = {
            "id": request_id or self._generate_id(),
            "timestamp": datetime.now().isoformat(),
            "provider": provider,
            "model": model,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": input_tokens + output_tokens,
            "input_cost": round(input_cost, 6),
            "output_cost": round(output_cost, 6),
            "total_cost": round(total_cost, 6),
            "metadata": metadata or {}
        }

        self.usage_records.append(record)
        self._save_data()
        return record

    def _generate_id(self) -> str:
        """Generate unique record ID"""
        import hashlib
        import time
        data = f"{time.time()}-{len(self.usage_records)}"
        return hashlib.md5(data.encode()).hexdigest()[:12]

    def get_summary(
        self,
        days: int = 7,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> Dict:
        """Get usage summary for specified period"""
        cutoff = datetime.now() - timedelta(days=days)
        cutoff_iso = cutoff.isoformat()

        records = [
            r for r in self.usage_records
            if r["timestamp"] >= cutoff_iso
        ]

        if provider:
            records = [r for r in records if r["provider"].lower() == provider.lower()]
        if model:
            records = [r for r in records if r["model"].lower() == model.lower()]

        total_input_tokens = sum(r["input_tokens"] for r in records)
        total_output_tokens = sum(r["output_tokens"] for r in records)
        total_tokens = total_input_tokens + total_output_tokens
        total_cost = sum(r["total_cost"] for r in records)

        # Group by provider
        by_provider: Dict[str, Dict] = {}
        for r in records:
            p = r["provider"]
            if p not in by_provider:
                by_provider[p] = {
                    "requests": 0,
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "cost": 0.0
                }
            by_provider[p]["requests"] += 1
            by_provider[p]["input_tokens"] += r["input_tokens"]
            by_provider[p]["output_tokens"] += r["output_tokens"]
            by_provider[p]["cost"] += r["total_cost"]

        # Group by model
        by_model: Dict[str, Dict] = {}
        for r in records:
            m = f"{r['provider']}/{r['model']}"
            if m not in by_model:
                by_model[m] = {
                    "requests": 0,
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "cost": 0.0
                }
            by_model[m]["requests"] += 1
            by_model[m]["input_tokens"] += r["input_tokens"]
            by_model[m]["output_tokens"] += r["output_tokens"]
            by_model[m]["cost"] += r["total_cost"]

        return {
            "period_days": days,
            "start_date": cutoff_iso,
            "end_date": datetime.now().isoformat(),
            "total_requests": len(records),
            "total_input_tokens": total_input_tokens,
            "total_output_tokens": total_output_tokens,
            "total_tokens": total_tokens,
            "total_cost_usd": round(total_cost, 6),
            "by_provider": by_provider,
            "by_model": by_model
        }

    def get_daily_stats(self, days: int = 30) -> List[Dict]:
        """Get daily usage statistics"""
        cutoff = datetime.now() - timedelta(days=days)
        records = [r for r in self.usage_records if r["timestamp"] >= cutoff.isoformat()]

        daily_data: Dict[str, Dict] = {}
        for r in records:
            date = r["timestamp"][:10]  # YYYY-MM-DD
            if date not in daily_data:
                daily_data[date] = {
                    "requests": 0,
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "cost": 0.0
                }
            daily_data[date]["requests"] += 1
            daily_data[date]["input_tokens"] += r["input_tokens"]
            daily_data[date]["output_tokens"] += r["output_tokens"]
            daily_data[date]["cost"] += r["total_cost"]

        return [
            {
                "date": date,
                **stats
            }
            for date, stats in sorted(daily_data.items())
        ]

    def export_csv(self, output_file: str = "~/.apimonitor/export.csv"):
        """Export usage records to CSV"""
        import csv
        output_file = os.path.expanduser(output_file)

        if not self.usage_records:
            print("No records to export.")
            return

        fieldnames = ["timestamp", "provider", "model", "input_tokens", "output_tokens",
                      "total_tokens", "input_cost", "output_cost", "total_cost", "id"]

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for record in self.usage_records:
                writer.writerow({k: record.get(k, '') for k in fieldnames})

        print(f"Exported {len(self.usage_records)} records to {output_file}")

    def clear_data(self, days: Optional[int] = None):
        """Clear usage records"""
        if days is None:
            self.usage_records = []
            self._save_data()
            print("All records cleared.")
        else:
            cutoff = (datetime.now() - timedelta(days=days)).isoformat()
            original_count = len(self.usage_records)
            self.usage_records = [r for r in self.usage_records if r["timestamp"] >= cutoff]
            removed = original_count - len(self.usage_records)
            self._save_data()
            print(f"Cleared {removed} records older than {days} days.")


def format_tokens(tokens: int) -> str:
    """Format token count for display"""
    if tokens >= 1_000_000:
        return f"{tokens / 1_000_000:.2f}M"
    elif tokens >= 1_000:
        return f"{tokens / 1_000:.2f}K"
    return str(tokens)


def format_cost(cost: float) -> str:
    """Format cost for display"""
    if cost >= 1:
        return f"${cost:.4f}"
    return f"${cost:.6f}"


def display_summary(summary: Dict):
    """Display usage summary in formatted style"""
    print("\n" + "=" * 60)
    print("📊 API Usage Summary")
    print("=" * 60)
    print(f"⏰ Period: Last {summary['period_days']} days")
    print(f"📅 {summary['start_date'][:10]} ~ {summary['end_date'][:10]}")
    print("-" * 60)
    print(f"📝 Total Requests:    {summary['total_requests']:,}")
    print(f"🔤 Input Tokens:      {format_tokens(summary['total_input_tokens'])}")
    print(f"📤 Output Tokens:     {format_tokens(summary['total_output_tokens'])}")
    print(f"💰 Total Cost:        {format_cost(summary['total_cost_usd'])}")
    print("-" * 60)

    if summary['by_provider']:
        print("\n📈 By Provider:")
        for provider, stats in sorted(summary['by_provider'].items()):
            print(f"  • {provider}: {stats['requests']} reqs, "
                  f"{format_tokens(stats['input_tokens'] + stats['output_tokens'])} tokens, "
                  f"{format_cost(stats['cost'])}")

    if summary['by_model']:
        print("\n🤖 By Model:")
        for model, stats in sorted(summary['by_model'].items(), key=lambda x: -x[1]['cost']):
            print(f"  • {model}: {stats['requests']} reqs, "
                  f"{format_tokens(stats['input_tokens'] + stats['output_tokens'])} tokens, "
                  f"{format_cost(stats['cost'])}")

    print("\n" + "=" * 60)


def display_daily_stats(stats: List[Dict]):
    """Display daily statistics"""
    print("\n" + "=" * 60)
    print("📅 Daily Usage Statistics")
    print("=" * 60)
    print(f"{'Date':<12} {'Requests':>10} {'Tokens':>15} {'Cost':>12}")
    print("-" * 60)

    for day in stats:
        print(f"{day['date']:<12} {day['requests']:>10,} "
              f"{format_tokens(day['input_tokens'] + day['output_tokens']):>15} "
              f"{format_cost(day['cost']):>12}")

    if stats:
        total_cost = sum(d['cost'] for d in stats)
        total_requests = sum(d['requests'] for d in stats)
        total_tokens = sum(d['input_tokens'] + d['output_tokens'] for d in stats)
        print("-" * 60)
        print(f"{'TOTAL':<12} {total_requests:>10,} {format_tokens(total_tokens):>15} {format_cost(total_cost):>12}")

    print("=" * 60)


def display_providers():
    """Display supported providers and models with pricing"""
    print("\n" + "=" * 60)
    print("🌐 Supported Providers & Models")
    print("=" * 60)

    providers = {}
    for key, prices in PRICING.items():
        if '-' in key:
            provider, model = key.split('-', 1)
        else:
            provider, model = key, key

        if provider not in providers:
            providers[provider] = []
        providers[provider].append((model, prices))

    for provider, models in sorted(providers.items()):
        print(f"\n📦 {provider.upper()}:")
        for model, prices in sorted(models, key=lambda x: x[1]['input']):
            print(f"  • {model}")
            print(f"    Input: ${prices['input']}/1M | Output: ${prices['output']}/1M")

    print("\n" + "=" * 60)


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="🔍 APIMonitor-CLI - LLM API Usage Tracker & Cost Analysis Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Log an API call
  apimonitor log --provider glm --model glm-4-flash --input 1000 --output 2000

  # View usage summary
  apimonitor summary --days 7

  # View daily statistics
  apimonitor daily --days 30

  # Export to CSV
  apimonitor export --output usage.csv

  # List supported providers
  apimonitor providers

  # Clear old records
  apimonitor clear --days 30
        """
    )

    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Log command
    log_parser = subparsers.add_parser('log', help='Log an API usage record')
    log_parser.add_argument('--provider', '-p', required=True, help='API provider (e.g., glm, openai)')
    log_parser.add_argument('--model', '-m', required=True, help='Model name')
    log_parser.add_argument('--input', '-i', type=int, required=True, help='Input tokens')
    log_parser.add_argument('--output', '-o', type=int, required=True, help='Output tokens')
    log_parser.add_argument('--id', help='Custom request ID')
    log_parser.add_argument('--meta', help='Metadata JSON string')
    log_parser.add_argument('--file', '-f', default='~/.apimonitor/data.json', help='Data file path')

    # Summary command
    summary_parser = subparsers.add_parser('summary', help='Show usage summary')
    summary_parser.add_argument('--days', '-d', type=int, default=7, help='Days to analyze (default: 7)')
    summary_parser.add_argument('--provider', help='Filter by provider')
    summary_parser.add_argument('--model', help='Filter by model')
    summary_parser.add_argument('--file', '-f', default='~/.apimonitor/data.json', help='Data file path')

    # Daily command
    daily_parser = subparsers.add_parser('daily', help='Show daily statistics')
    daily_parser.add_argument('--days', '-d', type=int, default=30, help='Days to analyze (default: 30)')
    daily_parser.add_argument('--file', '-f', default='~/.apimonitor/data.json', help='Data file path')

    # Export command
    export_parser = subparsers.add_parser('export', help='Export records to CSV')
    export_parser.add_argument('--output', '-o', default='~/.apimonitor/export.csv', help='Output file')
    export_parser.add_argument('--file', '-f', default='~/.apimonitor/data.json', help='Data file path')

    # Providers command (no file needed)
    subparsers.add_parser('providers', help='Show supported providers and pricing')

    # Clear command
    clear_parser = subparsers.add_parser('clear', help='Clear usage records')
    clear_parser.add_argument('--days', '-d', type=int, help='Clear records older than N days')
    clear_parser.add_argument('--file', '-f', default='~/.apimonitor/data.json', help='Data file path')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # Handle commands that don't need data file
    if args.command == 'providers':
        display_providers()
        return

    # Get data file path for commands that need it
    file_path = getattr(args, 'file', '~/.apimonitor/data.json')
    monitor = APIMonitor(file_path)

    if args.command == 'log':
        metadata = None
        if args.meta:
            try:
                metadata = json.loads(args.meta)
            except json.JSONDecodeError:
                print("Error: Invalid JSON in --meta")
                return

        record = monitor.log_usage(
            provider=args.provider,
            model=args.model,
            input_tokens=args.input,
            output_tokens=args.output,
            request_id=args.id,
            metadata=metadata
        )

        print("\n✅ Usage logged successfully!")
        print(f"   Provider: {record['provider']}")
        print(f"   Model:    {record['model']}")
        print(f"   Tokens:   {record['input_tokens']} in / {record['output_tokens']} out")
        print(f"   Cost:     {format_cost(record['total_cost'])}")
        print(f"   ID:       {record['id']}")

    elif args.command == 'summary':
        summary = monitor.get_summary(
            days=args.days,
            provider=args.provider,
            model=args.model
        )
        display_summary(summary)

    elif args.command == 'daily':
        stats = monitor.get_daily_stats(days=args.days)
        display_daily_stats(stats)

    elif args.command == 'export':
        monitor.export_csv(output_file=args.output)

    elif args.command == 'providers':
        display_providers()

    elif args.command == 'clear':
        monitor.clear_data(days=args.days)


if __name__ == '__main__':
    main()
