

def test():
    print("this is test functions")

# __name__  != __main__
print("Name of the name variable when we import::",__name__)

if __name__=="__main__":
    test()