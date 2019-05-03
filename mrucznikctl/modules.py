import json
from PyInquirer import prompt

from mrucznikctl.code_generation import generate_module
from mrucznikctl.commands import create_command
from mrucznikctl.validators import NameValidator


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
            'message': 'Kto jest autorem modułu?'
        },
        {
            'type': 'confirm',
            'name': 'commands',
            'message': 'Czy chcesz dodać komendy do modułu?'
        }
    ]

    answers = prompt(questions)
    want_commands = answers.pop('commands')

    with open('module.json', 'w') as file:
        json.dump(answers, file, indent=4)

    print('Moduł pomyślnie utworzony jako plik module.json')
    print('Uruchamiam generator modułu...')
    generate_module(answers)

    if want_commands == True:
        answers['commands'] = []
        next = True
        while next:
            answers['commands'].append(create_command(args)['name'])
            next = prompt([{
                'type': 'confirm',
                'name': 'next',
                'message': 'Czy chcesz dodać kolejną komendę?'
            }])['next']