fileObj = open("data2.txt","w+")

print( fileObj.tell() ,"Cursor position")

fileObj.write("123456")
print( fileObj.tell() ,"Cursor position after write")

fileObj.seek(2)
print( fileObj.tell() ,"Cursor position after read")

print(fileObj.read())

fileObj.close()
