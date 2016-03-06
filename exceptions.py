# TooDamnMuchDammitError: exception to be raised when there's more than 1024 
# bits being set


class TooDamnMuchDammitError(AttributeError):
    def __str__(self):
        return "Error: Max is 1024 bits, thus 2**1024 - 1 is the max"


class IsNotNumericalValue(AttributeError):
    def __str__(self):
        return "Error: Value is not a numeric"


class ValueTooLarge(AttributeError):
    def __str__(self):
        return "Error: Value is too large"

class PFError(IndexError):
    def __str__(self):
        return "Error: Found -1"

class IsNotStringValue(AttributeError):
    def __str__(self):
        return "Error: Value is not type String"

class ZeroError(AttributeError):
    def __str__(self):
        return "Error: Zero Error"
