#Many ways to join two or more lists in python

myIntList = [0, 1, 2, 3, 4]

myFloatList = [0.0, 0.25, 0.50, 0.75, 1.00]

myJoinedList = myIntList + myFloatList

print("Our connected lists: \n" +str(myJoinedList) +"\n")





#We can add further arrays to our newest array - myJoinedList:
myFurtherStringsList = ["Hello", "World", "!"]


#Simply adding myFurtherStringsList elements to the already existing myJoinedList array
myJoinedList += myFurtherStringsList

print(myJoinedList)


mySimpleListBuilder = myIntList + myFloatList + myFurtherStringsList

print(mySimpleListBuilder)
