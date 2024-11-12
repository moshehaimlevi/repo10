# FILTER USING FOR LIST OF NUMBERS, SECTION NUMBER 1:

import random

print('bigger than 50',list(filter(lambda x: x >=50, [random.randint(1, 100) for _ in range(50)])))

print('div by7',list(filter(lambda x: x % 7 == 0, [random.randint(1, 100) for _ in range(50)])))

print('2 dig min',list(filter(lambda x: x >=10, [random.randint(1, 100) for _ in range(50)])))

print('same',list(filter(lambda x: (x // 10) % 10, [random.randint(1, 100) for _ in range(50)])))

print('sum of 9',list(filter(lambda x: sum(int(digit) for digit in str(x)) == 9, [random.randint(1, 100) for _ in range(50)])))

# FILTER USING FOR LIST OF CHARACTERS, SECTION NUMBER 2:

print(list(filter(lambda word: len(word) > 8,["The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch","V Auto Theft Grand ","Fortnite"])))

print(list(filter(lambda word:word.upper().startswith("F"),["The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch","V Auto Theft Grand ","Fortnite"])))

print(list(filter(lambda word: len(word.split()) == 2, ["The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch", "V Auto Theft Grand", "Fortnite"])))

print(list(filter(lambda word: 'V' in word.upper(), ["The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch", "V Auto Theft Grand", "Fortnite"])))

# MAP USING NUMBERS, SECTION NUMBER 3:

print('map1', list(map(lambda x: x, [random.randint(-50, 50) for _ in range(20)])))

print('map2', list(map(lambda x: x ** 3,[random.randint(-50, 50) for _ in range(20)] )))

print('map3', list(map(lambda x: x % 10,[random.randint(-50, 50) for _ in range(20)] )))

print('map4', list(map(lambda x: f"{(9/5) * x + 32:.2f}",[random.randint(-50, 50) for _ in range(20)] )))

# MAP USING STR, SECTION NUMBER 4:

print('map str 1', list(map(lambda w: w[::-1], ["Mango ", "Orange ", "Banana ", "Apple", "Strawberry", "Pineapple", "Grapes", "Watermelon"])))

print('map str 2', list(map(lambda w: w.strip()[0], ["Mango ", "Orange ", "Banana ", "Apple", "Strawberry", "Pineapple", "Grapes", "Watermelon"])))

print('map str 3', list(map(lambda w: w.upper(), ["Mango ", "Orange ", "Banana ", "Apple", "Strawberry", "Pineapple", "Grapes", "Watermelon"])))

print('map str 4', list(map(lambda w: w[len(w) // 2], ["Mango ", "Orange ", "Banana ", "Apple", "Strawberry", "Pineapple", "Grapes", "Watermelon"])))
































































