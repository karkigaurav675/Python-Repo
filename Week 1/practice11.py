cities = {
    'Delhi': '3.3 crore', 'Mumbai': '2.1 crore', 'Kolkata': '1.5 crore', 'Bengaluru': '1.4 crore', 'Chennai': '1.2 crore'
}
print(cities)

population_of_Mumbai = cities.get('Mumbai')
print("\nUsing the get method to access the population of a specific city: ", population_of_Mumbai)

remove_city = cities.pop('Chennai')
print("\nUsing the pop method to remove a city from the dictionary: ", 'Chennai')

print("\nFinal dictionary: ", cities)