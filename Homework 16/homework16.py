# Decorator for positive numbers

def positive_numbers(func):
    def wrapper(number):
        if number > 0: 
            result = func(number)
            print(result)
            return result
        else:
            raise ValueError("Please input positive number.")
    return wrapper

@positive_numbers
def return_number(number):
    return number

try:
    return_number(5)  
    return_number(-5)  
except ValueError as e:
    print(e)






# Functor for positive numbers

class PositiveNumbers:
    def __call__(self, number):
        if number > 0:
            return number
        else:
            raise ValueError("Please input positive number.")
        
positive_numbers = PositiveNumbers()

def return_number(number):
    result = positive_numbers(number)
    print(result)
    return result

try:
    return_number(5)
    return_number(-5)
except ValueError as e:
    print(e)






# Decorator for func time

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' took: {elapsed_time:.4f} seconds.")
        return result

    return wrapper


@timer
def example_function(n):
   return f"The sum is {sum(range(n))}"

print(example_function(123456))






# LoggingMeta

class LoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Creating class: {name}.")
        functions = [func for func in attrs if callable(attrs[func]) and not func.startswith('__')]
        print(f"Functions: {functions}.")
        return super().__new__(cls, name, bases, attrs)
    
class FirstClass(metaclass=LoggingMeta):
    def first_method(self):
        pass

    def second_method(self):
        pass


class SecondClass(metaclass=LoggingMeta):
    def method_one(self):
        pass

class ThirdClass(metaclass=LoggingMeta):
    def __init__(self) -> None:
        pass


first_instance = FirstClass()
second_instance = SecondClass()
third_instance = ThirdClass()


