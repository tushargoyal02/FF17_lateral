# fileObj = open("data.txt","r")

with open("data.txt","r") as fileObj:
    print( fileObj.readline()) 


print("outside the with statment")
 