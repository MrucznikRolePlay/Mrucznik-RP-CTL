groups = [
    {'name': 'everyone'},
    {'name': 'admini'},
    {'name': 'frakcja_LSPD'},
    {'name': 'frakcja_FBI'},
    {'name': 'frakcja_SASP'},
    {'name': 'frakcja_LSMC'},
    {'name': 'frakcja_USSS'},
    {'name': 'frakcja_HA'},
    {'name': 'frakcja_SAN'},
    {'name': 'frakcja_KT'},
    {'name': 'frakcja_GOV'},
    {'name': 'frakcja_LSFD'}
]

parameterTypes = [
    'player',
    'integer',
    'hex',
    'string',
    'float',
    'character'
]

parameterSymbols = {
    'player': 'k<fix>',
    'integer': 'd',
    'hex': 'h',
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
