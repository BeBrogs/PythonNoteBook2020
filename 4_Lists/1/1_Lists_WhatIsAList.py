#Array that is ordered and changeable.
#written with [square brackets].

myFirstInts = [1,2,3,4,5]  #int list - ordered & changeable

print("\n1. Printing the 1st element in our int array:")
print ("\n"+str(myFirstInts[0]))

myFirstFloats=[0.00, 0.25,  0.50, 0.75, 1.00] #float list - ordered & changeable

print("\n2. Printing the 1st element in our float array:")
print("\n"+str(myFirstFloats[0]))

myFirstWords = ["Mother", "Father", "Im not counting right!!"] 
    #str list - ordered & changeable

print("\n3. Printing the last element in our str array via negative access format:")
print("\n"+str(myFirstWords[-1])+"\n")


print("\n4. Printing the First 2 elements in our str array via range format:")
#Print from index 0 (place 1) up to but not including index 2 (place 3)
print("\n"+str(myFirstWords[0:2]))




print("\n5. Printing last 2 elements of str array via range format:")
print("\n"+str(myFirstWords[1:]))

print("\n6. Printing whole str array via range format:")
#Even though our list doesn't have 4 elements, if we want to print the whole array
#We have to include an outer boundary which doesn't exist (Array.size() + 1)
print("\n"+str(myFirstWords[:3]))


print("\n7. Printing str whole array (Easiest):")
print("\n"+str(myFirstWords))
