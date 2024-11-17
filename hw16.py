

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

# SECTION NUMBER 3:

times_3 = {
    "1": 1 ** 3,
    "2": 2**3,
    "3": 3** 3,
    "4": 4** 3,
    "5": 5** 3,
    "6" :6 ** 3,
    "7": 7** 3,
    "8": 8** 3,
    "9": 9** 3,
    "10": 10** 3,
    "11": 11** 3,
    "12": 12** 3,
    "13": 13** 3,
    "14": 14** 3,
    "15": 15** 3,
    "16": 16** 3,
    "17": 17** 3,
    "18": 18** 3,
    "19": 19** 3,
    "20": 20** 3,

}
print(times_3.get("6", "invalid number"))











































