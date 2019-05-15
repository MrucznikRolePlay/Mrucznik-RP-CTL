import json
import os
import getpass
import datetime
from PyInquirer import prompt

from mrucznikctl.cd import cd
from mrucznikctl.code_generation import generate_module, generate_modules_inc
from mrucznikctl.commands import create_command
from mrucznikctl.validators import ComponentNameValidator


# --- entry point ---
def create_module(args):
    print('Witaj w narzędziu tworzącym moduł mapy Mrucznik Role Play')

    questions = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Jak ma nazywać się moduł?',
            'validate': ComponentNameValidator
        },
        {
            'type': 'input',
            'name': 'description',
            'message': 'Uzupełnij opis modułu:',
        },
        {
            'type': 'input',
            'name': 'author',
            'message': 'Kto jest autorem modułu?',
            'default': getpass.getuser()
        },
        {
            'type': 'confirm',
            'name': 'timers',
            'message': 'Czy moduł będzie posiadał timery?'
        },
        {
            'type': 'confirm',
            'name': 'callbacks',
            'message': 'Czy moduł posiadał callbacki?'
        },
        {
            'type': 'confirm',
            'name': 'mysql',
            'message': 'Czy moduł będzie korzystał z mysql?'
        },
        {
            'type': 'confirm',
            'name': 'files',
            'message': 'Czy moduł będzie posiadał dodatkowe pliki?'
        },
        {
            'type': 'confirm',
            'name': 'commands',
            'message': 'Czy chcesz dodać komendy do modułu?'
        }
    ]

    answers = prompt(questions)
    answers['date'] = datetime.datetime.now().strftime("%d.%m.%Y")

    os.mkdir(answers['name'])
    with cd(answers['name']):
        with open('module.json', 'w') as file:
            json.dump(answers, file, indent=4, ensure_ascii=False)
            print('Moduł pomyślnie utworzony jako plik module.json')

        files = []
        if answers.pop('files'):
            next_element = True
            while next_element:
                files.append(prompt([{
                    'type': 'input',
                    'name': 'file',
                    'message': 'Wpisz nazwę dodatkowego pliku razem z rozszerzeniem:'
                }])['file'])
                next_element = prompt([{
                    'type': 'confirm',
                    'name': 'next',
                    'message': 'Czy chcesz dodać kolejny plik?'
                }])['next']
        answers['files'] = files

        if answers.pop('commands'):
            os.mkdir('commands')
            with cd('commands'):
                next_element = True
                while next_element:
                    create_command(args)
                    next_element = prompt([{
                        'type': 'confirm',
                        'name': 'next',
                        'message': 'Czy chcesz dodać kolejną komendę?'
                    }])['next']
                print('Pomyślnie utworzono pliki konfiguracyjne komendy')

        if args.build:
            print('Uruchamiam generator modułu...')
            generate_module()

    if args.build:
        print('Generowanie modules.pwn')
        generate_modules_inc()
    print('Gotowe. Możesz zacząć skrypcić ;)')
