natural_numbers = []

for num in range(1, 21):
    natural_numbers.append(num)

print("List of first 20 natural numbers:")
print(natural_numbers)

first_10_numbers = natural_numbers[0:10]
print("\nFirst 10 element slice:")
print(first_10_numbers)

last_5_numbers = natural_numbers[-5:None]
print("\nLast 5 element slice:")
print(last_5_numbers)

print("\nBoth Slices:")
print(first_10_numbers)
print(last_5_numbers)