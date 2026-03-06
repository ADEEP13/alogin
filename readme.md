# ALogin

![PyPI](https://img.shields.io/pypi/v/alogin)
![Python](https://img.shields.io/pypi/pyversions/alogin)
![License](https://img.shields.io/github/license/adeep13/alogin)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/alogin?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/alogin)


ALogin is a lightweight CLI-based authentication helper for Python.
It provides simple account creation and login functionality for small projects, prototypes, and hackathon demos.

---

## Installation

pip install alogin

---

## Usage

```python
from alogin import create_account, login_account

create_account()
login_account()
```

---

## Features

* Account creation
* Login authentication
* JSON-based local user database
* Duplicate email protection
* Password hashing using SHA256
* Simple CLI interface

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

## Version

### v0.1.2

Fixes:

* Resolved bugs in `__init__.py`

---

### v0.1.1

Improvements:

* Exported both `create_account()` and `login_account()` from the package
* Cleaner import style:

```python
from alogin import create_account, login_account
```

---

### v0.1.0

Initial authentication system release with:

* JSON-based user database
* Login authentication system
* Password hashing
* Duplicate email protection

---

## License

MIT License

