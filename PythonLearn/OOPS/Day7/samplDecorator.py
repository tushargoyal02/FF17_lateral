import functools

def decorator_function( func ):
    
    @functools.wraps(func)
    def wrapper_function():
        print("We are inside wrapper")
        func()
    return wrapper_function


@decorator_function
def function_to_decorate():
    """
        this is docstring for the funcion_to_decorate
    """
    print("We need to modify the functions")

@decorator_function
def test():
    print("We are inside test function")


# function_to_decorate()

print(function_to_decorate.__name__)
print(function_to_decorate.__doc__)


# test()
# print("Doc of test",test.__doc__)
# # print(function_to_decorate)
