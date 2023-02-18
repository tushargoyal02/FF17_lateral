
#  x, a, w => in case the file doesn't exist

fileObj = open("data333.txt","a")

fileObj.seek(0)
print(fileObj.read(3))

fileObj.seek(5)
fileObj.write("$$")

fileObj.close()

