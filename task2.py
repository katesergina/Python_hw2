# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def calculate_prod(numbers):
    prod = 1
    for i in numbers:
        prod *= i
    return prod

N = int(input("Введите число: "))

s = []
for i in range(1, N + 1):
    s.append(i)
    if i > 1:
        print(', ', end='')

    print(calculate_prod(s), end='')

print("\n")