#Checking if a value already in our array

thisList = ["Follow", "The", "Flow", "Bro"]


#To determine if "FLow" already exists in our list:
mySearchingString=input("Enter the string you want to search for: ")


if mySearchingString in thisList:
    print(mySearchingString + " already exists in our list")

else:
    print(mySearchingString + " doensn't exist in our list")

