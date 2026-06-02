#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for APIMonitor-CLI
"""

import unittest
import os
import sys
import json
import tempfile
import shutil

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from apimonitor import APIMonitor, format_tokens, format_cost, PRICING


class TestAPIMonitor(unittest.TestCase):
    """Test cases for APIMonitor class"""

    def setUp(self):
        """Set up test fixtures"""
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, 'test_data.json')
        self.monitor = APIMonitor(data_file=self.test_file)

    def tearDown(self):
        """Clean up test fixtures"""
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_log_usage(self):
        """Test logging API usage"""
        record = self.monitor.log_usage(
            provider="glm",
            model="glm-4-flash",
            input_tokens=1000,
            output_tokens=2000
        )

        self.assertIsNotNone(record['id'])
        self.assertEqual(record['provider'], 'glm')
        self.assertEqual(record['model'], 'glm-4-flash')
        self.assertEqual(record['input_tokens'], 1000)
        self.assertEqual(record['output_tokens'], 2000)
        self.assertEqual(record['total_tokens'], 3000)
        self.assertGreater(record['total_cost'], 0)

    def test_log_usage_with_metadata(self):
        """Test logging with metadata"""
        metadata = {"user_id": "123", "session": "abc"}
        record = self.monitor.log_usage(
            provider="openai",
            model="gpt-4o-mini",
            input_tokens=500,
            output_tokens=1500,
            metadata=metadata
        )

        self.assertEqual(record['metadata'], metadata)

    def test_get_summary_empty(self):
        """Test summary with no data"""
        summary = self.monitor.get_summary()
        self.assertEqual(summary['total_requests'], 0)
        self.assertEqual(summary['total_cost_usd'], 0)

    def test_get_summary_with_data(self):
        """Test summary with usage data"""
        # Add some records
        self.monitor.log_usage("glm", "glm-4-flash", 1000, 2000)
        self.monitor.log_usage("openai", "gpt-4o-mini", 500, 1500)

        summary = self.monitor.get_summary()
        self.assertEqual(summary['total_requests'], 2)
        self.assertGreater(summary['total_cost_usd'], 0)
        self.assertIn('glm', summary['by_provider'])
        self.assertIn('openai', summary['by_provider'])

    def test_get_summary_by_provider(self):
        """Test summary filtering by provider"""
        self.monitor.log_usage("glm", "glm-4-flash", 1000, 2000)
        self.monitor.log_usage("openai", "gpt-4o-mini", 500, 1500)

        summary = self.monitor.get_summary(provider="glm")
        self.assertEqual(summary['total_requests'], 1)

    def test_get_daily_stats(self):
        """Test daily statistics"""
        self.monitor.log_usage("glm", "glm-4-flash", 1000, 2000)
        stats = self.monitor.get_daily_stats(days=7)
        self.assertGreaterEqual(len(stats), 1)

    def test_export_csv(self):
        """Test CSV export"""
        self.monitor.log_usage("glm", "glm-4-flash", 1000, 2000)
        csv_file = os.path.join(self.test_dir, 'export.csv')
        self.monitor.export_csv(output_file=csv_file)

        self.assertTrue(os.path.exists(csv_file))
        with open(csv_file, 'r') as f:
            content = f.read()
            self.assertIn('timestamp', content)
            self.assertIn('glm', content)

    def test_clear_data(self):
        """Test clearing data"""
        self.monitor.log_usage("glm", "glm-4-flash", 1000, 2000)
        self.assertEqual(len(self.monitor.usage_records), 1)

        self.monitor.clear_data()
        self.assertEqual(len(self.monitor.usage_records), 0)

    def test_data_persistence(self):
        """Test data is saved and loaded"""
        self.monitor.log_usage("glm", "glm-4-flash", 1000, 2000)

        # Create new monitor instance with same file
        new_monitor = APIMonitor(data_file=self.test_file)
        self.assertEqual(len(new_monitor.usage_records), 1)


class TestFormatting(unittest.TestCase):
    """Test formatting functions"""

    def test_format_tokens(self):
        """Test token formatting"""
        self.assertEqual(format_tokens(500), "500")
        self.assertEqual(format_tokens(1500), "1.50K")
        self.assertEqual(format_tokens(1500000), "1.50M")
        self.assertEqual(format_tokens(10000000), "10.00M")

    def test_format_cost(self):
        """Test cost formatting"""
        self.assertEqual(format_cost(0.0005), "$0.000500")
        self.assertEqual(format_cost(1.5), "$1.5000")
        self.assertEqual(format_cost(100.25), "$100.2500")


class TestPricing(unittest.TestCase):
    """Test pricing constants"""

    def test_pricing_exists(self):
        """Test pricing data exists"""
        self.assertIsInstance(PRICING, dict)
        self.assertGreater(len(PRICING), 0)

    def test_pricing_format(self):
        """Test pricing data format"""
        for model, prices in PRICING.items():
            self.assertIn('input', prices)
            self.assertIn('output', prices)
            self.assertIsInstance(prices['input'], (int, float))
            self.assertIsInstance(prices['output'], (int, float))


if __name__ == '__main__':
    unittest.main(verbosity=2)
