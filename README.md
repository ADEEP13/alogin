# ALogin

![PyPI](https://img.shields.io/pypi/v/alogin)
![Python](https://img.shields.io/pypi/pyversions/alogin)
![License](https://img.shields.io/github/license/ADEEP13/alogin)
![GitHub last commit](https://img.shields.io/github/last-commit/ADEEP13/alogin)
![GitHub Repo stars](https://img.shields.io/github/stars/ADEEP13/alogin)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/alogin?period=total\&units=INTERNATIONAL_SYSTEM\&left_color=BLACK\&right_color=GREEN\&left_text=downloads)](https://pepy.tech/projects/alogin)
![GitHub release](https://img.shields.io/github/v/release/ADEEP13/alogin)

📖 **Documentation:** https://adeep13.github.io/alogin/

ALogin is a lightweight Python authentication library that provides simple account creation and login functionality using a local JSON database.

Perfect for:

* Learning projects
* Hackathons
* Small applications
* Rapid prototyping
* Beginner Python projects

---

## Installation

```bash
pip install alogin
```

---

## Quick Start

```python
from alogin import create_account, login_account

create_account()
login_account()
```

---

## Features

* User account creation
* Login authentication
* JSON-based local user database
* Duplicate email protection
* SHA-256 password hashing
* Simple CLI interface
* Lightweight and beginner-friendly
* Easy integration into Python projects

---

## Example

```python
from alogin import create_account, login_account

print("Create a new account")
create_account()

print("Login")
login_account()
```

---

## Documentation

Visit the documentation site for detailed usage instructions and examples:

https://adeep13.github.io/alogin/

---

## Version History

### v0.1.2

#### Fixes

* Fixed import issues in `__init__.py`
* Improved package exports

### v0.1.1

#### Improvements

* Exported `create_account()` and `login_account()` from the package root
* Simplified imports

```python
from alogin import create_account, login_account
```

### v0.1.0

#### Initial Release

* JSON-based local user database
* Login authentication system
* Password hashing using SHA-256
* Duplicate email protection

---

## Project Structure

```text
alogin/
├── alogin/
│   ├── __init__.py
│   └── core.py
├── docs/
├── tests/
├── CHANGELOG.md
├── LICENSE
└── README.md
```

---

## Contributing

Contributions, bug reports, feature requests, and suggestions are welcome.

You can:

* Open an Issue
* Start a Discussion
* Submit a Pull Request

Every contribution helps improve ALogin.

---

## Links

* GitHub Repository: https://github.com/ADEEP13/alogin
* Documentation: https://adeep13.github.io/alogin/
* PyPI Package: https://pypi.org/project/alogin/

---

## License

This project is licensed under the MIT License.
