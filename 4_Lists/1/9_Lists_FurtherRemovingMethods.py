#We have a few more methods for removing items in our list:


#1. pop()

#The pop method removes the specified index when we give it one
#If we haven't given our method our an index value, it simply POPs OUT
#the last item in our list:


myList = [0.25, "Hello, World!", 12, True, False]
print("Original list:\n" + str(myList))


#AN OPTIONAL array to store popped values
myPopped =[]

myPopped = myList.pop(0) #Remove index 0 from orig array & store return here

print ("\nList after we have popped index 0" + str(myList))

print("\nNow our myPopped list contains: \n" +str(myPopped))





#2. del()

#The del() metho works similarly to the pop() method
#- but we won't store the deleted list element anywhere

myList1 =  [0.25, "Hello, World!", 12, True, False]

del myList1[4]

print("\nList after we have deleted last elenment [4]: \n"+ str(myList1))



#3. clear()

#The clear method simply clears all elements in our list

myList1.clear()
print("\nAfter we have cleared 'myList1', our new list holds the following values: \n" + str(myList1))
