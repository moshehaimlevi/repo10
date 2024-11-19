

# SORTING BY KEY:

# SECTION NUMBER 1:

# SECTION A:
cities1: list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
print(sorted(cities1, key=lambda w: len(w)))

# SECTION B:
cities2: list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
print(sorted(cities2, key=lambda w: len(w.split())))

# SECTION C:
cities3: list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
print(sorted(cities3, key=lambda w: w == w[::-1]))

# SECTION D:
cities4: list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
print(sorted(cities4, key=lambda w: len(w), reverse=True ))

# SECTION E:
cities5: list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
print(sorted(cities5), sum(city.lower().count('a') for city in cities5))

# SECTION F:

# NUMBER 1:

cities_far: list[str] = [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050,
"Europe"], ["London", 2240, "Europe"], ["Sydney", 8780, "Australia"],
["Dubai", 1300, "Asia"], ["Shanghai", 4920, "Asia"]]
print(sorted(cities_far, key=lambda miles_far: miles_far[1]))

# NUMBER 2:
cities_far2: list[str] = [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050,
"Europe"], ["London", 2240, "Europe"], ["Sydney", 8780, "Australia"],
["Dubai", 1300, "Asia"], ["Shanghai", 4920, "Asia"]]
print(sorted(cities_far2, key=lambda miles_far: miles_far[1], reverse=True))

# NUMBER 3:
cities_far3: list[str] = [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050,
"Europe"], ["London", 2240, "Europe"], ["Sydney", 8780, "Australia"],
["Dubai", 1300, "Asia"], ["Shanghai", 4920, "Asia"]]
print(sorted(cities_far3, key=lambda conti: (conti[2], conti[1])))

# NUMBER 4:

cities_far4: list[str] = [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050,
"Europe"], ["London", 2240, "Europe"], ["Sydney", 8780, "Australia"],
["Dubai", 1300, "Asia"], ["Shanghai", 4920, "Asia"]]
print(sorted(cities_far4, key=lambda conti: (conti[1], conti[1]), reverse=True))

# SECTION B:
import random

numbers2 = [random.randint(1, 100) for _ in range(50)]

print(sorted(numbers2, key=lambda x: x))

average = sum(numbers2) / len(numbers2)

print("Average:", average)

# SECTION NUMBER 2:

cake_recipe: str = """
This chocolate cake is rich, moist, and full of delicious chocolate flavor.
To make the cake, you will need chocolate, flour, sugar, eggs, and butter.
After baking the chocolate cake, let the cake cool before adding the chocolate frosting.
"""
words: list[str] = (cake_recipe.lower().replace(".", "").
                    replace(",", "").split())
print(cake_recipe)

dict_count_words: dict[str: int] = dict()
for word in words:
    dict_count_words[word] = dict_count_words.get(word, 0) + 1
print(dict_count_words)


dict_count_letters: dict[str: int] = dict()
for lett in cake_recipe.lower().replace(" ", ""):
    dict_count_letters[lett] = dict_count_letters.get(lett, 0) + 1
print(dict_count_letters)


# SECTION NUMBER 3:

dict_hezka3: dict[int, int] = dict()
for i in range(0, 20 + 1):
    dict_hezka3[i] = i ** 3
print(dict_hezka3)























































