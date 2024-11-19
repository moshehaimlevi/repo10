isr_id = {
    "Name": "Israel",
    "Birth": 1948,
    "Population_millions": 9.3,
    "Capital": "Jerusalem",
    "Language": "Hebrew",
    "Cities": ["Jerusalem", "Tel Aviv", "Haifa", "Rishon LeZion", "Petah Tikva", "Ashdod"],
    "Currency": "ILS",
    "Area_Kilometer": 22145,
    "GDP_Billion": 450
}

print(isr_id)
print('capital:',isr_id.get("Capital"))
print('keys:', list(isr_id.keys()))
print('values:', list(isr_id.values()))


for key, value in isr_id.items(): # UNPACK
    print(f"{key}: {value}")

isr_id_dup = isr_id.copy()
print('copy',isr_id_dup)


print(isr_id_dup)             # POP
gdp_billion = isr_id_dup.pop('GDP_Billion')
print(gdp_billion)
print(isr_id_dup)

keys = ["name", "birth", "population_millions", "capital", "language", "cities", "currency", "area_Kilometer", "gdp_billion"]
new_isr_id = dict.fromkeys(keys)
new_isr_id["name"] = input("Enter the name of the country: ")
new_isr_id["birth"] = int(input("Enter the year of birth of the country: "))
new_isr_id["population_millions"] = float(input("Enter the population : "))
new_isr_id["capital"] = input("Enter the capital city: ")
new_isr_id["language"] = input("Enter the language: ")

cities = []
for i in range(3):
    city = input(f"Enter city {i+1}: ")
    cities.append(city)
new_isr_id["cities"] = cities
new_isr_id["currency"] = input("Enter the currency: ")
new_isr_id["area_Kilometer"] = int(input("Enter the area in square kilometers: "))
new_isr_id["gdp_billion"] = float(input("Enter the GDP in billions: "))
print(new_isr_id)


# SECTION NUMBER 2:

sentence: str = str(input('enter your sentence:'))
words = sentence.split()
if words:
    last_word = words[-1]
    print(f"Last word: {last_word}")
    print(f"Number of char in the last word: {len(last_word)}")
else:
    print("The sentence is empty!")


















