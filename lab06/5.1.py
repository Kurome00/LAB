def count_numbers_in_range(digits, start, end):
    count = 0
    for number in range(start, end + 1):
        str_num = str(number)
        if all(char in digits for char in str_num):
            count += 1
    return count
a = input("Введите первую цифру (a): ")
b = input("Введите вторую цифру (b): ")
c = input("Введите третью цифру (c): ")
digits = {a, b, c}
N = int(input("Введите значение N (210 < N < 231): "))
while N <= 210 or N >= 231:
    print("Ошибка: N должно быть в диапазоне (210, 231).")
    N = int(input("Введите значение N (210 < N < 231): "))
result = count_numbers_in_range(digits, 100, N)
print(f'Количество чисел на отрезке [100, {N}]: {result}')
