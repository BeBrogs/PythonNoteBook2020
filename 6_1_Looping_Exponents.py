#Create a function named exponents() that takes two lists as parameters named bases and powers. 
#Return a new list containing every number in bases raised to every number in powers.


def exponents(bases, powers):
  new_ar = []
  for a in bases:
    for b in powers:
      new_ar.append(a**b)

  return new_ar

print(exponents([2, 3, 4], [1, 2, 3]))
