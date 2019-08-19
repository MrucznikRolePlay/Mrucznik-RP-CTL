import regex
import os
from PyInquirer import Validator, ValidationError


class NameValidator(Validator):
    def validate(self, document):
        ok = regex.match('^[a-z_]*$', document.text)
        if not ok:
            raise ValidationError(
                message='Nazwa musi zawierać tylko małe litery oraz "_"',
                cursor_position=len(document.text))


class ComponentNameValidator(Validator):
    def validate(self, document):
        ok = regex.match('^[a-z_]*$', document.text)
        if not ok:
            raise ValidationError(
                message='Nazwa musi zawierać tylko małe litery oraz "_"',
                cursor_position=len(document.text))
        if os.path.exists(document.text):
            raise ValidationError(
                message='Taki katalog już istnieje, wybierz inną nazwę.',
                cursor_position=len(document.text))


class VariableValidator(Validator):
    def validate(self, document):
        ok = regex.match('^[a-z]+((\d)|([A-Z0-9][a-z0-9]+))*([A-Z])?$', document.text)
        if not ok:
            raise ValidationError(
                message='Nazwa zmiennej musi być w formacie camelCase',
                cursor_position=len(document.text))
