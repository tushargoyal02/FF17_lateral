



def decorator_function( func ):
    
    def wrapper_function(*args,**kwargs):
        
        func(*args,**kwargs)
    return wrapper_function


@decorator_function
def function_to_decorate(num1):
    print("We need to modify the functions",num1)

@decorator_function
def test():
    print("No argument in test function")

function_to_decorate(30)

test()