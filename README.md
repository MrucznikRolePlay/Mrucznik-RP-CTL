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
- Create commands in `\[module name\]/commands` directory
- Create modules in modules directory
