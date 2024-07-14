primenum = {2, 3, 5, 7, 11}
print("First 5 prime numbers: ", primenum)

primenum.add(11)
print("\nAdding 11 to the set: ", primenum)
# 11 is already present in the set so it cant be added as sets have unique elements only.

primenum.remove(2)
print("\nRemoving number 2 from set: ", primenum)

is_seven_in_set = 7 in primenum
print("\nChecking if 7 is in set: ", is_seven_in_set) #True or False, Boolean value.

print("\nFinal set: ", primenum)