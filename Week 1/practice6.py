nested_tuple = ((365, 2.56, "Hello"), ('ABCD', 57, 7.89))
print(nested_tuple)

second_element = nested_tuple[0][1]
print("\nSecond element of first tuple")
print(second_element)

first_element = nested_tuple[1][0]
print("\nFirst element of second tuple")
print(first_element)

print("\nPrinting Both elements")
print(second_element)
print(first_element)