# paoloctf

[![PyPI version](https://img.shields.io/pypi/v/paoloctf)](https://pypi.org/project/paoloctf/)
[![GitHub License](https://img.shields.io/github/license/PascalCTF/CTF-Tools)](LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/PascalCTF/CTF-Tools)](https://github.com/PascalCTF/CTF-Tools/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/PascalCTF/CTF-Tools)](https://github.com/PascalCTF/CTF-Tools/pulls)

## About

**paoloctf** is a command-line tool for creating and managing CTF challenges. It is designed for the [PascalCTF](https://github.com/PascalCTF) cybersecurity event and ensures compatibility with the [CTF-Checker](https://github.com/PascalCTF/CTF-Checker) validation tool.

## Installation

Install from PyPI:

```bash
pip install paoloctf
```

Install from source:

```bash
git clone https://github.com/PascalCTF/CTF-Tools.git
cd CTF-Tools
pip install -e .
```

### Optional Dependencies

For challenge checker functionality (pwntools, requests):

```bash
pip install paoloctf[checker]
```

## Usage

### Generate a New Challenge

Create a new CTF challenge directory structure:

```bash
paoloctf generate web
paoloctf generate pwn --name buffer_overflow
paoloctf gen crypto -n rsa_challenge
```

This creates a challenge directory with the following structure:

```
challenge/
├── attachments/        # Files to distribute to participants
├── src/                # Source code (not distributed)
├── writeup/            # Official writeup
├── checker/            # Automated flag checker
│   └── __main__.py
├── authors.txt         # Challenge authors
├── description.md      # Challenge description
├── endpoint.txt        # Connection details
├── flags.txt           # Challenge flags
├── order.txt           # Display order
├── points.txt          # Point value
├── tags.txt            # Category tags
├── timeout.txt         # Checker timeout
└── title.txt           # Challenge title
```

### Export Challenges to CSV

Parse CTF challenges into a CSV file for CTFd import:

```bash
paoloctf load ./challenges
paoloctf load ./challenges --output ctfd_import.csv
paoloctf export ./challenges -o export.csv
```

### Command Reference

```
paoloctf --help
paoloctf generate --help
paoloctf load --help
```

## Development

### Setup

```bash
git clone https://github.com/PascalCTF/CTF-Tools.git
cd CTF-Tools
pip install -e ".[dev]"
```

### Build

```bash
python -m build
```

### Publish

```bash
python -m twine upload dist/*
```

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome. Please submit a pull request or open an issue on GitHub.
