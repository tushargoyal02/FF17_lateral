fileObj = open("data2.txt","r+")


print( fileObj.tell() ,"Cursor position")


fileObj.write("------")
print(fileObj.tell(), "Cursor position after write")


fileObj.close()
