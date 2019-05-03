import regex
from PyInquirer import Validator, ValidationError

class NameValidator(Validator):
    def validate(self, document):
        ok = regex.match('^[a-z_]*$', document.text)
        if not ok:
            raise ValidationError(
                message='Nazwa musi zawierać tylko małe litery oraz "_"',
                cursor_position=len(document.text))


class VariableValidator(Validator):
    def validate(self, document):
        ok = regex.match('^[a-z0-9_]*$', document.text)
        if not ok:
            raise ValidationError(
                message='Nazwa zmiennej musi być w formacie camelCase',
                cursor_position=len(document.text))