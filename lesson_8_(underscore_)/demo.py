import underscore_demo

print(underscore_demo._recipe)
print(underscore_demo.vat)


from underscore_demo import *

_customer # <-- This can because it add to __all__ variable
_recipe   # <-- This will be variable error (When Import with *)

