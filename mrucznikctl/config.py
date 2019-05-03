groups = [
    {'name': 'everyone'},
    {'name': 'admin'},
    {'name': 'lspd'}
]

parameterTypes = [
    'player',
    'integer',
    'string',
    'float',
    'character'
]

parameterSymbols = {
    'player': 'r',
    'integer': 'd',
    'string': 's',
    'float': 'f',
    'character': 'c'
}

parameterVariablePrefixes = {
    'float': 'Float:'
}

parameterDefaultNames = {
    'player': 'giveplayerid'
}

parameterDefaultDescriptions = {
    'player': 'Nick/ID'
}


def get_default_parameter_name(param):
    return parameterDefaultNames.get(param, '')


def get_default_parameter_description(param):
    return parameterDefaultDescriptions.get(param, '')
