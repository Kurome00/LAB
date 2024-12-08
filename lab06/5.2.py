def geometric_sum(a, r, n):
    if n == 0:
        return 0
    else:
        return a + geometric_sum(a * r, r, n - 1)
a = float(input("Введите первый член (a): "))
r = float(input("Введите знаменатель (r): "))
n = int(input("Введите количество членов (n): "))
result = geometric_sum(a, r, n)
print(f'Сумма первых {n} членов геометрической прогрессии: {result}')
