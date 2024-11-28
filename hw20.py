
# SECTION NUMBER 1:
def str_no(list: str) -> bool:
    if "[]" in list or "{}" in list or "()" in list:
        return True
    else:
        return False
print(str_no("[]"))

# SECTION NUMBER 2:
def no_dupl(num1: list[int]) -> list:
    list1 = []
    for num in num1:
        if num not in list1:
            list1.append(num)
    return list1
num1: list[int] = [2, 2, 5, 5, 3, 3, 4, 4]
print(sorted(no_dupl(num1)))

# SECTION NUMBER 3:
def comb_tup(tup1, tup2) -> tuple:
    tup3 = list(tup1 + tup2)
    result = []
    while tup3:
        num = tup3[0]
        count_tup1 = tup1.count(num)
        count_tup2 = tup2.count(num)
        result.extend([num] * (count_tup1 + count_tup2))
        tup3 = [x for x in tup3 if x != num]
    return tuple(result)
tup1: tuple[int, int, int, int] =(1, 2, 3, 4)
tup2: tuple[int, int, int, int] =(3, 4, 5, 6)

print(comb_tup(tup1, tup2))




































