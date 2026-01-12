#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for openSquat.

This setup.py is provided for compatibility with older build systems.
The project uses pyproject.toml as the primary configuration file.
"""
from setuptools import setup, find_packages
import os

# Ler o README para usar como long_description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Ler a versão do __init__.py
def get_version():
    init_path = os.path.join(os.path.dirname(__file__), "opensquat", "__init__.py")
    if os.path.exists(init_path):
        with open(init_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("__VERSION__"):
                    return line.split("=")[1].strip().strip('"').strip("'")
    return "2.1.2"

setup(
    name="opensquat",
    version=get_version(),
    description="Domain squatting and phishing detection library",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    author="Andre Tenreiro",
    author_email="",
    url="https://github.com/atenreiro/opensquat",
    license="GPL-3.0",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    python_requires=">=3.8",
    install_requires=[
        "beautifulsoup4>=4.14.3",
        "colorama>=0.4.6",
        "confusable-homoglyphs>=3.3.1",
        "dnspython>=2.8.0",
        "homoglyphs>=2.0.4",
        "numpy>=2.4.1",
        "requests>=2.32.5",
        "strsimpy>=0.2.1",
    ],
    extras_require={
        "dev": [
            "black>=25.12.0",
            "codecov>=2.1.13",
            "coverage>=7.13.1",
            "flake8>=7.3.0",
            "packaging>=25.0",
            "pytest>=9.0.2",
            "pytest-cov>=7.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "opensquat=opensquat.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="domain-squatting, phishing, security, dns, certificate-transparency",
    project_urls={
        "Bug Reports": "https://github.com/atenreiro/opensquat/issues",
        "Source": "https://github.com/atenreiro/opensquat",
        "Documentation": "https://github.com/atenreiro/opensquat#readme",
    },
)