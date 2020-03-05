myTuple = ("Did", "I", "Change", "?!")

print("Here's the current state of our Tuple:\n" + str(myTuple) +"\n")
mySearch = input("What word would you like to search for?\n")

if mySearch in myTuple:
    print ("\nThe word '" + str(mySearch) + "' Was found in the tuple: \n" + str(myTuple))

else:
    print("\nThe word '" + mySearch + "' Wasn't found in the tuple: \n" + str(myTuple))
