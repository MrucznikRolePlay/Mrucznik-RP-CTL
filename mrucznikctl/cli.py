#!/usr/bin/python
# coding=<utf-8>

from argparse import ArgumentParser

from mrucznikctl.code_generation import generate_code
from mrucznikctl.commands import create_command
from mrucznikctl.modules import create_module


def main():
    """Command line tool for generating code for Mrucznik Role Play gamemode"""
    # create the top-level parser
    parser = ArgumentParser(prog='mrucznikctl',
                            description="Narzędzie do generowania kodu dla gamemodu Mrucznik Role Play")
    subparsers = parser.add_subparsers(title='Dostępne opcje:', metavar='opcja', required=True)

    # --- create ---
    opcja_create = subparsers.add_parser('create', description='Tworzenie komponentów mapy.',
                                         help='- tworzenie komponentów mapy')
    subparser_create = opcja_create.add_subparsers(title='Dostępne komponenty', metavar='komponenty', required=True)
    # options
    parser_create_module = subparser_create.add_parser('module', help='- tworzy moduł')
    parser_create_module.set_defaults(func=create_module)
    parser_create_module.add_argument('--build', dest='build', action='store_true',
                                      help='czy od razu budować moduł?', default=False)

    parser_create_command = subparser_create.add_parser('command', help='- tworzy nową komendę')
    parser_create_command.set_defaults(func=create_command)
    parser_create_command.add_argument('--build', dest='build', action='store_true',
                                       help='czy od razu budować komendę?', default=False)

    # --- build ---
    parser_build = subparsers.add_parser('build', description='Generuje kod na podstawie plików json.',
                                         help='- generowanie kodu')
    parser_build.set_defaults(func=generate_code)

    # parse arguments
    args = parser.parse_args()
    args.func(args)

# struktura mapy mrucznika
# legenda:
# A - kod generowany automatycznie
# T - szablon
# Mrucznik-RP.pwn
# - modules
#   - modules.pwn A
#   - przykładowy_moduł
#       - module .json
#       - przykładowy_moduł.def T
#       - przykładowy_moduł.hwn T
#       - przykładowy_moduł.pwn T
#       - commands
#           - commands.pwn A
#           - przykładowa komenda
#               - command.json
#               - command.pwn A
#               - command_impl.pwn T
#       - dialogs

# ------- builder -------
# na podstawie jsona generuje 2 pliki:
# command = nazwa komendy
# - command.pwn - wygenerowany kod z
#   - include "command_impl.pwn";
#   - command_Init() - do zainicjowania uprawnień komendy i aliasów
#   - command_PlayerInit() - opcjonalnie
#   - YCMD:command - zawierająca pobieranie parametrów przez sscanf
#   oraz zawierającą wywołanie funkcji z pliku command_impl.pwn oraz wszelkie komunikaty itd.
# - command_impl.pwn - wygenerowana funkcja command_run(playerid, parametry)

# generator modułów dodatkowo dodaje:
# module.pwn
# - includowanie wszystkich komend modułu
# - module_Init() zawierającą wywołanie wszystkich funkcji command_Init()
# - module_PlayerInit() zawierającą wywołanie wszystkich funkcji command_PlayerInit()
# - plik module_impl.pwn gdzie zawarty jest kod własnoręcznie napisany

# łącznik modulów dodaje:
# modules.pwn
# - includowanie wszystkich modułów
# - modules_Init() zawierającą wywołanie wszystkich funkcji module_Init()
# - modules_PlayerInit() zawierającą wywołanie wszystkich funkcji module_PlayerInit()

# TODO: Problem z polskimi znakami w generowanych plikach JSON
