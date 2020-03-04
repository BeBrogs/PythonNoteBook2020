#There are two methods in order to add new items to our list:

#Method 1: The append() method

print("\nTo add an item to the end of the list, use the append() method: \n")

myBreakfast  = ["Bread", "Eggs", "Cereal"]

myBreakfast.append("Milk")

print(myBreakfast)



print("\n\n" + "To add to a specified index position, use the insert() method:")

myLunch = ["Subway", "Protein Milk", "Coffee"]


#I want to add water to position 2 (index pos 1) in the myLunch array
myLunch.insert(1, "Water")


print("\n" + str(myLunch) + "\n")


