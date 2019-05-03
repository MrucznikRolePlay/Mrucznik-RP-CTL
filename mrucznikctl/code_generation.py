import json
import os
from jinja2 import Environment, PackageLoader

from mrucznikctl.config import parameterVariablePrefixes, parameterSymbols

env = Environment(
    loader=PackageLoader('mrucznikctl', 'templates')
)

# --- entrypoint ---
def generate_code(args):
    with open('kick.json') as commandFile:
        commandJson = json.load(commandFile)
        prepareParameters(commandJson['parameters'])
        generate_command(commandJson)
    print('Komenda poprawnie wygenerowana')


# --- functions ---
def generate_command(data):
    command_name = data['name']

    env.get_template('command.pwn.jinja2').stream(data).dump('./{0}/{0}.pwn'.format(command_name))

    command_impl_path = './{0}/{0}_impl.pwn'.format(command_name)
    if not os.path.exists(command_impl_path):
        env.get_template('command_impl.pwn.jinja2').stream(data).dump(command_impl_path)


def generate_module(data):
    module_name = data['name']
    if not os.path.exists(module_name):
        env.get_template('module.def.jinja2').stream(data).dump('module.def')
        env.get_template('module.hwn.jinja2').stream(data).dump('module.hwn')
        env.get_template('module.pwn.jinja2').stream(data).dump('module.pwn')


def generate_modules_inc():
    print('generate command')


def generate_commands_inc():
    print('generate command')


def prepareParameters(parameters):
    for parameter in parameters:
        parameter['variable'] = generateParameterVariableName(parameter)
        parameter['symbol'] = generateParameterSymbol(parameter)


def generateParameterVariableName(parameter):
    paramPrefix = parameterVariablePrefixes.get(parameter['type'], '')
    if ('size' in parameter):
        return "{}{}[{}]".format(paramPrefix, parameter['name'], parameter['size'])
    return "{}{}".format(paramPrefix, parameter['name'])


def generateParameterSymbol(parameter):
    symbol = parameterSymbols[parameter['type']]
    if ('defaultValue' in parameter):
        symbol = '{}({})'.format(symbol.upper(), parameter['defaultValue'])
    if ('size' in parameter):
        symbol = '{}[{}]'.format(symbol, parameter['size'])
    return symbol