#
def Greeting(func):     
    def message():      

        print("We are inside message functions") 
        func()      

    return message   

@Greeting
def userWelcome():      
    print("hey user Welcome")



userWelcome()

# userWelcome=Greeting(userWelcome) 

