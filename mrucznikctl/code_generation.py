import json
import os
from jinja2 import Environment, PackageLoader

from mrucznikctl.cd import cd
from mrucznikctl.config import parameterVariablePrefixes, parameterSymbols

env = Environment(
    loader=PackageLoader('mrucznikctl', 'templates'),
    autoescape=False
)


# --- entry point ---
def generate_code(args):
    if os.path.exists('modules'):
        with cd('modules'):
            generate_from_template('modules.pwn.jinja2', generate_modules(), 'modules.pwn', force=True)
        print('Moduły zostały poprawnie wygenerowane.')
    elif os.path.exists('module.json'):
        generate_module()
        print('Moduł został poprawnie wygenerowany.')
    elif os.path.exists('command.json'):
        generate_command()
        print('Komenda została poprawnie wygenerowana.')
    else:
        print('Nie znajdujesz się w katalogu z plikiem command.json lub module.json')


# --- functions ---
def generate_command():
    with open('command.json') as command_file:
        data = json.load(command_file)
        prepare_parameters(data['parameters'])
        command_name = data['name']

        # if os.path.exists('{0}.xd'.format(command_name)):
        #     with open('{0}.xd'.format(command_name)) as f:
        #         data['code'] = f.readlines()

        force = False if 'custom' in data else True
        generate_from_template('command.pwn.jinja2', data, '{0}.pwn'.format(command_name), force)
        generate_from_template('command_impl.pwn.jinja2', data, '{0}_impl.pwn'.format(command_name), True)
        return command_name


def generate_module():
    with open('module.json') as module_file:
        data = json.load(module_file)
        print('Generowanie plików modułu {}'.format(data['name']))

        generate_from_template('module.def.jinja2', data, '{}.def'.format(data['name']))
        generate_from_template('module.hwn.jinja2', data, '{}.hwn'.format(data['name']))
        generate_from_template('module.pwn.jinja2', data, '{}.pwn'.format(data['name']))

        if data['commands']:
            print('Generowanie komend:')
            commands = []
            with cd('commands'):
                for r, d, f in os.walk('.'):
                    if 'command.json' in f:
                        with cd(r):
                            commands.append(generate_command())
                generate_from_template('commands.pwn.jinja2', {'commands': commands}, 'commands.pwn', force=True)
        return data


def generate_modules():
    modules = []
    for r, d, f in os.walk('.'):
        if 'module.json' in f:
            with cd(r):
                modules.append(generate_module())
    return {'modules': modules}


def generate_modules_inc():
    modules = []
    for r, d, f in os.walk('.'):
        if 'module.json' in f:
            with cd(r):
                with open('module.json') as module_file:
                    data = json.load(module_file)
                    modules.append(data)
    generate_from_template('modules.pwn.jinja2', {'modules': modules}, 'modules.pwn', force=True)


def generate_commands_inc():
    commands = []
    for r, d, f in os.walk('.'):
        if 'module.json' in f:
            with cd(r):
                with open('module.json') as command_file:
                    data = json.load(command_file)
                    commands.append(data['name'])
    generate_from_template('commands.pwn.jinja2', {'commands': commands}, 'commands.pwn', force=True)


def prepare_parameters(parameters):
    for parameter in parameters:
        parameter['variable'] = generate_parameter_variable_name(parameter)
        parameter['symbol'] = generate_parameter_symbol(parameter)


def generate_parameter_variable_name(parameter):
    param_prefix = parameterVariablePrefixes.get(parameter['type'], '')
    if 'size' in parameter:
        return "{}{}[{}]".format(param_prefix, parameter['name'], parameter['size'])
    return "{}{}".format(param_prefix, parameter['name'])


def generate_parameter_symbol(parameter):
    symbol = parameterSymbols[parameter['type']]
    if 'defaultValue' in parameter:
        symbol = '{}({})'.format(symbol.upper(), parameter['defaultValue'])
    if 'size' in parameter:
        symbol = '{}[{}]'.format(symbol, parameter['size'])
    return symbol


def generate_from_template(template, data, target_file, force=False):
    if force or not os.path.exists(target_file):
        print('Generowanie pliku ' + target_file)
        env.get_template(template).stream(data).dump(target_file, encoding='windows-1250')
    else:
        print('Plik ' + target_file + ' jest już wygenerowany, pomijam.')
