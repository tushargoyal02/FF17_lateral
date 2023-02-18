def userInfo(name, email,userList=[]):
    print(name,email)
    userList.append(name)

    return {"name":name,
            "email":email,
            "userList":userList

    }

u1= userInfo("tushar","tushar@gmail.com")
u2= userInfo("aman","aman@gmail.com")


print(u2)
