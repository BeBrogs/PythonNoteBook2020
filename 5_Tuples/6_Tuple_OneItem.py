#To create a tuple with only one item, you have add a comma after the item,
#If you don't add comma, you'll only have a variable

myTuple = ("Cheese",) #Comma == a tuple

notATuple = ("Cheese") #No comma == no tuple


print("\n"+str(myTuple) + " is of type: ")
print(type(myTuple))#Prints our datatype - tuple

print("\n"+str(notATuple) + "is of type: ")
print(type(notATuple)) #Prints our datatype - str


