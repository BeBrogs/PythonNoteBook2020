#Tuples are unchangeable in theory
#But there is a work around
#1. You convert the tuple into a list
#2. Change whatever you require inside the list
#3. Then turn your now-updated list back to the orignal tuple format


myTuple = ("Never", "Gonna", "Change")

myList = list(myTuple)  #1. Converting tuple into list

myList[0]="I'm" #2. Changing index [0] 'Never' to 'I'm'

myTuple = tuple(myList) #3.  onverting list back to tuple

print(myTuple)

