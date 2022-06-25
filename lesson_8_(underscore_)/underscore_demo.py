import random

# for _ in range(5):
#     print(random.randint(1,6))
    

_recipe = "a7b3c15" # private variable
vat = .07           # public variable
_customer = "Chell"

__all__ = ["_customer"]
class Alpha:
    @staticmethod
    def foo():
        print("Hello")
        