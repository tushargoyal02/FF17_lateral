
#  file handling ?
# Logging => Module ( Logs )
#  read & write ( permanet)
#  Hard disk
#  output with the ( Flash / RAM )

# SQL -> Cursor
# open the file in memory  => file Object ( reference variable for the memory)
#  do operations
# closing the file

fileObj = open("data.txt","rb")

dataFile=fileObj.read()

fileObj.close()

print(dataFile)