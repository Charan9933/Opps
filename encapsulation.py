class MyClass:
    def __init__(self):
        self._private_var = 42 # Private variable denoted by a single underscore
        self.public_var = 43 # Public variable

    def _private_method(self): # Private method denoted by a single underscore
        print("This is a private method")

    def public_method(self):
        print("This is a public method")
        self._private_method() # Private method can be accessed within the class

obj = MyClass()
print(obj.public_var) # Access public variable outside class
# print(obj._private_var) # Error: Cannot access private variable outside class
obj.public_method() # Access public method outside class
# obj._private_method() # Error: Cannot access private method outside class
