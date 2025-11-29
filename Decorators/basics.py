from functools import wraps;

# what is decorator?
# A decorator in Python is a callable (usually a function) that takes another function or class as input and returns a modified callable, letting you add or change behavior without editing the original code.
def my_decorator(func):

    # this preserves the metadata of the func.
    @wraps(func)
    def wrapper():
        print('Before')
        func()
        print('After')

    return wrapper

@my_decorator
def greet():
    print('HELLO');

greet();

# It will print the name of the wrapper function if we don't use @wraps.
print(greet.__name__);