import json
import os
import getpass
import datetime
from PyInquirer import prompt

from mrucznikctl.code_generation import generate_module
from mrucznikctl.commands import create_command
from mrucznikctl.validators import NameValidator


# --- entry point ---
def create_module(args):
    print('Witaj w narzędziu tworzącym moduł mapy Mrucznik Role Play')

    questions = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Jak ma nazywać się moduł?',
            'validate': NameValidator
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
            'name': 'commands',
            'message': 'Czy chcesz dodać komendy do modułu?'
        }
    ]

    answers = prompt(questions)
    answers['date'] = datetime.datetime.now().strftime("%d.%m.%Y")

    with open('module.json', 'w') as file:
        json.dump(answers, file, indent=4)
        print('Moduł pomyślnie utworzony jako plik module.json')

    if answers.pop('commands'):
        if not os.path.exists('commands'):
            os.mkdir('commands')

        os.chdir('commands')
        next_element = True
        while next_element:
            create_command(args)
            next_element = prompt([{
                'type': 'confirm',
                'name': 'next',
                'message': 'Czy chcesz dodać kolejną komendę?'
            }])['next']
        print('Pomyślnie utworzono pliki konfiguracyjne komendy')

    print('Uruchamiam generator modułu...')
    generate_module('module.json')
    print('Gotowe. Możesz zacząć skrypcić ;)')
