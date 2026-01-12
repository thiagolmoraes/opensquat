<p align="center">
  <img src="https://raw.githubusercontent.com/atenreiro/opensquat/master/screenshots/openSquat_logo.png" alt="openSquat Logo" width="400"/>
</p>

<h1 align="center">openSquat</h1>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/python-3.11+-blue.svg" alt="Python 3.11+"></a>
  <a href="https://github.com/atenreiro/opensquat/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="License: GPL v3"></a>
  <a href="https://github.com/atenreiro/opensquat/issues"><img src="https://img.shields.io/github/issues/atenreiro/opensquat" alt="GitHub issues"></a>
  <a href="https://github.com/atenreiro/opensquat/stargazers"><img src="https://img.shields.io/github/stars/atenreiro/opensquat" alt="GitHub stars"></a>
</p>

---

## 📑 Table of Contents

- [What is openSquat?](#-what-is-opensquat)
- [Key Features](#-key-features)
- [Quick Start](#-quick-start)
- [Requirements](#-requirements)
- [Usage](#-usage)
- [Configuration](#%EF%B8%8F-configuration)
- [Automation](#-automation)
- [Integrations](#-integrations)
- [CLI Reference](#-cli-reference)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

---

## 🎯 What is openSquat?

openSquat is an **Open Source Intelligence (OSINT)** security tool that identifies cyber squatting threats targeting your brand or domains:

| Threat Type | Description |
|-------------|-------------|
| 🎣 **Phishing** | Fraudulent domains mimicking your brand |
| 🔤 **Typosquatting** | Domains with common typos (e.g., `gooogle.com`) |
| 🌐 **IDN Homograph** | Look-alike characters from other alphabets |
| 👥 **Doppelgänger** | Domains containing your brand name |
| 🔀 **Bitsquatting** | Single-bit errors in domain names |

## ✨ Key Features

- 📅 **Daily NRD feeds** — Automatic newly registered domain updates
- 🔍 **Similarity detection** — Levenshtein & Jaro-Winkler algorithms
- 🛡️ **VirusTotal integration** — Check domain reputation
- 🌐 **Quad9 DNS validation** — Identify malicious domains
- 📜 **Certificate Transparency** — Monitor SSL/TLS certificates
- 📊 **Multiple output formats** — TXT, JSON, CSV

---

## 🚀 Quick Start

### Option 1: Using Docker (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/atenreiro/opensquat
cd opensquat

# 2. Build the Docker image
docker build -t opensquat:latest .

# 3. Run with your keywords
docker run --rm \
  -v $(pwd)/results:/app/results \
  -v $(pwd)/examples:/app/examples \
  opensquat -k examples/keywords.txt -o results/output.txt
```

### Option 2: Using uv 

```bash
# 1. Clone the repository
git clone https://github.com/atenreiro/opensquat
cd opensquat

# 2. Install using uv
uv sync

# 3. Run with your keywords
uv run opensquat -k examples/keywords.txt -o results.txt
```

### Option 3: Using pip

```bash
# 1. Clone the repository
git clone https://github.com/atenreiro/opensquat
cd opensquat

# 2. Install the package
pip install -e .

# 3. Run with your keywords
opensquat -k examples/keywords.txt -o results.txt
```

### Option 4: Using setup.py

```bash
# 1. Clone the repository
git clone https://github.com/atenreiro/opensquat
cd opensquat

# 2. Install using setup.py
python setup.py install

# 3. Run with your keywords
opensquat -k examples/keywords.txt -o results.txt
```

---

## 📦 Requirements

- **Python 3.11+** (required for numpy 2.4.1+)
- Dependencies: See `pyproject.toml` for full list
- Optional: Docker for containerized deployment

---

## 📖 Usage

### Basic Commands

```bash
# Show help
opensquat -h

# Default run (uses keywords.txt)
opensquat

# Use custom keywords file
opensquat -k my_keywords.txt

# Specify output file
opensquat -k keywords.txt -o results.txt
```

### Validation Options

```bash
# DNS validation via Quad9
opensquat -k keywords.txt --dns

# Check Certificate Transparency logs
opensquat -k keywords.txt --ct

# Scan for open ports (80/443)
opensquat -k keywords.txt --portcheck

# Cross-reference phishing databases
opensquat -k keywords.txt --phishing results.txt

# VirusTotal validation
opensquat -k keywords.txt --vt

# Search for subdomains
opensquat -k keywords.txt --subdomains
```

### Output Formats

```bash
# Save as JSON
opensquat -k keywords.txt -o results.json -t json

# Save as CSV
opensquat -k keywords.txt -o results.csv -t csv

# Save as TXT (default)
opensquat -k keywords.txt -o results.txt -t txt
```

### Using as a Python Library

```python
from opensquat import Domain, Phishing, VirusTotal

# Detect domain squatting
domain_checker = Domain()
results = domain_checker.main(
    keywords_file="keywords.txt",
    confidence_level=1,
    domains_file="",
    method="Levenshtein",
    dns=False
)

# Check phishing sites
phishing_checker = Phishing()
phishing_results = phishing_checker.main("paypal")
```

### Confidence Levels

| Level | Flag | Description |
|-------|------|-------------|
| 0 | `-c 0` | Very high (fewer results, high accuracy) |
| 1 | `-c 1` | High (default) |
| 2 | `-c 2` | Medium |
| 3 | `-c 3` | Low |
| 4 | `-c 4` | Very low (more results, more false positives) |

---

## ⚙️ Configuration

### Keywords File (`keywords.txt`)

```text
# Lines starting with # are comments
mycompany
mybrand
myproduct
```

### VirusTotal API Key (`vt_key.txt`)

To use `--vt` or `--subdomains`, add your API key:
```text
# Get your free API key at https://www.virustotal.com
your_api_key_here
```

---

## 🤖 Automation

Run daily via crontab:

```bash
# Every day at 8 AM (feeds update ~7:30 AM UTC)
# Using installed CLI
0 8 * * * /path/to/venv/bin/opensquat -k keywords.txt -o results.json -t json

# Or using Docker
0 8 * * * docker run --rm -v /path/to/results:/app/results opensquat -k keywords.txt -o results.json -t json
```

---

## 🔗 Integrations

| Platform | Link |
|----------|------|
| 🤖 Telegram Bot | [@opensquat_bot](https://telegram.me/opensquat_bot) |
| 🔌 REST API | [RapidAPI](https://rapidapi.com/atenreiro/api/opensquat1) |

---

## 📋 CLI Reference

| Argument | Default | Description |
|----------|---------|-------------|
| `-k, --keywords` | `keywords.txt` | Keywords file to search |
| `-o, --output` | `results.txt` | Output filename |
| `-t, --type` | `txt` | Output format: `txt`, `json`, `csv` |
| `-c, --confidence` | `1` | Confidence level (0-4) |
| `-d, --domains` | — | Use local domain file instead of downloading |
| `-m, --method` | `Levenshtein` | Algorithm: `Levenshtein` or `JaroWinkler` |
| `--dns` | — | Enable Quad9 DNS validation |
| `--ct` | — | Search Certificate Transparency logs |
| `--phishing` | — | Cross-reference phishing database |
| `--subdomains` | — | Fetch subdomains via VirusTotal |
| `--portcheck` | — | Check for open ports 80/443 |
| `--vt` | — | Validate against VirusTotal |

---

## 🤝 Contributing

We welcome contributions! See our [Contributing Guide](CONTRIBUTING.md) for details.

- 🐛 **Report bugs** via [GitHub Issues](https://github.com/atenreiro/opensquat/issues)
- 💡 **Request features** by opening an issue
- 🔧 **Submit PRs** for bug fixes or enhancements

---

## 👤 Author

**Andre Tenreiro** — [LinkedIn](https://www.linkedin.com/in/andretenreiro/) · [PGP Key](https://mail-api.proton.me/pks/lookup?op=get&search=andre@opensquat.com)

---

## 📜 License

This project is licensed under the [GNU GPL v3](LICENSE).
