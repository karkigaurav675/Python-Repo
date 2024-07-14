odd_numbers = [2*num - 1 for num in range(1, 11)]

print("List of the first 10 odd numbers:")
print(odd_numbers)

square_odd_numbers = [num**2 for num in odd_numbers]
print("\nList of squares of the first 10 odd numbers:")
print(square_odd_numbers)

print("\nPrinting both lists:")
print(odd_numbers)
print(square_odd_numbers)