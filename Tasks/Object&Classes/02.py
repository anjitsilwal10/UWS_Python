# Magic Methods/ Dunder Methods 
''' -> Magic methods are special methods that Python calls automatically in certain situations. They always start and end with double underscores, like __init__, __str__, and __repr__. These methods allow us to customize the behavior of objects in a class, making them more powerful and user-friendly.
Here are a few important magic methods:
- __init__ → Initializes an object when created.
- __str__ → Defines how an object is printed (print(obj)).
- __repr__ → Used for debugging; returns an official string representation.
- __add__ → Defines how objects handle + (addition).
- __eq__ → Controls equality checks (==).
- __len__ → Returns the length of an object.
Magic methods are a core part of Python’s object-oriented programming!
'''
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'Name:{self.name}, Age:{self.age}';

    def __repr__(self):
        return f'Person:{self.name}, Age:{self.name}';

p = person('Alice',30);  # uses __str__
print(p);

as10 = person('Anjit',26);

print(repr(p))  # Uses __repr__

print(as10.age);