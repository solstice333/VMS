# TooDamnMuchDammitError: exception to be raised when there's more than 1024 
# bits being set
class TooDamnMuchDammitError(AttributeError):
   def __str__(self):
      return "Error: Max is 1024 bits, thus 2**1024 - 1 is the max" 
