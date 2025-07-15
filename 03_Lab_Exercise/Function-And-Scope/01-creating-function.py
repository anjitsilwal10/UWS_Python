def greet_user():    #function defifniton ends with : colon
    print('hello world!')


"""Function Parameters
- Functions can take parameters, which can be passed into functions when it is called. 
- Before using parameter in a function, you need to define them in the function. 
"""
def greet_user(name):
    print(f'hello {name}!')

greet_user('Golay Molay')

"""Function And Parameter
- In function, we use the term "parameter" and "argument", they both mean the same.
- There is difference between data passed and used by the function.
    - Parameter is varibale listed inside the parenthesis in the function definition, which is used in the function's 
    body
    - An argument is the valued we pass to the function when we call it.

"""

def greet_user(first_name, last_name):   #two parameter
    print(f'hello {first_name} {last_name}!')

    # Now when we call this function, it is important to pass the parameter in correct order and correct number 
    # of parameters

greet_user('Samip','Parajuli')

