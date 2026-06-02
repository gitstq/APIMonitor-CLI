#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLI Entry Point - APIMonitor-CLI
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.apimonitor import main

if __name__ == '__main__':
    main()
