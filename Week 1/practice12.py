countries = {
    'USA': {'capital': 'Washington D.C.', 'population': 331449281},
    'India': {'capital': 'New Delhi', 'population': 1380004385},
    'Australia': {'capital': 'Canberra', 'population': 27297500}
}
print("Initial Dictionary: ", countries)

capital_of_India = countries['India']['capital']
print("\nPrinting the capital of one country: ")
print("Capital of India: ", capital_of_India)

countries['USA']['population'] = 551456891

print("\nFinal dictionary: ", countries)