![Logo](logo.png)

Command line tool for generating code for Mrucznik Role Play gamemode


# Installation

Simply run:

    $ pip install --editable .


# Usage

To use it:

    $ mrucznikctl --help

### Examples:
- Generate code
    `$ mrucznikctl build`
- Create module
    `$ mrucznikctl create module`
- Create command
    `$ mrucznikctl create command`
- Create command & build
    `$ mrucznikctl create command --build`

### Tips
- Create commands in `[module name]/commands` directory
- Create modules in `modules` directory

If you use Python 3.10 and you have error like:
```
ImportError: cannot import name 'Mapping' from 'collections' (/usr/lib/python3.10/collections/__init__.py)
```
Go to venv/lib/python3.10/site-packages/prompt_toolkit/styles/from_dict.py and replace
```python
from collections import Mapping
```
with
```python
try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping
```

