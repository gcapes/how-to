# Decorators wrap a function to modify its behaviour.
# So when you decorate a function, you're passing it into a wrapper,
# which returns a reference to that modified function.

# The example below is designed to illustrate passing in arguments to
# both the function, and the decorator.

import functools


def use_cache(overwrite_cache=False):
    """Decorator function which modifies a load function, and (pretends to) cache(s) results.
    Once the cache has been made, subsequent loads will use the cached data,
    unless the user chooses to overwrite the cache using `overwrite_cache=True`"""
    def decorator(load_function):
        print("this is the decorator")
        # Keep the original 'identity' of the decorated function
        # This makes 'help' point to the correct docstring.
        @functools.wraps(load_function)
        def wrapper(*args, **kwargs):
            print("this is the wrapper")
            if overwrite_cache:
                data = load_function(*args, **kwargs)
                print("Saving result to cache")
                return data
            else:
                print("Using cached result")
                return "Cached fake news"
        return wrapper
    return decorator

# The '@' notation makes the function behave the same way each time it is called.
@use_cache(overwrite_cache=True)
def dummy_load_function(data_path):
    """Dummy function, which pretends to load some data"""
    print("Load function using @decorator syntax")
    print(f"Pretending to load data from {data_path}")
    data = "Fake news"
    return data

data = dummy_load_function("Some fake path")
print(data)

def other_dummy_load_function(data_path):
    """Dummy function, which pretends to load some data"""
    print("Other load function using decorator(option=something)(load_function)(arg) syntax")
    print(f"Pretending to load data from {data_path}")
    data = "Fake news"
    return data

# Using the decorator in the manner below allows you to define the value of the argument
# passed to the decorator at run-time, rather than when defining the function.
# Because decorators work by returning a reference to a function,
# rather than the result of calling it, we have to separate passing the function,
# and the arguments to the function.
data = use_cache(overwrite_cache=True)(other_dummy_load_function)("another made up path")
print(data)

data = use_cache(overwrite_cache=False)(other_dummy_load_function)("another made up path")
print(data)
