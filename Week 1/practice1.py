square_numbers = []

for num in range(1, 11):
    square_numbers.append(num*num)

print("First 10 square numbers:")
print(square_numbers)

square_numbers[2] = 50
print("\nReplacing the third element with 50:")
print(square_numbers)

square_numbers.insert(4, 25)
print("\nInserting 25 at the fifth position:")
print(square_numbers)

square_numbers.pop()
print("\nRemoving the last element from the list and the final list:")
print(square_numbers)