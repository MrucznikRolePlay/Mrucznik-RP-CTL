groups = [
    {'name': 'everyone'},
    {'name': 'admin'},
    {'name': 'frakcja'},
    {'name': 'rcon'}
]

fractions = [
    {'name': 'Los Santos Police Department'},
    {'name': 'Federal Bureau of Investigation'},
    {'name': 'San Andreas Sherrifs Department'},
    {'name': 'Emergency Rescue Service'},
    {'name': 'SA Bahamas'},
    {'name': 'Yakuza'},
    {'name': 'Government Security Agency'},
    {'name': 'Hitman Agency'},
    {'name': 'San News'},
    {'name': 'Korporacja Transportowa'},
    {'name': 'Urząd Stanu San Andreas'},
    {'name': 'Grove Street Families'},
    {'name': '187 North Park Avenue'},
    {'name': 'Hillside Nortenos 14'},
    {'name': 'Nightmare of Adrenalin'},
    {'name': 'IV Saint Reich'}
]

fraction_ids = {
    "Los Santos Police Department": 1,
    "Federal Bureau of Investigation": 2,
    "San Andreas Sherrifs Department": 3,
    "Emergency Rescue Service": 4,
    "SA Bahamas": 5,
    "Yakuza": 6,
    "Government Security Agency": 7,
    "Hitman Agency": 8,
    "San News": 9,
    "Korporacja Transportowa": 10,
    "Urząd Stanu San Andreas": 11,
    "Grove Street Families": 12,
    "187 North Park Avenue": 13,
    "Hillside Nortenos 14": 14,
    "Nightmare of Adrenalin": 15,
    "IV Saint Reich": 16
}

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
