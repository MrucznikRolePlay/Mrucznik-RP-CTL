import os
import json
from PyInquirer import prompt

from mrucznikctl.config import groups, parameterTypes, getDefaultParameterDescription, getDefaultParameterName
from mrucznikctl.validators import NameValidator, VariableValidator


def create_command(args):
    print('Witaj w narzędziu tworzącym komendę dla mapy Mrucznik Role Play')

    command = command_creator()

    if not os.path.exists(command['name']):
        os.mkdir(command['name'])

    commandName = '{0}/{0}.json'.format(command['name'])
    with open(commandName, 'w') as file:
        json.dump(command, file, indent=4)
    print('Komenda pomyślnie utworzona jako plik {}'.format(commandName))

    return command


def command_creator():
    questions = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Jak ma nazywać się komenda?',
            'validate': NameValidator
        },
        {
            'type': 'input',
            'name': 'description',
            'message': 'Wpisz opis komendy, który będzie widoczny dla graczy:',
        },
        {
            'type': 'checkbox',
            'name': 'permissions',
            'message': 'Wybierz, które grupy mają mieć dostęp do komendy:',
            'choices': groups
        },
        {
            'type': 'input',
            'name': 'author',
            'message': 'Kto jest autorem komendy?'
        },
        {
            'type': 'confirm',
            'name': 'aliases',
            'message': 'Czy komenda będzie miała dodatkowe aliasy?'
        }
    ]

    answers = prompt(questions)

    if (answers['aliases'] == True):
        answers['aliases'] = command_aliases()
    else:
        answers['aliases'] = []

    answers.update(prompt([
        {
            'type': 'confirm',
            'name': 'parameters',
            'message': 'Czy komenda będzie posiadała parametry?'
        }])
    )

    if (answers['parameters'] == True):
        answers['parameters'] = command_parameters()
    else:
        answers['parameters'] = []

    return answers


def command_aliases():
    aliases = []
    next = True
    while next:
        questions = [
            {
                'type': 'input',
                'name': 'alias',
                'message': 'Wpisz alias:',
                'validate': NameValidator
            },
            {
                'type': 'confirm',
                'name': 'next',
                'message': 'Dodać następny alias?'
            }
        ]
        answers = prompt(questions)
        next = answers.pop('next')
        aliases.append(answers['alias'])

    return aliases


def command_parameters():
    parameters = []
    next = True
    while next:
        answers = prompt(
            {
                'type': 'list',
                'name': 'type',
                'message': 'Wybierz typ parametru:',
                'choices': parameterTypes
            }
        )

        questions = []
        if answers['type'] == 'string':
            questions.append(
                {
                    'type': 'input',
                    'name': 'size',
                    'message': 'Wpisz rozmiar ciągu znaków:',
                    'default': getDefaultParameterDescription(answers['type'])
                }
            )

        questions.append(
            {
                'type': 'input',
                'name': 'name',
                'message': 'Wpisz nazwę parametru:',
                'default': getDefaultParameterName(answers['type']),
                'validate': VariableValidator
            }
        )
        questions.append(
            {
                'type': 'input',
                'name': 'description',
                'message': 'Wpisz opis parametru:',
                'default': getDefaultParameterDescription(answers['type'])
            }
        )
        questions.append(
            {
                'type': 'confirm',
                'name': 'default',
                'message': 'Czy parametr powinien mieć wartość domyślną?',
            }
        )

        answers.update(prompt(questions))

        if (answers.pop('default') == True):
            answers.update(prompt([
                {
                    'type': 'input',
                    'name': 'defaultValue',
                    'message': 'Wpisz wartość domyślną:'
                }
            ]))

        answers.update(prompt([
            {
                'type': 'confirm',
                'name': 'next',
                'message': 'Dodać następny parametr?'
            }
        ]))
        next = answers.pop('next')
        parameters.append(answers)

    return parameters