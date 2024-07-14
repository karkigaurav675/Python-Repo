odd_numbers = {1, 3, 5, 7, 9}
print("Odd Numbers:", odd_numbers)
even_numbers = {2, 4, 6, 8, 10}
print("\nEven Numbers:", even_numbers)

union = odd_numbers.union(even_numbers)
print("\nUnion of numbers:", union)

intersection = odd_numbers.intersection(even_numbers)
print("\nIntersection of numbers:", intersection)

print("\nUnion of the sets:", union)
print("\nIntersection of the sets:", intersection)
# Intersection is empty because there is no common element between these sets.