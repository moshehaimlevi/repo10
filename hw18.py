# USING TUPLE:
# SECTION A:
from xml.sax.handler import property_interning_dict

tup1: tuple[int] = (99,)
print(tup1[0])

# SECTION B:
tup2: tuple[int,int,int] = (99,88,77)
print(tup2)

# SECTION C
def tup_length(tup3:tuple) -> tuple:
    return len(tup3)
tup3: tuple[int, int, int, int, int, int, int] = (1, 6, 8, 10, 23, 17, 66)
print('len',tup_length(tup3))

# SECTION D:

def connect_tup(tuple_1: tuple, tuple_2: tuple) -> tuple:
    con_tup = tuple_1 + tuple_2
    return con_tup
tuple_1 : tuple[int, int] = (6, 3)
tuple_2 : tuple[int, int] = (5,9)
print('2 tuples connected:', connect_tup(tuple_1, tuple_2))

# SECTION E:
def same_num(tuple_3: tuple, tuple_4: tuple) -> tuple:
    num = tuple(i for i in tuple_3 if i in tuple_4)
    return num
tuple_3 : tuple[int, int, int, int] = (5, 1, 3, 2)
tuple_4 : tuple[int, int, int, int] = (7, 2, 5, 6)
print('matching numbers:', same_num(tuple_3, tuple_4))

# SECTION F:
def diff_num(tuple_5: tuple, tuple_6: tuple) -> tuple:
    new_tuple = tuple_5 + tuple_6
    result = []
    for num in new_tuple:
        if new_tuple.count(num) == 1:
            result.append(num)
    return tuple(result)
tuple_5 : tuple[int, int, int, int] = (3, 1, 7, 2)
tuple_6 : tuple[int, int, int, int] = (7, 2, 5, 6)
print('different numbers:', diff_num(tuple_5, tuple_6))

# SECTION G:
def tup_ind(tuple_7: tuple) -> tuple:
    index = []
    for i in range(len(tuple_7)):
        index.append(f"Index {i}: {tuple_7[i]}")
    return tuple(index)
tuple_7 : tuple[int, int, int, int, int] = (2, 5, 6, 8, 9)
print("Numbers with index:", tup_ind(tuple_7))

# SECTION H:
def reverse_tuple(tuple_8: tuple) -> tuple:
    return tuple_8[::-1]
tuple_8: tuple[int, int, int, int, int] = (1, 4, 7, 15, 23)
print('reverse', reverse_tuple(tuple_8))

# SECTION I:
def dub_tup(tuple_9: tuple) -> tuple:
    return tuple_9 * 5
tuple_9: tuple[int, int] = (5, 8)
print('multi by', dub_tup(tuple_9))

# SECTION J:
def remove_n(tuple_10: tuple) -> tuple:
    list_remove = [num for num in tuple_10 if num != 5]
    return tuple(list_remove)
tuple_10: tuple[int, int, int, int, int, int] = (2, 3, 6, 5, 10, 5)
print('without 5', remove_n(tuple_10))

# SECTION K:
def no_dup(tup11: tuple) -> tuple:
     result = []
     for item in tup11:
         if not item in result:
             result.append(item)
     return tuple(result)
tuple_11: tuple[int, int, int, int, int, int] = (1, 3, 4, 3, 4, 8)
print('no duplicates', no_dup(tuple_11))

# SECTION L:
def index_by_value(tup12: tuple, value) -> tuple:
    result = []
    for index in range(len(tup12)):
        if tup12[index] == value:
            result.append(index)
    return tuple(result)
tup12: tuple[int, int, int, int, int, int] = (1, 3, 5, 1, 9, 1)
print('index and value', index_by_value(tup12, 1))

# SECTION M:
names = []
grades = []
name: str = input('ENTER NAME:')
while not name == "done":
    names.append(name)
    name = input('ENTER NAME:')
grade: int = int(input('ENTER GRADE:'))
while not grade == -999:
    grades.append(grade)
    grade = int(input('ENTER GRADE:'))
print(tuple(zip(names, grades)))















