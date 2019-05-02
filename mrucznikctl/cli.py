from __future__ import print_function, unicode_literals
import os
import json
import re
from jinja2 import Environment, PackageLoader, select_autoescape
from argparse import ArgumentParser
from PyInquirer import prompt, print_json
from PyInquirer import Validator, ValidationError


def main(name, as_cowboy):
    """Command line tool for generating code for Mrucznik Role Play gamemode"""
    print('OK')
