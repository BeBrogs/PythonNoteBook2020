#1. copy() method
#The built in list method 'copy()' allows you to make a copy of a whole list

myList = [0.25, "Hello, World!", 12, True, False]

myCopiedList = myList.copy()

print("\nPrinting our copied list... \n" + str(myCopiedList) + "\n")




#2. The list() method
#The list() method also allows us to make a copy of a list

myNewestList = list(myCopiedList)

print("\nLadies and Gentlemen!! \nI present to you... \nOUR NEWEST LIST! \n\n" +str(myNewestList))
