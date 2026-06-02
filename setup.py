#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for APIMonitor-CLI
"""

from setuptools import setup, find_packages
import os

# Read README
def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8') as f:
        return f.read()

setup(
    name="apimonitor-cli",
    version="1.0.0",
    author="gitstq",
    author_email="",
    description="🛠️ LLM API Usage Tracker & Cost Analysis Engine - 零依赖跨平台API用量监控工具",
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url="https://github.com/gitstq/APIMonitor-CLI",
    project_urls={
        "Bug Tracker": "https://github.com/gitstq/APIMonitor-CLI/issues",
        "Documentation": "https://github.com/gitstq/APIMonitor-CLI#readme",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Monitoring",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=find_packages(),
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'apimonitor=cli:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
