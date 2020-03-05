#Q. How do I print/access individual tuples
#A. By specifying the index position you want to print in [Sq Brackets]


myFirstTuple = ("Never", "Gonna", "Change")


#Positive indexing
print("\n"+str(myFirstTuple[2]))
#Prints pos 3 in myFirstTuple

#Neg. Indexing
print("\n"+str(myFirstTuple[-1]))


#Range indexing
print("\n"+str(myFirstTuple[1:2]))
print("\n"+str(myFirstTuple[2:3]))

#Neg. Range indexing
print("\n"+str(myFirstTuple[-3:-1]))
#This example returns the items from index -2 (included) to index -1 (excluded)


