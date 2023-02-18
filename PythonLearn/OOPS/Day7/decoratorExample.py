
#  func=userWelcome

#
def Greeting(func):     # STEP2  , func=userWelcome
    def message():      #STEP3 declare the functions 

        print("We are inside message functions")  #STEP 7 <= calling function
        func()      #step 8  func=useWelcome

    return message    # STEP4 => return object of messge() function

def userWelcome():      #Step 9 where I called it
    print("hey user Welcome")



userWelcome=Greeting(userWelcome)  #step1   Greeting functions  , object refernece of userWelcome
#  step5  userWelcome got object reference of message function()

userWelcome()  #step6  => where x=message   x() function is going to called

