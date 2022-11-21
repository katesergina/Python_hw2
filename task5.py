# 5) Реализуйте алгоритм перемешивания списка.

import random

def shuffle_list(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i + 1)
        lst[i], lst[j] = lst[j], lst[i]

lst = [random.randint(0,10) for i in range(random.randint(1,20))]
print(lst)
shuffle_list(lst)
print(lst)



