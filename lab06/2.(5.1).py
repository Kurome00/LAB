a = int(input ('Введите число a'))
b = int(input ('Введите число b'))
if (a>b):
    print('числа введены неправильно введите заново')
 
else:
    L=0
    for i in range(a,b+1):
        L += i
print(f"Сумма всех целых чисел от {a} до {b} равна: {L}")
